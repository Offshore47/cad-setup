"""
TJI I-Joist Generator - pythonocc
Generates engineered wood I-joists (TJI)

TJI Series:
  110 - Residential, light commercial
  210 - Residential, commercial
  230 - Commercial, heavy residential
  360 - Heavy commercial
  560 - Heavy commercial, long spans

Geometry: I-beam with rectangular flanges (top/bottom) + OSB web (center)

Units: INCHES (US construction standard)
"""

import csv
import os
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse
from OCC.Core.gp import gp_Pnt, gp_Vec
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform
from OCC.Core.gp import gp_Trsf
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.IFSelect import IFSelect_RetDone
from OCC.Core.Interface import Interface_Static

# Set STEP units to INCH for US construction
Interface_Static.SetCVal("write.step.unit", "IN")


def load_tji_data():
    """
    Get TJI dimensions (hardcoded for reliability).
    
    Returns:
        dict: {designation: {flange_width, flange_thickness, web_thickness, overall_height}}
    """
    tji_data = {
        "TJI 110  9 1/2": {"flange_width": 1.75, "flange_thickness": 1.325, "web_thickness": 0.375, "overall_height": 9.5},
        "TJI 110 117/8": {"flange_width": 1.75, "flange_thickness": 1.325, "web_thickness": 0.375, "overall_height": 11.875},
        "TJI 110 14": {"flange_width": 1.75, "flange_thickness": 1.325, "web_thickness": 0.375, "overall_height": 14},
        "TJI 110 16": {"flange_width": 1.75, "flange_thickness": 1.325, "web_thickness": 0.375, "overall_height": 16},
        
        "TJI 210 9 1/2": {"flange_width": 2.0625, "flange_thickness": 1.325, "web_thickness": 0.375, "overall_height": 9.5},
        "TJI 210 11 7/8": {"flange_width": 2.0625, "flange_thickness": 1.325, "web_thickness": 0.375, "overall_height": 11.875},
        "TJI 210 14": {"flange_width": 2.0625, "flange_thickness": 1.325, "web_thickness": 0.375, "overall_height": 14},
        "TJI 210 16": {"flange_width": 2.0625, "flange_thickness": 1.325, "web_thickness": 0.375, "overall_height": 16},
        
        "TJI 230 9 1/2": {"flange_width": 2.3125, "flange_thickness": 1.325, "web_thickness": 0.375, "overall_height": 9.5},
        "TJI 230 11 7/8": {"flange_width": 2.3125, "flange_thickness": 1.325, "web_thickness": 0.375, "overall_height": 11.875},
        "TJI 230 14": {"flange_width": 2.3125, "flange_thickness": 1.325, "web_thickness": 0.375, "overall_height": 14},
        "TJI 230 16": {"flange_width": 2.3125, "flange_thickness": 1.325, "web_thickness": 0.375, "overall_height": 16},
        
        "TJI 360 11 7/8": {"flange_width": 2.3125, "flange_thickness": 1.325, "web_thickness": 0.375, "overall_height": 11.875},
        "TJI 360 14": {"flange_width": 2.3125, "flange_thickness": 1.325, "web_thickness": 0.375, "overall_height": 14},
        "TJI 360 16": {"flange_width": 2.3125, "flange_thickness": 1.325, "web_thickness": 0.375, "overall_height": 16},
        
        "TJI 560 11 7/8": {"flange_width": 3.5, "flange_thickness": 1.325, "web_thickness": 0.4375, "overall_height": 11.875},
        "TJI 560 14": {"flange_width": 3.5, "flange_thickness": 1.325, "web_thickness": 0.4375, "overall_height": 14},
        "TJI 560 16 ": {"flange_width": 3.5, "flange_thickness": 1.325, "web_thickness": 0.4375, "overall_height": 16},
    }
    
    return tji_data


