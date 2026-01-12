"""
Dimensional Lumber Generator - pythonocc
Generates standard dimensional lumber (2x4, 4x4, 6x8, etc.)

Dimensions use actual sizes (not nominal):
  2x4 = 1.5" x 3.5"
  4x4 = 3.5" x 3.5"
  6x8 = 5.5" x 7.25"

Units: INCHES (US construction standard)
"""

import os
from pathlib import Path
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Core.gp import gp_Pnt
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.IFSelect import IFSelect_RetDone
from OCC.Core.Interface import Interface_Static

# Set STEP units to INCH for US construction
Interface_Static.SetCVal("write.step.unit", "IN")

# Dimensional lumber data: nominal -> (actual_width, actual_height)
DIMENSIONAL_LUMBER = {
    "2x4": (1.5, 3.5),
    "2x6": (1.5, 5.5),
    "2x8": (1.5, 7.25),
    "2x10": (1.5, 9.25),
    "2x12": (1.5, 11.25),
    "4x4": (3.5, 3.5),
    "4x6": (3.5, 5.5),
    "4x8": (3.5, 7.25),
    "4x10": (3.5, 9.25),
    "4x12": (3.5, 11.25),
    "6x6": (5.5, 5.5),
    "6x8": (5.5, 7.25),
    "6x10": (5.5, 9.25),
    "6x12": (5.5, 11.25),
    "8x8": (7.25, 7.25),
    "8x10": (7.25, 9.25),
    "8x12": (7.25, 11.25),
    "10x10": (9.25, 9.25),
    "10x12": (9.25, 11.25),
    "12x12": (11.25, 11.25),
}


def generate_dimensional_lumber(size: str, length_ft: float, output_file: str = None):
    """
    Generate dimensional lumber.
    
    Parameters:
        size: Nominal size (e.g., "2x4", "4x4", "6x8")
        length_ft: Length in feet
        output_file: Output STEP filename (auto-generated if None)
    
    Returns:
        dict: {success: bool, message: str, filename: str, size: str}
    """
    
    if size not in DIMENSIONAL_LUMBER:
        return {
            'success': False,
            'message': f"Size {size} not in database. Available: {list(DIMENSIONAL_LUMBER.keys())}",
            'filename': None,
            'size': size
        }
    
    width, height = DIMENSIONAL_LUMBER[size]
    length_in = length_ft * 12
    
    print(f"Generating Dimensional Lumber: {size}")
    print(f"  Actual Dimensions: {width}\" x {height}\"")
    print(f"  Length: {length_ft} ft ({length_in:.3f}\")")
    
    # Create rectangular beam (dimensions in inches)
    beam = BRepPrimAPI_MakeBox(gp_Pnt(0, 0, 0), width, height, length_in).Shape()
    
    # Generate filename
    if output_file is None:
        output_dir = Path("Library/Lumber/Dimensional")
        output_dir.mkdir(parents=True, exist_ok=True)
        filename = f"Lumber-{size}-{length_ft:.3g}ft.step"
        output_file = str(output_dir / filename)
    else:
        filename = Path(output_file).name
    
    # Export to STEP
    step_writer = STEPControl_Writer()
    step_writer.Transfer(beam, STEPControl_AsIs)
    status = step_writer.Write(output_file)
    
    if status == IFSelect_RetDone:
        print(f"[SUCCESS] Generated: {output_file}")
        return {
            'success': True,
            'message': 'Dimensional lumber generated successfully',
            'filename': output_file,
            'size': size
        }
    else:
        return {
            'success': False,
            'message': 'STEP file write failed',
            'filename': None,
            'size': size
        }
