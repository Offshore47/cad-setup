"""
API 6A/6BX Flange Generator - Correct Geometry from Drawing
Based on API 6A TYPE 6BX WELDING NECK FLANGE RTJ drawingUnits: MM (metric flange standards)
Profile (face down on table, looking from side, tracing counterclockwise from OD):
1. OD with C chamfer at back
2. Up to back of flange
3. Back of flange (T thickness from face)
4. In along back to hub
5. Down hub taper (J1 to land)
6. Land (1.6mm) 
7. 37.5° weld bevel to bore
8. Bore goes straight to face
9. At face: flat from bore to J2 (inner groove edge)
10. 23° wall down to groove flat (depth Q)
11. Flat at groove bottom (ring seats here, at bolt face level)
12. 23° wall back up to K (outer groove edge at face)
13. At face: raised face from K to... step down Q
14. Bolt seating face (T-Q from back)
15. Out to OD

Ring groove geometry:
- K = groove OD at face (wide at top)
- J2 = groove ID at face  
- Walls at 23° angle going inward as you go down
- Depth = Q
- Flat at bottom where ring seats (width ≈ ring flat C)
- Groove bottom is at SAME LEVEL as bolt seating face
"""

import math
from OCC.Core.gp import gp_Pnt, gp_Dir, gp_Ax1, gp_Ax2
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeRevol, BRepPrimAPI_MakeCylinder
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire, BRepBuilderAPI_MakeFace
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.Interface import Interface_Static

# Set STEP file units to millimeters
Interface_Static.SetCVal("write.step.unit", "MM")

# =============================================================================
# API 6BX FLANGE DATA (dimensions in mm)
# =============================================================================
# (B, OD, C, E1, Q, G, K, T, J1, J2, J3, J4, R, BC, N, H, RingNo)

