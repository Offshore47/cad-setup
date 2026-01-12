"""
Reducer Generator - pythonocc
Generates pipe reducers with ASME B16.25 weld bevels
Units: INCHES
Types:
  Concentric - Both ends centered on same axis
  Eccentric  - Bottom of pipe flat (BOP)

Geometry: Hollow frustum (cone section) or lofted for eccentric

Bevel: ASME B16.25 - 37.5° angle, 1/16" land
"""

import math
import argparse
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCone
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut
from OCC.Core.BRepFilletAPI import BRepFilletAPI_MakeChamfer
from OCC.Core.BRepOffsetAPI import BRepOffsetAPI_ThruSections
from OCC.Core.gp import gp_Ax2, gp_Pnt, gp_Dir, gp_Circ
from OCC.Core.TopAbs import TopAbs_EDGE, TopAbs_FACE
from OCC.Core.TopTools import TopTools_IndexedDataMapOfShapeListOfShape, TopTools_IndexedMapOfShape, TopTools_ListIteratorOfListOfShape
from OCC.Core.TopExp import topexp
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.IFSelect import IFSelect_RetDone
from OCC.Core.Interface import Interface_Static
from OCC.Core.BRepAdaptor import BRepAdaptor_Curve, BRepAdaptor_Surface
from OCC.Core.GeomAbs import GeomAbs_Circle, GeomAbs_Cone, GeomAbs_BSplineSurface
from OCC.Core.TopoDS import topods
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire

# Set STEP export units to INCHES
Interface_Static.SetCVal("write.step.unit", "IN")

# Pipe schedule data: NPS -> {Schedule -> (OD, Wall)}
PIPE_DATA = {
    0.5:  {'40': (0.840, 0.109), '80': (0.840, 0.147), '160': (0.840, 0.187)},
    0.75: {'40': (1.050, 0.113), '80': (1.050, 0.154), '160': (1.050, 0.218)},
    1:    {'40': (1.315, 0.133), '80': (1.315, 0.179), '160': (1.315, 0.250)},
    1.25: {'40': (1.660, 0.140), '80': (1.660, 0.191), '160': (1.660, 0.250)},
    1.5:  {'40': (1.900, 0.145), '80': (1.900, 0.200), '160': (1.900, 0.281)},
    2:    {'40': (2.375, 0.154), '80': (2.375, 0.218), '160': (2.375, 0.343)},
    2.5:  {'40': (2.875, 0.203), '80': (2.875, 0.276), '160': (2.875, 0.375)},
    3:    {'40': (3.500, 0.216), '80': (3.500, 0.300), '160': (3.500, 0.437)},
    3.5:  {'40': (4.000, 0.226), '80': (4.000, 0.318)},
    4:    {'40': (4.500, 0.237), '80': (4.500, 0.337), '160': (4.500, 0.531)},
    5:    {'40': (5.563, 0.258), '80': (5.563, 0.375), '160': (5.563, 0.625)},
    6:    {'40': (6.625, 0.280), '80': (6.625, 0.432), '160': (6.625, 0.718)},
    8:    {'40': (8.625, 0.322), '80': (8.625, 0.500), '160': (8.625, 0.906)},
    10:   {'40': (10.75, 0.365), '80': (10.75, 0.593), '160': (10.75, 1.125)},
    12:   {'40': (12.75, 0.406), '80': (12.75, 0.687), '160': (12.75, 1.312)},
    14:   {'40': (14.0, 0.437), '80': (14.0, 0.750), '160': (14.0, 1.406)},
    16:   {'40': (16.0, 0.500), '80': (16.0, 0.843), '160': (16.0, 1.593)},
    18:   {'40': (18.0, 0.562), '80': (18.0, 0.937), '160': (18.0, 1.781)},
    20:   {'40': (20.0, 0.593), '80': (20.0, 1.031), '160': (20.0, 1.969)},
    24:   {'40': (24.0, 0.687), '80': (24.0, 1.218), '160': (24.0, 2.343)},
}


