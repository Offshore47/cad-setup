"""
API 6A/6BX Flange Generator - Wedding Cake Approach
Build up layers, then cut grooveUnits: MM (metric flange standards)"""

import math
from OCC.Core.gp import gp_Pnt, gp_Dir, gp_Ax1, gp_Ax2, gp_Vec
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCylinder, BRepPrimAPI_MakeCone
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut, BRepAlgoAPI_Fuse
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire, BRepBuilderAPI_MakeFace
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeRevol
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.Interface import Interface_Static

# Set STEP file units to millimeters
Interface_Static.SetCVal("write.step.unit", "MM")

# =============================================================================
# API 6BX 20000 PSI DATA (corrected)
# =============================================================================
# (B, OD, C, E1, Q, G, K, T, J1, J2, J3, J4, R, BC, N, H, RingNo)

API_6BX_20K = {
    "1-13/16": (46.8, 255, 3, None, 5.56, 77.77, 117, 63.5, 133.4, 109.5, 49.2, None, 10, 203.20, 8, 29, 151),
    "2-1/16": (53.2, 285, 3, None, 5.95, 86.23, 132, 71.5, 154.0, 127.0, 52.4, None, 10, 230.20, 8, 32, 152),
    "2-9/16": (65.9, 325, 3, None, 6.75, 102.77, 151, 79.4, 173.0, 144.5, 58.7, None, 10, 261.90, 8, 35, 153),
    "3-1/16": (78.6, 355, 3, None, 7.54, 119.00, 171, 85.8, 192.1, 160.3, 63.5, None, 10, 287.30, 8, 39, 154),
    "4-1/16": (104.0, 445, 3, None, 8.33, 150.62, 219, 106.4, 242.9, 206.4, 73.0, None, 10, 357.20, 8, 48, 155),
    "7-1/16": (180.2, 655, 6, 11.1, 11.11, 241.83, 352, 165.1, 385.8, 338.1, 96.8, 7.9, 16, 554, 16, 54, 156),
    "9": (229.4, 805, 6, 12.7, 12.7, 299.06, 441, 204.8, 481.0, 428.6, 107.9, 6.4, 25, 685.80, 16, 67, 157),
    "11": (280.2, 885, 6, 14.3, 14.29, 357.23, 505, 223.9, 566.7, 508.0, 103.2, 12.7, 25, 749.30, 16, 74, 158),
    "13-5/8": (346.9, 1160, 6, 15.9, 15.88, 432.64, 614, 292.1, 693.7, 628.6, 133.3, 14.2, 25, 1016, 20, 80, 159),
}

# BX Ring data: RingNo -> (OD, H, A, C_flat, ...)
BX_RINGS = {
    151: {"od": 74.22, "h": 8.74, "flat": 7.49},
    152: {"od": 82.68, "h": 9.53, "flat": 8.18},
    153: {"od": 99.22, "h": 10.72, "flat": 9.22},
    154: {"od": 115.06, "h": 11.91, "flat": 10.21},
    155: {"od": 147.96, "h": 14.22, "flat": 12.22},
    156: {"od": 238.18, "h": 17.48, "flat": 15.01},
    157: {"od": 295.40, "h": 19.84, "flat": 17.02},
    158: {"od": 353.57, "h": 22.23, "flat": 19.05},
    159: {"od": 429.01, "h": 24.61, "flat": 21.11},
}

# Constants
BEVEL_ANGLE = 37.5  # weld prep
LAND_HEIGHT = 1.6   # mm
RING_GROOVE_ANGLE = 23.0  # degrees


def make_cylinder(r, h, z_base=0):
    """Make a cylinder at origin, radius r, height h, base at z_base."""
    ax = gp_Ax2(gp_Pnt(0, 0, z_base), gp_Dir(0, 0, 1))
    return BRepPrimAPI_MakeCylinder(ax, r, h).Shape()


def make_ring(r_outer, r_inner, h, z_base=0):
    """Make a ring (washer) by subtracting inner cylinder from outer."""
    outer = make_cylinder(r_outer, h, z_base)
    inner = make_cylinder(r_inner, h, z_base - 1)  # extend for clean cut
    inner = make_cylinder(r_inner, h + 2, z_base - 1)
    return BRepAlgoAPI_Cut(outer, inner).Shape()


