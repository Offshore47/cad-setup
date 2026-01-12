"""
Cold-Formed Steel Framing Generator - pythonocc
Generates CFS studs, track, and floor joists with punchouts

Standards: SSMA/AISI
Punchout pattern: ClarkDietrich standard (1.5" wide x 4" tall stadium, 24" O.C.)
Orientation: VERTICAL (4" tall x 1.5" wide) per industry standard
"""

import math
import json
import argparse
from pathlib import Path
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCylinder
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut, BRepAlgoAPI_Fuse
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeWire, BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeFace
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakePrism
from OCC.Core.gp import gp_Pnt, gp_Vec, gp_Dir, gp_Ax2
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.IFSelect import IFSelect_RetDone
from OCC.Core.TopoDS import TopoDS_Shape
from OCC.Core.Interface import Interface_Static

# Set STEP units to INCH
Interface_Static.SetCVal("write.step.unit", "IN")


# Load CFS data
SCRIPT_DIR = Path(__file__).parent
DATA_FILE = SCRIPT_DIR / "cfs_framing_data.json"

def load_cfs_data():
    """Load CFS framing data from JSON file"""
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

CFS_DATA = load_cfs_data()


def create_stadium_shape(height: float, width: float, thickness: float, center_z: float) -> TopoDS_Shape:
    """
    Create a stadium (rounded rectangle) shaped solid for punchout.
    VERTICAL ORIENTATION: height is vertical (Z), width is horizontal (Y along member)
    
    Parameters:
        height: Height of punchout (vertical dimension on web) - typically 4"
        width: Width of punchout (horizontal along member) - typically 1.5"
        thickness: Extrusion depth (material thickness to cut through)
        center_z: Z position of punchout center on web
    
    Returns:
        TopoDS_Shape - stadium prism for boolean cut
    """
    # Stadium = rectangle with semicircle ends (vertically oriented)
    # Semicircles are at top and bottom, straight edges on sides
    radius = width / 2
    straight_height = height - width  # Height of straight section
    
    # Build profile wire in YZ plane (will extrude in X for cutting web)
    pts = []
    
    # Start at bottom center, go counter-clockwise
    # Bottom semicircle
    num_arc_pts = 10
    for i in range(num_arc_pts + 1):
        angle = -math.pi/2 - (math.pi * i / num_arc_pts)  # -90° to -270° (or 90°)
        y = radius * math.cos(angle)
        z = center_z - straight_height/2 + radius * math.sin(angle)
        pts.append(gp_Pnt(0, y, z))
    
    # Left edge going up
    # Already at top of bottom semicircle, left side
    
    # Top semicircle
    for i in range(num_arc_pts + 1):
        angle = math.pi/2 - (math.pi * i / num_arc_pts)  # 90° to -90°
        y = radius * math.cos(angle)
        z = center_z + straight_height/2 + radius * math.sin(angle)
        pts.append(gp_Pnt(0, y, z))
    
    # Right edge going down - closes back to start
    
    # Build wire
    wire_builder = BRepBuilderAPI_MakeWire()
    for i in range(len(pts) - 1):
        edge = BRepBuilderAPI_MakeEdge(pts[i], pts[i+1]).Edge()
        wire_builder.Add(edge)
    # Close wire
    closing_edge = BRepBuilderAPI_MakeEdge(pts[-1], pts[0]).Edge()
    wire_builder.Add(closing_edge)
    
    wire = wire_builder.Wire()
    face = BRepBuilderAPI_MakeFace(wire).Face()
    
    # Extrude in X direction (through material thickness + extra for clean cut)
    prism = BRepPrimAPI_MakePrism(face, gp_Vec(thickness + 0.1, 0, 0)).Shape()
    
    return prism


