"""
Gasket Generator - Full Face, Flat Ring, Spiral Wound, Ring Joint
Generates STEP files for gaskets per ASME B16.5, B16.47, B16.20, API 6A
"""

import math
from OCC.Core.gp import gp_Pnt, gp_Dir, gp_Ax1, gp_Ax2, gp_Vec, gp_Circ
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCylinder, BRepPrimAPI_MakeRevol
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut, BRepAlgoAPI_Fuse
from OCC.Core.BRepBuilderAPI import (BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire, 
                                       BRepBuilderAPI_MakeFace)
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.Interface import Interface_Static

# Import data
import sys
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)

from gasket_data import get_gasket_info, list_gasket_sizes
from flange_data import get_flange_info  # For bolt hole pattern


def make_flat_disc(id_mm, od_mm, thickness_mm):
    """
    Create a flat disc (annular or full).
    
    Args:
        id_mm: Inner diameter (mm)
        od_mm: Outer diameter (mm)
        thickness_mm: Thickness (mm)
    
    Returns:
        TopoDS_Shape: Flat disc
    """
    # Outer cylinder
    ax = gp_Ax2(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1))
    outer = BRepPrimAPI_MakeCylinder(ax, od_mm / 2.0, thickness_mm).Shape()
    
    # Inner cylinder (hole)
    inner = BRepPrimAPI_MakeCylinder(ax, id_mm / 2.0, thickness_mm + 2).Shape()
    
    # Cut hole from outer
    disc = BRepAlgoAPI_Cut(outer, inner).Shape()
    
    return disc


def add_bolt_holes(gasket_shape, bolt_circle_diameter_mm, num_bolts, bolt_hole_diameter_mm, thickness_mm):
    """
    Add bolt holes to full face gasket.
    
    Args:
        gasket_shape: Base gasket shape
        bolt_circle_diameter_mm: Bolt circle diameter
        num_bolts: Number of bolts
        bolt_hole_diameter_mm: Bolt hole diameter
        thickness_mm: Gasket thickness
    
    Returns:
        TopoDS_Shape: Gasket with bolt holes
    """
    bc_radius = bolt_circle_diameter_mm / 2.0
    hole_radius = bolt_hole_diameter_mm / 2.0
    
    result = gasket_shape
    
    for i in range(num_bolts):
        angle = (2 * math.pi * i) / num_bolts
        x = bc_radius * math.cos(angle)
        y = bc_radius * math.sin(angle)
        
        # Create bolt hole
        ax = gp_Ax2(gp_Pnt(x, y, -1), gp_Dir(0, 0, 1))
        hole = BRepPrimAPI_MakeCylinder(ax, hole_radius, thickness_mm + 2).Shape()
        
        # Cut hole from gasket
        result = BRepAlgoAPI_Cut(result, hole).Shape()
    
    return result


def generate_full_face_gasket(nps, pressure_class, series=None, thickness_mm=1.5, output_dir=None):
    """
    Generate STEP file for full face gasket.
    
    Args:
        nps: Nominal pipe size
        pressure_class: Pressure class
        series: 'A' or 'B' for B16.47, None for B16.5
        thickness_mm: Gasket thickness (default 1/16" = 1.5mm)
        output_dir: Output directory path
    
    Returns:
        str: Output file path
    """
    # Get gasket dimensions
    gasket_info = get_gasket_info(nps, pressure_class, 'full_face', series)
    
    if not gasket_info:
        raise ValueError(f"No full face gasket data for NPS {nps} Class {pressure_class}")
    
    id_mm = gasket_info['id_mm']
    od_mm = gasket_info['od_mm']
    
    print(f"\nGenerating Full Face Gasket - NPS {nps}\" Class {pressure_class}")
    print(f"  ID: {id_mm}mm, OD: {od_mm}mm, Thickness: {thickness_mm}mm")
    
    # Create base disc
    gasket = make_flat_disc(id_mm, od_mm, thickness_mm)
    
    # Get flange info for bolt holes
    flange_info = get_flange_info(nps, pressure_class, 'weld_neck', series)
    
    if flange_info:
        bc_diam = flange_info['bolt_circle_diameter_mm']
        num_bolts = flange_info['number_of_bolts']
        bolt_hole_diam = flange_info['bolt_hole_diameter_mm']
        
        print(f"  Adding {num_bolts} bolt holes at BC {bc_diam}mm")
        gasket = add_bolt_holes(gasket, bc_diam, num_bolts, bolt_hole_diam, thickness_mm)
    
    # Generate filename
    nps_str = str(nps).replace('/', '-').replace(' ', '')
    standard = 'B165' if not series else f'B1647{series}'
    filename = f"Gasket-FullFace-{standard}-{nps_str}-Class{pressure_class}-{thickness_mm}mm.step"
    
    # Set output directory
    if output_dir is None:
        output_dir = os.path.join(os.path.expanduser("~"), "EquationParadise", "CAD", "gaskets", "full_face")
    os.makedirs(output_dir, exist_ok=True)
    
    filepath = os.path.join(output_dir, filename)
    
    # Write STEP file
    step_writer = STEPControl_Writer()
    Interface_Static.SetCVal("write.step.schema", "AP214")
    Interface_Static.SetCVal("write.step.unit", "MM")
    step_writer.Transfer(gasket, STEPControl_AsIs)
    status = step_writer.Write(filepath)
    
    if status == 1:
        print(f"[SUCCESS] Created: {filepath}")
        return filepath
    else:
        raise RuntimeError(f"Failed to write STEP file: {filepath}")


