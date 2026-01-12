"""
Sheet Steel Generator - pythonocc
Generates rectangular steel plates with optional edge bevels
Units: INCHES
Sheet Steel Specs:
  Bevel: 30° angle (standard for sheet goods)
  Land: 1/16" minimum, 1/8" maximum
  Edge Selection: Individual control for each edge (4 edges)

Usage:
  Sheet defined by length x width x thickness
  Edges numbered: 1=+X, 2=+Y, 3=-X, 4=-Y
"""

import math
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakePrism
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut, BRepAlgoAPI_Fuse
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeFace, BRepBuilderAPI_MakePolygon, BRepBuilderAPI_MakeWire
from OCC.Core.gp import gp_Pnt, gp_Vec, gp_Pln, gp_Ax2, gp_Dir
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.IFSelect import IFSelect_RetDone
from OCC.Core.Interface import Interface_Static
import os

# Set STEP export units to INCHES
Interface_Static.SetCVal("write.step.unit", "IN")


def inches_to_mm(inches: float) -> float:
    """Convert inches to millimeters"""
    return inches * 25.4


def add_edge_bevels(sheet_shape, length_mm, width_mm, thickness_mm, 
                    bevel_angle, land_mm, 
                    bevel_edge1, bevel_edge2, bevel_edge3, bevel_edge4):
    """
    Add bevels to selected edges using Boolean cut operations.
    
    Constructs cutting boxes positioned at angle to remove material,
    leaving the specified land dimension.
    
    Edge numbering (looking down at sheet, Z-up):
      Edge 1: +X side (at X=length, parallel to Y)
      Edge 2: +Y side (at Y=width, parallel to X)
      Edge 3: -X side (at X=0, parallel to Y)
      Edge 4: -Y side (at Y=0, parallel to X)
    
    Parameters:
        sheet_shape: TopoDS_Shape of rectangular box
        length_mm, width_mm, thickness_mm: Sheet dimensions
        bevel_angle: Bevel angle in degrees (typically 30° for sheet steel)
        land_mm: Land thickness (1.6mm to 3.2mm typical)
        bevel_edge1-4: Boolean flags for each edge
    
    Returns:
        TopoDS_Shape with bevels cut
    """
    
    if not any([bevel_edge1, bevel_edge2, bevel_edge3, bevel_edge4]):
        return sheet_shape  # No bevels requested
    
    # Calculate bevel geometry
    bevel_rad = math.radians(bevel_angle)
    # Horizontal distance to cut back from edge
    cutback = (thickness_mm - land_mm) / math.tan(bevel_rad)
    
    result_shape = sheet_shape
    edges_beveled = 0
    
    # Edge 1: +X side (at X=length, parallel to Y)
    if bevel_edge1:
        result_shape = cut_bevel_edge_x(result_shape, length_mm, width_mm, thickness_mm, 
                                       land_mm, cutback, is_positive_x=True)
        edges_beveled += 1
    
    # Edge 2: +Y side (at Y=width, parallel to X)
    if bevel_edge2:
        result_shape = cut_bevel_edge_y(result_shape, length_mm, width_mm, thickness_mm,
                                       land_mm, cutback, is_positive_y=True)
        edges_beveled += 1
    
    # Edge 3: -X side (at X=0, parallel to Y)
    if bevel_edge3:
        result_shape = cut_bevel_edge_x(result_shape, length_mm, width_mm, thickness_mm,
                                       land_mm, cutback, is_positive_x=False)
        edges_beveled += 1
    
    # Edge 4: -Y side (at Y=0, parallel to X)
    if bevel_edge4:
        result_shape = cut_bevel_edge_y(result_shape, length_mm, width_mm, thickness_mm,
                                       land_mm, cutback, is_positive_y=False)
        edges_beveled += 1
    
    print(f"  Beveled {edges_beveled} edges at {bevel_angle}° with {land_mm:.2f}mm land")
    return result_shape


