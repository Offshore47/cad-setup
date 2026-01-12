"""
Glulam Generator - pythonocc
Generates glued laminated timber (glulam) beams

Standard glulam widths: 3-1/8", 5-1/8", 6-3/4"
Depths vary from 6" to 30"

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

# Glulam data: size -> (width, depth)
GLULAM_SIZES = {
    "3-1/8 x 6": (3.125, 6),
    "3-1/8 x 9": (3.125, 9),
    "3-1/8 x 10-1/2": (3.125, 10.5),
    "3-1/8 x 12": (3.125, 12),
    "3-1/8 x 13-1/2": (3.125, 13.5),
    "3-1/8 x 15": (3.125, 15),
    "3-1/8 x 16-1/2": (3.125, 16.5),
    "3-1/8 x 18": (3.125, 18),
    "5-1/8 x 9": (5.125, 9),
    "5-1/8 x 10-1/2": (5.125, 10.5),
    "5-1/8 x 12": (5.125, 12),
    "5-1/8 x 13-1/2": (5.125, 13.5),
    "5-1/8 x 15": (5.125, 15),
    "5-1/8 x 16-1/2": (5.125, 16.5),
    "5-1/8 x 18": (5.125, 18),
    "5-1/8 x 19-1/2": (5.125, 19.5),
    "5-1/8 x 21": (5.125, 21),
    "5-1/8 x 22-1/2": (5.125, 22.5),
    "5-1/8 x 24": (5.125, 24),
    "6-3/4 x 12": (6.75, 12),
    "6-3/4 x 15": (6.75, 15),
    "6-3/4 x 18": (6.75, 18),
    "6-3/4 x 21": (6.75, 21),
    "6-3/4 x 24": (6.75, 24),
    "6-3/4 x 30": (6.75, 30),
}


def generate_glulam(size: str, length_ft: float, output_file: str = None):
    """
    Generate glulam beam.
    
    Parameters:
        size: Glulam size (e.g., "3-1/8 x 12", "5-1/8 x 18")
        length_ft: Length in feet
        output_file: Output STEP filename (auto-generated if None)
    
    Returns:
        dict: {success: bool, message: str, filename: str, size: str}
    """
    
    if size not in GLULAM_SIZES:
        return {
            'success': False,
            'message': f"Size {size} not in database. Available: {list(GLULAM_SIZES.keys())}",
            'filename': None,
            'size': size
        }
    
    width, depth = GLULAM_SIZES[size]
    length_in = length_ft * 12
    
    print(f"Generating Glulam: {size}")
    print(f"  Dimensions: {width}\" x {depth}\"")
    print(f"  Length: {length_ft} ft ({length_in:.3f}\")")
    
    # Create rectangular beam (dimensions in inches)
    beam = BRepPrimAPI_MakeBox(gp_Pnt(0, 0, 0), width, depth, length_in).Shape()
    
    # Generate filename
    if output_file is None:
        output_dir = Path("Library/Lumber/Glulam")
        output_dir.mkdir(parents=True, exist_ok=True)
        size_clean = size.replace(" ", "").replace("/", "-")
        filename = f"Glulam-{size_clean}-{length_ft:.3g}ft.step"
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
            'message': 'Glulam generated successfully',
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
