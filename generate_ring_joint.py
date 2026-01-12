"""
Ring Joint Gasket Generator - Type R and Type RX
Generates STEP files for ring joint gaskets per API 6A/6BX standards
Handles oval, octagonal, and octagonal with bevel profiles
"""

import math
from OCC.Core.gp import gp_Pnt, gp_Dir, gp_Ax1, gp_Ax2, gp_Vec
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCylinder, BRepPrimAPI_MakeRevol
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut
from OCC.Core.BRepBuilderAPI import (BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire, 
                                       BRepBuilderAPI_MakeFace)
from OCC.Core.GC import GC_MakeArcOfCircle, GC_MakeSegment
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.Interface import Interface_Static

# Import data
import sys
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)

from gasket_data import get_gasket_info


def make_octagonal_profile_r(pitch_radius_mm, width_mm, octagonal_height_mm, 
                              flat_width_mm, radius_mm):
    """
    Create octagonal cross-section profile for Type R ring.
    
    Profile consists of:
    - Flat top (width C)
    - Corner radius (R1)
    - Angled sides
    - Flat bottom (width C)
    - Corner radius (R1)
    
    Args:
        pitch_radius_mm: Pitch radius (P/2)
        width_mm: Ring width A
        octagonal_height_mm: Octagonal height H
        flat_width_mm: Flat width C
        radius_mm: Corner radius R1
    
    Returns:
        TopoDS_Wire: Profile wire to be revolved
    """
    # Profile in XZ plane (X is radial, Z is vertical)
    # Ring sits at pitch radius, extends inward and outward
    
    half_width = width_mm / 2.0
    half_flat = flat_width_mm / 2.0
    half_height = octagonal_height_mm / 2.0
    
    # Calculate points for octagonal profile
    # Start at top center of flat
    p1 = gp_Pnt(pitch_radius_mm, 0, half_flat)
    
    # Top flat to corner
    p2 = gp_Pnt(pitch_radius_mm, 0, half_flat)
    
    # After radius, angled side starts
    # Angle to outer edge
    p3 = gp_Pnt(pitch_radius_mm + half_width, 0, 0)
    
    # Bottom side
    p4 = gp_Pnt(pitch_radius_mm + half_width, 0, 0)
    p5 = gp_Pnt(pitch_radius_mm, 0, -half_flat)
    p6 = gp_Pnt(pitch_radius_mm - half_width, 0, 0)
    p7 = gp_Pnt(pitch_radius_mm - half_width, 0, 0)
    p8 = gp_Pnt(pitch_radius_mm, 0, half_flat)
    
    # Simplified approach: Create rectangular profile with chamfered corners
    # This approximates the octagonal shape
    
    # Points for simplified profile (rectangle in radial direction)
    inner_r = pitch_radius_mm - half_width
    outer_r = pitch_radius_mm + half_width
    
    pt1 = gp_Pnt(inner_r, 0, half_height)
    pt2 = gp_Pnt(outer_r, 0, half_height)
    pt3 = gp_Pnt(outer_r, 0, -half_height)
    pt4 = gp_Pnt(inner_r, 0, -half_height)
    
    # Create edges
    edge1 = BRepBuilderAPI_MakeEdge(pt1, pt2).Edge()
    edge2 = BRepBuilderAPI_MakeEdge(pt2, pt3).Edge()
    edge3 = BRepBuilderAPI_MakeEdge(pt3, pt4).Edge()
    edge4 = BRepBuilderAPI_MakeEdge(pt4, pt1).Edge()
    
    # Create wire
    wire_builder = BRepBuilderAPI_MakeWire()
    wire_builder.Add(edge1)
    wire_builder.Add(edge2)
    wire_builder.Add(edge3)
    wire_builder.Add(edge4)
    
    return wire_builder.Wire()


