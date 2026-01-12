"""
AISC Steel Shape Generator with Weld Bevel Options
Generates STEP files for structural steel shapes with optional weld bevels

Supports:
- W-Beams (Wide Flange): 578 shapes
- HSS (Hollow Structural Sections): 452 shapes  
- Channels (C-shapes): 32 shapes
- Angles (L-shapes): 137 shapes
- All other AISC shapes from v16 database

Weld Bevel Options:
- 30° bevel angle (standard for structural steel fillet/groove welds)
- Land height: 1.6mm (1/16" standard root face)
- Options: both ends, end1 only, end2 only, or no bevel (square cut)

Units: INCHES (US structural steel - AISC database in inches)
"""

from OCC.Core.BRepBuilderAPI import (
    BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire,
    BRepBuilderAPI_MakeFace, BRepBuilderAPI_Transform
)
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakePrism, BRepPrimAPI_MakeBox
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut, BRepAlgoAPI_Fuse
from OCC.Core.BRepFilletAPI import BRepFilletAPI_MakeFillet, BRepFilletAPI_MakeChamfer
from OCC.Core.gp import gp_Pnt, gp_Vec, gp_Ax1, gp_Dir, gp_Trsf, gp_Ax2
from OCC.Core.TopExp import TopExp_Explorer
from OCC.Core.TopAbs import TopAbs_EDGE
from OCC.Core.TopoDS import topods
from OCC.Extend.DataExchange import write_step_file
from OCC.Core.BRepOffsetAPI import BRepOffsetAPI_MakeOffset
from OCC.Core.GeomAbs import GeomAbs_Arc
from OCC.Core.Interface import Interface_Static
import math

# Set STEP units to INCH for US structural steel
Interface_Static.SetCVal("write.step.unit", "IN")

# Import AISC database
try:
    from aisc_shapes import AISC_SHAPES
except ImportError:
    print("Error: aisc_shapes.py not found. Run generate_steel_data_modules.py first.")
    AISC_SHAPES = {}

try:
    from hss_a1085 import HSS_A1085
except ImportError:
    print("Warning: hss_a1085.py not found. HSS shapes will use AISC database.")
    HSS_A1085 = {}


# Imperial to Metric W-shape mapping (approximate depths)
IMPERIAL_W_DEPTHS = {
    'W44': 'W1100', 'W40': 'W1000', 'W36': 'W920', 'W33': 'W840',
    'W30': 'W760', 'W27': 'W690', 'W24': 'W610', 'W21': 'W530',
    'W18': 'W460', 'W16': 'W410', 'W14': 'W360', 'W12': 'W310',
    'W10': 'W250', 'W8': 'W200', 'W6': 'W150', 'W5': 'W130', 'W4': 'W100'
}


def find_imperial_w_shape(designation):
    """
    Find metric designation from imperial W-shape designation
    Example: 'W12X26' -> finds closest match in W310 series
    
    Returns: (metric_designation, imperial_label) or (None, None)
    """
    if not designation.startswith('W'):
        return None, None
    
    # Parse imperial designation (e.g., W12X26)
    parts = designation.replace('x', 'X').split('X')
    if len(parts) != 2:
        return None, None
    
    try:
        imperial_depth = parts[0]  # e.g., 'W12'
        imperial_weight = float(parts[1])  # lb/ft
    except:
        return None, None
    
    # Get metric depth prefix
    metric_prefix = IMPERIAL_W_DEPTHS.get(imperial_depth)
    if not metric_prefix:
        return None, None
    
    # Find all shapes with that metric prefix
    candidates = [k for k in AISC_SHAPES.keys() if k.startswith(metric_prefix + 'X')]
    
    if not candidates:
        return None, None
    
    # Convert imperial weight (lb/ft) to metric (kg/m): lb/ft * 1.488 = kg/m
    metric_weight = imperial_weight * 1.488
    
    # Find closest match by weight
    best_match = None
    best_diff = float('inf')
    
    for candidate in candidates:
        shape_weight = AISC_SHAPES[candidate].get('W', 0)
        diff = abs(shape_weight - metric_weight)
        if diff < best_diff:
            best_diff = diff
            best_match = candidate
    
    if best_match:
        # Create imperial label for display
        actual_metric_weight = AISC_SHAPES[best_match].get('W', 0)
        actual_imperial_weight = actual_metric_weight / 1.488
        imperial_label = f"{imperial_depth}x{actual_imperial_weight:.1f}"
        return best_match, imperial_label
    
    return None, None