def make_tji_profile(flange_width_inches, flange_thickness_inches, 
                     web_thickness_inches, overall_height_inches, length_inches):
    """
    Create TJI I-beam profile.
    
    Profile built as:
      - Bottom flange (rectangular)
      - Web (thin vertical rectangle, centered)
      - Top flange (rectangular)
    
    Parameters:
        flange_width_inches: Width of top/bottom flanges
        flange_thickness_inches: Thickness of top/bottom flanges
        web_thickness_inches: Thickness of center web (OSB)
        overall_height_inches: Total height of I-beam
        length_inches: Length along beam axis
    
    Returns:
        TopoDS_Shape: TJI I-beam solid
    """
    # Use inch dimensions directly (STEP will export as inches)
    flange_width = flange_width_inches
    flange_thickness = flange_thickness_inches
    web_thickness = web_thickness_inches
    overall_height = overall_height_inches
    length = length_inches
    
    # Web height (between flanges)
    web_height = overall_height - (2 * flange_thickness)
    
    # Build bottom flange
    # Centered at origin, extends in +X (length), +/-Y (width/2)
    bottom_flange = BRepPrimAPI_MakeBox(
        gp_Pnt(-flange_width/2, 0, 0),
        flange_width,
        length,
        flange_thickness
    ).Shape()
    
    # Build web (centered on flanges)
    # Web is centered on the flange width
    web = BRepPrimAPI_MakeBox(
        gp_Pnt(-web_thickness/2, 0, flange_thickness),
        web_thickness,
        length,
        web_height
    ).Shape()
    
    # Build top flange
    top_flange = BRepPrimAPI_MakeBox(
        gp_Pnt(-flange_width/2, 0, flange_thickness + web_height),
        flange_width,
        length,
        flange_thickness
    ).Shape()
    
    # Fuse all three components
    fuse1 = BRepAlgoAPI_Fuse(bottom_flange, web).Shape()
    tji_beam = BRepAlgoAPI_Fuse(fuse1, top_flange).Shape()
    
    return tji_beam


def generate_tji(
    designation: str,
    length_ft: float,
    output_file: str = None
):
    """
    Generate a TJI I-joist.
    
    Parameters:
        designation: TJI designation (e.g., "TJI 210 14", "TJI 110 9 1/2")
        length_ft: Length in feet (supports decimals: 16.5, 20.333, etc.)
        output_file: Output STEP filename (auto-generated if None)
    
    Returns:
        dict: {'success': bool, 'message': str, 'filename': str, 'designation': str}
    """
    
    try:
        # Load TJI database
        tji_data = load_tji_data()
        
        if not tji_data:
            return {
                'success': False,
                'message': 'Failed to load TJI database',
                'filename': None,
                'designation': designation
            }
        
        # Find TJI in database
        if designation not in tji_data:
            return {
                'success': False,
                'message': f'TJI designation "{designation}" not found in database',
                'filename': None,
                'designation': designation
            }
        
        tji_info = tji_data[designation]
        
        # Convert length to inches (preserve float precision)
        length_inches = length_ft * 12
        
        print(f"\nGenerating TJI: {designation}")
        print(f"  Flange Width: {tji_info['flange_width']}\"")
        print(f"  Flange Thickness: {tji_info['flange_thickness']}\"")
        print(f"  Web Thickness: {tji_info['web_thickness']}\"")
        print(f"  Overall Height: {tji_info['overall_height']}\"")
        print(f"  Length: {length_ft} ft ({length_inches:.3f}\")")
        
        # Generate TJI beam
        tji_beam = make_tji_profile(
            flange_width_inches=tji_info['flange_width'],
            flange_thickness_inches=tji_info['flange_thickness'],
            web_thickness_inches=tji_info['web_thickness'],
            overall_height_inches=tji_info['overall_height'],
            length_inches=length_inches
        )
        
        # Generate filename if not provided
        if output_file is None:
            # Format: TJI-210-14-20ft.step
            # Clean designation for filename
            series_depth = designation.replace("TJI ", "").replace(" ", "-").replace("/", "-")
            filename = f"TJI-{series_depth}-{length_ft:.3g}ft.step"
            
            # Create output directory
            output_dir = os.path.join("Library", "Lumber", "TJI")
            os.makedirs(output_dir, exist_ok=True)
            output_file = os.path.join(output_dir, filename)
        
        # Write STEP file
        step_writer = STEPControl_Writer()
        step_writer.Transfer(tji_beam, STEPControl_AsIs)
        status = step_writer.Write(output_file)
        
        if status == IFSelect_RetDone:
            print(f"[SUCCESS] Generated: {output_file}")
            return {
                'success': True,
                'message': f'TJI generated successfully',
                'filename': output_file,
                'designation': designation
            }
        else:
            return {
                'success': False,
                'message': 'Failed to write STEP file',
                'filename': None,
                'designation': designation
            }
    
    except Exception as e:
        return {
            'success': False,
            'message': f'Error: {str(e)}',
            'filename': None,
            'designation': designation
        }


if __name__ == "__main__":
    # Test with various TJI sizes and lengths
    
    # Standard residential TJI 210 14" at 16ft
    result = generate_tji(
        designation="TJI 210 14",
        length_ft=16
    )
    print(f"\nTest 1 - TJI 210 14\" @ 16ft: {result}")
    
    # Heavy commercial TJI 560 16" at 24.5ft
    result = generate_tji(
        designation="TJI 560 16 ",
        length_ft=24.5
    )
    print(f"\nTest 2 - TJI 560 16\" @ 24.5ft: {result}")
    
    # Light TJI 110 at odd length (precision test)
    result = generate_tji(
        designation="TJI 110 117/8",
        length_ft=12.875
    )
    print(f"\nTest 3 - TJI 110 11-7/8\" @ 12.875ft: {result}")