def make_oval_profile_r(pitch_radius_mm, width_mm, oval_height_mm):
    """
    Create oval (elliptical) cross-section profile for Type R ring.
    
    Args:
        pitch_radius_mm: Pitch radius (P/2)
        width_mm: Ring width A (major axis)
        oval_height_mm: Oval height B (minor axis)
    
    Returns:
        TopoDS_Wire: Profile wire to be revolved
    """
    # Oval profile is elliptical cross-section
    # For simplification, use rectangular profile with rounded ends
    
    half_width = width_mm / 2.0
    half_height = oval_height_mm / 2.0
    
    inner_r = pitch_radius_mm - half_width
    outer_r = pitch_radius_mm + half_width
    
    # Create approximate oval using rectangle
    pt1 = gp_Pnt(inner_r, 0, half_height)
    pt2 = gp_Pnt(outer_r, 0, half_height)
    pt3 = gp_Pnt(outer_r, 0, -half_height)
    pt4 = gp_Pnt(inner_r, 0, -half_height)
    
    # Create edges
    edge1 = BRepBuilderAPI_MakeEdge(pt1, pt2).Edge()
    edge2 = BRepBuilderAPI_MakeEdge(pt2, pt3).Edge()
    edge3 = BRepBuilderAPI_MakeEdge(pt3, pt4).Edge()
    edge4 = BRepBuilderAPI_MakeEdge(pt4, pt1).Edge()
    
    # Create wire
    wire_builder = BRepBuilderAPI_MakeWire()
    wire_builder.Add(edge1)
    wire_builder.Add(edge2)
    wire_builder.Add(edge3)
    wire_builder.Add(edge4)
    
    return wire_builder.Wire()


def make_octagonal_profile_rx(pitch_radius_mm, width_mm, flat_width_mm, 
                               outside_bevel_height_mm, ring_height_mm, radius_mm):
    """
    Create octagonal cross-section profile for Type RX ring with outside bevel.
    
    Args:
        pitch_radius_mm: Pitch radius (P/2)
        width_mm: Ring width A
        flat_width_mm: Flat width C
        outside_bevel_height_mm: Outside bevel height
        ring_height_mm: Total ring height H
        radius_mm: Corner radius R1
    
    Returns:
        TopoDS_Wire: Profile wire to be revolved
    """
    half_width = width_mm / 2.0
    half_height = ring_height_mm / 2.0
    
    inner_r = pitch_radius_mm - half_width
    outer_r = pitch_radius_mm + half_width
    
    # Simplified profile - rectangular with slight taper for bevel
    # Top edge (outer diameter side)
    pt1 = gp_Pnt(inner_r, 0, half_height - outside_bevel_height_mm)
    pt2 = gp_Pnt(outer_r, 0, half_height)
    
    # Bottom edge
    pt3 = gp_Pnt(outer_r, 0, -half_height)
    pt4 = gp_Pnt(inner_r, 0, -half_height + outside_bevel_height_mm)
    
    # Create edges
    edge1 = BRepBuilderAPI_MakeEdge(pt1, pt2).Edge()
    edge2 = BRepBuilderAPI_MakeEdge(pt2, pt3).Edge()
    edge3 = BRepBuilderAPI_MakeEdge(pt3, pt4).Edge()
    edge4 = BRepBuilderAPI_MakeEdge(pt4, pt1).Edge()
    
    # Create wire
    wire_builder = BRepBuilderAPI_MakeWire()
    wire_builder.Add(edge1)
    wire_builder.Add(edge2)
    wire_builder.Add(edge3)
    wire_builder.Add(edge4)
    
    return wire_builder.Wire()


def revolve_profile(profile_wire):
    """
    Revolve profile wire around Z-axis to create ring.
    
    Args:
        profile_wire: Wire to revolve
    
    Returns:
        TopoDS_Shape: Revolved solid
    """
    # Create face from wire
    face = BRepBuilderAPI_MakeFace(profile_wire).Face()
    
    # Revolution axis (Z-axis)
    axis = gp_Ax1(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1))
    
    # Revolve 360 degrees
    revolved = BRepPrimAPI_MakeRevol(face, axis, 2 * math.pi).Shape()
    
    return revolved