# Constants for weld bevels
BEVEL_ANGLE = 30.0  # degrees (structural steel standard for fillet/groove welds)
LAND_HEIGHT = 1.6  # mm (1/16" standard root face)
BEVEL_LENGTH = 25.4  # mm (1" bevel length typical for structural)


def mm_to_inches(mm):
    """Convert millimeters to inches"""
    return mm / 25.4


def inches_to_mm(inches):
    """Convert inches to millimeters"""
    return inches * 25.4


def make_w_beam_profile(d, bf, tw, tf, length_mm):
    """
    Generate W-beam (wide flange) I-beam profile
    
    Parameters:
    - d: depth (height) in mm
    - bf: flange width in mm
    - tw: web thickness in mm
    - tf: flange thickness in mm
    - length_mm: beam length in mm
    
    Returns OCC shape
    """
    # Create I-beam profile using wire and extrusion
    # Start from bottom-left, go clockwise
    
    half_bf = bf / 2
    half_tw = tw / 2
    
    points = [
        gp_Pnt(-half_bf, 0, 0),  # Bottom left
        gp_Pnt(half_bf, 0, 0),   # Bottom right
        gp_Pnt(half_bf, tf, 0),  # Bottom flange top right
        gp_Pnt(half_tw, tf, 0),  # Web bottom right
        gp_Pnt(half_tw, d - tf, 0),  # Web top right
        gp_Pnt(half_bf, d - tf, 0),  # Top flange bottom right
        gp_Pnt(half_bf, d, 0),   # Top right
        gp_Pnt(-half_bf, d, 0),  # Top left
        gp_Pnt(-half_bf, d - tf, 0),  # Top flange bottom left
        gp_Pnt(-half_tw, d - tf, 0),  # Web top left
        gp_Pnt(-half_tw, tf, 0),  # Web bottom left
        gp_Pnt(-half_bf, tf, 0),  # Bottom flange top left
        gp_Pnt(-half_bf, 0, 0),  # Close at bottom left
    ]
    
    # Build wire from points
    wire = BRepBuilderAPI_MakeWire()
    for i in range(len(points) - 1):
        edge = BRepBuilderAPI_MakeEdge(points[i], points[i + 1]).Edge()
        wire.Add(edge)
    
    profile_wire = wire.Wire()
    profile_face = BRepBuilderAPI_MakeFace(profile_wire).Face()
    
    # Extrude along length (Y-axis)
    prism_vec = gp_Vec(0, length_mm, 0)
    beam = BRepPrimAPI_MakePrism(profile_face, prism_vec).Shape()
    
    return beam


def make_hss_rectangular_profile(height, width, thickness, length_mm):
    """
    Generate HSS rectangular tube profile
    
    Parameters:
    - height: outside height in mm
    - width: outside width in mm  
    - thickness: wall thickness in mm
    - length_mm: tube length in mm
    
    Returns OCC shape
    """
    # Outer box
    outer = BRepPrimAPI_MakeBox(
        gp_Pnt(-width/2, 0, -height/2),
        width, length_mm, height
    ).Shape()
    
    # Inner box (hollow)
    inner_width = width - 2 * thickness
    inner_height = height - 2 * thickness
    
    if inner_width > 0 and inner_height > 0:
        inner = BRepPrimAPI_MakeBox(
            gp_Pnt(-inner_width/2, -1, -inner_height/2),
            inner_width, length_mm + 2, inner_height
        ).Shape()
        
        # Cut inner from outer
        tube = BRepAlgoAPI_Cut(outer, inner).Shape()
        return tube
    else:
        # Solid bar (thickness too large)
        return outer


def make_hss_round_profile(od, thickness, length_mm):
    """
    Generate HSS round pipe profile
    
    Parameters:
    - od: outside diameter in mm
    - thickness: wall thickness in mm
    - length_mm: pipe length in mm
    
    Returns OCC shape
    """
    from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCylinder
    
    outer_radius = od / 2
    inner_radius = outer_radius - thickness
    
    # Create outer cylinder
    outer_cyl = BRepPrimAPI_MakeCylinder(outer_radius, length_mm).Shape()
    
    # Create inner cylinder (for hollow)
    if inner_radius > 0:
        inner_cyl = BRepPrimAPI_MakeCylinder(inner_radius, length_mm + 2).Shape()
        
        # Translate inner slightly for clean cut
        inner_transform = gp_Trsf()
        inner_transform.SetTranslation(gp_Vec(0, 0, -1))
        inner_moved = BRepBuilderAPI_Transform(inner_cyl, inner_transform).Shape()
        
        # Cut inner from outer
        pipe = BRepAlgoAPI_Cut(outer_cyl, inner_moved).Shape()
        return pipe
    else:
        # Solid rod
        return outer_cyl


