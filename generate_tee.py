"""
Tee Generator - pythonocc
Generates pipe tees with ASME B16.25 weld bevels
Units: INCHES
Tee Types:
  Equal    - All three ends same size
  Reducing - Branch (and optionally outlet) smaller than run

Geometry: Run pipe + perpendicular branch, beveled ends

Bevel: ASME B16.25 - 37.5° angle, 1/16" land
"""

import math
import argparse
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCylinder
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut, BRepAlgoAPI_Fuse
from OCC.Core.BRepFilletAPI import BRepFilletAPI_MakeChamfer
from OCC.Core.gp import gp_Ax2, gp_Pnt, gp_Dir, gp_Trsf, gp_Vec
from OCC.Core.TopAbs import TopAbs_EDGE, TopAbs_FACE
from OCC.Core.TopTools import TopTools_IndexedDataMapOfShapeListOfShape, TopTools_IndexedMapOfShape, TopTools_ListIteratorOfListOfShape
from OCC.Core.TopExp import topexp
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.IFSelect import IFSelect_RetDone
from OCC.Core.Interface import Interface_Static
from OCC.Core.BRepAdaptor import BRepAdaptor_Curve, BRepAdaptor_Surface
from OCC.Core.GeomAbs import GeomAbs_Circle, GeomAbs_Cylinder
from OCC.Core.TopoDS import topods
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform

# Set STEP export units to INCHES
Interface_Static.SetCVal("write.step.unit", "IN")

# Import complete pipe data
from pipe_data_complete import PIPE_DATA, get_pipe_dimensions