def generate_c_section(web: float, flange: float, lip: float, thickness: float, length: float) -> TopoDS_Shape:
    """
    Generate a C-section (stud/joist) profile extruded to length.
    
    Profile (looking at end):
        ___
       |   <- lip
       |
       |_______ <- flange
             |
             |  <- web
             |
       ______| <- flange
       |
       |___ <- lip
    
    Parameters:
        web: Web height (depth of stud)
        flange: Flange width
        lip: Lip length (return)
        thickness: Material thickness
        length: Extrusion length
    
    Returns:
        TopoDS_Shape - C-section solid
    """
    t = thickness
    
    # Build profile as series of boxes and fuse them
    # Web - vertical center piece
    web_box = BRepPrimAPI_MakeBox(
        gp_Pnt(-t/2, 0, 0),
        t, length, web
    ).Shape()
    
    # Bottom flange - horizontal piece at z=0
    bottom_flange = BRepPrimAPI_MakeBox(
        gp_Pnt(-t/2, 0, 0),
        flange + t/2, length, t
    ).Shape()
    
    # Top flange - horizontal piece at z=web-t
    top_flange = BRepPrimAPI_MakeBox(
        gp_Pnt(-t/2, 0, web - t),
        flange + t/2, length, t
    ).Shape()
    
    # Bottom lip - vertical piece at end of bottom flange
    bottom_lip = BRepPrimAPI_MakeBox(
        gp_Pnt(flange - t/2, 0, 0),
        t, length, lip
    ).Shape()
    
    # Top lip - vertical piece at end of top flange
    top_lip = BRepPrimAPI_MakeBox(
        gp_Pnt(flange - t/2, 0, web - lip),
        t, length, lip
    ).Shape()
    
    # Fuse all pieces
    fuse1 = BRepAlgoAPI_Fuse(web_box, bottom_flange)
    fuse1.Build()
    shape = fuse1.Shape()
    
    fuse2 = BRepAlgoAPI_Fuse(shape, top_flange)
    fuse2.Build()
    shape = fuse2.Shape()
    
    fuse3 = BRepAlgoAPI_Fuse(shape, bottom_lip)
    fuse3.Build()
    shape = fuse3.Shape()
    
    fuse4 = BRepAlgoAPI_Fuse(shape, top_lip)
    fuse4.Build()
    shape = fuse4.Shape()
    
    return shape


def generate_u_section(web: float, flange: float, thickness: float, length: float) -> TopoDS_Shape:
    """
    Generate a U-section (track) profile extruded to length.
    
    Profile (looking at end):
       |           |
       |           |  <- flanges
       |___________|  <- web
    
    Parameters:
        web: Web width (inside dimension)
        flange: Flange height
        thickness: Material thickness
        length: Extrusion length
    
    Returns:
        TopoDS_Shape - U-section solid
    """
    t = thickness
    
    # Web - horizontal bottom piece
    web_box = BRepPrimAPI_MakeBox(
        gp_Pnt(0, 0, 0),
        web + 2*t, length, t
    ).Shape()
    
    # Left flange - vertical piece
    left_flange = BRepPrimAPI_MakeBox(
        gp_Pnt(0, 0, 0),
        t, length, flange
    ).Shape()
    
    # Right flange - vertical piece
    right_flange = BRepPrimAPI_MakeBox(
        gp_Pnt(web + t, 0, 0),
        t, length, flange
    ).Shape()
    
    # Fuse all pieces
    fuse1 = BRepAlgoAPI_Fuse(web_box, left_flange)
    fuse1.Build()
    shape = fuse1.Shape()
    
    fuse2 = BRepAlgoAPI_Fuse(shape, right_flange)
    fuse2.Build()
    shape = fuse2.Shape()
    
    return shape


def add_punchouts(shape: TopoDS_Shape, web: float, length: float, thickness: float,
                  punchout_height: float = 4.0, punchout_width: float = 1.5,
                  spacing: float = 24.0, first_offset: float = 12.0) -> TopoDS_Shape:
    """
    Add punchouts (knockout holes) to a C-section.
    VERTICAL ORIENTATION: 4" tall x 1.5" wide (industry standard)
    
    Parameters:
        shape: The C-section shape to cut punchouts from
        web: Web height (to center punchouts)
        length: Total length of member
        thickness: Material thickness
        punchout_height: Height of punchout (vertical) - typically 4"
        punchout_width: Width of punchout (horizontal) - typically 1.5"
        spacing: Center-to-center spacing of punchouts
        first_offset: Distance from end to first punchout center
    
    Returns:
        TopoDS_Shape with punchouts cut
    """
    # Calculate punchout positions along length (Y axis)
    positions = []
    pos = first_offset
    while pos < length - first_offset:
        positions.append(pos)
        pos += spacing
    
    # Center Z position for punchouts on web
    center_z = web / 2
    
    result = shape
    for y_pos in positions:
        # Create stadium punchout shape (vertical orientation)
        # Height = 4" (vertical), Width = 1.5" (horizontal along member)
        punchout = create_stadium_shape(
            punchout_height,   # 4" tall (vertical)
            punchout_width,    # 1.5" wide (horizontal)
            thickness * 2,     # Extra thick to ensure clean cut
            center_z           # Centered on web
        )
        
        # Move punchout to correct position
        # X: position at web face (-thickness/2 to cut through web)
        # Y: along length of member
        from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform
        from OCC.Core.gp import gp_Trsf
        
        trsf = gp_Trsf()
        trsf.SetTranslation(gp_Vec(-thickness, y_pos, 0))
        punchout_positioned = BRepBuilderAPI_Transform(punchout, trsf).Shape()
        
        # Cut punchout from shape
        cut_op = BRepAlgoAPI_Cut(result, punchout_positioned)
        cut_op.Build()
        if cut_op.IsDone():
            result = cut_op.Shape()
    
    return result