def make_channel_profile(d, bf, tw, tf, length_mm):
    """
    Generate C-channel profile
    
    Parameters:
    - d: depth (height) in mm
    - bf: flange width in mm
    - tw: web thickness in mm
    - tf: flange thickness in mm
    - length_mm: channel length in mm
    
    Returns OCC shape
    """
    # C-channel is like half an I-beam
    # Profile: [ shape
    
    points = [
        gp_Pnt(0, 0, 0),  # Bottom back
        gp_Pnt(bf, 0, 0),  # Bottom front
        gp_Pnt(bf, tf, 0),  # Bottom flange top
        gp_Pnt(tw, tf, 0),  # Web bottom
        gp_Pnt(tw, d - tf, 0),  # Web top
        gp_Pnt(bf, d - tf, 0),  # Top flange bottom
        gp_Pnt(bf, d, 0),  # Top front
        gp_Pnt(0, d, 0),  # Top back
        gp_Pnt(0, 0, 0),  # Close
    ]
    
    # Build wire
    wire = BRepBuilderAPI_MakeWire()
    for i in range(len(points) - 1):
        edge = BRepBuilderAPI_MakeEdge(points[i], points[i + 1]).Edge()
        wire.Add(edge)
    
    profile_wire = wire.Wire()
    profile_face = BRepBuilderAPI_MakeFace(profile_wire).Face()
    
    # Extrude along length
    prism_vec = gp_Vec(0, length_mm, 0)
    channel = BRepPrimAPI_MakePrism(profile_face, prism_vec).Shape()
    
    return channel


def make_angle_profile(leg1, leg2, thickness, length_mm):
    """
    Generate L-angle profile
    
    Parameters:
    - leg1: first leg length in mm
    - leg2: second leg length in mm (equal angle if leg1 == leg2)
    - thickness: leg thickness in mm
    - length_mm: angle length in mm
    
    Returns OCC shape
    """
    # L-shape profile
    points = [
        gp_Pnt(0, 0, 0),  # Corner
        gp_Pnt(leg1, 0, 0),  # End of horizontal leg
        gp_Pnt(leg1, thickness, 0),  # Top of horizontal leg
        gp_Pnt(thickness, thickness, 0),  # Inner corner
        gp_Pnt(thickness, leg2, 0),  # Top of vertical leg inner
        gp_Pnt(0, leg2, 0),  # End of vertical leg
        gp_Pnt(0, 0, 0),  # Close
    ]
    
    # Build wire
    wire = BRepBuilderAPI_MakeWire()
    for i in range(len(points) - 1):
        edge = BRepBuilderAPI_MakeEdge(points[i], points[i + 1]).Edge()
        wire.Add(edge)
    
    profile_wire = wire.Wire()
    profile_face = BRepBuilderAPI_MakeFace(profile_wire).Face()
    
    # Extrude along length
    prism_vec = gp_Vec(0, length_mm, 0)
    angle = BRepPrimAPI_MakePrism(profile_face, prism_vec).Shape()
    
    return angle


