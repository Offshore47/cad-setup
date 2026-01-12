"""
Stud Bolt Generator - Continuous Thread
Generates STEP files for stud bolts per ASME B16.5, B16.47, API 6A/6BX
"""

import math
from OCC.Core.gp import gp_Pnt, gp_Dir, gp_Ax1, gp_Ax2
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCylinder
from OCC.Core.BRepFilletAPI import BRepFilletAPI_MakeChamfer
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.Interface import Interface_Static
from OCC.Core.TopAbs import TopAbs_EDGE
from OCC.Core.TopExp import TopExp_Explorer

# Import data
import sys
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)

from asme_b165_stud_data import get_b165_stud_info, list_b165_sizes
from api_6b_stud_data import get_api_6b_stud_info as get_6b_stud_info, list_api_6b_sizes as list_6b_sizes
from api_6bx_stud_data import get_api_6bx_stud_info as get_6bx_stud_info, list_api_6bx_sizes as list_6bx_sizes


def inches_to_mm(inches):
    """Convert inches to millimeters."""
    return inches * 25.4


def parse_thread_size(thread_size_str):
    """
    Parse thread size string to decimal inches.
    Examples: '1/2', '5/8', '3/4', '7/8', '1', '1-1/8', '2-3/8'
    """
    thread_size_str = thread_size_str.strip()
    
    if '-' in thread_size_str:
        # Handle format like '1-1/8' or '2-3/8'
        parts = thread_size_str.split('-')
        whole = float(parts[0])
        frac_parts = parts[1].split('/')
        fraction = float(frac_parts[0]) / float(frac_parts[1])
        return whole + fraction
    elif '/' in thread_size_str:
        # Handle format like '1/2', '5/8', '3/4'
        parts = thread_size_str.split('/')
        return float(parts[0]) / float(parts[1])
    else:
        # Handle format like '1', '2', '3'
        return float(thread_size_str)


def make_stud_cylinder(diameter_mm, length_mm, chamfer_mm=2.0):
    """
    Create a cylindrical stud with chamfered ends.
    Simplified - no actual thread geometry (would be too slow and large).
    
    Args:
        diameter_mm: Thread diameter in mm
        length_mm: Stud length in mm
        chamfer_mm: Chamfer height on ends (mm)
    
    Returns:
        TopoDS_Shape: Cylindrical stud
    """
    # Create cylinder at origin
    ax = gp_Ax2(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1))
    cylinder = BRepPrimAPI_MakeCylinder(ax, diameter_mm / 2.0, length_mm).Shape()
    
    # Note: Chamfers on cylinder ends require edge detection and BRepFilletAPI_MakeChamfer
    # For now, returning simple cylinder (chamfer is secondary detail)
    
    return cylinder