def generate_cfs_stud(size: str, gauge: str, length_ft: float, 
                      with_punchouts: bool = True, output_file: str = None) -> dict:
    """
    Generate a CFS wall stud.
    
    Parameters:
        size: Size code (e.g., "362S", "600S")
        gauge: Gauge/mil (e.g., "43", "54")
        length_ft: Length in feet
        with_punchouts: Whether to add punchout holes
        output_file: Output STEP file path
    
    Returns:
        dict with success status and file path
    """
    try:
        stud_data = CFS_DATA["studs"]["sizes"].get(size)
        if not stud_data:
            return {"success": False, "message": f"Unknown stud size: {size}"}
        
        gauge_data = CFS_DATA["gauges"].get(gauge)
        if not gauge_data:
            return {"success": False, "message": f"Unknown gauge: {gauge}"}
        
        web = stud_data["web"]
        flange = stud_data["flange"]
        lip = stud_data["lip"]
        thickness = gauge_data["decimal"]
        length = length_ft * 12  # Convert to inches
        
        print(f"=== CFS Stud Parameters ===")
        print(f"Designation: {stud_data['designation']}-{gauge}")
        print(f"Web: {web}\"")
        print(f"Flange: {flange}\"")
        print(f"Lip: {lip}\"")
        print(f"Thickness: {gauge} mil ({thickness:.4f}\")")
        print(f"Length: {length_ft}' = {length}\"")
        
        # Generate C-section
        shape = generate_c_section(web, flange, lip, thickness, length)
        print("C-section created")
        
        # Add punchouts if requested
        if with_punchouts and length >= 24:
            punchout_data = CFS_DATA["punchouts"]["standard"]
            shape = add_punchouts(
                shape, web, length, thickness,
                punchout_data["height"],   # 4" tall (vertical)
                punchout_data["width"],    # 1.5" wide (horizontal)
                punchout_data["spacing"],
                punchout_data["first_from_end"]
            )
            print("Punchouts added (vertical orientation: 4\" tall x 1.5\" wide)")
        
        # Generate filename if not provided
        if output_file is None:
            len_str = f"{length_ft:.3g}".replace('.', '-')
            output_file = f"Stud-{stud_data['designation']}-{gauge}-{len_str}ft.step"
        
        # Export STEP
        writer = STEPControl_Writer()
        writer.Transfer(shape, STEPControl_AsIs)
        status = writer.Write(output_file)
        
        if status == IFSelect_RetDone:
            print(f"Exported: {output_file}")
            return {"success": True, "file": output_file}
        else:
            return {"success": False, "message": "STEP export failed"}
            
    except Exception as e:
        return {"success": False, "message": str(e)}


def generate_cfs_track(size: str, gauge: str, length_ft: float, 
                       output_file: str = None) -> dict:
    """
    Generate a CFS track (U-channel).
    
    Parameters:
        size: Size code (e.g., "362T", "600T")
        gauge: Gauge/mil (e.g., "43", "54")
        length_ft: Length in feet
        output_file: Output STEP file path
    
    Returns:
        dict with success status and file path
    """
    try:
        track_data = CFS_DATA["track"]["sizes"].get(size)
        if not track_data:
            return {"success": False, "message": f"Unknown track size: {size}"}
        
        gauge_data = CFS_DATA["gauges"].get(gauge)
        if not gauge_data:
            return {"success": False, "message": f"Unknown gauge: {gauge}"}
        
        web = track_data["web"]
        flange = track_data["flange"]
        thickness = gauge_data["decimal"]
        length = length_ft * 12
        
        print(f"=== CFS Track Parameters ===")
        print(f"Designation: {track_data['designation']}-{gauge}")
        print(f"Web: {web}\"")
        print(f"Flange: {flange}\"")
        print(f"Thickness: {gauge} mil ({thickness:.4f}\")")
        print(f"Length: {length_ft}' = {length}\"")
        
        # Generate U-section
        shape = generate_u_section(web, flange, thickness, length)
        print("U-section created")
        
        # Generate filename if not provided
        if output_file is None:
            len_str = f"{length_ft:.3g}".replace('.', '-')
            output_file = f"Track-{track_data['designation']}-{gauge}-{len_str}ft.step"
        
        # Export STEP
        writer = STEPControl_Writer()
        writer.Transfer(shape, STEPControl_AsIs)
        status = writer.Write(output_file)
        
        if status == IFSelect_RetDone:
            print(f"Exported: {output_file}")
            return {"success": True, "file": output_file}
        else:
            return {"success": False, "message": "STEP export failed"}
            
    except Exception as e:
        return {"success": False, "message": str(e)}


