"""
PSL (Parallel Strand Lumber) Generator - pythonocc
Generates Parallam PSL beams

Standard PSL widths: 3-1/2", 5-1/4", 7"
Depths vary from 9-1/2" to 18"

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

# PSL data: size -> (width, depth)
PSL_SIZES = {
    "3-1/2 x 9-1/2": (3.5, 9.5),
    "3-1/2 x 11-7/8": (3.5, 11.875),
    "3-1/2 x 14": (3.5, 14),
    "3-1/2 x 16": (3.5, 16),
    "3-1/2 x 18": (3.5, 18),
    "5-1/4 x 9-1/2": (5.25, 9.5),
    "5-1/4 x 11-7/8": (5.25, 11.875),
    "5-1/4 x 14": (5.25, 14),
    "5-1/4 x 16": (5.25, 16),
    "5-1/4 x 18": (5.25, 18),
    "7 x 9-1/2": (7.0, 9.5),
    "7 x 11-7/8": (7.0, 11.875),
    "7 x 14": (7.0, 14),
    "7 x 16": (7.0, 16),
    "7 x 18": (7.0, 18),
    "7 x 9-1/4": (7.0, 9.25),
    "7 x 11-1/4": (7.0, 11.25),
    "7 x 20": (7.0, 20),
}


def generate_psl(size: str, length_ft: float, output_file: str = None):
    """
    Generate PSL beam.
    
    Parameters:
        size: PSL size (e.g., "3-1/2 x 11-7/8", "7 x 14")
        length_ft: Length in feet
        output_file: Output STEP filename (auto-generated if None)
    
    Returns:
        dict: {success: bool, message: str, filename: str, size: str}
    """
    
    if size not in PSL_SIZES:
        return {
            'success': False,
            'message': f"Size {size} not in database. Available: {list(PSL_SIZES.keys())}",
            'filename': None,
            'size': size
        }
    
    width, depth = PSL_SIZES[size]
    length_in = length_ft * 12
    
    print(f"Generating PSL: {size}")
    print(f"  Dimensions: {width}\" x {depth}\"")
    print(f"  Length: {length_ft} ft ({length_in:.3f}\")")
    
    # Create rectangular beam (dimensions in inches)
    beam = BRepPrimAPI_MakeBox(gp_Pnt(0, 0, 0), width, depth, length_in).Shape()
    
    # Generate filename
    if output_file is None:
        output_dir = Path("Library/Lumber/PSL")
        output_dir.mkdir(parents=True, exist_ok=True)
        size_clean = size.replace(" ", "").replace("/", "-")
        filename = f"PSL-{size_clean}-{length_ft:.3g}ft.step"
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
            'message': 'PSL generated successfully',
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
