"""
Pressure Vessel Generator - pythonocc
Generates pressure vessels with various head types
Units: INCHES
Head Types:
  Hemispherical (2:1 ratio - half sphere)
  Elliptical (2:1 ASME standard elliptical)
  Torispherical (ASME F&D - flanged and dished)
  Flat (simple flat plate)

Shell: Rolled plate cylinder based on specified ID/OD and wall thickness
"""

import math
import argparse
from pathlib import Path
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCylinder, BRepPrimAPI_MakeSphere
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut, BRepAlgoAPI_Fuse
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeWire, BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeFace
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeRevol
from OCC.Core.gp import gp_Ax1, gp_Ax2, gp_Pnt, gp_Dir, gp_Vec, gp_Circ
from OCC.Core.GC import GC_MakeArcOfEllipse, GC_MakeArcOfCircle, GC_MakeSegment
from OCC.Core.Geom import Geom_Ellipse
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.IFSelect import IFSelect_RetDone
from OCC.Core.Interface import Interface_Static
from OCC.Core.TopoDS import TopoDS_Shape

# Set STEP export units to INCHES
Interface_Static.SetCVal("write.step.unit", "IN")


# Standard wall thicknesses (inches) for reference
COMMON_WALL_THICKNESSES = [
    0.25, 0.3125, 0.375, 0.4375, 0.5, 0.5625, 0.625, 0.75, 0.875, 1.0,
    1.125, 1.25, 1.375, 1.5, 1.75, 2.0, 2.5, 3.0
]


def generate_hemispherical_head(ID: float, wall: float, at_end: str = 'top') -> TopoDS_Shape:
    """
    Generate a hemispherical head (half sphere).
    
    Parameters:
        ID: Inside diameter (inches)
        wall: Wall thickness (inches)
        at_end: 'top' or 'bottom' - which end of vessel
    
    Returns:
        TopoDS_Shape of the head
    """
    OD = ID + 2 * wall
    outer_radius = OD / 2
    inner_radius = ID / 2
    
    # Create outer hemisphere
    if at_end == 'top':
        ax = gp_Ax2(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1))
        outer_sphere = BRepPrimAPI_MakeSphere(ax, outer_radius, 0, math.pi/2).Shape()
        inner_sphere = BRepPrimAPI_MakeSphere(ax, inner_radius, 0, math.pi/2).Shape()
    else:  # bottom
        ax = gp_Ax2(gp_Pnt(0, 0, 0), gp_Dir(0, 0, -1))
        outer_sphere = BRepPrimAPI_MakeSphere(ax, outer_radius, 0, math.pi/2).Shape()
        inner_sphere = BRepPrimAPI_MakeSphere(ax, inner_radius, 0, math.pi/2).Shape()
    
    # Hollow it out
    cut_op = BRepAlgoAPI_Cut(outer_sphere, inner_sphere)
    cut_op.Build()
    return cut_op.Shape()


