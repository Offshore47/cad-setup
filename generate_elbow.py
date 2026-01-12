"""
Elbow Generator - pythonocc
Generates pipe elbows with ASME B16.25 weld bevels
Units: INCHES
Elbow Types:
  SR   = Short Radius (CLR = 1.0 × OD)
  LR   = Long Radius  (CLR = 1.5 × OD)
  LR3  = 3D Elbow     (CLR = 3.0 × OD)
  LR5  = 5D Elbow     (CLR = 5.0 × OD)
  LR10 = 10D Elbow    (CLR = 10.0 × OD)
  Custom = User-specified CLR multiplier

Angles: 90, 45, 22.5, or custom

Bevel: ASME B16.25 - 37.5° angle, 1/16" land
"""

import math
import argparse
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeTorus
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut
from OCC.Core.BRepFilletAPI import BRepFilletAPI_MakeChamfer
from OCC.Core.gp import gp_Ax2, gp_Pnt, gp_Dir
from OCC.Core.TopAbs import TopAbs_EDGE, TopAbs_FACE
from OCC.Core.TopTools import TopTools_IndexedDataMapOfShapeListOfShape, TopTools_IndexedMapOfShape, TopTools_ListIteratorOfListOfShape
from OCC.Core.TopExp import topexp
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.IFSelect import IFSelect_RetDone
from OCC.Core.Interface import Interface_Static
from OCC.Core.BRepAdaptor import BRepAdaptor_Curve, BRepAdaptor_Surface
from OCC.Core.GeomAbs import GeomAbs_Circle, GeomAbs_Torus
from OCC.Core.TopoDS import topods

# Set STEP export units to INCHES
Interface_Static.SetCVal("write.step.unit", "IN")

# CLR multipliers for elbow types
ELBOW_TYPES = {
    'SR': 1.0,
    'LR': 1.5,
    'LR3': 3.0,
    'LR5': 5.0,
    'LR10': 10.0
}

# Import complete pipe data
from pipe_data_complete import PIPE_DATA, get_pipe_dimensions as get_pipe_dims


def get_pipe_dimensions(nps: float, schedule: str) -> tuple:
    """Get OD and Wall thickness for given NPS and Schedule"""
    return get_pipe_dims(nps, schedule)


