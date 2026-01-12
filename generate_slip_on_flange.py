"""
Slip-On Flange Generator (RF and RTJ)
Generates ASME B16.5 slip-on flanges with raised face or ring joint facing.Units: MM (metric flange standards)
Slip-On Features:
- Short straight cylindrical hub
- Pipe slips inside hub and is fillet welded on both sides
- Simpler than weld neck (no taper or bevel)
- Available: Classes 150, 300, 400, 600, 900, 1500 (no Class 2500)
"""

import sys
import os
import math
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCylinder, BRepPrimAPI_MakeRevol
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse, BRepAlgoAPI_Cut
from OCC.Core.gp import gp_Pnt, gp_Ax1, gp_Dir, gp_Ax2
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire, BRepBuilderAPI_MakeFace
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.IFSelect import IFSelect_RetDone
from OCC.Core.Interface import Interface_Static
from OCC.Extend.TopologyUtils import TopologyExplorer

# Set STEP file units to millimeters
Interface_Static.SetCVal("write.step.unit", "MM")

# Import flange data
sys.path.append(r'C:\ParadiseSuite\scripts')
from flange_data import (
    CLASS_150_RF_WN, CLASS_300_RF_WN, CLASS_400_RF_WN,
    CLASS_600_RF_WN, CLASS_900_RF_WN, CLASS_1500_RF_WN
)
from slip_on_flange_data import get_slip_on_dimensions
from gasket_data import RING_JOINT_TYPE_R_GASKETS
from rtj_ring_map import get_ring_number_for_flange

# Constants
RF_HEIGHT = 1.6  # Raised face height in mm
GROOVE_ANGLE_DEG = 23.0  # RTJ groove wall angle
GROOVE_ANGLE_RAD = math.radians(GROOVE_ANGLE_DEG)

# Map class to data dictionaries
CLASS_DATA_MAP = {
    '150': CLASS_150_RF_WN,
    '300': CLASS_300_RF_WN,
    '400': CLASS_400_RF_WN,
    '600': CLASS_600_RF_WN,
    '900': CLASS_900_RF_WN,
    '1500': CLASS_1500_RF_WN
}


def make_cylinder(radius, height, z_start=0.0):
    """Create a cylinder at specified Z position."""
    ax = gp_Ax2(gp_Pnt(0, 0, z_start), gp_Dir(0, 0, 1))
    cylinder = BRepPrimAPI_MakeCylinder(ax, radius, height).Shape()
    return cylinder


def make_slip_on_hub(hub_bore, hub_outer_diameter, hub_length, z_flange_bottom):
    """
    Create slip-on hub - simple straight cylinder.
    
    Args:
        hub_bore: Inner diameter of hub (pipe slips inside)
        hub_outer_diameter: Outer diameter of hub
        hub_length: Length of hub extending below flange
        z_flange_bottom: Z coordinate of flange bottom
        
    Returns:
        Hub shape
    """
    hub_inner_radius = hub_bore / 2.0
    hub_outer_radius = hub_outer_diameter / 2.0
    
    # Hub extends below flange
    z_hub_bottom = z_flange_bottom - hub_length
    
    # Create outer cylinder
    hub_outer = make_cylinder(hub_outer_radius, hub_length, z_hub_bottom)
    
    # Cut inner bore
    hub_bore_cyl = make_cylinder(hub_inner_radius, hub_length, z_hub_bottom)
    hub_shape = BRepAlgoAPI_Cut(hub_outer, hub_bore_cyl).Shape()
    
    return hub_shape


def cut_bolt_holes(shape, bolt_circle_radius, num_bolts, bolt_hole_diameter, thickness, z_bottom):
    """Cut bolt holes around the bolt circle."""
    result = shape
    bolt_hole_radius = bolt_hole_diameter / 2.0
    
    for i in range(num_bolts):
        angle = (2.0 * math.pi * i) / num_bolts
        x = bolt_circle_radius * math.cos(angle)
        y = bolt_circle_radius * math.sin(angle)
        
        bolt_hole = make_cylinder(bolt_hole_radius, thickness + 20, z_bottom - 5)
        
        # Translate bolt hole to position
        from OCC.Core.gp import gp_Vec, gp_Trsf
        from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform
        trsf = gp_Trsf()
        trsf.SetTranslation(gp_Vec(x, y, 0))
        bolt_hole = BRepBuilderAPI_Transform(bolt_hole, trsf).Shape()
        
        result = BRepAlgoAPI_Cut(result, bolt_hole).Shape()
    
    return result