def generate_elliptical_head(ID: float, wall: float, ratio: float = 2.0, at_end: str = 'top') -> TopoDS_Shape:
    """
    Generate a 2:1 elliptical head (ASME standard).
    
    The 2:1 ratio means the major axis is 2x the minor axis.
    Major axis = ID (diameter), Minor axis = ID/4 (for 2:1, height = ID/4)
    
    Parameters:
        ID: Inside diameter (inches)
        wall: Wall thickness (inches)
        ratio: Major/minor axis ratio (default 2.0 for ASME 2:1)
        at_end: 'top' or 'bottom' - which end of vessel
    
    Returns:
        TopoDS_Shape of the head
    """
    from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform
    from OCC.Core.gp import gp_Trsf, gp_GTrsf
    from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_GTransform
    
    OD = ID + 2 * wall
    
    # 2:1 ellipse: height = diameter / 4
    inner_radius = ID / 2
    inner_height = ID / (2 * ratio)  # = ID/4 for 2:1 ratio
    outer_radius = OD / 2
    outer_height = inner_height + wall
    
    # Create outer ellipsoid by scaling a hemisphere
    # Start with hemisphere of radius = outer_radius
    if at_end == 'top':
        ax = gp_Ax2(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1))
    else:
        ax = gp_Ax2(gp_Pnt(0, 0, 0), gp_Dir(0, 0, -1))
    
    outer_hemi = BRepPrimAPI_MakeSphere(ax, outer_radius, 0, math.pi/2).Shape()
    inner_hemi = BRepPrimAPI_MakeSphere(ax, inner_radius, 0, math.pi/2).Shape()
    
    # Scale Z axis to create ellipsoid (2:1 ratio means height = radius/2)
    scale_factor = outer_height / outer_radius  # This should be ~0.5 for 2:1
    
    # Use GTransform for non-uniform scaling
    gtrsf_outer = gp_GTrsf()
    gtrsf_outer.SetValue(1, 1, 1.0)  # X scale
    gtrsf_outer.SetValue(2, 2, 1.0)  # Y scale  
    gtrsf_outer.SetValue(3, 3, scale_factor)  # Z scale
    
    outer_ellipsoid = BRepBuilderAPI_GTransform(outer_hemi, gtrsf_outer, True).Shape()
    
    # Scale inner hemisphere
    inner_scale = inner_height / inner_radius
    gtrsf_inner = gp_GTrsf()
    gtrsf_inner.SetValue(1, 1, 1.0)
    gtrsf_inner.SetValue(2, 2, 1.0)
    gtrsf_inner.SetValue(3, 3, inner_scale)
    
    inner_ellipsoid = BRepBuilderAPI_GTransform(inner_hemi, gtrsf_inner, True).Shape()
    
    # Cut inner from outer
    cut_op = BRepAlgoAPI_Cut(outer_ellipsoid, inner_ellipsoid)
    cut_op.Build()
    
    return cut_op.Shape()


def generate_torispherical_head(ID: float, wall: float, at_end: str = 'top') -> TopoDS_Shape:
    """
    Generate a torispherical (F&D - Flanged and Dished) head.
    
    ASME F&D Standard - approximated using 2:1 ellipsoid geometry.
    For manufacturing, true F&D uses compound curves (dish + knuckle radii).
    
    Parameters:
        ID: Inside diameter (inches)
        wall: Wall thickness (inches)
        at_end: 'top' or 'bottom' - which end of vessel
    
    Returns:
        TopoDS_Shape of the head
    """
    from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_GTransform
    from OCC.Core.gp import gp_GTrsf
    
    OD = ID + 2 * wall
    
    # Use 2:1 ellipsoid approximation (same as elliptical for simplicity)
    inner_radius = ID / 2
    inner_height = ID / 4  # approximate F&D depth
    outer_radius = OD / 2
    outer_height = inner_height + wall
    
    # Create outer ellipsoid by scaling a hemisphere
    if at_end == 'top':
        ax = gp_Ax2(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1))
    else:
        ax = gp_Ax2(gp_Pnt(0, 0, 0), gp_Dir(0, 0, -1))
    
    outer_hemi = BRepPrimAPI_MakeSphere(ax, outer_radius, 0, math.pi/2).Shape()
    inner_hemi = BRepPrimAPI_MakeSphere(ax, inner_radius, 0, math.pi/2).Shape()
    
    # Scale Z axis to create ellipsoid
    scale_factor = outer_height / outer_radius
    
    gtrsf_outer = gp_GTrsf()
    gtrsf_outer.SetValue(1, 1, 1.0)
    gtrsf_outer.SetValue(2, 2, 1.0)
    gtrsf_outer.SetValue(3, 3, scale_factor)
    
    outer_ellipsoid = BRepBuilderAPI_GTransform(outer_hemi, gtrsf_outer, True).Shape()
    
    # Scale inner hemisphere
    inner_scale = inner_height / inner_radius
    gtrsf_inner = gp_GTrsf()
    gtrsf_inner.SetValue(1, 1, 1.0)
    gtrsf_inner.SetValue(2, 2, 1.0)
    gtrsf_inner.SetValue(3, 3, inner_scale)
    
    inner_ellipsoid = BRepBuilderAPI_GTransform(inner_hemi, gtrsf_inner, True).Shape()
    
    # Cut inner from outer
    cut_op = BRepAlgoAPI_Cut(outer_ellipsoid, inner_ellipsoid)
    cut_op.Build()
    
    return cut_op.Shape()