def generate_elbow(
    nps: float,
    schedule: str,
    elbow_type: str = 'LR',
    angle: float = 90.0,
    custom_clr_mult: float = None,
    bevel_angle_end1: float = 37.5,
    bevel_land_end1: float = 1/16,
    bevel_angle_end2: float = 37.5,
    bevel_land_end2: float = 1/16,
    output_file: str = None
):
    """
    Generate a pipe elbow with weld bevels.
    
    Parameters:
        nps: Nominal Pipe Size (inches)
        schedule: Pipe schedule ('40', '80', '160', etc.)
        elbow_type: 'SR', 'LR', 'LR3', 'LR5', 'LR10', or 'Custom'
        angle: Elbow angle in degrees (90, 45, 22.5, or custom)
        custom_clr_mult: CLR multiplier for Custom elbow type
        bevel_angle_end1: Weld bevel angle for end 1 (default 37.5°, set 0 for square cut)
        bevel_land_end1: Weld bevel land thickness for end 1 (default 1/16")
        bevel_angle_end2: Weld bevel angle for end 2 (default 37.5°, set 0 for square cut)
        bevel_land_end2: Weld bevel land thickness for end 2 (default 1/16")
        output_file: Output STEP filename (auto-generated if None)
    
    Note: Common bevel angles: 37.5° (ASME B16.25 standard), 30° (common shop practice)
          Set angle to 0 for square cut ends
    
    Returns:
        Path to generated STEP file
    """
    
    # Get pipe dimensions
    OD, WALL = get_pipe_dimensions(nps, schedule)
    ID = OD - 2 * WALL
    
    # Determine CLR multiplier
    if elbow_type == 'Custom':
        if custom_clr_mult is None:
            raise ValueError("custom_clr_mult required for Custom elbow type")
        clr_mult = custom_clr_mult
    else:
        if elbow_type not in ELBOW_TYPES:
            raise ValueError(f"Unknown elbow type: {elbow_type}. Use: {list(ELBOW_TYPES.keys())} or 'Custom'")
        clr_mult = ELBOW_TYPES[elbow_type]
    
    CLR = OD * clr_mult
    angle_rad = math.radians(angle)
    
    print(f"=== Elbow Parameters ===")
    print(f"NPS: {nps}\"  Schedule: {schedule}")
    print(f"Type: {elbow_type} (CLR = {clr_mult} × OD)")
    print(f"Angle: {angle}°")
    print(f"OD = {OD}\" = {OD * 25.4:.2f} mm")
    print(f"ID = {ID:.4f}\" = {ID * 25.4:.2f} mm")
    print(f"Wall = {WALL}\" = {WALL * 25.4:.2f} mm")
    print(f"CLR = {CLR}\" = {CLR * 25.4:.2f} mm")
    
    # Create elbow body (hollow torus section)
    ax = gp_Ax2(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1))
    outer_torus = BRepPrimAPI_MakeTorus(ax, CLR, OD/2, angle_rad).Shape()
    inner_torus = BRepPrimAPI_MakeTorus(ax, CLR, ID/2, angle_rad).Shape()
    cut_op = BRepAlgoAPI_Cut(outer_torus, inner_torus)
    cut_op.Build()
    elbow = cut_op.Shape()
    print("Elbow body created")
    
    # Chamfer sizes = wall - land (ASME B16.25 weld bevel)
    chamfer_size_end1 = WALL - bevel_land_end1 if bevel_angle_end1 > 0 else 0
    chamfer_size_end2 = WALL - bevel_land_end2 if bevel_angle_end2 > 0 else 0
    
    print(f"=== Bevel Parameters ===")
    if bevel_angle_end1 > 0:
        print(f"End 1: {chamfer_size_end1:.4f}\" chamfer @ {bevel_angle_end1}°, land={bevel_land_end1 * 25.4:.3f}mm")
    else:
        print(f"End 1: Square cut (no bevel)")
    
    if bevel_angle_end2 > 0:
        print(f"End 2: {chamfer_size_end2:.4f}\" chamfer @ {bevel_angle_end2}°, land={bevel_land_end2 * 25.4:.3f}mm")
    else:
        print(f"End 2: Square cut (no bevel)")
    
    # Get all edges
    edge_map = TopTools_IndexedMapOfShape()
    topexp.MapShapes(elbow, TopAbs_EDGE, edge_map)
    num_edges = edge_map.Size()
    
    # Build edge->face map
    edge_face_map = TopTools_IndexedDataMapOfShapeListOfShape()
    topexp.MapShapesAndAncestors(elbow, TopAbs_EDGE, TopAbs_FACE, edge_face_map)
    
    # Find outer edges at elbow ends
    outer_edges = []
    edge_faces = []
    for i in range(1, num_edges + 1):
        edge = edge_map.FindKey(i)
        adaptor = BRepAdaptor_Curve(edge)
        if adaptor.GetType() == GeomAbs_Circle:
            radius = adaptor.Circle().Radius()
            center = adaptor.Circle().Location()
            dist_from_origin = math.sqrt(center.X()**2 + center.Y()**2)
            # Outer edges at end faces: radius = OD/2, center at CLR from origin
            if abs(radius - OD/2) < 0.01 and abs(dist_from_origin - CLR) < 0.01:
                outer_edges.append(edge)
                face_list = edge_face_map.FindFromKey(edge)
                # Find the torus face (outer curved surface)
                torus_face = None
                first_face = None
                it = TopTools_ListIteratorOfListOfShape(face_list)
                while it.More():
                    f = topods.Face(it.Value())
                    if first_face is None:
                        first_face = f
                    surf = BRepAdaptor_Surface(f)
                    if surf.GetType() == GeomAbs_Torus:
                        torus_face = f
                    it.Next()
                if torus_face is not None:
                    edge_faces.append(torus_face)
                elif first_face is not None:
                    edge_faces.append(first_face)
    
    print(f"Found {len(outer_edges)} outer edges to chamfer")
    
    # Apply chamfer with Size and Angle (AddDA method)
    # Elbow has 2 ends - need to identify which is which and apply appropriate bevel
    if outer_edges and len(edge_faces) == len(outer_edges) and len(outer_edges) == 2:
        chamfer = BRepFilletAPI_MakeChamfer(elbow)
        for idx, (edge, face) in enumerate(zip(outer_edges, edge_faces)):
            # Apply bevel based on which end (0=end1, 1=end2)
            if idx == 0 and bevel_angle_end1 > 0:
                chamfer.AddDA(chamfer_size_end1, math.radians(bevel_angle_end1), edge, face)
                print(f"  Applied end 1 bevel: {chamfer_size_end1:.4f}\" @ {bevel_angle_end1}°")
            elif idx == 1 and bevel_angle_end2 > 0:
                chamfer.AddDA(chamfer_size_end2, math.radians(bevel_angle_end2), edge, face)
                print(f"  Applied end 2 bevel: {chamfer_size_end2:.4f}\" @ {bevel_angle_end2}°")
        chamfer.Build()
        if chamfer.IsDone():
            elbow = chamfer.Shape()
            print("Bevels applied successfully!")
        else:
            print("WARNING: Chamfer failed!")
    else:
        print(f"WARNING: Edge/face mismatch: {len(outer_edges)} edges, {len(edge_faces)} faces")
    
    # Generate output filename
    if output_file is None:
        nps_str = str(nps).replace('.', '-')
        output_file = f"Elbow-{elbow_type}{int(angle)}-NPS{nps_str}-Sch{schedule}.step"
    
    # Export STEP file
    writer = STEPControl_Writer()
    writer.Transfer(elbow, STEPControl_AsIs)
    status = writer.Write(output_file)
    if status == IFSelect_RetDone:
        print(f"Exported: {output_file}")
    else:
        print(f"ERROR: Failed to export {output_file}")
    
    return output_file