def get_pipe_dimensions(nps: float, schedule: str) -> tuple:
    """Get OD and Wall thickness for given NPS and Schedule"""
    if nps not in PIPE_DATA:
        raise ValueError(f"NPS {nps} not in database. Available: {list(PIPE_DATA.keys())}")
    if schedule not in PIPE_DATA[nps]:
        raise ValueError(f"Schedule {schedule} not available for NPS {nps}. Available: {list(PIPE_DATA[nps].keys())}")
    return PIPE_DATA[nps][schedule]


def generate_reducer(
    large_nps: float,
    large_schedule: str,
    small_nps: float,
    small_schedule: str = None,
    reducer_type: str = 'concentric',
    bevel_angle_large: float = 37.5,
    bevel_land_large: float = 1/16,
    bevel_angle_small: float = 37.5,
    bevel_land_small: float = 1/16,
    output_file: str = None
):
    """
    Generate a pipe reducer with weld bevels.
    
    Parameters:
        large_nps: Large end NPS (inches)
        large_schedule: Large end schedule ('40', '80', '160', etc.)
        small_nps: Small end NPS (inches)
        small_schedule: Small end schedule (default: same as large)
        reducer_type: 'concentric' or 'eccentric' (BOP - bottom of pipe flat)
        bevel_angle_large: Large end bevel angle (default 37.5°, set 0 for square cut)
        bevel_land_large: Large end land thickness (default 1/16")
        bevel_angle_small: Small end bevel angle (default 37.5°, set 0 for square cut)
        bevel_land_small: Small end land thickness (default 1/16")
        output_file: Output STEP filename (auto-generated if None)
    
    Note: Common bevel angles: 37.5° (ASME standard), 30° (shop practice)
    
    Returns:
        Path to generated STEP file
    """
    
    if small_schedule is None:
        small_schedule = large_schedule
    
    # Get pipe dimensions
    LARGE_OD, LARGE_WALL = get_pipe_dimensions(large_nps, large_schedule)
    LARGE_ID = LARGE_OD - 2 * LARGE_WALL
    
    SMALL_OD, SMALL_WALL = get_pipe_dimensions(small_nps, small_schedule)
    SMALL_ID = SMALL_OD - 2 * SMALL_WALL
    
    # Reducer length per ASME B16.9 (approximate)
    # H = length based on size difference
    LENGTH = max(LARGE_OD, 3.0)  # Minimum 3", or large OD
    
    print(f"=== Reducer Parameters ===")
    print(f"Type: {reducer_type.capitalize()}")
    print(f"Large End: NPS {large_nps}\" Sch {large_schedule}")
    print(f"  OD = {LARGE_OD}\" = {LARGE_OD * 25.4:.2f} mm")
    print(f"  ID = {LARGE_ID:.4f}\" = {LARGE_ID * 25.4:.2f} mm")
    print(f"  Wall = {LARGE_WALL}\" = {LARGE_WALL * 25.4:.2f} mm")
    print(f"Small End: NPS {small_nps}\" Sch {small_schedule}")
    print(f"  OD = {SMALL_OD}\" = {SMALL_OD * 25.4:.2f} mm")
    print(f"  ID = {SMALL_ID:.4f}\" = {SMALL_ID * 25.4:.2f} mm")
    print(f"  Wall = {SMALL_WALL}\" = {SMALL_WALL * 25.4:.2f} mm")
    print(f"Length = {LENGTH}\" = {LENGTH * 25.4:.2f} mm")
    
    # === CREATE REDUCER ===
    # Large end at z=0, small end at z=LENGTH
    
    if reducer_type == 'concentric':
        # Both ends centered on Z axis - simple cone
        ax = gp_Ax2(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1))
        outer_cone = BRepPrimAPI_MakeCone(ax, LARGE_OD/2, SMALL_OD/2, LENGTH).Shape()
        inner_cone = BRepPrimAPI_MakeCone(ax, LARGE_ID/2, SMALL_ID/2, LENGTH).Shape()
        
        # Cut inner from outer
        cut_op = BRepAlgoAPI_Cut(outer_cone, inner_cone)
        cut_op.Build()
        reducer = cut_op.Shape()
    else:
        # Eccentric - bottom of pipe flat (BOP)
        # Large end centered at origin, small end center offset upward
        offset = (LARGE_OD - SMALL_OD) / 2
        print(f"  Eccentric offset = {offset}\" = {offset * 25.4:.2f} mm")
        
        # Use ThruSections to loft between circles at different positions
        # Outer surface: large circle at z=0, small circle offset at z=LENGTH
        # Inner surface: same offset pattern with ID
        
        # Create outer loft
        outer_loft = BRepOffsetAPI_ThruSections(True, True)  # solid=True, ruled=True
        
        # Large end circle (centered at origin, z=0)
        large_circ = gp_Circ(gp_Ax2(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1)), LARGE_OD/2)
        large_edge = BRepBuilderAPI_MakeEdge(large_circ).Edge()
        large_wire = BRepBuilderAPI_MakeWire(large_edge).Wire()
        
        # Small end circle (offset in Y by (LARGE_OD-SMALL_OD)/2, at z=LENGTH)
        small_circ = gp_Circ(gp_Ax2(gp_Pnt(0, offset, LENGTH), gp_Dir(0, 0, 1)), SMALL_OD/2)
        small_edge = BRepBuilderAPI_MakeEdge(small_circ).Edge()
        small_wire = BRepBuilderAPI_MakeWire(small_edge).Wire()
        
        outer_loft.AddWire(large_wire)
        outer_loft.AddWire(small_wire)
        outer_loft.Build()
        outer_shape = outer_loft.Shape()
        
        # Create inner loft (same offset pattern)
        inner_loft = BRepOffsetAPI_ThruSections(True, True)
        
        large_inner_circ = gp_Circ(gp_Ax2(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1)), LARGE_ID/2)
        large_inner_edge = BRepBuilderAPI_MakeEdge(large_inner_circ).Edge()
        large_inner_wire = BRepBuilderAPI_MakeWire(large_inner_edge).Wire()
        
        # Inner small end - offset accounts for wall thickness following outer
        inner_offset = offset  # Same offset to maintain wall thickness
        small_inner_circ = gp_Circ(gp_Ax2(gp_Pnt(0, inner_offset, LENGTH), gp_Dir(0, 0, 1)), SMALL_ID/2)
        small_inner_edge = BRepBuilderAPI_MakeEdge(small_inner_circ).Edge()
        small_inner_wire = BRepBuilderAPI_MakeWire(small_inner_edge).Wire()
        
        inner_loft.AddWire(large_inner_wire)
        inner_loft.AddWire(small_inner_wire)
        inner_loft.Build()
        inner_shape = inner_loft.Shape()
        
        # Cut inner from outer
        cut_op = BRepAlgoAPI_Cut(outer_shape, inner_shape)
        cut_op.Build()
        reducer = cut_op.Shape()
    
    print("Reducer body created")
    
    # === APPLY BEVELS ===
    chamfer_size_large = LARGE_WALL - bevel_land_large if bevel_angle_large > 0 else 0
    chamfer_size_small = SMALL_WALL - bevel_land_small if bevel_angle_small > 0 else 0
    
    print(f"=== Bevel Parameters ===")
    if bevel_angle_large > 0:
        print(f"Large End: {chamfer_size_large:.4f}\" chamfer @ {bevel_angle_large}°, land={bevel_land_large * 25.4:.3f}mm")
    else:
        print(f"Large End: Square cut (no bevel)")
    
    if bevel_angle_small > 0:
        print(f"Small End: {chamfer_size_small:.4f}\" chamfer @ {bevel_angle_small}°, land={bevel_land_small * 25.4:.3f}mm")
    else:
        print(f"Small End: Square cut (no bevel)")
    
    # Get all edges
    edge_map = TopTools_IndexedMapOfShape()
    topexp.MapShapes(reducer, TopAbs_EDGE, edge_map)
    num_edges = edge_map.Size()
    
    # Build edge->face map
    edge_face_map = TopTools_IndexedDataMapOfShapeListOfShape()
    topexp.MapShapesAndAncestors(reducer, TopAbs_EDGE, TopAbs_FACE, edge_face_map)
    
    # Find outer edges at both ends
    edges_to_chamfer = []
    
    for i in range(1, num_edges + 1):
        edge = edge_map.FindKey(i)
        adaptor = BRepAdaptor_Curve(edge)
        if adaptor.GetType() == GeomAbs_Circle:
            radius = adaptor.Circle().Radius()
            center = adaptor.Circle().Location()
            cz = center.Z()
            
            # Large end at z=0
            if abs(cz) < 0.1 and abs(radius - LARGE_OD/2) < 0.01:
                face = find_cone_face(edge, edge_face_map)
                if face is not None:
                    edges_to_chamfer.append((edge, face, chamfer_size_large, bevel_angle_large, 'large'))
            
            # Small end at z=LENGTH
            if abs(cz - LENGTH) < 0.1 and abs(radius - SMALL_OD/2) < 0.01:
                face = find_cone_face(edge, edge_face_map)
                if face is not None:
                    edges_to_chamfer.append((edge, face, chamfer_size_small, bevel_angle_small, 'small'))
    
    print(f"Found {len(edges_to_chamfer)} outer edges to chamfer")
    
    # Apply chamfers
    if edges_to_chamfer:
        chamfer = BRepFilletAPI_MakeChamfer(reducer)
        for edge, face, size, angle, location in edges_to_chamfer:
            if angle > 0:  # Only apply if bevel requested
                chamfer.AddDA(size, math.radians(angle), edge, face)
                print(f"  Added {location} end bevel: Size={size:.4f}\" @ {angle}°")
        chamfer.Build()
        if chamfer.IsDone():
            reducer = chamfer.Shape()
            print("Bevels applied successfully!")
        else:
            print("WARNING: Chamfer failed!")
    
    # Generate output filename
    if output_file is None:
        large_str = str(large_nps).replace('.', '-')
        small_str = str(small_nps).replace('.', '-')
        type_str = 'Con' if reducer_type == 'concentric' else 'Ecc'
        output_file = f"Reducer-{type_str}-{large_str}x{small_str}-Sch{large_schedule}.step"
    
    # Export STEP file
    writer = STEPControl_Writer()
    writer.Transfer(reducer, STEPControl_AsIs)
    status = writer.Write(output_file)
    if status == IFSelect_RetDone:
        print(f"Exported: {output_file}")
    else:
        print(f"ERROR: Failed to export {output_file}")
    
    return output_file