def generate_flat_head(ID: float, wall: float, head_thickness: float = None, at_end: str = 'top') -> TopoDS_Shape:
    """
    Generate a flat head (simple disc).
    
    Parameters:
        ID: Inside diameter (inches)
        wall: Wall thickness (inches)
        head_thickness: Thickness of flat head (default = wall * 2 for strength)
        at_end: 'top' or 'bottom' - which end of vessel
    
    Returns:
        TopoDS_Shape of the head
    """
    OD = ID + 2 * wall
    if head_thickness is None:
        head_thickness = wall * 2  # flat heads are typically thicker
    
    radius = OD / 2
    
    if at_end == 'top':
        ax = gp_Ax2(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1))
        head = BRepPrimAPI_MakeCylinder(ax, radius, head_thickness).Shape()
    else:  # bottom
        ax = gp_Ax2(gp_Pnt(0, 0, -head_thickness), gp_Dir(0, 0, 1))
        head = BRepPrimAPI_MakeCylinder(ax, radius, head_thickness).Shape()
    
    return head


def generate_shell(ID: float, wall: float, length: float) -> TopoDS_Shape:
    """
    Generate the cylindrical shell portion.
    
    Parameters:
        ID: Inside diameter (inches)
        wall: Wall thickness (inches)
        length: Shell length (tan-to-tan, inches)
    
    Returns:
        TopoDS_Shape of the shell
    """
    OD = ID + 2 * wall
    outer_radius = OD / 2
    inner_radius = ID / 2
    
    # Create cylinders centered at z=0
    ax = gp_Ax2(gp_Pnt(0, 0, -length/2), gp_Dir(0, 0, 1))
    outer_cyl = BRepPrimAPI_MakeCylinder(ax, outer_radius, length).Shape()
    
    ax_inner = gp_Ax2(gp_Pnt(0, 0, -length/2 - 1), gp_Dir(0, 0, 1))  # extend to ensure clean cut
    inner_cyl = BRepPrimAPI_MakeCylinder(ax_inner, inner_radius, length + 2).Shape()
    
    cut_op = BRepAlgoAPI_Cut(outer_cyl, inner_cyl)
    cut_op.Build()
    return cut_op.Shape()


