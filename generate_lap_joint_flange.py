"""
Lap Joint Flange Generator (RF and FF)
Generates ASME B16.5 lap joint flanges (loose flanges for use with stub ends).Units: MM (metric flange standards)
Lap Joint Features:
- Loose flange that slides over stub end
- Simple bore with no hub or attachment to pipe
- Lap radius provides bearing surface for stub end
- Typically flat face (FF) or raised face (RF), rarely RTJ
- Available: All classes 150-2500
"""

import sys
import os
import math
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCylinder, BRepPrimAPI_MakeRevol
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse, BRepAlgoAPI_Cut
from OCC.Core.BRepFilletAPI import BRepFilletAPI_MakeFillet
from OCC.Core.gp import gp_Pnt, gp_Ax1, gp_Dir, gp_Ax2
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire, BRepBuilderAPI_MakeFace
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.IFSelect import IFSelect_RetDone
from OCC.Core.Interface import Interface_Static
from OCC.Extend.TopologyUtils import TopologyExplorer
from OCC.Core.TopExp import TopExp_Explorer
from OCC.Core.TopAbs import TopAbs_EDGE

# Set STEP file units to millimeters
Interface_Static.SetCVal("write.step.unit", "MM")

# Import flange data
sys.path.append(r'C:\ParadiseSuite\scripts')
from flange_data import (
    CLASS_150_RF_WN, CLASS_300_RF_WN, CLASS_400_RF_WN,
    CLASS_600_RF_WN, CLASS_900_RF_WN, CLASS_1500_RF_WN, CLASS_2500_RF_WN
)

# Constants
RF_HEIGHT = 1.6  # Raised face height in mm
LAP_RADIUS = 3.0  # Lap radius on inner bore in mm

# Map class to data dictionaries
CLASS_DATA_MAP = {
    '150': CLASS_150_RF_WN,
    '300': CLASS_300_RF_WN,
    '400': CLASS_400_RF_WN,
    '600': CLASS_600_RF_WN,
    '900': CLASS_900_RF_WN,
    '1500': CLASS_1500_RF_WN,
    '2500': CLASS_2500_RF_WN
}


def make_cylinder(radius, height, z_start=0.0):
    """Create a cylinder at specified Z position."""
    ax = gp_Ax2(gp_Pnt(0, 0, z_start), gp_Dir(0, 0, 1))
    cylinder = BRepPrimAPI_MakeCylinder(ax, radius, height).Shape()
    return cylinder


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