def generate_cfs_joist(size: str, gauge: str, length_ft: float,
                       with_punchouts: bool = True, output_file: str = None) -> dict:
    """
    Generate a CFS floor/ceiling joist.
    
    Parameters:
        size: Size code (e.g., "800J", "1000J")
        gauge: Gauge/mil (e.g., "54", "68")
        length_ft: Length in feet
        with_punchouts: Whether to add punchout holes
        output_file: Output STEP file path
    
    Returns:
        dict with success status and file path
    """
    try:
        joist_data = CFS_DATA["joists"]["sizes"].get(size)
        if not joist_data:
            return {"success": False, "message": f"Unknown joist size: {size}"}
        
        gauge_data = CFS_DATA["gauges"].get(gauge)
        if not gauge_data:
            return {"success": False, "message": f"Unknown gauge: {gauge}"}
        
        web = joist_data["web"]
        flange = joist_data["flange"]
        lip = joist_data["lip"]
        thickness = gauge_data["decimal"]
        length = length_ft * 12
        
        print(f"=== CFS Joist Parameters ===")
        print(f"Designation: {joist_data['designation']}-{gauge}")
        print(f"Web (Depth): {web}\"")
        print(f"Flange: {flange}\"")
        print(f"Lip: {lip}\"")
        print(f"Thickness: {gauge} mil ({thickness:.4f}\")")
        print(f"Length: {length_ft}' = {length}\"")
        
        # Generate C-section
        shape = generate_c_section(web, flange, lip, thickness, length)
        print("C-section created")
        
        # Add punchouts if requested
        if with_punchouts and length >= 24:
            punchout_data = CFS_DATA["punchouts"]["standard"]
            shape = add_punchouts(
                shape, web, length, thickness,
                punchout_data["height"],   # 4" tall (vertical)
                punchout_data["width"],    # 1.5" wide (horizontal)
                punchout_data["spacing"],
                punchout_data["first_from_end"]
            )
            print("Punchouts added (vertical orientation: 4\" tall x 1.5\" wide)")
        
        # Generate filename if not provided
        if output_file is None:
            len_str = f"{length_ft:.3g}".replace('.', '-')
            output_file = f"Joist-{joist_data['designation']}-{gauge}-{len_str}ft.step"
        
        # Export STEP
        writer = STEPControl_Writer()
        writer.Transfer(shape, STEPControl_AsIs)
        status = writer.Write(output_file)
        
        if status == IFSelect_RetDone:
            print(f"Exported: {output_file}")
            return {"success": True, "file": output_file}
        else:
            return {"success": False, "message": "STEP export failed"}
            
    except Exception as e:
        return {"success": False, "message": str(e)}


def main():
    parser = argparse.ArgumentParser(description='Generate CFS framing members')
    parser.add_argument('type', choices=['stud', 'track', 'joist'], 
                        help='Type of framing member')
    parser.add_argument('size', help='Size code (e.g., 362S, 600T, 800J)')
    parser.add_argument('gauge', help='Gauge in mil (e.g., 43, 54, 68)')
    parser.add_argument('length', type=float, help='Length in feet')
    parser.add_argument('--no-punchouts', action='store_true',
                        help='Generate without punchouts (for headers, etc.)')
    parser.add_argument('--output', '-o', type=str, default=None,
                        help='Output STEP filename')
    
    args = parser.parse_args()
    
    if args.type == 'stud':
        result = generate_cfs_stud(
            args.size, args.gauge, args.length,
            with_punchouts=not args.no_punchouts,
            output_file=args.output
        )
    elif args.type == 'track':
        result = generate_cfs_track(
            args.size, args.gauge, args.length,
            output_file=args.output
        )
    elif args.type == 'joist':
        result = generate_cfs_joist(
            args.size, args.gauge, args.length,
            with_punchouts=not args.no_punchouts,
            output_file=args.output
        )
    
    if not result['success']:
        print(f"ERROR: {result['message']}")


if __name__ == '__main__':
    main()
