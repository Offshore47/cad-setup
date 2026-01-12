"""
Cross Generator - pythonocc
Generates pipe crosses with ASME B16.25 weld bevels
Units: INCHES
Cross: Run pipe with two perpendicular branches (up and down)
All 4 ends same size (equal cross)

Bevel: ASME B16.25 - 37.5° angle, 1/16" land
"""

import math
import argparse
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCylinder
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut, BRepAlgoAPI_Fuse
from OCC.Core.BRepFilletAPI import BRepFilletAPI_MakeChamfer
from OCC.Core.gp import gp_Ax2, gp_Pnt, gp_Dir
from OCC.Core.TopAbs import TopAbs_EDGE, TopAbs_FACE
from OCC.Core.TopTools import TopTools_IndexedDataMapOfShapeListOfShape, TopTools_IndexedMapOfShape, TopTools_ListIteratorOfListOfShape
from OCC.Core.TopExp import topexp
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.IFSelect import IFSelect_RetDone
from OCC.Core.Interface import Interface_Static
from OCC.Core.BRepAdaptor import BRepAdaptor_Curve, BRepAdaptor_Surface
from OCC.Core.GeomAbs import GeomAbs_Circle, GeomAbs_Cylinder
from OCC.Core.TopoDS import topods

# Set STEP export units to INCHES
Interface_Static.SetCVal("write.step.unit", "IN")

# Import complete pipe data
from pipe_data_complete import PIPE_DATA, get_pipe_dimensions


