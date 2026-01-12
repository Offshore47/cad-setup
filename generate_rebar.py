"""
Rebar Generator - pythonocc
Generates standard reinforcement bar (rebar)
Units: INCHES
Standard bar sizes: #3 through #11, #14, #18
Diameters follow imperial bar size system
"""

import os
from pathlib import Path
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCylinder
from OCC.Core.gp import gp_Ax2, gp_Pnt, gp_Dir
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.IFSelect import IFSelect_RetDone
from OCC.Core.Interface import Interface_Static

# Set STEP export units to INCHES
Interface_Static.SetCVal("write.step.unit", "IN")

# Rebar data: bar_number -> diameter_inches
REBAR_SIZES = {
    # Imperial bars (standard)
    "#2": 0.250,
    "#3": 0.375,
    "#4": 0.500,
    "#5": 0.625,
    "#6": 0.750,
    "#7": 0.875,
    "#8": 1.000,
    "#9": 1.128,
    "#10": 1.270,
    "#11": 1.410,
    "#12": 1.500,
    "#13": 1.625,
    "#14": 1.693,
    "#18": 2.257,
    "#20": 2.500,
    # Jumbo bars (J designation - larger diameter, threaded ends)
    "#14J": 1.812,   # Jumbo #14 for threading
    "#18J": 2.375,   # Jumbo #18 for threading
    # Metric bars (M-bar designation)
    "10M": 0.433,   # 11.3mm
    "15M": 0.630,   # 16mm
    "20M": 0.787,   # 19.5mm
    "25M": 0.984,   # 25mm
    "30M": 1.181,   # 29.9mm
    "35M": 1.378,   # 35mm
    "45M": 1.772,   # 45mm
    "55M": 2.165,   # 55mm
}


def generate_rebar(bar_size: str, length_ft: float, material: str = "Steel", output_file: str = None):
    """
    Generate rebar.
    
    Parameters:
        bar_size: Bar size (e.g., "#3", "#4", "#5", "#8", "14J", "10M")
        length_ft: Length in feet
        material: Material type ("Steel", "Basalt FRP", "Carbon Fiber (CFRP)", "Fiberglass (GFRP)")
        output_file: Output STEP filename (auto-generated if None)
    
    Returns:
        dict: {success: bool, message: str, filename: str, bar_size: str}
    """
    
    if bar_size not in REBAR_SIZES:
        return {
            'success': False,
            'message': f"Bar size {bar_size} not in database. Available: {list(REBAR_SIZES.keys())}",
            'filename': None,
            'bar_size': bar_size
        }
    
    diameter_in = REBAR_SIZES[bar_size]
    length_in = length_ft * 12
    
    # Convert to mm
    diameter_mm = diameter_in * 25.4
    radius_mm = diameter_mm / 2
    length_mm = length_in * 25.4
    
    print(f"Generating Rebar: {bar_size}")
    print(f"  Material: {material}")
    print(f"  Diameter: {diameter_in}\"")
    print(f"  Length: {length_ft} ft ({length_in:.3f}\")")
    
    # Create cylinder along Z-axis
    axis = gp_Ax2(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1))
    cylinder = BRepPrimAPI_MakeCylinder(axis, radius_mm, length_mm).Shape()
    
    # Generate filename
    if output_file is None:
        output_dir = Path("Library/Rebar")
        output_dir.mkdir(parents=True, exist_ok=True)
        bar_clean = bar_size.replace("#", "No").replace("/", "-")
        mat_prefix = material.split()[0]  # Steel, Basalt, Carbon, Fiberglass
        filename = f"Rebar-{mat_prefix}-{bar_clean}-{length_ft:.3g}ft.step"
        output_file = str(output_dir / filename)
    else:
        filename = Path(output_file).name
    
    # Export to STEP
    step_writer = STEPControl_Writer()
    step_writer.Transfer(cylinder, STEPControl_AsIs)
    status = step_writer.Write(output_file)
    
    if status == IFSelect_RetDone:
        print(f"[SUCCESS] Generated: {output_file}")
        return {
            'success': True,
            'message': 'Rebar generated successfully',
            'filename': output_file,
            'bar_size': bar_size
        }
    else:
        return {
            'success': False,
            'message': 'STEP file write failed',
            'filename': None,
            'bar_size': bar_size
        }