def generate_flat_ring_gasket(nps, pressure_class, series=None, thickness_mm=1.5, output_dir=None):
    """
    Generate STEP file for flat ring gasket (no bolt holes).
    
    Args:
        nps: Nominal pipe size
        pressure_class: Pressure class
        series: 'A' or 'B' for B16.47, None for B16.5
        thickness_mm: Gasket thickness (default 1/16" = 1.5mm)
        output_dir: Output directory path
    
    Returns:
        str: Output file path
    """
    # Get gasket dimensions
    gasket_info = get_gasket_info(nps, pressure_class, 'flat_ring', series)
    
    if not gasket_info:
        raise ValueError(f"No flat ring gasket data for NPS {nps} Class {pressure_class}")
    
    id_mm = gasket_info['id_mm']
    od_mm = gasket_info['od_mm']
    
    print(f"\nGenerating Flat Ring Gasket - NPS {nps}\" Class {pressure_class}")
    print(f"  ID: {id_mm}mm, OD: {od_mm}mm, Thickness: {thickness_mm}mm")
    
    # Create annular ring (no bolt holes)
    gasket = make_flat_disc(id_mm, od_mm, thickness_mm)
    
    # Generate filename
    nps_str = str(nps).replace('/', '-').replace(' ', '')
    standard = 'B165' if not series else f'B1647{series}'
    filename = f"Gasket-FlatRing-{standard}-{nps_str}-Class{pressure_class}-{thickness_mm}mm.step"
    
    # Set output directory
    if output_dir is None:
        output_dir = os.path.join(os.path.expanduser("~"), "EquationParadise", "CAD", "gaskets", "flat_ring")
    os.makedirs(output_dir, exist_ok=True)
    
    filepath = os.path.join(output_dir, filename)
    
    # Write STEP file
    step_writer = STEPControl_Writer()
    Interface_Static.SetCVal("write.step.schema", "AP214")
    Interface_Static.SetCVal("write.step.unit", "MM")
    step_writer.Transfer(gasket, STEPControl_AsIs)
    status = step_writer.Write(filepath)
    
    if status == 1:
        print(f"[SUCCESS] Created: {filepath}")
        return filepath
    else:
        raise RuntimeError(f"Failed to write STEP file: {filepath}")