def cut_rtj_groove(shape, pitch_radius, groove_depth, groove_width, z_face_top):
    """Cut RTJ groove with 23° tapered walls and flat bottom."""
    half_width = groove_width / 2.0
    inner_radius = pitch_radius - half_width
    outer_radius = pitch_radius + half_width
    
    horizontal_travel = groove_depth * math.tan(GROOVE_ANGLE_RAD)
    z_bottom = z_face_top - groove_depth
    
    outer_top_r = outer_radius
    outer_bottom_r = outer_radius - horizontal_travel
    inner_bottom_r = inner_radius + horizontal_travel
    inner_top_r = inner_radius
    
    # Create wire for groove profile
    p1 = gp_Pnt(outer_top_r, 0, z_face_top)
    p2 = gp_Pnt(outer_bottom_r, 0, z_bottom)
    p3 = gp_Pnt(inner_bottom_r, 0, z_bottom)
    p4 = gp_Pnt(inner_top_r, 0, z_face_top)
    
    edge1 = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
    edge2 = BRepBuilderAPI_MakeEdge(p2, p3).Edge()
    edge3 = BRepBuilderAPI_MakeEdge(p3, p4).Edge()
    edge4 = BRepBuilderAPI_MakeEdge(p4, p1).Edge()
    
    wire_builder = BRepBuilderAPI_MakeWire()
    wire_builder.Add(edge1)
    wire_builder.Add(edge2)
    wire_builder.Add(edge3)
    wire_builder.Add(edge4)
    wire = wire_builder.Wire()
    
    face = BRepBuilderAPI_MakeFace(wire).Face()
    revolve_axis = gp_Ax1(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1))
    groove_solid = BRepPrimAPI_MakeRevol(face, revolve_axis, 2 * math.pi).Shape()
    
    result = BRepAlgoAPI_Cut(shape, groove_solid).Shape()
    return result


def get_ring_data(ring_number):
    """Get ring gasket dimensions from gasket_data."""
    ring_key = ring_number.replace('-', '')
    
    if ring_key not in RING_JOINT_TYPE_R_GASKETS:
        ring_key = f"R-{ring_number[1:]}" if ring_number.startswith('R') else ring_number
        if ring_key not in RING_JOINT_TYPE_R_GASKETS:
            raise ValueError(f"Ring gasket data not found for {ring_number}")
    
    return RING_JOINT_TYPE_R_GASKETS[ring_key]