def generate_stud(standard, nps, pressure_class, series=None, facing_type='RF', output_dir=None):
    """
    Generate STEP file for stud bolt.
    
    Args:
        standard: 'B16.5', 'API 6B', or 'API 6BX'
        nps: Nominal pipe size (e.g., '1/2', '2', '6')
        pressure_class: Pressure class (150, 300, 600, etc.) or API class (2K, 5K, 10K, 20K)
        series: 'A' or 'B' for B16.47 Series A/B, None for B16.5
        facing_type: 'RF' (Raised Face) or 'RTJ' (Ring Type Joint) for B16.5 only
        output_dir: Output directory path
    
    Returns:
        str: Output file path
    """
    # Get stud specifications based on standard
    if standard.upper() == 'B16.5' or standard.upper() == 'ASME B16.5':
        stud_info = get_b165_stud_info(nps, pressure_class, facing_type)
        standard_short = 'B165'
    elif standard.upper() == 'API 6B' or standard.upper() == '6B':
        stud_info = get_6b_stud_info(nps, pressure_class)
        standard_short = 'API6B'
    elif standard.upper() == 'API 6BX' or standard.upper() == '6BX':
        stud_info = get_6bx_stud_info(nps, pressure_class)
        standard_short = 'API6BX'
    else:
        raise ValueError(f"Unknown standard: {standard}")
    
    if not stud_info:
        facing_str = f" {facing_type}" if facing_type != 'RF' else ""
        raise ValueError(f"No stud data found for {standard}{facing_str} NPS {nps} Class {pressure_class}")
    
    # Extract dimensions - convert from data module format
    length_mm = stud_info['stud_length_mm']
    diameter_inches = stud_info['stud_diameter_inches']
    diameter_mm = diameter_inches * 25.4
    
    print(f"\nGenerating Stud - {standard_short} NPS {nps}\" Class {pressure_class}")
    print(f"  Length: {length_mm:.1f}mm")
    print(f"  Diameter: {diameter_inches}\" ({diameter_mm:.2f}mm)")
    
    # Create stud cylinder (simplified, no threads)
    stud = make_stud_cylinder(diameter_mm, length_mm)
    
    # Generate filename
    nps_str = nps.replace('/', '-').replace(' ', '')
    diameter_str = str(diameter_inches).replace('.', '-')
    filename = f"Stud-{standard_short}-{nps_str}-Class{pressure_class}-{length_mm}mm-{diameter_str}in.step"
    
    # Set output directory
    if output_dir is None:
        output_dir = os.path.join(os.path.expanduser("~"), "EquationParadise", "CAD", "studs")
    os.makedirs(output_dir, exist_ok=True)
    
    filepath = os.path.join(output_dir, filename)
    
    # Write STEP file
    step_writer = STEPControl_Writer()
    Interface_Static.SetCVal("write.step.schema", "AP214")
    Interface_Static.SetCVal("write.step.unit", "MM")
    step_writer.Transfer(stud, STEPControl_AsIs)
    status = step_writer.Write(filepath)
    
    if status == 1:  # IFSelect_RetDone
        print(f"[SUCCESS] Created: {filepath}")
        return filepath
    else:
        raise RuntimeError(f"Failed to write STEP file: {filepath}")


def generate_all_studs_for_class(standard, pressure_class, output_dir=None):
    """
    Generate all studs for a specific pressure class.
    
    Args:
        standard: 'B16.5', 'API 6B', or 'API 6BX'
        pressure_class: Pressure class
        output_dir: Output directory path
    
    Returns:
        list: List of generated file paths
    """
    # Get list of sizes for this class
    if standard.upper() == 'B16.5' or standard.upper() == 'ASME B16.5':
        sizes = list_b165_sizes(pressure_class)
    elif standard.upper() == 'API 6B' or standard.upper() == '6B':
        sizes = list_6b_sizes(pressure_class)
    elif standard.upper() == 'API 6BX' or standard.upper() == '6BX':
        sizes = list_6bx_sizes(pressure_class)
    else:
        raise ValueError(f"Unknown standard: {standard}")
    
    generated_files = []
    
    print(f"\n{'='*70}")
    print(f"Generating All {standard} Class {pressure_class} Studs ({len(sizes)} sizes)")
    print(f"{'='*70}")
    
    for nps in sizes:
        try:
            filepath = generate_stud(standard, nps, pressure_class, output_dir=output_dir)
            generated_files.append(filepath)
        except Exception as e:
            print(f"✗ Error generating NPS {nps}: {e}")
    
    print(f"\n{'='*70}")
    print(f"Generated {len(generated_files)} of {len(sizes)} studs")
    print(f"{'='*70}\n")
    
    return generated_files


if __name__ == "__main__":
    # Test generation
    import sys
    
    if len(sys.argv) > 1:
        # Command line: python generate_stud.py B16.5 2 150
        # Or: python generate_stud.py "API 6BX" 4-1/16 10K
        standard = sys.argv[1]
        nps = sys.argv[2] if len(sys.argv) > 2 else '2'
        pressure_class = sys.argv[3] if len(sys.argv) > 3 else 150
        
        # Try to convert pressure_class to int if it's numeric
        try:
            pressure_class = int(pressure_class)
        except ValueError:
            pass  # Keep as string (e.g., '10K', '20K')
        
        generate_stud(standard, nps, pressure_class)
    else:
        # Test with a few samples
        print("\nTest Mode: Generating sample studs")
        
        # ASME B16.5 samples
        test_cases = [
            ('B16.5', '2', 150),
            ('B16.5', '6', 300),
            ('B16.5', '12', 600),
        ]
        
        for standard, nps, pclass in test_cases:
            try:
                generate_stud(standard, nps, pclass)
            except Exception as e:
                print(f"Error: {e}")