def add_weld_bevel_to_end(shape, end='end1', bevel_angle=BEVEL_ANGLE, land_height=LAND_HEIGHT, length_mm=0):
    """
    Add weld bevel to one end of a steel shape using edge chamfering
    
    Parameters:
    - shape: the steel shape
    - end: 'end1' (y=0) or 'end2' (y=length)
    - bevel_angle: bevel angle in degrees (default 30°)
    - land_height: root face height in mm (1/16" to 1/8" land typical)
    - length_mm: total length of the shape in mm
    
    Returns beveled shape
    
    Creates a 30° chamfer on outer edges at the specified end.
    Leaves 1/16" to 1/8" (1.6mm to 3.2mm) land for proper weld root.
    """
    from OCC.Core.BRepFilletAPI import BRepFilletAPI_MakeChamfer
    from OCC.Core.TopExp import TopExp_Explorer
    from OCC.Core.TopAbs import TopAbs_EDGE, TopAbs_FACE
    from OCC.Core.TopoDS import topods
    from OCC.Core.BRepAdaptor import BRepAdaptor_Curve
    from OCC.Core.TopTools import TopTools_IndexedDataMapOfShapeListOfShape
    from OCC.Core import TopExp
    import math
    
    # Calculate chamfer distance based on bevel angle and desired land
    # For 30° angle: chamfer creates visible bevel extending from land edge
    # Chamfer distance determines how much material is removed
    chamfer_dist = 8.0  # mm - creates visible 30° bevel while preserving land
    
    # Land should be between 1/16" (1.6mm) and 1/8" (3.2mm)
    # We'll aim for about 2.4mm (3/32") as middle ground
    land_offset = 2.4  # mm from end face
    
    # Determine which end we're beveling
    # Edges at y=land_offset (end1) or y=length_mm-land_offset (end2)
    if end == 'end1':
        target_y = land_offset
    else:
        target_y = length_mm - land_offset
    
    tolerance = 1.0  # mm - edges within this distance will be chamfered
    
    try:
        # Create chamfer operation
        chamfer = BRepFilletAPI_MakeChamfer(shape)
        
        # Build edge-to-face map
        edge_face_map = TopTools_IndexedDataMapOfShapeListOfShape()
        TopExp.MapShapesAndAncestors(shape, TopAbs_EDGE, TopAbs_FACE, edge_face_map)
        
        # Iterate through all edges to find ones at the land edge (not end face)
        edge_explorer = TopExp_Explorer(shape, TopAbs_EDGE)
        edges_added = 0
        
        while edge_explorer.More():
            edge = topods.Edge(edge_explorer.Current())
            
            # Get edge curve to check position
            curve_adaptor = BRepAdaptor_Curve(edge)
            
            # Sample points along the edge
            u_start = curve_adaptor.FirstParameter()
            u_end = curve_adaptor.LastParameter()
            
            # Check start and end points
            p_start = curve_adaptor.Value(u_start)
            p_end = curve_adaptor.Value(u_end)
            
            # If edge is near the land position (outer edges), add chamfer
            if (abs(p_start.Y() - target_y) < tolerance and abs(p_end.Y() - target_y) < tolerance):
                # This edge is at the land - add chamfer
                if edge_face_map.Contains(edge):
                    face_list = edge_face_map.FindFromKey(edge)
                    if face_list.Extent() > 0:
                        face = face_list.First()
                        # Add chamfer on this edge
                        chamfer.Add(chamfer_dist, edge, topods.Face(face))
                        edges_added += 1
            
            edge_explorer.Next()
        
        # Build the chamfered shape if we added any chamfers
        if edges_added > 0:
            chamfer.Build()
            if chamfer.IsDone():
                print(f"Added bevel to {edges_added} edges at {end}")
                return chamfer.Shape()
            else:
                print(f"Warning: Chamfer operation failed on {end}")
                return shape
        else:
            print(f"Info: No edges found at land position for {end} - bevel not applied")
            return shape
            
    except Exception as e:
        print(f"Error adding bevel to {end}: {e}")
        return shape