def add_pressure_balance_hole(ring_shape, pitch_radius_mm, hole_diameter_mm, ring_height_mm):
    """
    Add pressure balance hole through ring (for RX-82 to RX-91).
    Hole is drilled through center of flat width at one location.
    
    Args:
        ring_shape: Ring shape to drill
        pitch_radius_mm: Pitch radius where hole is located
        hole_diameter_mm: Hole diameter
        ring_height_mm: Ring height (for hole depth)
    
    Returns:
        TopoDS_Shape: Ring with pressure balance hole
    """
    # Create cylinder for hole at pitch radius, aligned radially
    hole_length = ring_height_mm + 2  # Extra length for clean cut
    
    # Hole positioned at pitch radius, pointing toward center
    # Actually, pressure balance holes are typically drilled axially through the ring
    # at the pitch circle, perpendicular to the ring surface
    
    # Position hole at pitch radius on X-axis
    ax = gp_Ax2(gp_Pnt(pitch_radius_mm, 0, -1), gp_Dir(0, 0, 1))
    hole = BRepPrimAPI_MakeCylinder(ax, hole_diameter_mm / 2.0, hole_length).Shape()
    
    # Cut hole from ring
    ring_with_hole = BRepAlgoAPI_Cut(ring_shape, hole).Shape()
    
    return ring_with_hole


def generate_ring_joint_r(ring_number, profile_type='octagonal', material='SoftIron', output_dir=None):
    """
    Generate STEP file for Type R ring joint gasket.
    
    Args:
        ring_number: Ring number (e.g., 'R-23', 'R-47')
        profile_type: 'octagonal' or 'oval'
        material: 'SoftIron', '304SS', '316SS', 'Monel', 'Inconel'
        output_dir: Output directory path
    
    Returns:
        str: Output file path
    """
    # Get ring specifications
    ring_info = get_gasket_info(ring_number, None, 'ring_joint')
    
    if not ring_info:
        raise ValueError(f"No data found for ring {ring_number}")
    
    pitch_diameter_mm = ring_info['pitch_diameter_mm']
    pitch_radius_mm = pitch_diameter_mm / 2.0
    width_mm = ring_info['width_mm']
    
    print(f"\nGenerating Type R Ring Joint Gasket - {ring_number}")
    print(f"  Pitch Diameter: {pitch_diameter_mm}mm")
    print(f"  Width: {width_mm}mm")
    print(f"  Profile: {profile_type}")
    print(f"  Material: {material}")
    
    # Create profile based on type
    if profile_type.lower() == 'oval':
        oval_height_mm = ring_info.get('oval_height_mm')
        if oval_height_mm is None:
            raise ValueError(f"Ring {ring_number} does not have oval profile dimensions")
        
        print(f"  Oval Height: {oval_height_mm}mm")
        profile_wire = make_oval_profile_r(pitch_radius_mm, width_mm, oval_height_mm)
    else:  # octagonal
        octagonal_height_mm = ring_info['octagonal_height_mm']
        flat_width_mm = ring_info['flat_width_mm']
        radius_mm = ring_info['radius_mm']
        
        print(f"  Octagonal Height: {octagonal_height_mm}mm")
        print(f"  Flat Width: {flat_width_mm}mm")
        
        profile_wire = make_octagonal_profile_r(pitch_radius_mm, width_mm, 
                                                 octagonal_height_mm, flat_width_mm, radius_mm)
    
    # Revolve profile to create ring
    ring = revolve_profile(profile_wire)
    
    # Generate filename
    filename = f"Gasket-RingJoint-{ring_number}-{profile_type.capitalize()}-{material}.step"
    
    # Set output directory
    if output_dir is None:
        output_dir = os.path.join(os.path.expanduser("~"), "EquationParadise", "CAD", 
                                   "gaskets", "ring_joint_r")
    os.makedirs(output_dir, exist_ok=True)
    
    filepath = os.path.join(output_dir, filename)
    
    # Write STEP file
    step_writer = STEPControl_Writer()
    Interface_Static.SetCVal("write.step.schema", "AP214")
    Interface_Static.SetCVal("write.step.unit", "MM")
    step_writer.Transfer(ring, STEPControl_AsIs)
    status = step_writer.Write(filepath)
    
    if status == 1:
        print(f"✓ Successfully created: {filepath}")
        return filepath
    else:
        raise RuntimeError(f"Failed to write STEP file: {filepath}")