def generate_pressure_vessel(
    ID: float,
    wall: float,
    shell_length: float,
    head_type: str = 'elliptical',
    head_type_top: str = None,
    head_type_bottom: str = None,
    output_file: str = None
):
    """
    Generate a complete pressure vessel with shell and heads.
    
    Parameters:
        ID: Inside diameter (inches)
        wall: Wall thickness (inches)
        shell_length: Tangent-to-tangent shell length (inches)
        head_type: Default head type for both ends ('hemispherical', 'elliptical', 'torispherical', 'flat')
        head_type_top: Override head type for top (optional)
        head_type_bottom: Override head type for bottom (optional)
        output_file: Output STEP filename (auto-generated if None)
    
    Returns:
        Path to generated STEP file
    """
    OD = ID + 2 * wall
    
    # Resolve head types
    top_type = head_type_top if head_type_top else head_type
    bottom_type = head_type_bottom if head_type_bottom else head_type
    
    print(f"=== Pressure Vessel Parameters ===")
    print(f"ID: {ID}\" = {ID * 25.4:.1f} mm")
    print(f"OD: {OD}\" = {OD * 25.4:.1f} mm")
    print(f"Wall: {wall}\" = {wall * 25.4:.2f} mm")
    print(f"Shell Length (T-T): {shell_length}\" = {shell_length * 25.4:.1f} mm")
    print(f"Top Head: {top_type}")
    print(f"Bottom Head: {bottom_type}")
    
    # Generate shell
    shell = generate_shell(ID, wall, shell_length)
    print("Shell created")
    
    # Generate heads
    head_generators = {
        'hemispherical': generate_hemispherical_head,
        'elliptical': generate_elliptical_head,
        'torispherical': generate_torispherical_head,
        'flat': generate_flat_head,
    }
    
    # Calculate head heights for positioning
    if top_type == 'hemispherical':
        top_height = OD / 2  # hemisphere height = radius
    elif top_type in ['elliptical', 'torispherical']:
        top_height = ID / 4 + wall  # 2:1 ellipse height
    else:  # flat
        top_height = wall * 2
    
    if bottom_type == 'hemispherical':
        bottom_height = OD / 2
    elif bottom_type in ['elliptical', 'torispherical']:
        bottom_height = ID / 4 + wall
    else:  # flat
        bottom_height = wall * 2
    
    # Generate top head
    if top_type in head_generators:
        top_head = head_generators[top_type](ID, wall, at_end='top')
        print(f"Top head ({top_type}) created")
    else:
        raise ValueError(f"Unknown head type: {top_type}")
    
    # Generate bottom head
    if bottom_type in head_generators:
        bottom_head = head_generators[bottom_type](ID, wall, at_end='bottom')
        print(f"Bottom head ({bottom_type}) created")
    else:
        raise ValueError(f"Unknown head type: {bottom_type}")
    
    # Position heads - shell is centered at z=0, extends from -L/2 to +L/2
    from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform
    from OCC.Core.gp import gp_Trsf
    
    # Move top head to top of shell
    trsf_top = gp_Trsf()
    trsf_top.SetTranslation(gp_Vec(0, 0, shell_length/2))
    top_head = BRepBuilderAPI_Transform(top_head, trsf_top).Shape()
    
    # Move bottom head to bottom of shell
    trsf_bottom = gp_Trsf()
    trsf_bottom.SetTranslation(gp_Vec(0, 0, -shell_length/2))
    bottom_head = BRepBuilderAPI_Transform(bottom_head, trsf_bottom).Shape()
    
    # Fuse all parts together
    fuse1 = BRepAlgoAPI_Fuse(shell, top_head)
    fuse1.Build()
    vessel = fuse1.Shape()
    
    fuse2 = BRepAlgoAPI_Fuse(vessel, bottom_head)
    fuse2.Build()
    vessel = fuse2.Shape()
    print("Vessel assembled")
    
    # Calculate overall dimensions
    overall_length = shell_length + top_height + bottom_height
    print(f"\n=== Final Dimensions ===")
    print(f"Overall Length: {overall_length:.2f}\" = {overall_length * 25.4:.1f} mm")
    print(f"Top Head Height: {top_height:.2f}\"")
    print(f"Bottom Head Height: {bottom_height:.2f}\"")
    
    # Generate output filename
    if output_file is None:
        id_str = str(int(ID)) if ID == int(ID) else str(ID).replace('.', '-')
        output_file = f"PressureVessel-ID{id_str}-Wall{wall}-L{int(shell_length)}-{top_type[:4].title()}-{bottom_type[:4].title()}.step"
    
    # Export STEP file
    writer = STEPControl_Writer()
    writer.Transfer(vessel, STEPControl_AsIs)
    status = writer.Write(output_file)
    if status == IFSelect_RetDone:
        print(f"\nExported: {output_file}")
    else:
        print(f"ERROR: Failed to export {output_file}")
    
    return output_file


def main():
    parser = argparse.ArgumentParser(description='Generate pressure vessels with various head types')
    parser.add_argument('ID', type=float, help='Inside diameter (inches)')
    parser.add_argument('wall', type=float, help='Wall thickness (inches)')
    parser.add_argument('length', type=float, help='Shell length, tangent-to-tangent (inches)')
    parser.add_argument('--head', '-H', default='elliptical',
                        choices=['hemispherical', 'elliptical', 'torispherical', 'flat'],
                        help='Head type for both ends (default: elliptical)')
    parser.add_argument('--top', type=str, default=None,
                        choices=['hemispherical', 'elliptical', 'torispherical', 'flat'],
                        help='Override head type for top end')
    parser.add_argument('--bottom', type=str, default=None,
                        choices=['hemispherical', 'elliptical', 'torispherical', 'flat'],
                        help='Override head type for bottom end')
    parser.add_argument('--output', '-o', type=str, default=None,
                        help='Output STEP filename')
    
    args = parser.parse_args()
    
    generate_pressure_vessel(
        ID=args.ID,
        wall=args.wall,
        shell_length=args.length,
        head_type=args.head,
        head_type_top=args.top,
        head_type_bottom=args.bottom,
        output_file=args.output
    )


if __name__ == '__main__':
    main()