def make_groove_cutter(g_r, ring_flat_r, Q, z_face):
    """
    Make the BX ring groove cutter - a revolved 23° profile.
    
    At face: starts at G/2 radius
    Goes down at 23° inward for Q vertical distance
    Flat at bottom (ring flat width)
    Goes back up at 23° to inner raised face
    """
    angle_rad = math.radians(RING_GROOVE_ANGLE)
    
    # Horizontal travel for 23° over Q vertical
    h_travel = Q * math.tan(angle_rad)
    
    # Profile points (in XZ plane)
    # Start outside at G radius, face level
    p1 = gp_Pnt(g_r, 0, z_face)
    
    # Down and inward at 23° to groove bottom
    flat_outer_r = g_r - h_travel
    p2 = gp_Pnt(flat_outer_r, 0, z_face - Q)
    
    # Across flat to inner edge
    flat_inner_r = ring_flat_r + h_travel  # inner edge of flat plus travel back up
    # Actually, we need to determine where inner wall meets face
    # Inner wall goes up at 23° from flat_inner_r
    inner_face_r = ring_flat_r  # This is where we want the flat to end
    
    # Let's recalculate:
    # Flat width = ring flat dimension (e.g., 12.22mm for BX-155)
    # Flat is centered... or is it?
    # From your description: outer wall at G, inner wall goes to bore area
    
    # Simple approach: flat width = ring flat, centered on ring OD/2
    # But actually the flat should match the ring sealing surface
    
    # Let me use: flat_outer = g_r - h_travel, flat_inner = flat_outer - ring_flat_width
    flat_inner_r = flat_outer_r - (ring_flat_r * 2 - g_r + h_travel)
    
    # Simpler: just use ring flat directly
    # Groove flat outer radius = g_r - h_travel
    # Groove flat inner radius = groove flat outer - ring_flat
    ring_flat_width = (ring_flat_r * 2) / 2  # half the flat for radius
    
    # Actually let's be more direct:
    # Ring OD/2 gives us center of ring contact
    # Ring flat is the width of the sealing surface
    # Groove walls at 23° meet the flat
    
    # For BX-155: od=147.96, flat=12.22
    # Ring sits centered in groove
    ring_center_r = ring_flat_r  # This should be ring OD / 2
    half_flat = 12.22 / 2  # Using BX-155 for now - should be parameterized
    
    flat_outer_r = ring_center_r + half_flat / 2
    flat_inner_r = ring_center_r - half_flat / 2
    
    # Where walls meet face
    outer_face_r = flat_outer_r + h_travel  # This should equal G/2 if math is right
    inner_face_r = flat_inner_r - h_travel
    
    p1 = gp_Pnt(outer_face_r, 0, z_face + 0.1)  # Start just above face
    p2 = gp_Pnt(outer_face_r, 0, z_face)        # At face, outer edge
    p3 = gp_Pnt(flat_outer_r, 0, z_face - Q)    # Bottom of outer wall
    p4 = gp_Pnt(flat_inner_r, 0, z_face - Q)    # Bottom of inner wall  
    p5 = gp_Pnt(inner_face_r, 0, z_face)        # At face, inner edge
    p6 = gp_Pnt(inner_face_r, 0, z_face + 0.1)  # Just above face
    
    # Build wire
    from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire
    
    wire = BRepBuilderAPI_MakeWire()
    wire.Add(BRepBuilderAPI_MakeEdge(p1, p2).Edge())
    wire.Add(BRepBuilderAPI_MakeEdge(p2, p3).Edge())
    wire.Add(BRepBuilderAPI_MakeEdge(p3, p4).Edge())
    wire.Add(BRepBuilderAPI_MakeEdge(p4, p5).Edge())
    wire.Add(BRepBuilderAPI_MakeEdge(p5, p6).Edge())
    wire.Add(BRepBuilderAPI_MakeEdge(p6, p1).Edge())
    
    # Make face and revolve
    face = BRepBuilderAPI_MakeFace(wire.Wire()).Face()
    axis = gp_Ax1(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1))
    
    return BRepPrimAPI_MakeRevol(face, axis, 2 * math.pi).Shape()