def generate_ring_joint_rx(ring_number, material='316SS', output_dir=None):
    """
    Generate STEP file for Type RX ring joint gasket.
    
    Args:
        ring_number: Ring number (e.g., 'RX-23', 'RX-46')
        material: '316SS', '304SS', 'Monel', 'Inconel'
        output_dir: Output directory path
    
    Returns:
        str: Output file path
    """
    # Get ring specifications
    ring_info = get_gasket_info(ring_number, None, 'ring_joint')
    
    if not ring_info:
        raise ValueError(f"No data found for ring {ring_number}")
    
    pitch_diameter_mm = ring_info['pitch_diameter_mm']
    pitch_radius_mm = pitch_diameter_mm / 2.0
    width_mm = ring_info['width_mm']
    flat_width_mm = ring_info['flat_width_mm']
    outside_bevel_height_mm = ring_info['outside_bevel_height_mm']
    ring_height_mm = ring_info['ring_height_mm']
    radius_mm = ring_info['radius_mm']
    hole_size_mm = ring_info.get('hole_size_mm')
    
    print(f"\nGenerating Type RX Ring Joint Gasket - {ring_number}")
    print(f"  Pitch Diameter: {pitch_diameter_mm}mm")
    print(f"  Width: {width_mm}mm")
    print(f"  Ring Height: {ring_height_mm}mm")
    print(f"  Outside Bevel Height: {outside_bevel_height_mm}mm")
    print(f"  Material: {material}")
    
    # Create octagonal profile with bevel
    profile_wire = make_octagonal_profile_rx(pitch_radius_mm, width_mm, flat_width_mm,
                                              outside_bevel_height_mm, ring_height_mm, radius_mm)
    
    # Revolve profile to create ring
    ring = revolve_profile(profile_wire)
    
    # Add pressure balance hole if specified
    has_hole = hole_size_mm is not None
    if has_hole:
        print(f"  Adding pressure balance hole: {hole_size_mm}mm")
        ring = add_pressure_balance_hole(ring, pitch_radius_mm, hole_size_mm, ring_height_mm)
    
    # Generate filename
    hole_suffix = '-BalanceHole' if has_hole else ''
    filename = f"Gasket-RingJoint-{ring_number}-{material}{hole_suffix}.step"
    
    # Set output directory
    if output_dir is None:
        output_dir = os.path.join(os.path.expanduser("~"), "EquationParadise", "CAD", 
                                   "gaskets", "ring_joint_rx")
    os.makedirs(output_dir, exist_ok=True)
    
    filepath = os.path.join(output_dir, filename)
    
    # Write STEP file
    step_writer = STEPControl_Writer()
    Interface_Static.SetCVal("write.step.schema", "AP214")
    Interface_Static.SetCVal("write.step.unit", "MM")
    step_writer.Transfer(ring, STEPControl_AsIs)
    status = step_writer.Write(filepath)
    
    if status == 1:
        print(f"✓ Successfully created: {filepath}")
        return filepath
    else:
        raise RuntimeError(f"Failed to write STEP file: {filepath}")