def generate_tee(
    run_nps: float,
    run_schedule: str,
    branch_nps: float = None,
    branch_schedule: str = None,
    bevel_angle_inlet: float = 37.5,
    bevel_land_inlet: float = 1/16,
    bevel_angle_outlet: float = 37.5,
    bevel_land_outlet: float = 1/16,
    bevel_angle_branch: float = 37.5,
    bevel_land_branch: float = 1/16,
    output_file: str = None
):
    """
    Generate a pipe tee with weld bevels.
    
    Parameters:
        run_nps: Nominal Pipe Size for run (inches)
        run_schedule: Pipe schedule for run ('40', '80', '160', etc.)
        branch_nps: NPS for branch (None = equal tee, same as run)
        branch_schedule: Schedule for branch (None = same as run)
        bevel_angle_inlet: Run inlet bevel angle (default 37.5°, set 0 for square cut)
        bevel_land_inlet: Run inlet land thickness (default 1/16")
        bevel_angle_outlet: Run outlet bevel angle (default 37.5°, set 0 for square cut)
        bevel_land_outlet: Run outlet land thickness (default 1/16")
        bevel_angle_branch: Branch bevel angle (default 37.5°, set 0 for square cut)
        bevel_land_branch: Branch land thickness (default 1/16")
        output_file: Output STEP filename (auto-generated if None)
    
    Note: Common bevel angles: 37.5° (ASME standard), 30° (shop practice)
    
    Returns:
        Path to generated STEP file
    """
    
    # Get run dimensions
    RUN_OD, RUN_WALL = get_pipe_dimensions(run_nps, run_schedule)
    RUN_ID = RUN_OD - 2 * RUN_WALL
    
    # Get branch dimensions (default to equal tee)
    if branch_nps is None:
        branch_nps = run_nps
    if branch_schedule is None:
        branch_schedule = run_schedule
    
    BRANCH_OD, BRANCH_WALL = get_pipe_dimensions(branch_nps, branch_schedule)
    BRANCH_ID = BRANCH_OD - 2 * BRANCH_WALL
    
    is_equal = (run_nps == branch_nps)
    
    # Tee dimensions per ASME B16.9
    # C = Center to end (run) 
    # M = Center to end (branch/outlet)
    # For simplicity, use standard proportions:
    # Run length = 2 x OD (1 x OD each side of center)
    # Branch height = 1 x Run_OD (from centerline of run to end of branch)
    
    RUN_LENGTH = RUN_OD * 2.0  # Total run length
    BRANCH_HEIGHT = RUN_OD * 1.0  # From run centerline to branch end
    
    print(f"=== Tee Parameters ===")
    print(f"Run: NPS {run_nps}\" Sch {run_schedule}")
    print(f"  OD = {RUN_OD}\" = {RUN_OD * 25.4:.2f} mm")
    print(f"  ID = {RUN_ID:.4f}\" = {RUN_ID * 25.4:.2f} mm")
    print(f"  Wall = {RUN_WALL}\" = {RUN_WALL * 25.4:.2f} mm")
    print(f"Branch: NPS {branch_nps}\" Sch {branch_schedule}")
    print(f"  OD = {BRANCH_OD}\" = {BRANCH_OD * 25.4:.2f} mm")
    print(f"  ID = {BRANCH_ID:.4f}\" = {BRANCH_ID * 25.4:.2f} mm")
    print(f"  Wall = {BRANCH_WALL}\" = {BRANCH_WALL * 25.4:.2f} mm")
    print(f"Type: {'Equal' if is_equal else 'Reducing'} Tee")
    print(f"Run Length = {RUN_LENGTH}\" = {RUN_LENGTH * 25.4:.2f} mm")
    print(f"Branch Height = {BRANCH_HEIGHT}\" = {BRANCH_HEIGHT * 25.4:.2f} mm")
    
    # === CREATE RUN PIPE (HOLLOW) ===
    # Run along X-axis, centered at origin
    run_start = gp_Pnt(-RUN_LENGTH/2, 0, 0)
    run_ax = gp_Ax2(run_start, gp_Dir(1, 0, 0))  # X direction
    
    outer_run = BRepPrimAPI_MakeCylinder(run_ax, RUN_OD/2, RUN_LENGTH).Shape()
    inner_run = BRepPrimAPI_MakeCylinder(run_ax, RUN_ID/2, RUN_LENGTH).Shape()
    run_pipe = BRepAlgoAPI_Cut(outer_run, inner_run).Shape()
    print("Run pipe created (hollow)")
    
    # === CREATE BRANCH PIPE (HOLLOW) ===
    # Branch along Z-axis, starting at run CENTERLINE (z=0)
    # Goes from center of run up to BRANCH_HEIGHT
    branch_start = gp_Pnt(0, 0, 0)  # Start at run centerline
    branch_ax = gp_Ax2(branch_start, gp_Dir(0, 0, 1))  # Z direction
    
    outer_branch = BRepPrimAPI_MakeCylinder(branch_ax, BRANCH_OD/2, BRANCH_HEIGHT).Shape()
    inner_branch = BRepPrimAPI_MakeCylinder(branch_ax, BRANCH_ID/2, BRANCH_HEIGHT).Shape()
    branch_pipe = BRepAlgoAPI_Cut(outer_branch, inner_branch).Shape()
    print("Branch pipe created (hollow, from run centerline)")
    
    # === FUSE RUN AND BRANCH ===
    # Two hollow pipes fused together
    fuse_op = BRepAlgoAPI_Fuse(run_pipe, branch_pipe)
    fuse_op.Build()
    tee = fuse_op.Shape()
    print("Tee fused")
    
    # === CUT RUN BORE TO CLEAR INTERSECTION ===
    # Full cut of run ID through the entire length to clear any blockage
    run_bore_start = gp_Pnt(-RUN_LENGTH/2 - 1, 0, 0)
    run_bore_ax = gp_Ax2(run_bore_start, gp_Dir(1, 0, 0))
    run_bore = BRepPrimAPI_MakeCylinder(run_bore_ax, RUN_ID/2, RUN_LENGTH + 2).Shape()
    
    cut_op = BRepAlgoAPI_Cut(tee, run_bore)
    cut_op.Build()
    tee = cut_op.Shape()
    print("Run bore cut to clear intersection")
    
    # === APPLY BEVELS ===
    # Find the 3 outer edges at the ends (2 run ends + 1 branch end)
    chamfer_size_inlet = RUN_WALL - bevel_land_inlet if bevel_angle_inlet > 0 else 0
    chamfer_size_outlet = RUN_WALL - bevel_land_outlet if bevel_angle_outlet > 0 else 0
    chamfer_size_branch = BRANCH_WALL - bevel_land_branch if bevel_angle_branch > 0 else 0
    
    print(f"=== Bevel Parameters ===")
    if bevel_angle_inlet > 0:
        print(f"Run Inlet: {chamfer_size_inlet:.4f}\" chamfer @ {bevel_angle_inlet}°, land={bevel_land_inlet * 25.4:.3f}mm")
    else:
        print(f"Run Inlet: Square cut (no bevel)")
    
    if bevel_angle_outlet > 0:
        print(f"Run Outlet: {chamfer_size_outlet:.4f}\" chamfer @ {bevel_angle_outlet}°, land={bevel_land_outlet * 25.4:.3f}mm")
    else:
        print(f"Run Outlet: Square cut (no bevel)")
    
    if bevel_angle_branch > 0:
        print(f"Branch: {chamfer_size_branch:.4f}\" chamfer @ {bevel_angle_branch}°, land={bevel_land_branch * 25.4:.3f}mm")
    else:
        print(f"Branch: Square cut (no bevel)")
    
    # Get all edges
    edge_map = TopTools_IndexedMapOfShape()
    topexp.MapShapes(tee, TopAbs_EDGE, edge_map)
    num_edges = edge_map.Size()
    
    # Build edge->face map
    edge_face_map = TopTools_IndexedDataMapOfShapeListOfShape()
    topexp.MapShapesAndAncestors(tee, TopAbs_EDGE, TopAbs_FACE, edge_face_map)
    
    # Find outer edges at tee ends
    # Run ends: circles at x = ±RUN_LENGTH/2, radius = RUN_OD/2
    # Branch end: circle at z = BRANCH_HEIGHT, radius = BRANCH_OD/2
    
    run_end_x_neg = -RUN_LENGTH/2
    run_end_x_pos = RUN_LENGTH/2
    branch_end_z = BRANCH_HEIGHT  # Branch end is at BRANCH_HEIGHT from run centerline
    
    edges_to_chamfer = []
    
    for i in range(1, num_edges + 1):
        edge = edge_map.FindKey(i)
        adaptor = BRepAdaptor_Curve(edge)
        if adaptor.GetType() == GeomAbs_Circle:
            radius = adaptor.Circle().Radius()
            center = adaptor.Circle().Location()
            cx, cy, cz = center.X(), center.Y(), center.Z()
            
            # Check for run end edges (outer diameter) and identify inlet vs outlet
            if abs(radius - RUN_OD/2) < 0.01:
                if abs(cx - run_end_x_neg) < 0.1:
                    # Run inlet (negative X)
                    face = find_cylinder_face(edge, edge_face_map, RUN_OD/2)
                    if face is not None:
                        edges_to_chamfer.append((edge, face, chamfer_size_inlet, bevel_angle_inlet, 'run inlet'))
                elif abs(cx - run_end_x_pos) < 0.1:
                    # Run outlet (positive X)
                    face = find_cylinder_face(edge, edge_face_map, RUN_OD/2)
                    if face is not None:
                        edges_to_chamfer.append((edge, face, chamfer_size_outlet, bevel_angle_outlet, 'run outlet'))
            
            # Check for branch end edge (outer diameter)
            if abs(radius - BRANCH_OD/2) < 0.01:
                if abs(cz - branch_end_z) < 0.1:
                    # This is the branch end outer edge
                    face = find_cylinder_face(edge, edge_face_map, BRANCH_OD/2)
                    if face is not None:
                        edges_to_chamfer.append((edge, face, chamfer_size_branch, bevel_angle_branch, 'branch'))
    
    print(f"Found {len(edges_to_chamfer)} outer edges to chamfer")
    
    # Apply chamfers
    if edges_to_chamfer:
        chamfer = BRepFilletAPI_MakeChamfer(tee)
        for edge, face, size, angle, location in edges_to_chamfer:
            if angle > 0:  # Only apply if bevel requested
                chamfer.AddDA(size, math.radians(angle), edge, face)
                print(f"  Added {location} bevel: Size={size:.4f}\" @ {angle}°")
        chamfer.Build()
        if chamfer.IsDone():
            tee = chamfer.Shape()
            print("Bevels applied successfully!")
        else:
            print("WARNING: Chamfer failed!")
    
    # Generate output filename
    if output_file is None:
        run_str = str(run_nps).replace('.', '-')
        branch_str = str(branch_nps).replace('.', '-')
        if is_equal:
            output_file = f"Tee-Equal-NPS{run_str}-Sch{run_schedule}.step"
        else:
            output_file = f"Tee-Reducing-{run_str}x{branch_str}-Sch{run_schedule}.step"
    
    # Export STEP file
    writer = STEPControl_Writer()
    writer.Transfer(tee, STEPControl_AsIs)
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
    parser = argparse.ArgumentParser(description='Generate pipe tees with weld bevels')
    parser.add_argument('run_nps', type=float, help='Nominal Pipe Size for run (inches)')
    parser.add_argument('run_schedule', type=str, help='Pipe schedule for run (40, 80, 160, etc.)')
    parser.add_argument('--branch-nps', '-b', type=float, default=None,
                        help='NPS for branch (default: same as run = equal tee)')
    parser.add_argument('--branch-schedule', '-s', type=str, default=None,
                        help='Schedule for branch (default: same as run)')
    parser.add_argument('--bevel-angle', type=float, default=37.5,
                        help='Weld bevel angle (default: 37.5)')
    parser.add_argument('--land', type=float, default=0.0625,
                        help='Weld bevel land thickness in inches (default: 0.0625 = 1/16)')
    parser.add_argument('--output', '-o', type=str, default=None,
                        help='Output STEP filename')
    
    args = parser.parse_args()
    
    generate_tee(
        run_nps=args.run_nps,
        run_schedule=args.run_schedule,
        branch_nps=args.branch_nps,
        branch_schedule=args.branch_schedule,
        bevel_angle=args.bevel_angle,
        bevel_land=args.land,
        output_file=args.output
    )


if __name__ == '__main__':
    main()