def generate_cross(
    nps: float,
    schedule: str,
    bevel_angle_end1: float = 37.5,
    bevel_land_end1: float = 1/16,
    bevel_angle_end2: float = 37.5,
    bevel_land_end2: float = 1/16,
    bevel_angle_end3: float = 37.5,
    bevel_land_end3: float = 1/16,
    bevel_angle_end4: float = 37.5,
    bevel_land_end4: float = 1/16,
    output_file: str = None
):
    """
    Generate a pipe cross with weld bevels.
    
    Parameters:
        nps: Nominal Pipe Size (inches)
        schedule: Pipe schedule ('40', '80', '160', etc.)
        bevel_angle_end1: End 1 bevel angle (default 37.5°, set 0 for square cut)
        bevel_land_end1: End 1 land thickness (default 1/16")
        bevel_angle_end2: End 2 bevel angle (default 37.5°, set 0 for square cut)
        bevel_land_end2: End 2 land thickness (default 1/16")
        bevel_angle_end3: End 3 bevel angle (default 37.5°, set 0 for square cut)
        bevel_land_end3: End 3 land thickness (default 1/16")
        bevel_angle_end4: End 4 bevel angle (default 37.5°, set 0 for square cut)
        bevel_land_end4: End 4 land thickness (default 1/16")
        output_file: Output STEP filename (auto-generated if None)
    
    Note: Common bevel angles: 37.5° (ASME standard), 30° (shop practice)
    
    Returns:
        Path to generated STEP file
    """
    
    # Get pipe dimensions
    OD, WALL = get_pipe_dimensions(nps, schedule)
    ID = OD - 2 * WALL
    
    # Cross dimensions - same proportions as tee
    RUN_LENGTH = OD * 2.0  # Total run length
    BRANCH_HEIGHT = OD * 1.0  # From run centerline to branch end (each direction)
    
    print(f"=== Cross Parameters ===")
    print(f"NPS: {nps}\" Schedule: {schedule}")
    print(f"OD = {OD}\" = {OD * 25.4:.2f} mm")
    print(f"ID = {ID:.4f}\" = {ID * 25.4:.2f} mm")
    print(f"Wall = {WALL}\" = {WALL * 25.4:.2f} mm")
    print(f"Run Length = {RUN_LENGTH}\" = {RUN_LENGTH * 25.4:.2f} mm")
    print(f"Branch Height = {BRANCH_HEIGHT}\" = {BRANCH_HEIGHT * 25.4:.2f} mm (each direction)")
    
    # === CREATE RUN PIPE (HOLLOW) ===
    run_start = gp_Pnt(-RUN_LENGTH/2, 0, 0)
    run_ax = gp_Ax2(run_start, gp_Dir(1, 0, 0))
    
    outer_run = BRepPrimAPI_MakeCylinder(run_ax, OD/2, RUN_LENGTH).Shape()
    inner_run = BRepPrimAPI_MakeCylinder(run_ax, ID/2, RUN_LENGTH).Shape()
    run_pipe = BRepAlgoAPI_Cut(outer_run, inner_run).Shape()
    print("Run pipe created (hollow)")
    
    # === CREATE BRANCH UP (HOLLOW) ===
    branch_up_start = gp_Pnt(0, 0, 0)
    branch_up_ax = gp_Ax2(branch_up_start, gp_Dir(0, 0, 1))
    
    outer_branch_up = BRepPrimAPI_MakeCylinder(branch_up_ax, OD/2, BRANCH_HEIGHT).Shape()
    inner_branch_up = BRepPrimAPI_MakeCylinder(branch_up_ax, ID/2, BRANCH_HEIGHT).Shape()
    branch_up = BRepAlgoAPI_Cut(outer_branch_up, inner_branch_up).Shape()
    print("Branch up created (hollow)")
    
    # === CREATE BRANCH DOWN (HOLLOW) ===
    branch_down_start = gp_Pnt(0, 0, 0)
    branch_down_ax = gp_Ax2(branch_down_start, gp_Dir(0, 0, -1))  # Negative Z
    
    outer_branch_down = BRepPrimAPI_MakeCylinder(branch_down_ax, OD/2, BRANCH_HEIGHT).Shape()
    inner_branch_down = BRepPrimAPI_MakeCylinder(branch_down_ax, ID/2, BRANCH_HEIGHT).Shape()
    branch_down = BRepAlgoAPI_Cut(outer_branch_down, inner_branch_down).Shape()
    print("Branch down created (hollow)")
    
    # === FUSE ALL THREE ===
    fuse1 = BRepAlgoAPI_Fuse(run_pipe, branch_up)
    fuse1.Build()
    cross = fuse1.Shape()
    
    fuse2 = BRepAlgoAPI_Fuse(cross, branch_down)
    fuse2.Build()
    cross = fuse2.Shape()
    print("Cross fused")
    
    # === CUT RUN BORE TO CLEAR INTERSECTION ===
    run_bore_start = gp_Pnt(-RUN_LENGTH/2 - 1, 0, 0)
    run_bore_ax = gp_Ax2(run_bore_start, gp_Dir(1, 0, 0))
    run_bore = BRepPrimAPI_MakeCylinder(run_bore_ax, ID/2, RUN_LENGTH + 2).Shape()
    
    cut_op = BRepAlgoAPI_Cut(cross, run_bore)
    cut_op.Build()
    cross = cut_op.Shape()
    print("Run bore cut to clear intersection")
    
    # === APPLY BEVELS ===
    chamfer_size_end1 = WALL - bevel_land_end1 if bevel_angle_end1 > 0 else 0
    chamfer_size_end2 = WALL - bevel_land_end2 if bevel_angle_end2 > 0 else 0
    chamfer_size_end3 = WALL - bevel_land_end3 if bevel_angle_end3 > 0 else 0
    chamfer_size_end4 = WALL - bevel_land_end4 if bevel_angle_end4 > 0 else 0
    
    print(f"=== Bevel Parameters ===")
    if bevel_angle_end1 > 0:
        print(f"End 1 (-X): {chamfer_size_end1:.4f}\" chamfer @ {bevel_angle_end1}°, land={bevel_land_end1 * 25.4:.3f}mm")
    else:
        print(f"End 1 (-X): Square cut (no bevel)")
    
    if bevel_angle_end2 > 0:
        print(f"End 2 (+X): {chamfer_size_end2:.4f}\" chamfer @ {bevel_angle_end2}°, land={bevel_land_end2 * 25.4:.3f}mm")
    else:
        print(f"End 2 (+X): Square cut (no bevel)")
    
    if bevel_angle_end3 > 0:
        print(f"End 3 (+Z): {chamfer_size_end3:.4f}\" chamfer @ {bevel_angle_end3}°, land={bevel_land_end3 * 25.4:.3f}mm")
    else:
        print(f"End 3 (+Z): Square cut (no bevel)")
    
    if bevel_angle_end4 > 0:
        print(f"End 4 (-Z): {chamfer_size_end4:.4f}\" chamfer @ {bevel_angle_end4}°, land={bevel_land_end4 * 25.4:.3f}mm")
    else:
        print(f"End 4 (-Z): Square cut (no bevel)")
    
    # Get all edges
    edge_map = TopTools_IndexedMapOfShape()
    topexp.MapShapes(cross, TopAbs_EDGE, edge_map)
    num_edges = edge_map.Size()
    
    # Build edge->face map
    edge_face_map = TopTools_IndexedDataMapOfShapeListOfShape()
    topexp.MapShapesAndAncestors(cross, TopAbs_EDGE, TopAbs_FACE, edge_face_map)
    
    # Find outer edges at all 4 ends
    run_end_x_neg = -RUN_LENGTH/2
    run_end_x_pos = RUN_LENGTH/2
    branch_end_z_up = BRANCH_HEIGHT
    branch_end_z_down = -BRANCH_HEIGHT
    
    edges_to_chamfer = []
    
    for i in range(1, num_edges + 1):
        edge = edge_map.FindKey(i)
        adaptor = BRepAdaptor_Curve(edge)
        if adaptor.GetType() == GeomAbs_Circle:
            radius = adaptor.Circle().Radius()
            center = adaptor.Circle().Location()
            cx, cy, cz = center.X(), center.Y(), center.Z()
            
            # Check for outer diameter edges at ends
            if abs(radius - OD/2) < 0.01:
                # End 1 (negative X)
                if abs(cx - run_end_x_neg) < 0.1:
                    face = find_cylinder_face(edge, edge_face_map, OD/2)
                    if face is not None:
                        edges_to_chamfer.append((edge, face, chamfer_size_end1, bevel_angle_end1, 'end1 (-X)'))
                # End 2 (positive X)
                elif abs(cx - run_end_x_pos) < 0.1:
                    face = find_cylinder_face(edge, edge_face_map, OD/2)
                    if face is not None:
                        edges_to_chamfer.append((edge, face, chamfer_size_end2, bevel_angle_end2, 'end2 (+X)'))
                # End 3 (positive Z)
                elif abs(cz - branch_end_z_up) < 0.1:
                    face = find_cylinder_face(edge, edge_face_map, OD/2)
                    if face is not None:
                        edges_to_chamfer.append((edge, face, chamfer_size_end3, bevel_angle_end3, 'end3 (+Z)'))
                # End 4 (negative Z)
                elif abs(cz - branch_end_z_down) < 0.1:
                    face = find_cylinder_face(edge, edge_face_map, OD/2)
                    if face is not None:
                        edges_to_chamfer.append((edge, face, chamfer_size_end4, bevel_angle_end4, 'end4 (-Z)'))
    
    print(f"Found {len(edges_to_chamfer)} outer edges to chamfer")
    
    # Apply chamfers
    if edges_to_chamfer:
        chamfer = BRepFilletAPI_MakeChamfer(cross)
        for edge, face, size, angle, location in edges_to_chamfer:
            if angle > 0:  # Only apply if bevel requested
                chamfer.AddDA(size, math.radians(angle), edge, face)
                print(f"  Added {location} bevel: Size={size:.4f}\" @ {angle}°")
        chamfer.Build()
        if chamfer.IsDone():
            cross = chamfer.Shape()
            print("Bevels applied successfully!")
        else:
            print("WARNING: Chamfer failed!")
    
    # Generate output filename
    if output_file is None:
        nps_str = str(nps).replace('.', '-')
        output_file = f"Cross-NPS{nps_str}-Sch{schedule}.step"
    
    # Export STEP file
    writer = STEPControl_Writer()
    writer.Transfer(cross, STEPControl_AsIs)
    status = writer.Write(output_file)
    if status == IFSelect_RetDone:
        print(f"Exported: {output_file}")
    else:
        print(f"ERROR: Failed to export {output_file}")
    
    return output_file