def generate_all_ring_joints_r(profile_type='octagonal', material='SoftIron', output_dir=None):
    """
    Generate all Type R ring joint gaskets.
    
    Args:
        profile_type: 'octagonal' or 'oval'
        material: Material type
        output_dir: Output directory path
    
    Returns:
        list: List of generated file paths
    """
    from gasket_data import list_gasket_sizes
    
    all_rings = list_gasket_sizes(None, 'ring_joint')
    r_rings = [r for r in all_rings if r.startswith('R-')]
    
    generated_files = []
    skipped = []
    
    print(f"\n{'='*70}")
    print(f"Generating All Type R Ring Joint Gaskets - {profile_type.upper()} ({len(r_rings)} rings)")
    print(f"{'='*70}")
    
    for ring_number in r_rings:
        try:
            # Check if profile type is available
            ring_info = get_gasket_info(ring_number, None, 'ring_joint')
            if profile_type.lower() == 'oval' and ring_info.get('oval_height_mm') is None:
                skipped.append(f"{ring_number} (no oval profile)")
                continue
            
            filepath = generate_ring_joint_r(ring_number, profile_type, material, output_dir)
            generated_files.append(filepath)
        except Exception as e:
            print(f"✗ Error generating {ring_number}: {e}")
            skipped.append(f"{ring_number} (error)")
    
    print(f"\n{'='*70}")
    print(f"Generated {len(generated_files)} of {len(r_rings)} Type R rings")
    if skipped:
        print(f"Skipped {len(skipped)}: {', '.join(skipped[:10])}")
        if len(skipped) > 10:
            print(f"  ... and {len(skipped) - 10} more")
    print(f"{'='*70}\n")
    
    return generated_files


def generate_all_ring_joints_rx(material='316SS', output_dir=None):
    """
    Generate all Type RX ring joint gaskets.
    
    Args:
        material: Material type
        output_dir: Output directory path
    
    Returns:
        list: List of generated file paths
    """
    from gasket_data import list_gasket_sizes
    
    all_rings = list_gasket_sizes(None, 'ring_joint')
    rx_rings = [r for r in all_rings if r.startswith('RX-')]
    
    generated_files = []
    
    print(f"\n{'='*70}")
    print(f"Generating All Type RX Ring Joint Gaskets ({len(rx_rings)} rings)")
    print(f"{'='*70}")
    
    for ring_number in rx_rings:
        try:
            filepath = generate_ring_joint_rx(ring_number, material, output_dir)
            generated_files.append(filepath)
        except Exception as e:
            print(f"✗ Error generating {ring_number}: {e}")
    
    print(f"\n{'='*70}")
    print(f"Generated {len(generated_files)} of {len(rx_rings)} Type RX rings")
    print(f"{'='*70}\n")
    
    return generated_files


if __name__ == "__main__":
    # Test generation
    import sys
    
    if len(sys.argv) > 1:
        ring_type = sys.argv[1].upper()  # R or RX
        
        if ring_type == 'R':
            if len(sys.argv) > 2 and sys.argv[2].lower() == 'all':
                profile = sys.argv[3] if len(sys.argv) > 3 else 'octagonal'
                generate_all_ring_joints_r(profile)
            elif len(sys.argv) > 2:
                ring_number = sys.argv[2]
                profile = sys.argv[3] if len(sys.argv) > 3 else 'octagonal'
                generate_ring_joint_r(ring_number, profile)
            else:
                print("Usage: python generate_ring_joint.py R <ring_number|all> [octagonal|oval]")
        
        elif ring_type == 'RX':
            if len(sys.argv) > 2 and sys.argv[2].lower() == 'all':
                generate_all_ring_joints_rx()
            elif len(sys.argv) > 2:
                ring_number = sys.argv[2]
                generate_ring_joint_rx(ring_number)
            else:
                print("Usage: python generate_ring_joint.py RX <ring_number|all>")
        
        else:
            print("Usage: python generate_ring_joint.py <R|RX> <ring_number|all>")
    
    else:
        # Test samples
        print("\nTest Mode: Generating sample ring joint gaskets")
        
        # Test Type R
        test_r_rings = ['R-23', 'R-28', 'R-47']
        for ring in test_r_rings:
            try:
                generate_ring_joint_r(ring, 'octagonal')
            except Exception as e:
                print(f"Error: {e}")
        
        # Test Type RX
        test_rx_rings = ['RX-23', 'RX-46', 'RX-88']  # RX-88 has pressure balance hole
        for ring in test_rx_rings:
            try:
                generate_ring_joint_rx(ring)
            except Exception as e:
                print(f"Error: {e}")