def make_hub_and_bevel(bore_r, j1_r, j3, land_r, T, z_back):
    """
    Make the hub taper + 37.5° weld bevel + 1/16" land.
    Hub tapers from j1_r down to land_r at hub end, then bevel at 37.5° to bore, then 1/16" flat land.
    
    Args:
        bore_r: Bore radius (pipe ID)
        j1_r: Hub base radius at flange back (widest point)
        j3: Hub length (axial dimension T)
        land_r: Hub end radius (where bevel starts)
        T: Total hub length
        z_back: Z coordinate of flange back
    """
    bevel_rad = math.radians(BEVEL_ANGLE)
    
    # Wall thickness at hub end
    wall_thickness = land_r - bore_r
    
    # Bevel axial distance = (wall_thickness - LAND_HEIGHT) / tan(37.5°)
    bevel_axial_distance = (wall_thickness - LAND_HEIGHT) / math.tan(bevel_rad)
    
    # Z coordinates
    z_hub_start = z_back         # Hub starts at flange back
    z_hub_end = z_back - j3      # Hub end (where bevel starts)
    z_land_top = z_hub_end - bevel_axial_distance  # Where bevel ends
    z_land_bottom = z_land_top - LAND_HEIGHT       # Bottom of 1/16" land
    
    # Profile points: hub taper → bevel (37.5°) → land (1/16" flat)
    points = [
        gp_Pnt(bore_r, 0, z_hub_start),      # Bore at flange back
        gp_Pnt(j1_r, 0, z_hub_start),        # Hub base (widest)
        gp_Pnt(land_r, 0, z_hub_end),        # Hub end (bevel starts)
        gp_Pnt(bore_r, 0, z_land_top),       # Bevel ends at bore (37.5° taper)
        gp_Pnt(bore_r, 0, z_land_bottom),    # 1/16" flat land
    ]
    
    # Build wire
    wire = BRepBuilderAPI_MakeWire()
    for i in range(len(points) - 1):
        wire.Add(BRepBuilderAPI_MakeEdge(points[i], points[i+1]).Edge())
    wire.Add(BRepBuilderAPI_MakeEdge(points[-1], points[0]).Edge())
    
    face = BRepBuilderAPI_MakeFace(wire.Wire()).Face()
    axis = gp_Ax1(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1))
    
    return BRepPrimAPI_MakeRevol(face, axis, 2 * math.pi).Shape()


def add_bolt_holes(shape, BC, N, H, z_min, z_max):
    """Add bolt holes in circular pattern."""
    result = shape
    bolt_r = H / 2
    bc_r = BC / 2
    
    for i in range(N):
        angle = 2 * math.pi * i / N
        x = bc_r * math.cos(angle)
        y = bc_r * math.sin(angle)
        
        ax = gp_Ax2(gp_Pnt(x, y, z_min - 5), gp_Dir(0, 0, 1))
        hole = BRepPrimAPI_MakeCylinder(ax, bolt_r, z_max - z_min + 10).Shape()
        result = BRepAlgoAPI_Cut(result, hole).Shape()
    
    return result