API_6BX_DATA = {
    # 10000 psi
    ("6BX", 10000, "1-13/16"): (46.8, 210, 3, None, 4.37, 101.6, 114.3, 44.5, 133.4, 82.6, 36.5, None, 6, 158.8, 4, 26, 164),
    ("6BX", 10000, "2-1/16"): (53.2, 235, 3, None, 4.76, 114.3, 127.0, 47.6, 149.2, 93.7, 38.9, None, 6, 177.8, 4, 29, 165),
    ("6BX", 10000, "2-9/16"): (65.9, 280, 3, None, 5.16, 133.4, 152.4, 54.0, 173.0, 111.1, 42.9, None, 8, 215.9, 8, 29, 166),
    ("6BX", 10000, "3-1/16"): (78.6, 305, 3, None, 5.56, 149.2, 165.1, 57.2, 190.5, 125.4, 46.0, None, 8, 235, 8, 32, 167),
    ("6BX", 10000, "4-1/16"): (104.0, 315, 3, None, 8.33, 150.62, 185.0, 70.3, 182.6, 146.1, 73.1, None, 10, 258.80, 8, 32, 155),
    ("6BX", 10000, "5-1/8"): (131.0, 430, 3, None, 6.75, 215.9, 241.3, 76.2, 279.4, 184.2, 57.2, 4.8, 10, 336.6, 8, 42, 169),
    ("6BX", 10000, "7-1/16"): (180.2, 530, 3, None, 7.94, 279.4, 298.5, 98.4, 346.1, 241.3, 68.3, 4.8, 10, 419.1, 8, 48, 170),
    ("6BX", 10000, "9"): (229.4, 635, 3, None, 9.53, 346.1, 365.1, 117.5, 415.9, 298.5, 77.8, 4.8, 13, 508, 8, 57, 171),
    ("6BX", 10000, "11"): (280.2, 750, 3, None, 11.11, 415.9, 438.2, 130.2, 496.9, 365.1, 84.1, 6.4, 13, 609.6, 12, 54, 172),
    ("6BX", 10000, "13-5/8"): (347.7, 890, 3, None, 11.91, 496.9, 528.7, 149.2, 593.7, 438.2, 92.1, 9.5, 16, 730.30, 12, 60, 173),
    
    # 15000 psi
    ("6BX", 15000, "1-13/16"): (46.8, 225, 3, None, 4.76, 108.0, 127.0, 50.8, 154.0, 88.9, 39.7, None, 6, 165.1, 4, 29, 177),
    ("6BX", 15000, "2-1/16"): (53.2, 265, 3, None, 5.56, 127.0, 152.4, 57.2, 173.0, 104.8, 44.5, None, 8, 200, 8, 29, 178),
    ("6BX", 15000, "2-9/16"): (65.9, 295, 3, None, 5.56, 139.7, 165.1, 60.3, 190.5, 117.5, 47.6, None, 8, 222.3, 8, 32, 179),
    ("6BX", 15000, "3-1/16"): (78.6, 340, 3, None, 5.95, 158.8, 184.2, 66.7, 215.9, 134.9, 52.4, None, 8, 260.4, 8, 35, 180),
    ("6BX", 15000, "4-1/16"): (104.0, 405, 3, None, 6.35, 190.5, 231.8, 79.4, 279.4, 163.5, 60.3, None, 10, 311.2, 8, 42, 181),
    ("6BX", 15000, "7-1/16"): (180.2, 600, 3, None, 8.73, 304.8, 374.7, 120.7, 447.7, 263.5, 82.6, 6.4, 13, 476.3, 8, 54, 183),
    
    # 20000 psi
    ("6BX", 20000, "1-13/16"): (46.8, 255, 3, None, 5.56, 133.4, 154.0, 63.5, 173.0, 109.5, 49.2, None, 10, 203.20, 8, 29, 151),
    ("6BX", 20000, "2-1/16"): (53.2, 285, 3, None, 5.95, 154.0, 173.0, 71.5, 192.1, 127.0, 52.4, None, 10, 230.20, 8, 32, 152),
    ("6BX", 20000, "2-9/16"): (65.9, 325, 3, None, 6.75, 173.0, 190.5, 79.4, 215.9, 144.5, 58.7, None, 10, 261.90, 8, 35, 153),
    ("6BX", 20000, "3-1/16"): (78.6, 355, 3, None, 7.54, 192.1, 215.9, 85.8, 242.9, 160.3, 63.5, None, 10, 287.30, 8, 39, 154),
    ("6BX", 20000, "4-1/16"): (104.0, 445, 3, None, 8.33, 242.9, 279.4, 106.4, 304.8, 206.4, 73.0, None, 10, 357.20, 8, 48, 155),
    ("6BX", 20000, "7-1/16"): (180.2, 655, 6, 11.1, 11.11, 385.8, 447.7, 165.1, 481.0, 338.1, 96.8, 7.9, 16, 554, 16, 54, 156),
}

# BX Ring data for reference
# Format: RingNo: (OD, Height, Width_A, Flat_C, Flat_OD, Hole_D, R1_min, R1_max)
BX_RING_DATA = {
    155: (147.96, 14.22, 14.22, 12.22, 145.95, 1.6, 1.1, 1.7),
    # Add others as needed
}

# Constants
BEVEL_ANGLE = 37.5  # degrees - weld prep bevel
LAND_HEIGHT = 1.6   # mm (1/16") - weld prep land
RING_GROOVE_ANGLE = 23.0  # degrees - BX ring groove sidewall angle


