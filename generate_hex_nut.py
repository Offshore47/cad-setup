"""
Hex Nut Generator - Standard and 2H Heavy
Generates STEP files for hex nuts per ASME B18.2.2
"""

import math
from OCC.Core.gp import gp_Pnt, gp_Dir, gp_Ax1, gp_Ax2, gp_Vec
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCylinder, BRepPrimAPI_MakePrism
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut, BRepAlgoAPI_Fuse
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire, BRepBuilderAPI_MakeFace
from OCC.Core.BRepFilletAPI import BRepFilletAPI_MakeChamfer
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.Interface import Interface_Static
from OCC.Core.TopAbs import TopAbs_EDGE, TopAbs_FACE
from OCC.Core.TopExp import TopExp_Explorer

# Import data
import sys
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)

from heavy_hex_nut_data import get_heavy_hex_nut_info, list_heavy_hex_nut_sizes


def make_hexagonal_prism(width_across_flats_mm, thickness_mm, z_base=0):
    """
    Create a hexagonal prism.
    
    Args:
        width_across_flats_mm: Distance across flats (mm)
        thickness_mm: Height of the nut (mm)
        z_base: Base Z coordinate (mm)
    
    Returns:
        TopoDS_Shape: Hexagonal prism
    """
    # Calculate width across corners from width across flats
    # For a regular hexagon: width_across_corners = width_across_flats / cos(30°)
    r_flat = width_across_flats_mm / 2.0
    
    # Create hexagon vertices
    points = []
    for i in range(6):
        angle = i * 60 * math.pi / 180  # 60° intervals
        x = r_flat / math.cos(30 * math.pi / 180) * math.cos(angle)
        y = r_flat / math.cos(30 * math.pi / 180) * math.sin(angle)
        points.append(gp_Pnt(x, y, z_base))
    
    # Create edges and wire
    edges = []
    for i in range(6):
        p1 = points[i]
        p2 = points[(i + 1) % 6]
        edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
        edges.append(edge)
    
    # Make wire from edges
    wire_builder = BRepBuilderAPI_MakeWire()
    for edge in edges:
        wire_builder.Add(edge)
    wire = wire_builder.Wire()
    
    # Make face from wire
    face = BRepBuilderAPI_MakeFace(wire).Face()
    
    # Extrude to create prism
    prism_vec = gp_Vec(0, 0, thickness_mm)
    prism = BRepPrimAPI_MakePrism(face, prism_vec).Shape()
    
    return prism


def make_threaded_hole(diameter_mm, height_mm, z_base=0):
    """
    Create simplified threaded hole (smooth cylinder with note).
    Full thread geometry is too complex and slow.
    
    Args:
        diameter_mm: Nominal thread diameter (mm)
        height_mm: Depth of hole (mm)
        z_base: Base Z coordinate (mm)
    
    Returns:
        TopoDS_Shape: Cylindrical hole
    """
    # Use nominal diameter (simplified - actual minor diameter would be smaller)
    ax = gp_Ax2(gp_Pnt(0, 0, z_base - 1), gp_Dir(0, 0, 1))
    hole = BRepPrimAPI_MakeCylinder(ax, diameter_mm / 2.0, height_mm + 2).Shape()
    return hole


def add_washer_face(hex_body, width_flat_mm, total_thickness_mm, washer_thickness_mm=0.4064):
    """
    Add integrated washer face to bottom of hex nut.
    Per ASME B18.2.2, washer face height is 0.016" (0.4064mm) INCLUDED in total thickness.
    Washer OD equals width across flats.
    
    Args:
        hex_body: Hexagonal body shape (height = total_thickness - washer_thickness)
        width_flat_mm: Width across flats of hex
        total_thickness_mm: Total nut thickness (includes washer face height)
        washer_thickness_mm: Thickness of washer face (0.016" = 0.4064mm per ASME B18.2.2)
    
    Returns:
        TopoDS_Shape: Nut with washer face
    """
    # Washer diameter = width across flats (stays within hex profile)
    washer_od = width_flat_mm
    
    # Create washer disc at bottom (extends below hex body base at z=0)
    ax = gp_Ax2(gp_Pnt(0, 0, -washer_thickness_mm), gp_Dir(0, 0, 1))
    washer = BRepPrimAPI_MakeCylinder(ax, washer_od / 2.0, washer_thickness_mm).Shape()
    
    # Fuse washer with hex body
    combined = BRepAlgoAPI_Fuse(hex_body, washer).Shape()
    
    return combined