def generate_spiral_wound_gasket(nps, pressure_class, series=None, thickness_mm=4.8, output_dir=None):
    """
    Generate STEP file for spiral wound gasket (simplified 3-ring model).
    
    Args:
        nps: Nominal pipe size
        pressure_class: Pressure class
        series: 'A' or 'B' for B16.47, None for B16.5
        thickness_mm: Gasket thickness (default 3/16" = 4.8mm)
        output_dir: Output directory path
    
    Returns:
        str: Output file path
    """
    # Get gasket dimensions
    gasket_info = get_gasket_info(nps, pressure_class, 'spiral_wound', series)
    
    if not gasket_info:
        raise ValueError(f"No spiral wound gasket data for NPS {nps} Class {pressure_class}")
    
    d1 = gasket_info['inner_ring_id_mm']
    d2 = gasket_info['sealing_element_id_mm']
    d3 = gasket_info['sealing_element_od_mm']
    d4 = gasket_info['outer_ring_od_mm']
    
    print(f"\nGenerating Spiral Wound Gasket - NPS {nps}\" Class {pressure_class}")
    print(f"  Inner Ring ID: {d1}mm")
    print(f"  Sealing Element: {d2}mm - {d3}mm")
    print(f"  Outer Ring OD: {d4}mm")
    print(f"  Thickness: {thickness_mm}mm")
    
    # Create inner ring (solid cylinder)
    ax = gp_Ax2(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1))
    inner_ring = BRepPrimAPI_MakeCylinder(ax, d2 / 2.0, thickness_mm).Shape()
    
    # Create sealing element (simplified as solid annulus - actual spiral is too complex)
    sealing_outer = BRepPrimAPI_MakeCylinder(ax, d3 / 2.0, thickness_mm).Shape()
    sealing_inner = BRepPrimAPI_MakeCylinder(ax, d2 / 2.0, thickness_mm + 2).Shape()
    sealing_element = BRepAlgoAPI_Cut(sealing_outer, sealing_inner).Shape()
    
    # Create outer ring (annulus)
    outer_outer = BRepPrimAPI_MakeCylinder(ax, d4 / 2.0, thickness_mm).Shape()
    outer_inner = BRepPrimAPI_MakeCylinder(ax, d3 / 2.0, thickness_mm + 2).Shape()
    outer_ring = BRepAlgoAPI_Cut(outer_outer, outer_inner).Shape()
    
    # Fuse all components
    gasket = BRepAlgoAPI_Fuse(inner_ring, sealing_element).Shape()
    gasket = BRepAlgoAPI_Fuse(gasket, outer_ring).Shape()
    
    # Generate filename
    nps_str = str(nps).replace('/', '-').replace(' ', '')
    standard = 'B165' if not series else f'B1647{series}'
    filename = f"Gasket-SpiralWound-{standard}-{nps_str}-Class{pressure_class}.step"
    
    # Set output directory
    if output_dir is None:
        output_dir = os.path.join(os.path.expanduser("~"), "EquationParadise", "CAD", "gaskets", "spiral_wound")
    os.makedirs(output_dir, exist_ok=True)
    
    filepath = os.path.join(output_dir, filename)
    
    # Write STEP file
    step_writer = STEPControl_Writer()
    Interface_Static.SetCVal("write.step.schema", "AP214")
    Interface_Static.SetCVal("write.step.unit", "MM")
    step_writer.Transfer(gasket, STEPControl_AsIs)
    status = step_writer.Write(filepath)
    
    if status == 1:
        print(f"[SUCCESS] Created: {filepath}")
        return filepath
    else:
        raise RuntimeError(f"Failed to write STEP file: {filepath}")


# Note: Ring joint gasket generator will be in a separate file (generate_ring_joint.py)
# due to complex octagonal/oval profile geometry


if __name__ == "__main__":
    # Test generation
    import sys
    
    if len(sys.argv) > 1:
        gasket_type = sys.argv[1].lower()  # full_face, flat_ring, spiral_wound
        nps = sys.argv[2] if len(sys.argv) > 2 else '2'
        pressure_class = int(sys.argv[3]) if len(sys.argv) > 3 else 150
        
        if gasket_type == 'full_face':
            generate_full_face_gasket(nps, pressure_class)
        elif gasket_type == 'flat_ring':
            generate_flat_ring_gasket(nps, pressure_class)
        elif gasket_type == 'spiral_wound':
            generate_spiral_wound_gasket(nps, pressure_class)
        else:
            print(f"Unknown gasket type: {gasket_type}")
    else:
        # Test samples
        print("\nTest Mode: Generating sample gaskets")
        
        test_cases = [
            ('full_face', '2', 150),
            ('flat_ring', '6', 300),
            ('spiral_wound', '12', 600),
        ]
        
        for gtype, nps, pclass in test_cases:
            try:
                if gtype == 'full_face':
                    generate_full_face_gasket(nps, pclass)
                elif gtype == 'flat_ring':
                    generate_flat_ring_gasket(nps, pclass)
                elif gtype == 'spiral_wound':
                    generate_spiral_wound_gasket(nps, pclass)
            except Exception as e:
                print(f"Error generating {gtype} NPS {nps} Class {pclass}: {e}")