def generate_slip_on_flange(nps, pressure_class, facing='RF', output_dir=None):
    """
    Generate a slip-on flange.
    
    Args:
        nps: Nominal pipe size (e.g., '2', '1-1/2')
        pressure_class: Pressure class (e.g., '150', '600')
        facing: 'RF' for raised face or 'RTJ' for ring joint
        output_dir: Output directory for STEP file
        
    Returns:
        Path to generated STEP file
    """
    print(f"\n=== Generating Slip-On Flange: NPS {nps}, Class {pressure_class}, Facing: {facing} ===")
    
    # Get flange dimensions
    flange_data_dict = CLASS_DATA_MAP.get(pressure_class)
    if not flange_data_dict:
        raise ValueError(f"No flange data for Class {pressure_class}")
    
    if nps not in flange_data_dict:
        raise ValueError(f"No flange data for NPS {nps}, Class {pressure_class}")
    
    flange_dims = flange_data_dict[nps]
    
    # Get slip-on hub bore
    slip_on_dims = get_slip_on_dimensions(nps, pressure_class)
    hub_bore = slip_on_dims['hub_bore']
    
    # Extract dimensions
    flange_od = flange_dims['flange_od']
    flange_thickness = flange_dims['flange_thickness']
    rf_diameter = flange_dims['rf_diameter']
    bolt_circle_diameter = flange_dims['bolt_circle_diameter']
    num_bolts = flange_dims['bolt_holes']
    bolt_hole_diameter = flange_dims['bolt_hole_diameter']
    hub_diameter = flange_dims.get('hub_base_diameter', slip_on_dims['hub_bore'] * 1.4)
    hub_thickness = flange_dims.get('hub_thickness', 0)
    
    # Calculate radii
    flange_radius = flange_od / 2.0
    rf_radius = rf_diameter / 2.0
    bolt_circle_radius = bolt_circle_diameter / 2.0
    hub_outer_radius = hub_diameter / 2.0
    
    # Hub length estimate (typically 1/2 to 2/3 of flange thickness)
    hub_length = flange_thickness * 0.6
    
    print(f"Hub bore: {hub_bore:.1f}mm")
    print(f"Hub OD: {hub_diameter:.1f}mm")
    print(f"Hub length: {hub_length:.1f}mm (estimated)")
    
    # ===== Layer 1: Main flange body =====
    z_flange_bottom = 0.0
    z_flange_top = z_flange_bottom + flange_thickness
    
    print(f"\nLayer 1: Main body (OD={flange_od:.1f}mm, thickness={flange_thickness:.1f}mm)")
    body = make_cylinder(flange_radius, flange_thickness, z_flange_bottom)
    
    # ===== Layer 2: Raised face or RTJ collar =====
    if facing == 'RTJ':
        # Get ring data
        ring_number = get_ring_number_for_flange(nps, pressure_class)
        ring_data = get_ring_data(ring_number)
        pitch_radius = ring_data['pitch_diameter_mm'] / 2.0
        raised_collar_radius = pitch_radius * 1.1
        
        print(f"Layer 2: RTJ raised collar (R={raised_collar_radius:.1f}mm, height={RF_HEIGHT:.2f}mm)")
        print(f"Ring: {ring_number}, Pitch: {pitch_radius:.1f}mm")
    else:
        raised_collar_radius = rf_radius
        print(f"Layer 2: RF pad (R={rf_radius:.1f}mm, height={RF_HEIGHT:.2f}mm)")
    
    z_collar_bottom = z_flange_top
    z_face_top = z_collar_bottom + RF_HEIGHT
    
    collar = make_cylinder(raised_collar_radius, RF_HEIGHT, z_collar_bottom)
    body = BRepAlgoAPI_Fuse(body, collar).Shape()
    
    # Cut bore through main body AND raised face (start at flange bottom, not below)
    hub_bore_radius = hub_bore / 2.0
    bore_height = z_face_top - z_flange_bottom + 5  # Through flange + RF only
    through_bore = make_cylinder(hub_bore_radius, bore_height, z_flange_bottom)
    body = BRepAlgoAPI_Cut(body, through_bore).Shape()
    
    # ===== Layer 3: Slip-on hub =====
    print(f"Layer 3: Slip-on hub (bore={hub_bore:.1f}mm, OD={hub_diameter:.1f}mm)")
    slip_on_hub = make_slip_on_hub(hub_bore, hub_diameter, hub_length, z_flange_bottom)
    body = BRepAlgoAPI_Fuse(body, slip_on_hub).Shape()
    
    # ===== Layer 4: RTJ Groove (if RTJ facing) =====
    if facing == 'RTJ':
        groove_depth = ring_data['octagonal_height_mm'] + 1.0
        groove_width = ring_data['width_mm'] + 1.0
        print(f"Layer 4: RTJ groove (depth={groove_depth:.1f}mm, width={groove_width:.1f}mm)")
        body = cut_rtj_groove(body, pitch_radius, groove_depth, groove_width, z_face_top)
    
    # ===== Layer 5: Bolt holes =====
    print(f"Layer 5: Bolt holes (qty={num_bolts}, dia={bolt_hole_diameter:.1f}mm)")
    total_thickness = z_face_top - z_flange_bottom
    body = cut_bolt_holes(body, bolt_circle_radius, num_bolts, bolt_hole_diameter,
                          total_thickness, z_flange_bottom)
    
    # ===== Export to STEP =====
    if output_dir is None:
        output_dir = r'C:\Users\Jeff\EquationParadise\CAD\Slip_On_Flanges'
    
    os.makedirs(output_dir, exist_ok=True)
    
    facing_str = 'RTJ' if facing == 'RTJ' else 'RF'
    filename = f"SO-{nps.replace('/', '-')}-Class{pressure_class}-{facing_str}.step"
    output_path = os.path.join(output_dir, filename)
    
    print(f"\nExporting to: {output_path}")
    
    step_writer = STEPControl_Writer()
    step_writer.Transfer(body, STEPControl_AsIs)
    status = step_writer.Write(output_path)
    
    if status != IFSelect_RetDone:
        raise Exception("Error writing STEP file")
    
    # Count entities
    topo = TopologyExplorer(body)
    num_faces = sum(1 for _ in topo.faces())
    num_edges = sum(1 for _ in topo.edges())
    
    print(f"✓ Successfully generated: {filename}")
    print(f"  Faces: {num_faces}, Edges: {num_edges}")
    print(f"  Total height: {z_face_top - z_flange_bottom:.2f}mm")
    
    return output_path


if __name__ == '__main__':
    if len(sys.argv) >= 3:
        nps = sys.argv[1]
        pressure_class = sys.argv[2]
        facing = sys.argv[3] if len(sys.argv) > 3 else 'RF'
        generate_slip_on_flange(nps, pressure_class, facing)
    else:
        print("Usage: python generate_slip_on_flange.py <NPS> <Class> [RF|RTJ]")
        print("Examples:")
        print("  python generate_slip_on_flange.py 4 150 RF")
        print("  python generate_slip_on_flange.py 2 900 RTJ")
        print("  python generate_slip_on_flange.py 6 600")