def generate_6bx_wn_flange(size: str, output_file: str = None):
    """Generate a 6BX 20K Weld Neck flange."""
    
    if size not in API_6BX_20K:
        raise ValueError(f"Unknown size: {size}. Available: {list(API_6BX_20K.keys())}")
    
    B, OD, C, E1, Q, G, K, T, J1, J2, J3, J4, R, BC, N, H, ring_no = API_6BX_20K[size]
    ring = BX_RINGS.get(ring_no, {"od": 100, "h": 10, "flat": 8})
    
    print(f"\n=== Generating 6BX 20K {size} WN ===")
    print(f"  B={B}, OD={OD}, T={T}, Q={Q}")
    print(f"  G={G}, K={K}, (K-G)/2={(K-G)/2:.2f}mm")
    print(f"  Ring {ring_no}: OD={ring['od']}, flat={ring['flat']}")
    
    # Radii
    od_r = OD / 2
    bore_r = B / 2
    k_r = K / 2
    g_r = G / 2
    j1_r = J1 / 2
    ring_r = ring['od'] / 2
    land_r = bore_r + 4  # Approximate land OD
    
    # Z coordinates
    # Base disc goes from 0 to T-Q
    # Ring face sits on top from T-Q to T
    # Groove cuts into ring face, bottom at T-Q, top at T
    z_base_bottom = 0
    z_base_top = T - Q      # Top of base disc = bottom of ring groove
    z_face = T              # Top surface (ring sealing face)
    
    print(f"\n  Building layers...")
    print(f"  Z coords: base 0 to {z_base_top:.2f}, ring face {z_base_top:.2f} to {z_face:.2f}")
    
    # =========================================================================
    # LAYER 1: Base disc (bolt seating face)
    # OD diameter, T-Q thick, bore cut out
    # =========================================================================
    print(f"  Layer 1: Base disc OD={OD}, height={T-Q:.2f} (z=0 to z={z_base_top:.2f})")
    layer1 = make_cylinder(od_r, T - Q, z_base_bottom)
    # Cut bore through
    bore_cut = make_cylinder(bore_r, T - Q + 2, z_base_bottom - 1)
    layer1 = BRepAlgoAPI_Cut(layer1, bore_cut).Shape()
    
    # =========================================================================
    # CHAMFERS: 6mm at front and back edges of OD
    # =========================================================================
    chamfer = 6.0  # mm
    print(f"  Adding {chamfer}mm chamfers at OD edges...")
    
    # Front chamfer (at z=0, cuts inward and up)
    front_cham_pts = [
        gp_Pnt(od_r + 1, 0, z_base_bottom - 1),       # Outside below
        gp_Pnt(od_r + 1, 0, z_base_bottom + chamfer), # Outside above chamfer
        gp_Pnt(od_r, 0, z_base_bottom + chamfer),     # At OD, chamfer top
        gp_Pnt(od_r - chamfer, 0, z_base_bottom),     # Chamfer bottom (inward)
        gp_Pnt(od_r - chamfer, 0, z_base_bottom - 1), # Below
    ]
    wire_fc = BRepBuilderAPI_MakeWire()
    for i in range(len(front_cham_pts) - 1):
        wire_fc.Add(BRepBuilderAPI_MakeEdge(front_cham_pts[i], front_cham_pts[i+1]).Edge())
    wire_fc.Add(BRepBuilderAPI_MakeEdge(front_cham_pts[-1], front_cham_pts[0]).Edge())
    fc_face = BRepBuilderAPI_MakeFace(wire_fc.Wire()).Face()
    front_chamfer_cut = BRepPrimAPI_MakeRevol(fc_face, gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 2*math.pi).Shape()
    layer1 = BRepAlgoAPI_Cut(layer1, front_chamfer_cut).Shape()
    
    # Back chamfer (at z=T-Q, cuts inward and down)
    back_cham_pts = [
        gp_Pnt(od_r + 1, 0, z_base_top - chamfer),     # Outside below chamfer
        gp_Pnt(od_r + 1, 0, z_base_top + 1),           # Outside above
        gp_Pnt(od_r - chamfer, 0, z_base_top + 1),     # Above, inward
        gp_Pnt(od_r - chamfer, 0, z_base_top),         # At back, chamfer start
        gp_Pnt(od_r, 0, z_base_top - chamfer),         # Chamfer bottom at OD
    ]
    wire_bc = BRepBuilderAPI_MakeWire()
    for i in range(len(back_cham_pts) - 1):
        wire_bc.Add(BRepBuilderAPI_MakeEdge(back_cham_pts[i], back_cham_pts[i+1]).Edge())
    wire_bc.Add(BRepBuilderAPI_MakeEdge(back_cham_pts[-1], back_cham_pts[0]).Edge())
    bc_face = BRepBuilderAPI_MakeFace(wire_bc.Wire()).Face()
    back_chamfer_cut = BRepPrimAPI_MakeRevol(bc_face, gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 2*math.pi).Shape()
    layer1 = BRepAlgoAPI_Cut(layer1, back_chamfer_cut).Shape()

    # =========================================================================
    # LAYER 2: Ring face (K diameter, Q thick) - sits on top of base disc
    # =========================================================================
    print(f"  Layer 2: Ring face K={K}, height={Q} (z={z_base_top:.2f} to z={z_face:.2f})")
    layer2 = make_cylinder(k_r, Q, z_base_top)  # From T-Q to T
    bore_cut2 = make_cylinder(bore_r, Q + 2, z_base_top - 1)
    layer2 = BRepAlgoAPI_Cut(layer2, bore_cut2).Shape()
    
    # Fuse layers 1 and 2
    body = BRepAlgoAPI_Fuse(layer1, layer2).Shape()
    
    # =========================================================================
    # LAYER 3: Cut the ring groove into the ring face
    # Groove top at z=T (face), bottom at z=T-Q (base top)
    # 23° walls from G down to flat, flat = ring flat width
    # =========================================================================
    print(f"  Layer 3: Cutting ring groove...")
    
    # Calculate groove profile
    angle_rad = math.radians(RING_GROOVE_ANGLE)
    h_travel = Q * math.tan(angle_rad)  # Horizontal distance for 23° over Q
    
    # Groove geometry
    # Outer wall: starts at G/2 at face (z=T), goes inward to flat at z=T-Q
    flat_outer_r = g_r - h_travel
    flat_inner_r = flat_outer_r - ring['flat']
    inner_face_r = flat_inner_r - h_travel
    
    print(f"    Outer wall: face r={g_r:.2f} (z={z_face:.2f}) -> flat r={flat_outer_r:.2f} (z={z_base_top:.2f})")
    print(f"    Flat: r={flat_outer_r:.2f} to r={flat_inner_r:.2f} (width={ring['flat']}) at z={z_base_top:.2f}")
    print(f"    Inner wall: flat r={flat_inner_r:.2f} -> face r={inner_face_r:.2f} (z={z_face:.2f})")
    
    # Build groove cutter profile
    ext = 1.0  # Extension for clean boolean
    
    p1 = gp_Pnt(g_r + ext, 0, z_face + ext)         # Outside, above face
    p2 = gp_Pnt(g_r, 0, z_face)                      # Outer edge at face (z=T)
    p3 = gp_Pnt(flat_outer_r, 0, z_base_top)         # Outer edge of flat (z=T-Q)
    p4 = gp_Pnt(flat_inner_r, 0, z_base_top)         # Inner edge of flat (z=T-Q)
    p5 = gp_Pnt(inner_face_r, 0, z_face)             # Inner edge at face (z=T)
    p6 = gp_Pnt(inner_face_r - ext, 0, z_face + ext) # Inside, above face
    
    wire = BRepBuilderAPI_MakeWire()
    wire.Add(BRepBuilderAPI_MakeEdge(p1, p2).Edge())
    wire.Add(BRepBuilderAPI_MakeEdge(p2, p3).Edge())
    wire.Add(BRepBuilderAPI_MakeEdge(p3, p4).Edge())
    wire.Add(BRepBuilderAPI_MakeEdge(p4, p5).Edge())
    wire.Add(BRepBuilderAPI_MakeEdge(p5, p6).Edge())
    wire.Add(BRepBuilderAPI_MakeEdge(p6, p1).Edge())
    
    groove_face = BRepBuilderAPI_MakeFace(wire.Wire()).Face()
    axis = gp_Ax1(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1))
    groove_cutter = BRepPrimAPI_MakeRevol(groove_face, axis, 2 * math.pi).Shape()
    
    body = BRepAlgoAPI_Cut(body, groove_cutter).Shape()
    
    # =========================================================================
    # LAYER 4: Hub + Land + Bevel (back side) - extends from z=0 downward
    # =========================================================================
    print(f"  Layer 4: Hub J1={J1}, J3={J3}, land, bevel")
    hub = make_hub_and_bevel(bore_r, j1_r, J3, land_r, T, z_base_bottom)
    body = BRepAlgoAPI_Fuse(body, hub).Shape()
    
    # =========================================================================
    # BOLT HOLES
    # =========================================================================
    print(f"  Adding {N} bolt holes, H={H}, BC={BC}")
    body = add_bolt_holes(body, BC, N, H, -J3 - 20, z_face + 5)
    
    # =========================================================================
    # EXPORT
    # =========================================================================
    if output_file:
        writer = STEPControl_Writer()
        Interface_Static.SetCVal("write.step.schema", "AP214")
        writer.Transfer(body, STEPControl_AsIs)
        writer.Write(output_file)
        print(f"\n  Saved: {output_file}")
    
    return body


# =============================================================================
# MAIN
# =============================================================================
if __name__ == "__main__":
    print("\nAvailable 6BX 20K sizes:", list(API_6BX_20K.keys()))
    
    generate_6bx_wn_flange("4-1/16", "API-6BX-20K-4-1-16-WN-v5.step")
    
    print("\nDone!")