def main():
    parser = argparse.ArgumentParser(description='Generate pipe elbows with weld bevels')
    parser.add_argument('nps', type=float, help='Nominal Pipe Size (inches)')
    parser.add_argument('schedule', type=str, help='Pipe schedule (40, 80, 160, etc.)')
    parser.add_argument('--type', '-t', default='LR', 
                        choices=['SR', 'LR', 'LR3', 'LR5', 'LR10', 'Custom'],
                        help='Elbow type (default: LR)')
    parser.add_argument('--angle', '-a', type=float, default=90.0,
                        help='Elbow angle in degrees (default: 90)')
    parser.add_argument('--clr', type=float, default=None,
                        help='Custom CLR multiplier (only for --type Custom)')
    parser.add_argument('--bevel-angle', type=float, default=37.5,
                        help='Weld bevel angle (default: 37.5)')
    parser.add_argument('--land', type=float, default=0.0625,
                        help='Weld bevel land thickness in inches (default: 0.0625 = 1/16)')
    parser.add_argument('--output', '-o', type=str, default=None,
                        help='Output STEP filename')
    
    args = parser.parse_args()
    
    generate_elbow(
        nps=args.nps,
        schedule=args.schedule,
        elbow_type=args.type,
        angle=args.angle,
        custom_clr_mult=args.clr,
        bevel_angle=args.bevel_angle,
        bevel_land=args.land,
        output_file=args.output
    )


if __name__ == '__main__':
    main()