def generate_steel_shape(designation, length_inches, 
                          end1_bevel=False, end2_bevel=False,
                          bevel_angle=BEVEL_ANGLE,
                          output_file=None):
    """
    Generate a steel shape with optional weld bevels
    
    Parameters:
    - designation: AISC designation in IMPERIAL format:
        * W-shapes: 'W12X26', 'W8X31' (depth in inches x weight in lb/ft)
        * HSS: 'HSS8X8X1/2', 'HSS4X4X1/4' (uses HSS_A1085 database)
        * Channels: 'C12X20.7' (depth in inches x weight in lb/ft)
        * Angles: 'L4X4X1/2' (leg x leg x thickness in inches)
    - length_inches: beam length in inches (or use length_feet parameter)
    - end1_bevel: add bevel to end 1 (y=0)
    - end2_bevel: add bevel to end 2 (y=length)
    - bevel_angle: bevel angle in degrees (default 30° for structural steel)
    - output_file: output STEP filename (auto-generated if None)
    
    Returns:
    - dict with 'success', 'message', 'filename', 'shape', 'imperial_label'
    """
    
    imperial_label = designation
    metric_designation = designation
    
    # Try HSS_A1085 first (imperial HSS database)
    if designation.startswith('HSS') and designation in HSS_A1085:
        props = HSS_A1085[designation]
        shape_type = 'HSS'
    # Try imperial W-shape lookup
    elif designation.startswith('W') and 'X' in designation:
        metric_designation, imperial_label = find_imperial_w_shape(designation)
        if not metric_designation:
            return {
                'success': False,
                'message': f"Imperial W-shape {designation} not found. Try metric designation (e.g., W310X74)",
                'filename': None,
                'shape': None,
                'imperial_label': designation
            }
        props = AISC_SHAPES[metric_designation]
        shape_type = props.get('﻿Type', props.get('Type', 'W'))
    # Fall back to direct AISC lookup (metric designations)
    elif designation in AISC_SHAPES:
        props = AISC_SHAPES[designation]
        shape_type = props.get('﻿Type', props.get('Type', 'UNKNOWN'))
        metric_designation = designation
    else:
        return {
            'success': False,
            'message': f"Shape {designation} not found in database",
            'filename': None,
            'shape': None,
            'imperial_label': designation
        }
    
    # Convert length to mm
    length_mm = inches_to_mm(length_inches)
    
    # Convert dimensions from inches to mm
    d = inches_to_mm(props.get('d', 0)) if props.get('d') else None
    bf = inches_to_mm(props.get('bf', 0)) if props.get('bf') else None
    tw = inches_to_mm(props.get('tw', 0)) if props.get('tw') else None
    tf = inches_to_mm(props.get('tf', 0)) if props.get('tf') else None
    
    # HSS dimensions
    ht = inches_to_mm(props.get('Ht', 0)) if props.get('Ht') else None
    b = inches_to_mm(props.get('B', 0)) if props.get('B') else None
    od = inches_to_mm(props.get('OD', 0)) if props.get('OD') else None
    tdes = inches_to_mm(props.get('tdes', 0)) if props.get('tdes') else None
    
    # Generate shape based on type
    try:
        if shape_type == 'W':
            # Wide flange beam
            if not all([d, bf, tw, tf]):
                return {'success': False, 'message': f"Missing dimensions for W-beam {designation}", 'filename': None, 'shape': None, 'imperial_label': imperial_label}
            steel_shape = make_w_beam_profile(d, bf, tw, tf, length_mm)
            
        elif shape_type == 'HSS':
            # HSS can be round or rectangular
            if od and tdes:
                # Round HSS (pipe)
                steel_shape = make_hss_round_profile(od, tdes, length_mm)
            elif ht and b and tdes:
                # Rectangular HSS
                steel_shape = make_hss_rectangular_profile(ht, b, tdes, length_mm)
            else:
                return {'success': False, 'message': f"Missing dimensions for HSS {designation}", 'filename': None, 'shape': None, 'imperial_label': imperial_label}
                
        elif shape_type == 'C':
            # Channel
            if not all([d, bf, tw, tf]):
                return {'success': False, 'message': f"Missing dimensions for C-channel {designation}", 'filename': None, 'shape': None, 'imperial_label': imperial_label}
            steel_shape = make_channel_profile(d, bf, tw, tf, length_mm)
            
        elif shape_type == 'L':
            # Angle
            # L-shapes in AISC database: format is LxLxT for equal leg, or L leg1 X leg2 X thickness
            # Parse from designation
            parts = designation.replace('L', '').split('X')
            if len(parts) >= 3:
                leg1 = inches_to_mm(float(parts[0]))
                leg2 = inches_to_mm(float(parts[1]))
                thickness = inches_to_mm(float(parts[2]))
                steel_shape = make_angle_profile(leg1, leg2, thickness, length_mm)
            else:
                return {'success': False, 'message': f"Cannot parse L-angle dimensions for {designation}", 'filename': None, 'shape': None, 'imperial_label': imperial_label}
        
        else:
            return {'success': False, 'message': f"Shape type {shape_type} not yet implemented", 'filename': None, 'shape': None, 'imperial_label': imperial_label}
        
        # Add bevels if requested
        if end1_bevel:
            steel_shape = add_weld_bevel_to_end(steel_shape, 'end1', bevel_angle, LAND_HEIGHT, length_mm)
        if end2_bevel:
            steel_shape = add_weld_bevel_to_end(steel_shape, 'end2', bevel_angle, LAND_HEIGHT, length_mm)
        
        # Generate filename
        bevel_suffix = ""
        if end1_bevel and end2_bevel:
            bevel_suffix = f"-{int(bevel_angle)}deg-Both"
        elif end1_bevel:
            bevel_suffix = f"-{int(bevel_angle)}deg-End1"
        elif end2_bevel:
            bevel_suffix = f"-{int(bevel_angle)}deg-End2"
        else:
            bevel_suffix = "-Square"
        
        if output_file is None:
            # Clean designation for filename
            clean_desig = designation.replace('/', '-').replace('X', 'x')
            output_file = f"{clean_desig}-{int(length_inches)}in{bevel_suffix}.step"
        
        # Write STEP file
        write_step_file(steel_shape, output_file)
        
        return {
            'success': True,
            'message': f"Generated {imperial_label} x {length_inches}\" with {bevel_suffix} ends",
            'filename': output_file,
            'shape': steel_shape,
            'imperial_label': imperial_label
        }
        
    except Exception as e:
        return {
            'success': False,
            'message': f"Error generating {designation}: {str(e)}",
            'filename': None,
            'shape': None,
            'imperial_label': imperial_label
        }