def cut_bevel_edge_x(shape, length_mm, width_mm, thickness_mm, land_mm, cutback, is_positive_x):
    """
    Cut bevel on edge parallel to Y axis (sides of sheet in X direction).
    
    The bevel removes material above the land, sloping inward at the bevel angle.
    """
    x_edge = length_mm if is_positive_x else 0.0
    
    # Create simple triangular wedge profile
    # Triangle: edge at land -> edge at top -> inward at top -> close
    
    if is_positive_x:
        # Bevel slopes from +X edge inward toward -X
        p1 = gp_Pnt(x_edge, -5, land_mm)           # Land at edge
        p2 = gp_Pnt(x_edge, -5, thickness_mm + 5)   # Top at edge
        p3 = gp_Pnt(x_edge - cutback, -5, thickness_mm + 5)  # Top inward
    else:
        # Bevel slopes from X=0 edge inward toward +X
        p1 = gp_Pnt(x_edge, -5, land_mm)
        p2 = gp_Pnt(x_edge, -5, thickness_mm + 5)
        p3 = gp_Pnt(x_edge + cutback, -5, thickness_mm + 5)
    
    # Create triangular profile
    poly = BRepBuilderAPI_MakePolygon()
    poly.Add(p1)
    poly.Add(p2)
    poly.Add(p3)
    poly.Close()
    wire = poly.Wire()
    face = BRepBuilderAPI_MakeFace(wire).Face()
    
    # Extrude along Y to cover full width
    prism_vec = gp_Vec(0, width_mm + 10, 0)
    cutting_solid = BRepPrimAPI_MakePrism(face, prism_vec).Shape()
    
    # Perform cut
    cut_op = BRepAlgoAPI_Cut(shape, cutting_solid)
    return cut_op.Shape()


def cut_bevel_edge_y(shape, length_mm, width_mm, thickness_mm, land_mm, cutback, is_positive_y):
    """
    Cut bevel on edge parallel to X axis (sides of sheet in Y direction).
    """
    y_edge = width_mm if is_positive_y else 0.0
    
    # Create triangular wedge profile
    if is_positive_y:
        # Bevel slopes from +Y edge inward toward -Y
        p1 = gp_Pnt(-5, y_edge, land_mm)
        p2 = gp_Pnt(-5, y_edge, thickness_mm + 5)
        p3 = gp_Pnt(-5, y_edge - cutback, thickness_mm + 5)
    else:
        # Bevel slopes from Y=0 edge inward toward +Y
        p1 = gp_Pnt(-5, y_edge, land_mm)
        p2 = gp_Pnt(-5, y_edge, thickness_mm + 5)
        p3 = gp_Pnt(-5, y_edge + cutback, thickness_mm + 5)
    
    # Create triangular profile
    poly = BRepBuilderAPI_MakePolygon()
    poly.Add(p1)
    poly.Add(p2)
    poly.Add(p3)
    poly.Close()
    wire = poly.Wire()
    face = BRepBuilderAPI_MakeFace(wire).Face()
    
    # Extrude along X
    prism_vec = gp_Vec(length_mm + 10, 0, 0)
    cutting_solid = BRepPrimAPI_MakePrism(face, prism_vec).Shape()
    
    # Perform cut
    cut_op = BRepAlgoAPI_Cut(shape, cutting_solid)
    return cut_op.Shape()