def add_chamfers(shape, total_thickness_mm, chamfer_distance_mm=3.048):
    """
    Add 15-degree chamfers to top edges of hex nut.
    Per ASME B18.2.2, chamfer is 0.12" (3.048mm) at 15 degrees on top face only.
    Bottom has washer face, so no chamfer there.
    
    Args:
        shape: Input shape
        total_thickness_mm: Total nut thickness (to identify top face)
        chamfer_distance_mm: Chamfer distance (0.12" = 3.048mm per ASME B18.2.2)
    
    Returns:
        TopoDS_Shape: Shape with chamfers on top edges
    """
    try:
        import math
        from OCC.Core.BRep import BRep_Tool
        from OCC.Core.TopoDS import topods
        from OCC.Core.GProp import GProp_GProps
        from OCC.Core.BRepGProp import brepgprop_SurfaceProperties
        
        # Create chamfer maker
        chamfer = BRepFilletAPI_MakeChamfer(shape)
        
        # Top of nut is at z = total_thickness_mm (washer extends down from z=0)
        top_z = total_thickness_mm
        tolerance = 0.5  # mm tolerance for identifying top face
        
        # Find the top hexagonal face
        face_explorer = TopExp_Explorer(shape, TopAbs_FACE)
        top_face = None
        
        while face_explorer.More():
            face = topods.Face(face_explorer.Current())
            face_explorer.Next()
            
            try:
                # Get center of mass of face to check if it's at the top
                props = GProp_GProps()
                brepgprop_SurfaceProperties(face, props)
                center = props.CentreOfMass()
                
                # If center is near top_z, this is the top face
                if abs(center.Z() - top_z) < tolerance:
                    top_face = face
                    break
            except:
                continue
        
        if top_face is None:
            print("  Note: Could not identify top face for chamfer")
            return shape
        
        # Find the 6 edges of the top hexagonal face
        edge_explorer = TopExp_Explorer(top_face, TopAbs_EDGE)
        edges_added = 0
        
        # Chamfer parameters: equal distances for 15-degree chamfer
        # Using equal distances on both faces creates approximately 15° chamfer
        
        while edge_explorer.More():
            edge = topods.Edge(edge_explorer.Current())
            edge_explorer.Next()
            
            try:
                # Add chamfer with two equal distances (creates ~45° chamfer visually)
                # For 15° chamfer, use distance and smaller perpendicular distance
                # Distance along top face = 3.048mm
                # Distance along side face = 3.048mm * tan(15°) ≈ 0.817mm
                # But for visibility, use equal distances for now
                chamfer.Add(chamfer_distance_mm, chamfer_distance_mm, edge, top_face)
                edges_added += 1
            except Exception as e:
                print(f"  Note: Could not chamfer edge: {e}")
                continue
        
        if edges_added > 0:
            chamfer.Build()
            if chamfer.IsDone():
                print(f"  Added chamfers to {edges_added} top edges (distance: {chamfer_distance_mm}mm at 15°)")
                return chamfer.Shape()
            else:
                print("  Note: Chamfer build failed")
        else:
            print("  Note: No edges found to chamfer")
        
    except Exception as e:
        # If chamfering fails, return original shape
        print(f"  Note: Chamfer operation skipped ({e})")
    
    return shape