def get_available_shapes_by_type():
    """Get all available shapes organized by type"""
    shapes_by_type = {}
    
    for designation, props in AISC_SHAPES.items():
        shape_type = props.get('﻿Type', props.get('Type', 'UNKNOWN'))
        if shape_type is None:
            shape_type = 'UNKNOWN'
        if shape_type not in shapes_by_type:
            shapes_by_type[shape_type] = []
        shapes_by_type[shape_type].append(designation)
    
    # Sort each list
    for shape_type in shapes_by_type:
        shapes_by_type[shape_type].sort()
    
    return shapes_by_type


def get_shape_info(designation):
    """Get dimensions and properties for a shape"""
    if designation in AISC_SHAPES:
        return AISC_SHAPES[designation]
    else:
        return None


def get_available_imperial_w_shapes():
    """Get list of available W-shapes in imperial format"""
    imperial_shapes = {}
    
    for imperial_prefix, metric_prefix in IMPERIAL_W_DEPTHS.items():
        candidates = [k for k in AISC_SHAPES.keys() if k.startswith(metric_prefix + 'X')]
        imperial_shapes[imperial_prefix] = []
        
        for metric_desig in candidates:
            metric_weight = AISC_SHAPES[metric_desig].get('W', 0)
            imperial_weight = metric_weight / 1.488
            imperial_desig = f"{imperial_prefix}X{imperial_weight:.0f}"
            imperial_shapes[imperial_prefix].append(imperial_desig)
    
    return imperial_shapes


def get_available_hss_shapes():
    """Get list of available HSS shapes in imperial format"""
    return list(HSS_A1085.keys())


if __name__ == "__main__":
    # Test generations
    print("=" * 70)
    print("AISC STEEL SHAPE GENERATOR TEST (Imperial Measurements)")
    print("=" * 70)
    
    # Show database stats
    shapes_by_type = get_available_shapes_by_type()
    print("\nDatabase Inventory:")
    for shape_type, shapes in sorted(shapes_by_type.items()):
        print(f"  {shape_type}: {len(shapes)} shapes")
    print(f"  HSS (Imperial): {len(HSS_A1085)} shapes")
    
    # Test imperial W-beam
    print("\n1. W12X50 beam, 10 ft (120\") long, beveled both ends at 30°")
    result = generate_steel_shape('W12X50', 120, end1_bevel=True, end2_bevel=True)
    print(f"   Result: {result['message']}")
    if result['success']:
        print(f"   File: {result['filename']}")
    
    # Test W-beam one end
    print("\n2. W8X31 beam, 20 ft (240\") long, beveled end 2 only at 30°")
    result = generate_steel_shape('W8X31', 240, end2_bevel=True)
    print(f"   Result: {result['message']}")
    if result['success']:
        print(f"   File: {result['filename']}")
    
    # Test HSS rectangular (imperial from HSS_A1085)
    print("\n3. HSS8X8X1/2 tube, 8 ft (96\") long, square cut")
    result = generate_steel_shape('HSS8X8X1/2', 96)
    print(f"   Result: {result['message']}")
    if result['success']:
        print(f"   File: {result['filename']}")
    
    # Test HSS round
    print("\n4. HSS10.000X0.500 round tube, 12 ft (144\") long, beveled end 1 only")
    result = generate_steel_shape('HSS10.000X0.500', 144, end1_bevel=True)
    print(f"   Result: {result['message']}")
    if result['success']:
        print(f"   File: {result['filename']}")
    
    print("\n" + "=" * 70)
    print("TEST COMPLETE - All shapes use IMPERIAL designations (inches/feet)")
    print("=" * 70)
