"""
Pipe Generator - pythonocc
Generates straight pipe with ASME B16.25 weld bevels on both ends
Standard length: 40 feet (480 inches) - can be cut to length on site

Bevel: ASME B16.25 - 37.5° angle, 1/16" land

Units: INCHES (US piping standard)
"""

import math
import argparse
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCylinder
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut
from OCC.Core.BRepFilletAPI import BRepFilletAPI_MakeChamfer
from OCC.Core.gp import gp_Ax2, gp_Pnt, gp_Dir
from OCC.Core.TopAbs import TopAbs_EDGE, TopAbs_FACE
from OCC.Core.TopTools import TopTools_IndexedDataMapOfShapeListOfShape, TopTools_IndexedMapOfShape, TopTools_ListIteratorOfListOfShape
from OCC.Core.TopExp import topexp
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.IFSelect import IFSelect_RetDone
from OCC.Core.BRepAdaptor import BRepAdaptor_Curve
from OCC.Core.GeomAbs import GeomAbs_Circle
from OCC.Core.TopoDS import topods
from OCC.Core.Interface import Interface_Static

# Set STEP units to INCH for US piping
Interface_Static.SetCVal("write.step.unit", "IN")

# Import complete pipe data
from pipe_data_complete import PIPE_DATA, get_pipe_dimensions


def generate_pipe(
    nps: float,
    schedule: str,
    length_inches: float = 480.0,  # Default 40 feet
    bevel_angle: float = 37.5,
    bevel_land: float = 1/16,
    output_file: str = None
):
    """
    Generate a straight pipe with weld bevels.
    
    Parameters:
        nps: Nominal Pipe Size (inches)
        schedule: Pipe schedule ('20', '40', '80', etc.)
        length_inches: Pipe length in inches (default 480" = 40 feet)
        bevel_angle: Weld bevel angle (default 37.5°)
        bevel_land: Weld bevel land thickness (default 1/16")
        output_file: Output STEP filename (optional)
    
    Returns:
        Path to generated STEP file
    """
    
    # Get pipe dimensions
    OD, WALL = get_pipe_dimensions(nps, schedule)
    ID = OD - (2 * WALL)
    
    print("=" * 60)
    print(f"GENERATING PIPE: {nps}\" NPS Schedule {schedule}")
    print("=" * 60)
    print(f"Outside Diameter (OD): {OD:.3f}\"")
    print(f"Wall Thickness:        {WALL:.3f}\"")
    print(f"Inside Diameter (ID):  {ID:.3f}\"")
    print(f"Pipe Length:           {length_inches:.1f}\" ({length_inches/12:.1f} ft)")
    print(f"Bevel Angle:           {bevel_angle}°")
    print(f"Land:                  {bevel_land:.4f}\" ({bevel_land*25.4:.3f} mm)")
    print("=" * 60)
    
    # Create hollow cylinder (pipe body)
    ax = gp_Ax2(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1))
    outer_cylinder = BRepPrimAPI_MakeCylinder(ax, OD/2, length_inches).Shape()
    inner_cylinder = BRepPrimAPI_MakeCylinder(ax, ID/2, length_inches).Shape()
    
    cut_op = BRepAlgoAPI_Cut(outer_cylinder, inner_cylinder)
    cut_op.Build()
    pipe = cut_op.Shape()
    print("Pipe body created")
    
    # Calculate chamfer size (bevel depth = wall - land)
    chamfer_size = WALL - bevel_land if bevel_angle > 0 else 0
    
    if chamfer_size > 0:
        print(f"Applying bevels: {chamfer_size:.4f}\" chamfer @ {bevel_angle}°")
        
        # Get all edges
        edge_map = TopTools_IndexedMapOfShape()
        topexp.MapShapes(pipe, TopAbs_EDGE, edge_map)
        num_edges = edge_map.Size()
        
        # Build edge->face map
        edge_face_map = TopTools_IndexedDataMapOfShapeListOfShape()
        topexp.MapShapesAndAncestors(pipe, TopAbs_EDGE, TopAbs_FACE, edge_face_map)
        
        # Find the two outer circular edges at pipe ends (z=0 and z=length)
        chamfer_edges = []
        for i in range(1, num_edges + 1):
            edge = edge_map.FindKey(i)
            adaptor = BRepAdaptor_Curve(edge)
            
            if adaptor.GetType() == GeomAbs_Circle:
                radius = adaptor.Circle().Radius()
                center = adaptor.Circle().Location()
                z_pos = center.Z()
                
                # Check if it's outer diameter at top or bottom
                if abs(radius - OD/2) < 0.01:  # Outer edge
                    if abs(z_pos) < 0.01 or abs(z_pos - length_inches) < 0.01:  # At ends
                        chamfer_edges.append(edge)
        
        print(f"Found {len(chamfer_edges)} edges to bevel")
        
        if len(chamfer_edges) >= 2:
            # Apply chamfers
            chamfer_maker = BRepFilletAPI_MakeChamfer(pipe)
            
            for edge in chamfer_edges:
                # Find adjacent face
                face_list = edge_face_map.FindFromKey(edge)
                it = TopTools_ListIteratorOfListOfShape(face_list)
                if it.More():
                    face = topods.Face(it.Value())
                    chamfer_maker.Add(chamfer_size, bevel_angle * (math.pi/180), edge, face)
            
            chamfer_maker.Build()
            if chamfer_maker.IsDone():
                pipe = chamfer_maker.Shape()
                print("Bevels applied successfully")
            else:
                print("Warning: Bevel operation failed, using square-cut ends")
        else:
            print("Warning: Could not find edges for beveling, using square-cut ends")
    else:
        print("Square-cut ends (no bevel)")
    
    # Generate output filename if not provided
    if output_file is None:
        length_ft = int(length_inches / 12)
        output_file = f"Pipe_{nps:.1f}in_Sch{schedule}_{length_ft}ft.step".replace('.', '-')
    
    # Export to STEP
    writer = STEPControl_Writer()
    writer.Transfer(pipe, STEPControl_AsIs)
    status = writer.Write(output_file)
    
    if status == IFSelect_RetDone:
        print(f"✓ Exported: {output_file}")
    else:
        print(f"✗ ERROR: Failed to export {output_file}")
    
    return output_file


def main():
    parser = argparse.ArgumentParser(description='Generate pipe with weld bevels')
    parser.add_argument('nps', type=float, help='Nominal Pipe Size (inches)')
    parser.add_argument('schedule', type=str, help='Pipe schedule (20, 40, 80, etc.)')
    parser.add_argument('--length', '-l', type=float, default=480.0,
                        help='Pipe length in inches (default: 480" = 40 ft)')
    parser.add_argument('--bevel-angle', type=float, default=37.5,
                        help='Weld bevel angle (default: 37.5°)')
    parser.add_argument('--land', type=float, default=0.0625,
                        help='Weld bevel land in inches (default: 0.0625 = 1/16")')
    parser.add_argument('--output', '-o', type=str, default=None,
                        help='Output STEP filename')
    
    args = parser.parse_args()
    
    generate_pipe(
        nps=args.nps,
        schedule=args.schedule,
        length_inches=args.length,
        bevel_angle=args.bevel_angle,
        bevel_land=args.land,
        output_file=args.output
    )


if __name__ == '__main__':
    main()