def generate_sheet_steel(
    length_inches: float,
    width_inches: float,
    thickness_inches: float,
    bevel_angle: float = 30.0,
    land_inches: float = 1/16,
    bevel_edge1: bool = False,
    bevel_edge2: bool = False,
    bevel_edge3: bool = False,
    bevel_edge4: bool = False,
    output_file: str = None
):
    """
    Generate a rectangular sheet steel plate with optional edge bevels.
    
    Parameters:
        length_inches: Length (X dimension) in inches
        width_inches: Width (Y dimension) in inches  
        thickness_inches: Thickness (Z dimension) in inches
        bevel_angle: Bevel angle in degrees (default 30° for sheet steel)
        land_inches: Land thickness in inches (default 1/16", range 1/16" to 1/8")
        bevel_edge1: Bevel +X edge (length direction, far side)
        bevel_edge2: Bevel +Y edge (width direction, far side)
        bevel_edge3: Bevel -X edge (length direction, near side)
        bevel_edge4: Bevel -Y edge (width direction, near side)
        output_file: Output STEP filename (auto-generated if None)
    
    Returns:
        dict: {'success': bool, 'message': str, 'filename': str}
    """
    
    try:
        # Convert to millimeters
        length_mm = inches_to_mm(length_inches)
        width_mm = inches_to_mm(width_inches)
        thickness_mm = inches_to_mm(thickness_inches)
        land_mm = inches_to_mm(land_inches)
        
        # Validate dimensions
        if length_mm <= 0 or width_mm <= 0 or thickness_mm <= 0:
            return {
                'success': False,
                'message': 'All dimensions must be positive',
                'filename': None
            }
        
        # Validate land
        land_min = inches_to_mm(1/16)
        land_max = inches_to_mm(1/8)
        if land_mm < land_min or land_mm > land_max:
            return {
                'success': False,
                'message': f'Land must be between 1/16" and 1/8" ({land_min:.2f}mm to {land_max:.2f}mm)',
                'filename': None
            }
        
        # Validate bevel angle
        if bevel_angle < 15 or bevel_angle > 45:
            return {
                'success': False,
                'message': 'Bevel angle must be between 15° and 45°',
                'filename': None
            }
        
        print(f"\nGenerating sheet steel: {length_inches}\" × {width_inches}\" × {thickness_inches}\"")
        print(f"  Dimensions: {length_mm:.2f}mm × {width_mm:.2f}mm × {thickness_mm:.2f}mm")
        
        # Create basic rectangular box
        box = BRepPrimAPI_MakeBox(gp_Pnt(0, 0, 0), length_mm, width_mm, thickness_mm).Shape()
        
        # Add bevels if any edges are selected
        if any([bevel_edge1, bevel_edge2, bevel_edge3, bevel_edge4]):
            beveled_edges = []
            if bevel_edge1: beveled_edges.append("Edge 1 (+X)")
            if bevel_edge2: beveled_edges.append("Edge 2 (+Y)")
            if bevel_edge3: beveled_edges.append("Edge 3 (-X)")
            if bevel_edge4: beveled_edges.append("Edge 4 (-Y)")
            
            print(f"  Bevel: {bevel_angle}° with {land_inches}\" ({land_mm:.2f}mm) land")
            print(f"  Beveled edges: {', '.join(beveled_edges)}")
            
            sheet = add_edge_bevels(
                box, length_mm, width_mm, thickness_mm,
                bevel_angle, land_mm,
                bevel_edge1, bevel_edge2, bevel_edge3, bevel_edge4
            )
        else:
            print(f"  No bevels (square edges)")
            sheet = box
        
        # Generate filename if not provided
        if output_file is None:
            # Format: Sheet-24x12x0.25-30deg-E1E3.step
            bevel_str = ""
            if any([bevel_edge1, bevel_edge2, bevel_edge3, bevel_edge4]):
                edges = []
                if bevel_edge1: edges.append("E1")
                if bevel_edge2: edges.append("E2")
                if bevel_edge3: edges.append("E3")
                if bevel_edge4: edges.append("E4")
                bevel_str = f"-{int(bevel_angle)}deg-{''.join(edges)}"
            
            filename = f"Sheet-{length_inches:.3g}x{width_inches:.3g}x{thickness_inches:.3g}{bevel_str}.step"
            
            # Create output directory
            output_dir = os.path.join("Library", "Sheet_Steel")
            os.makedirs(output_dir, exist_ok=True)
            output_file = os.path.join(output_dir, filename)
        
        # Write STEP file
        step_writer = STEPControl_Writer()
        step_writer.Transfer(sheet, STEPControl_AsIs)
        status = step_writer.Write(output_file)
        
        if status == IFSelect_RetDone:
            print(f"[SUCCESS] Generated: {output_file}")
            return {
                'success': True,
                'message': f'Sheet steel generated successfully',
                'filename': output_file
            }
        else:
            return {
                'success': False,
                'message': 'Failed to write STEP file',
                'filename': None
            }
    
    except Exception as e:
        return {
            'success': False,
            'message': f'Error: {str(e)}',
            'filename': None
        }


if __name__ == "__main__":
    # Test with various configurations
    
    # 24" x 12" x 1/4" plate with all edges beveled
    result = generate_sheet_steel(
        length_inches=24,
        width_inches=12,
        thickness_inches=0.25,
        bevel_angle=30,
        land_inches=1/16,
        bevel_edge1=True,
        bevel_edge2=True,
        bevel_edge3=True,
        bevel_edge4=True
    )
    print(f"\nTest 1 - All edges beveled: {result}")
    
    # 48" x 24" x 1/2" plate with only opposing edges beveled (E1 and E3)
    result = generate_sheet_steel(
        length_inches=48,
        width_inches=24,
        thickness_inches=0.5,
        bevel_angle=30,
        land_inches=1/8,
        bevel_edge1=True,
        bevel_edge2=False,
        bevel_edge3=True,
        bevel_edge4=False
    )
    print(f"\nTest 2 - Opposing edges (E1, E3): {result}")
    
    # 12" x 12" x 3/8" plate with no bevels
    result = generate_sheet_steel(
        length_inches=12,
        width_inches=12,
        thickness_inches=0.375,
        bevel_angle=30,
        land_inches=1/16,
        bevel_edge1=False,
        bevel_edge2=False,
        bevel_edge3=False,
        bevel_edge4=False
    )
    print(f"\nTest 3 - No bevels: {result}")