def generate_lap_joint_flange(nps, pressure_class, facing='RF', output_dir=None):
    """
    Generate a lap joint flange (loose flange for stub ends).
    
    Args:
        nps: Nominal pipe size (e.g., '2', '1-1/2')
        pressure_class: Pressure class (e.g., '150', '600')
        facing: 'RF' for raised face or 'FF' for flat face
        output_dir: Output directory for STEP file
        
    Returns:
        Path to generated STEP file
    """
    print(f"\n=== Generating Lap Joint Flange: NPS {nps}, Class {pressure_class}, Facing: {facing} ===")
    
    # Get flange dimensions
    flange_data_dict = CLASS_DATA_MAP.get(pressure_class)
    if not flange_data_dict:
        raise ValueError(f"No flange data for Class {pressure_class}")
    
    if nps not in flange_data_dict:
        raise ValueError(f"No flange data for NPS {nps}, Class {pressure_class}")
    
    flange_dims = flange_data_dict[nps]
    
    # Extract dimensions
    flange_od = flange_dims['flange_od']
    flange_thickness = flange_dims['flange_thickness']
    rf_diameter = flange_dims['rf_diameter']
    bolt_circle_diameter = flange_dims['bolt_circle_diameter']
    num_bolts = flange_dims['bolt_holes']
    bolt_hole_diameter = flange_dims['bolt_hole_diameter']
    
    # Lap joint bore should accommodate stub end OD (use hub_base_diameter as reference)
    lap_bore = flange_dims.get('hub_base_diameter', flange_dims.get('bore_size', 50.0))
    
    # Calculate radii
    flange_radius = flange_od / 2.0
    rf_radius = rf_diameter / 2.0
    bolt_circle_radius = bolt_circle_diameter / 2.0
    lap_bore_radius = lap_bore / 2.0
    
    print(f"Lap bore: {lap_bore:.1f}mm (for stub end)")
    print(f"Flange OD: {flange_od:.1f}mm")
    print(f"Thickness: {flange_thickness:.1f}mm")
    
    # ===== Layer 1: Main flange body =====
    z_flange_bottom = 0.0
    z_flange_top = z_flange_bottom + flange_thickness
    
    print(f"\nLayer 1: Main body (OD={flange_od:.1f}mm, thickness={flange_thickness:.1f}mm)")
    body = make_cylinder(flange_radius, flange_thickness, z_flange_bottom)
    
    # ===== Layer 2: Raised face (if RF) =====
    if facing == 'RF':
        raised_collar_radius = rf_radius
        print(f"Layer 2: RF pad (R={rf_radius:.1f}mm, height={RF_HEIGHT:.2f}mm)")
        
        z_collar_bottom = z_flange_top
        z_face_top = z_collar_bottom + RF_HEIGHT
        
        collar = make_cylinder(raised_collar_radius, RF_HEIGHT, z_collar_bottom)
        body = BRepAlgoAPI_Fuse(body, collar).Shape()
    else:
        z_face_top = z_flange_top
        print(f"Layer 2: Flat face (no raised collar)")
    
    # Cut bore through flange (for stub end to pass through)
    bore_height = z_face_top - z_flange_bottom + 5
    through_bore = make_cylinder(lap_bore_radius, bore_height, z_flange_bottom)
    body = BRepAlgoAPI_Cut(body, through_bore).Shape()
    
    # Add lap radius fillet on back side inner edge
    print(f"Layer 3: Lap radius (R={LAP_RADIUS:.1f}mm) on inner bore back edge")
    try:
        fillet_maker = BRepFilletAPI_MakeFillet(body)
        edge_explorer = TopExp_Explorer(body, TopAbs_EDGE)
        edges_added = 0
        
        while edge_explorer.More():
            edge = edge_explorer.Current()
            # Try to add fillet to edges near the back bore
            try:
                fillet_maker.Add(LAP_RADIUS, edge)
                edges_added += 1
            except:
                pass  # Skip edges that can't be filleted
            edge_explorer.Next()
        
        if edges_added > 0:
            body = fillet_maker.Shape()
            print(f"  Applied fillet to {edges_added} edges")
    except Exception as e:
        print(f"  Note: Lap radius fillet not applied: {e}")
    
    # ===== Layer 4: Bolt holes =====
    print(f"Layer 4: Bolt holes (qty={num_bolts}, dia={bolt_hole_diameter:.1f}mm)")
    total_thickness = z_face_top - z_flange_bottom
    body = cut_bolt_holes(body, bolt_circle_radius, num_bolts, bolt_hole_diameter,
                          total_thickness, z_flange_bottom)
    
    # ===== Export to STEP =====
    if output_dir is None:
        output_dir = r'C:\Users\Jeff\EquationParadise\CAD\Lap_Joint_Flanges'
    
    os.makedirs(output_dir, exist_ok=True)
    
    facing_str = 'RF' if facing == 'RF' else 'FF'
    filename = f"LJ-{nps.replace('/', '-')}-Class{pressure_class}-{facing_str}.step"
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
        generate_lap_joint_flange(nps, pressure_class, facing)
    else:
        print("Usage: python generate_lap_joint_flange.py <NPS> <Class> [RF|FF]")
        print("Examples:")
        print("  python generate_lap_joint_flange.py 4 150 RF")
        print("  python generate_lap_joint_flange.py 2 600 FF")
        print("  python generate_lap_joint_flange.py 6 300")