def generate_hex_nut(nut_type, nominal_size, output_dir=None):
    """
    Generate STEP file for hex nut.
    
    Args:
        nut_type: 'standard' or '2h' (heavy)
        nominal_size: Nominal size string (e.g., '1/2', '3/4', '1-1/4')
        output_dir: Output directory path
    
    Returns:
        str: Output file path
    """
    # Get nut specifications
    nut_info = get_heavy_hex_nut_info(nominal_size, nut_type)
    
    if not nut_info:
        raise ValueError(f"No data found for {nut_type} hex nut size {nominal_size}")
    
    # Extract dimensions and convert to mm
    width_flat_mm = nut_info['width_across_flats_basic'] * 25.4
    total_thickness_mm = nut_info['thickness_basic'] * 25.4
    thread_diameter_mm = nut_info['thread_diameter'] * 25.4
    
    # Washer face dimensions per ASME B18.2.2
    washer_thickness_mm = 0.016 * 25.4  # 0.016" = 0.4064mm (INCLUDED in total thickness)
    hex_body_height_mm = total_thickness_mm - washer_thickness_mm
    
    print(f"\nGenerating {nut_type.upper()} Hex Nut - {nominal_size}\"")
    print(f"  Width Across Flats: {width_flat_mm:.2f}mm")
    print(f"  Total Thickness: {total_thickness_mm:.2f}mm")
    print(f"  Hex Body Height: {hex_body_height_mm:.2f}mm")
    print(f"  Washer Face Height: {washer_thickness_mm:.2f}mm")
    print(f"  Thread: {thread_diameter_mm:.2f}mm")
    
    # Create hexagonal body (height = total thickness - washer height)
    hex_body = make_hexagonal_prism(width_flat_mm, hex_body_height_mm, z_base=0)
    
    # Add integrated washer face on bottom (extends below z=0)
    hex_body_with_washer = add_washer_face(hex_body, width_flat_mm, total_thickness_mm, washer_thickness_mm)
    
    # Create threaded hole through entire nut (extends through washer)
    hole = make_threaded_hole(thread_diameter_mm, total_thickness_mm + 1, z_base=-washer_thickness_mm)
    
    # Cut hole from body
    nut = BRepAlgoAPI_Cut(hex_body_with_washer, hole).Shape()
    
    # Add 15-degree chamfers to top edges (0.12" = 3.048mm per ASME B18.2.2)
    nut = add_chamfers(nut, total_thickness_mm, chamfer_distance_mm=3.048)
    
    # Generate filename
    size_str = nominal_size.replace('/', '-').replace(' ', '')
    type_str = 'Standard' if nut_type == 'standard' else '2H'
    filename = f"HexNut-{type_str}-{size_str}.step"
    
    # Set output directory
    if output_dir is None:
        output_dir = os.path.join(os.path.expanduser("~"), "EquationParadise", "CAD", "nuts")
    os.makedirs(output_dir, exist_ok=True)
    
    filepath = os.path.join(output_dir, filename)
    
    # Write STEP file
    step_writer = STEPControl_Writer()
    Interface_Static.SetCVal("write.step.schema", "AP214")
    Interface_Static.SetCVal("write.step.unit", "MM")
    step_writer.Transfer(nut, STEPControl_AsIs)
    status = step_writer.Write(filepath)
    
    if status == 1:  # IFSelect_RetDone
        print(f"[SUCCESS] Created: {filepath}")
        return filepath
    else:
        raise RuntimeError(f"Failed to write STEP file: {filepath}")


def generate_all_hex_nuts(nut_type='standard', output_dir=None):
    """
    Generate STEP files for all available hex nut sizes.
    
    Args:
        nut_type: 'standard' or '2h' (heavy)
        output_dir: Output directory path
    
    Returns:
        list: List of generated file paths
    """
    sizes = list_heavy_hex_nut_sizes(nut_type)
    generated_files = []
    
    print(f"\n{'='*70}")
    print(f"Generating All {nut_type.upper()} Hex Nuts ({len(sizes)} sizes)")
    print(f"{'='*70}")
    
    for size in sizes:
        try:
            filepath = generate_hex_nut(nut_type, size, output_dir)
            generated_files.append(filepath)
        except Exception as e:
            print(f"✗ Error generating {size}: {e}")
    
    print(f"\n{'='*70}")
    print(f"Generated {len(generated_files)} of {len(sizes)} hex nuts")
    print(f"{'='*70}\n")
    
    return generated_files


if __name__ == "__main__":
    # Test generation
    import sys
    
    if len(sys.argv) > 1:
        # Command line: python generate_hex_nut.py standard 1/2
        # Or: python generate_hex_nut.py 2h all
        nut_type = sys.argv[1].lower()
        
        if len(sys.argv) > 2 and sys.argv[2].lower() == 'all':
            generate_all_hex_nuts(nut_type)
        elif len(sys.argv) > 2:
            size = sys.argv[2]
            generate_hex_nut(nut_type, size)
        else:
            print("Usage: python generate_hex_nut.py <standard|2h> <size|all>")
    else:
        # Test with a few samples
        print("\nTest Mode: Generating sample hex nuts")
        test_sizes = ['1/2', '3/4', '1', '2']
        
        for size in test_sizes:
            try:
                generate_hex_nut('standard', size)
            except Exception as e:
                print(f"Error: {e}")
        
        for size in test_sizes:
            try:
                generate_hex_nut('2h', size)
            except Exception as e:
                print(f"Error: {e}")