def build_wn_flange_profile(B, OD, C, Q, G, K, T, J1, J2, J3, R, include_bevel=True):
    """
    Build 2D profile for Weld Neck BX flange.
    
    Coordinate system:
    - Z = 0 at flange FACE (ring sealing surface, sits on table)
    - Z = T at back of flange
    - Z goes positive toward back/weld end
    
    Ring groove geometry:
    - K = outer groove edge at face (diameter)
    - G = inner groove edge at face (diameter)
    - Groove width at face = (K-G)/2 per side
    - Walls at 23° angle inward going down
    - Depth = Q
    
    Profile traced counterclockwise starting from weld bevel tip (or square end if no bevel).
    """
    # Convert to radii
    bore_r = B / 2
    od_r = OD / 2
    k_r = K / 2          # Ring groove OUTER radius at face
    g_r = G / 2          # Ring groove INNER radius at face
    j1_r = J1 / 2        # Hub base radius (widest)
    
    # Calculate groove geometry
    groove_angle_rad = math.radians(RING_GROOVE_ANGLE)
    bevel_angle_rad = math.radians(BEVEL_ANGLE)
    
    # Groove flat radii (walls angle inward at 23° over depth Q)
    # horizontal travel = Q * tan(23°)
    groove_inward = Q * math.tan(groove_angle_rad)
    flat_outer_r = k_r - groove_inward   # Outer edge of flat
    flat_inner_r = g_r + groove_inward   # Inner edge of flat
    
    # Z coordinates
    z_face = 0              # Ring sealing face (on table)
    z_bolt_face = Q         # Bolt seating surface (Q above face = T-Q from back)
    z_back = T              # Back of flange body
    z_hub_end = T + J3      # End of hub
    
    # Weld prep geometry
    land_r = bore_r + 4.0   # Approximate land OD (API specific)
    z_land_bottom = z_hub_end + LAND_HEIGHT
    bevel_height = (land_r - bore_r) / math.tan(bevel_angle_rad)
    z_bevel_tip = z_land_bottom + bevel_height
    
    # =========================================================================
    # BUILD PROFILE - counterclockwise from hub end
    # =========================================================================
    points = []
    
    if include_bevel:
        # With weld bevel prep
        # 1. Weld bevel tip (bore radius)
        points.append(gp_Pnt(bore_r, 0, z_bevel_tip))
        
        # 2. Top of bevel / bottom of land
        points.append(gp_Pnt(land_r, 0, z_land_bottom))
        
        # 3. Top of land / start of hub
        points.append(gp_Pnt(land_r, 0, z_hub_end))
        
        # 4. Hub at flange back (widest point J1)
        points.append(gp_Pnt(j1_r, 0, z_back))
    else:
        # Square end - no weld bevel (for piping system models)
        # Hub extends straight to same Z as bevel tip would be
        # 1. Square end at bore (same Z as bevel tip for consistent length)
        points.append(gp_Pnt(bore_r, 0, z_bevel_tip))
        
        # 2. Square end at hub radius
        points.append(gp_Pnt(j1_r, 0, z_bevel_tip))
        
        # 3. Hub at flange back (widest point J1)
        points.append(gp_Pnt(j1_r, 0, z_back))
    
    # 5. Back of flange at OD (before chamfer)
    points.append(gp_Pnt(od_r - C, 0, z_back))
    
    # 6. Chamfer point
    points.append(gp_Pnt(od_r, 0, z_back - C))
    
    # 7. OD at bolt face level
    points.append(gp_Pnt(od_r, 0, z_bolt_face))
    
    # 8. Step down to ring face level at K
    points.append(gp_Pnt(k_r, 0, z_bolt_face))
    
    # 9. K at ring face (outer groove edge at face)
    points.append(gp_Pnt(k_r, 0, z_face))
    
    # 10. Down 23° outer groove wall to flat
    points.append(gp_Pnt(flat_outer_r, 0, z_bolt_face))  # At groove bottom = bolt face level
    
    # 11. Across groove flat to inner wall
    points.append(gp_Pnt(flat_inner_r, 0, z_bolt_face))
    
    # 12. Up 23° inner groove wall to G at face
    points.append(gp_Pnt(g_r, 0, z_face))
    
    # 13. Across face to bore (flat from G to bore at face level)
    points.append(gp_Pnt(bore_r, 0, z_face))
    
    # 14. Bore straight up to back of flange
    points.append(gp_Pnt(bore_r, 0, z_back))
    
    # Close back to bevel tip (bore continues through hub)
    # This edge goes from z_back to z_bevel_tip at bore_r
    
    # Build wire from points
    wire_builder = BRepBuilderAPI_MakeWire()
    
    for i in range(len(points) - 1):
        edge = BRepBuilderAPI_MakeEdge(points[i], points[i + 1]).Edge()
        wire_builder.Add(edge)
    
    # Close back to start
    edge = BRepBuilderAPI_MakeEdge(points[-1], points[0]).Edge()
    wire_builder.Add(edge)
    
    return wire_builder.Wire()