def find_cylinder_face(edge, edge_face_map, target_radius):
    """Find the cylindrical face adjacent to an edge with given radius"""
    face_list = edge_face_map.FindFromKey(edge)
    cylinder_face = None
    first_face = None
    it = TopTools_ListIteratorOfListOfShape(face_list)
    while it.More():
        f = topods.Face(it.Value())
        if first_face is None:
            first_face = f
        surf = BRepAdaptor_Surface(f)
        if surf.GetType() == GeomAbs_Cylinder:
            cyl_radius = surf.Cylinder().Radius()
            if abs(cyl_radius - target_radius) < 0.01:
                cylinder_face = f
        it.Next()
    return cylinder_face if cylinder_face else first_face


def main():
    parser = argparse.ArgumentParser(description='Generate pipe crosses with weld bevels')
    parser.add_argument('nps', type=float, help='Nominal Pipe Size (inches)')
    parser.add_argument('schedule', type=str, help='Pipe schedule (40, 80, 160, etc.)')
    parser.add_argument('--bevel-angle', type=float, default=37.5,
                        help='Weld bevel angle (default: 37.5)')
    parser.add_argument('--land', type=float, default=0.0625,
                        help='Weld bevel land thickness in inches (default: 0.0625 = 1/16)')
    parser.add_argument('--output', '-o', type=str, default=None,
                        help='Output STEP filename')
    
    args = parser.parse_args()
    
    generate_cross(
        nps=args.nps,
        schedule=args.schedule,
        bevel_angle=args.bevel_angle,
        bevel_land=args.land,
        output_file=args.output
    )


if __name__ == '__main__':
    main()