def find_cone_face(edge, edge_face_map):
    """Find the conical or lofted (BSpline) face adjacent to an edge - the outer surface"""
    face_list = edge_face_map.FindFromKey(edge)
    outer_face = None
    first_face = None
    it = TopTools_ListIteratorOfListOfShape(face_list)
    while it.More():
        f = topods.Face(it.Value())
        if first_face is None:
            first_face = f
        surf = BRepAdaptor_Surface(f)
        # Accept cone (concentric) or BSpline (eccentric loft)
        if surf.GetType() == GeomAbs_Cone or surf.GetType() == GeomAbs_BSplineSurface:
            outer_face = f
        it.Next()
    return outer_face if outer_face else first_face


def main():
    parser = argparse.ArgumentParser(description='Generate pipe reducers with weld bevels')
    parser.add_argument('large_nps', type=float, help='Large end NPS (inches)')
    parser.add_argument('large_schedule', type=str, help='Large end schedule (40, 80, 160, etc.)')
    parser.add_argument('small_nps', type=float, help='Small end NPS (inches)')
    parser.add_argument('--small-schedule', '-s', type=str, default=None,
                        help='Small end schedule (default: same as large)')
    parser.add_argument('--type', '-t', default='concentric',
                        choices=['concentric', 'eccentric'],
                        help='Reducer type (default: concentric)')
    parser.add_argument('--bevel-angle', type=float, default=37.5,
                        help='Weld bevel angle (default: 37.5)')
    parser.add_argument('--land', type=float, default=0.0625,
                        help='Weld bevel land thickness in inches (default: 0.0625 = 1/16)')
    parser.add_argument('--output', '-o', type=str, default=None,
                        help='Output STEP filename')
    
    args = parser.parse_args()
    
    generate_reducer(
        large_nps=args.large_nps,
        large_schedule=args.large_schedule,
        small_nps=args.small_nps,
        small_schedule=args.small_schedule,
        reducer_type=args.type,
        bevel_angle=args.bevel_angle,
        bevel_land=args.land,
        output_file=args.output
    )


if __name__ == '__main__':
    main()