def add_bolt_holes(flange_body, BC, N, H, z_min, z_max):
    """Add bolt holes in circular pattern."""
    result = flange_body
    bolt_radius = H / 2
    bolt_circle_radius = BC / 2
    
    for i in range(N):
        angle = 2 * math.pi * i / N
        x = bolt_circle_radius * math.cos(angle)
        y = bolt_circle_radius * math.sin(angle)
        
        bolt_hole = BRepPrimAPI_MakeCylinder(
            gp_Ax2(gp_Pnt(x, y, z_min - 5), gp_Dir(0, 0, 1)),
            bolt_radius,
            (z_max - z_min) + 10
        ).Shape()
        
        result = BRepAlgoAPI_Cut(result, bolt_hole).Shape()
    
    return result


def generate_api_6bx_wn_flange(pressure: int, size: str, output_file: str = None, include_bevel: bool = True):
    """
    Generate an API 6BX Weld Neck flange.
    
    Args:
        pressure: Pressure rating (10000, 15000, or 20000 psi)
        size: Flange size (e.g., '2-1/16', '4-1/16', '7-1/16')
        output_file: Path to save STEP file (optional)
        include_bevel: Include weld bevel prep (default True)
    """
    key = ("6BX", pressure, size)
    
    if key not in API_6BX_DATA:
        available = [k for k in API_6BX_DATA.keys() if k[1] == pressure]
        raise ValueError(f"No data for 6BX {pressure} psi {size}. Available: {[k[2] for k in available]}")
    
    B, OD, C, E1, Q, G, K, T, J1, J2, J3, J4, R, BC, N, H, ring_no = API_6BX_DATA[key]
    
    bevel_note = "with weld bevel" if include_bevel else "square end"
    print(f"\nGenerating 6BX {pressure}psi {size} WN ({bevel_note})...")
    print(f"  B={B}, OD={OD}, T={T}, Q={Q}")
    print(f"  Ring groove: K={K}, G={G}")
    print(f"  Groove width at face: {K-G:.2f}mm (each side: {(K-G)/2:.2f}mm)")
    print(f"  Hub: J1={J1}, J3={J3}")
    print(f"  Bolts: BC={BC}, N={N}, H={H}")
    
    # Check groove geometry
    groove_angle_rad = math.radians(RING_GROOVE_ANGLE)
    groove_inward = Q * math.tan(groove_angle_rad)
    flat_outer_r = K/2 - groove_inward
    flat_inner_r = G/2 + groove_inward
    flat_width = flat_outer_r - flat_inner_r
    print(f"  Calculated groove flat width: {flat_width:.2f}mm")
    
    # Build profile and revolve
    profile_wire = build_wn_flange_profile(B, OD, C, Q, G, K, T, J1, J2, J3, R, include_bevel)
    
    face = BRepBuilderAPI_MakeFace(profile_wire).Face()
    axis = gp_Ax1(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1))
    flange_body = BRepPrimAPI_MakeRevol(face, axis, 2 * math.pi).Shape()
    
    # Add bolt holes (through the bolt face area)
    z_min = 0
    z_max = T + J3 + 20  # Through hub and beyond
    flange_complete = add_bolt_holes(flange_body, BC, N, H, z_min, z_max)
    
    # Export
    if output_file:
        writer = STEPControl_Writer()
        Interface_Static.SetCVal("write.step.schema", "AP214")
        writer.Transfer(flange_complete, STEPControl_AsIs)
        writer.Write(output_file)
        print(f"  Saved: {output_file}")
    
    return flange_complete


def list_available():
    """Print available configurations."""
    print("\n=== Available API 6BX Flanges ===")
    pressures = sorted(set(k[1] for k in API_6BX_DATA.keys()))
    for p in pressures:
        sizes = sorted([k[2] for k in API_6BX_DATA.keys() if k[1] == p],
                      key=lambda x: float(x.split("-")[0].replace("/", ".")))
        print(f"  {p} psi: {', '.join(sizes)}")


# =============================================================================
# MAIN
# =============================================================================
if __name__ == "__main__":
    list_available()
    
    print("\n" + "="*60)
    print("Generating: 6BX 10000psi 4-1/16\" WN")
    print("="*60)
    
    generate_api_6bx_wn_flange(10000, "4-1/16", "API-6BX-10000psi-4-1-16-WN-v4.step")
    
    print("\nDone!")
