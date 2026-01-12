"""
API 6A/6BX Flange Generator - All Pressure Classes Test Suite
Generates WN and Blind flanges for each pressure class
Tests both small sizes (no pocket/simple) and large sizes (with pocket)

Wedding Cake Approach: Build up layers, then cut features
"""

import math
import os
from OCC.Core.gp import gp_Pnt, gp_Dir, gp_Ax1, gp_Ax2
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCylinder, BRepPrimAPI_MakeRevol
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut, BRepAlgoAPI_Fuse
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire, BRepBuilderAPI_MakeFace
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.Interface import Interface_Static

# =============================================================================
# CONSTANTS
# =============================================================================
BEVEL_ANGLE = 37.5  # weld prep bevel angle
LAND_HEIGHT = 1.6   # mm
RING_GROOVE_ANGLE = 23.0  # degrees

# =============================================================================
# BX RING DATA: Ring Number -> dimensions from API 6A specification
# od = OD of Ring, h = Height, a = Width of Ring, flat = Width of Flat C, otd = OD of Flat
# =============================================================================
BX_RINGS = {
    150: {"od": 72.19, "h": 9.30, "a": 9.30, "flat": 7.98, "otd": 70.87},
    151: {"od": 76.40, "h": 9.63, "a": 9.63, "flat": 8.26, "otd": 75.03},
    152: {"od": 84.68, "h": 10.24, "a": 10.24, "flat": 8.79, "otd": 83.24},
    153: {"od": 100.94, "h": 11.38, "a": 11.38, "flat": 9.78, "otd": 99.31},
    154: {"od": 116.84, "h": 12.40, "a": 12.40, "flat": 10.64, "otd": 115.09},
    155: {"od": 147.96, "h": 14.22, "a": 14.22, "flat": 12.22, "otd": 145.95},
    156: {"od": 237.92, "h": 18.62, "a": 18.62, "flat": 15.98, "otd": 235.28},
    157: {"od": 294.46, "h": 20.98, "a": 20.98, "flat": 18.01, "otd": 291.49},
    158: {"od": 352.04, "h": 23.14, "a": 23.14, "flat": 19.86, "otd": 348.77},
    159: {"od": 426.72, "h": 25.70, "a": 25.70, "flat": 22.07, "otd": 423.09},
    160: {"od": 402.59, "h": 23.83, "a": 13.74, "flat": 10.36, "otd": 399.21},  # 5K 13-5/8"
    161: {"od": 491.41, "h": 28.07, "a": 16.21, "flat": 12.24, "otd": 487.45},  # 5K 16-5/8"
    162: {"od": 475.49, "h": 14.22, "a": 14.22, "flat": 12.22, "otd": 473.48},  # 5K/10K 16-3/4"
    163: {"od": 556.16, "h": 30.10, "a": 17.37, "flat": 13.11, "otd": 551.89},  # 5K 18-3/4"
    164: {"od": 570.56, "h": 30.10, "a": 24.59, "flat": 20.32, "otd": 566.29},  # 10K 18-3/4"
    165: {"od": 624.71, "h": 32.03, "a": 18.49, "flat": 13.97, "otd": 620.19},  # 5K 21-1/4"
    166: {"od": 640.03, "h": 32.03, "a": 26.14, "flat": 21.62, "otd": 635.51},  # 10K 21-1/4"
    167: {"od": 759.36, "h": 35.87, "a": 13.11, "flat": 8.03, "otd": 754.28},   # 2K 26-3/4"
    168: {"od": 765.25, "h": 35.87, "a": 16.05, "flat": 10.97, "otd": 760.17},  # 3K 26-3/4"
    169: {"od": 173.51, "h": 15.85, "a": 12.93, "flat": 10.69, "otd": 171.27},  # 10K 5-1/8"
    170: {"od": 218.03, "h": 14.22, "a": 14.22, "flat": 12.22, "otd": 216.03},  # 10K/15K 6-5/8"
    171: {"od": 267.44, "h": 14.22, "a": 14.22, "flat": 12.22, "otd": 265.43},  # 10K/15K 8-9/16"
    172: {"od": 333.07, "h": 14.22, "a": 14.22, "flat": 12.22, "otd": 331.06},  # 10K/15K 11-5/32"
    303: {"od": 852.75, "h": 37.95, "a": 16.97, "flat": 11.61, "otd": 847.37},  # 2K/3K 30"
}

# =============================================================================
# API 6BX FLANGE DATA BY PRESSURE CLASS
# Format: (B, OD, C, E1, Q, G, K, T, J1, J2, J3, J4, R, BC, N, H, RingNo)
# E1 = None means no front pocket, J4 = None means no back relief
# WN uses J2, J3; Blind uses J1, J4
# =============================================================================

# 20K PSI
API_6BX_20K = {
    # Small sizes (no pocket, E1=None)
    "1-13/16": (46.8, 255, 3, None, 5.56, 77.77, 117, 63.5, 133.4, 109.5, 49.2, None, 10, 203.20, 8, 29, 151),
    "2-1/16": (53.2, 285, 3, None, 5.95, 86.23, 132, 71.5, 154.0, 127.0, 52.4, None, 10, 230.20, 8, 32, 152),
    "2-9/16": (65.9, 325, 3, None, 6.75, 102.77, 151, 79.4, 173.0, 144.5, 58.7, None, 10, 261.90, 8, 35, 153),
    "3-1/16": (78.6, 355, 3, None, 7.54, 119.00, 171, 85.8, 192.1, 160.3, 63.5, None, 10, 287.30, 8, 39, 154),
    "4-1/16": (104.0, 445, 3, None, 8.33, 150.62, 219, 106.4, 242.9, 206.4, 73.0, None, 10, 357.20, 8, 48, 155),
    # Large sizes (with pocket, E1 has value)
    "7-1/16": (180.2, 655, 6, 11.1, 11.11, 241.83, 352, 165.1, 385.8, 338.1, 96.8, 7.9, 16, 554, 16, 54, 156),
    "9": (229.4, 805, 6, 12.7, 12.7, 299.06, 441, 204.8, 481.0, 428.6, 107.9, 6.4, 25, 685.80, 16, 67, 157),
    "11": (280.2, 885, 6, 14.3, 14.29, 357.23, 505, 223.9, 566.7, 508.0, 103.2, 12.7, 25, 749.30, 16, 74, 158),
    "13-5/8": (346.9, 1160, 6, 15.9, 15.88, 432.64, 614, 292.1, 693.7, 628.6, 133.3, 14.2, 25, 1016, 20, 80, 159),
}

# 15K PSI
API_6BX_15K = {
    "1-13/16": (46.8, 210, 3, None, 5.56, 77.77, 106, 45.3, 97.6, 82.6, 38.1, None, 10, 160.3, 8, 26, 151),
    "2-1/16": (53.2, 220, 3, None, 5.95, 86.23, 114, 50.8, 111.1, 95.3, 39.7, None, 10, 174.6, 8, 26, 152),
    "2-9/16": (65.9, 255, 3, None, 6.75, 102.77, 133, 57.2, 128.6, 109.5, 44.5, None, 10, 200, 8, 29, 153),
    "3-1/16": (78.6, 290, 3, None, 7.54, 119, 154, 64.3, 154.0, 130.2, 47.6, None, 10, 230.2, 8, 32, 154),
    "4-1/16": (104, 360, 3, None, 8.33, 150.62, 194, 78.6, 195.3, 162.7, 57.2, None, 10, 290.5, 8, 39, 155),
    "5-1/8": (131, 420, 3, 9.5, 9.53, 176.66, 225, 98.5, 244.5, 200.0, 66.7, 6.4, 16, 342.9, 12, 42, 169),
    "7-1/16": (180.2, 505, 6, 11.1, 11.11, 241.83, 305, 119.1, 325.4, 266.7, 73.0, 7.9, 16, 428.6, 16, 42, 156),
    "9": (229.4, 650, 6, 12.7, 12.7, 299.06, 381, 146.1, 431.8, 358.8, 88.9, 14.2, 16, 552.4, 16, 51, 157),
    "11": (280.2, 815, 6, 14.3, 14.29, 357.23, 454, 187.4, 584.2, 431.8, 101.6, 12.7, 16, 711.2, 20, 54, 158),
    "13-5/8": (346.9, 885, 6, 15.9, 15.88, 432.64, 541, 204.8, 595.3, 527.0, 114.3, 17.5, 25, 771.5, 20, 61, 159),
    "18-3/4": (477, 1160, 6, 18.3, 18.26, 577.9, 722, 255.6, 812.8, 685.8, 146.1, 35.1, 25, 1016, 20, 80, 164),
}

# 10K PSI
API_6BX_10K = {
    "1-13/16": (46.8, 185, 3, None, 5.56, 77.77, 105, 42.1, 88.9, 76.2, 34.9, None, 10, 146.1, 8, 23, 151),
    "2-1/16": (53.2, 200, 3, None, 5.95, 86.23, 111, 44.1, 100.0, 85.7, 34.1, None, 10, 158.8, 8, 23, 152),
    "2-9/16": (65.9, 230, 3, None, 6.75, 102.77, 132, 51.2, 120.7, 101.6, 38.1, None, 10, 184.2, 8, 26, 153),
    "3-1/16": (78.6, 270, 3, None, 7.54, 119, 152, 58.4, 142.1, 119.1, 42.9, None, 10, 215.9, 8, 29, 154),
    "4-1/16": (104, 315, 3, None, 8.33, 150.62, 185, 70.3, 182.6, 150.8, 50.8, None, 10, 258.8, 8, 32, 155),
    "5-1/8": (131, 360, 3, 9.5, 9.53, 176.66, 221, 79.4, 223.8, 181.0, 55.6, 6.4, 10, 300, 12, 32, 169),
    "7-1/16": (180.2, 480, 6, 11.1, 11.11, 241.83, 302, 103.2, 301.6, 254.0, 66.7, 9.7, 16, 403.2, 12, 42, 156),
    "9": (229.4, 550, 6, 12.7, 12.7, 299.06, 359, 123.9, 374.7, 312.7, 76.2, 9.7, 16, 476.3, 16, 42, 157),
    "11": (280.2, 655, 6, 14.3, 14.29, 357.23, 429, 141.3, 450.9, 374.7, 82.6, 14.2, 16, 565.2, 16, 48, 158),
    "13-5/8": (346.9, 770, 6, 15.9, 15.88, 432.64, 518, 168.3, 552.5, 463.6, 95.3, 17.5, 16, 673.1, 20, 51, 159),
    "16-3/4": (426.2, 870, 6, 8.3, 8.33, 478.33, 576, 168.3, 655.6, 519.1, 98.4, 30.2, 19, 776.3, 24, 51, 162),
    "18-3/4": (477, 1040, 6, 18.3, 18.26, 577.9, 697, 223.1, 752.5, 622.3, 127.0, 25.4, 16, 925.5, 24, 61, 164),
    "21-1/4": (540.5, 1145, 6, 19.1, 19.05, 647.88, 781, 241.3, 847.7, 698.5, 133.4, 31.8, 21, 1022.4, 24, 67, 166),
}

# 5K PSI
API_6BX_5K = {
    "13-5/8": (346.9, 675, 6, 14.3, 14.29, 408, 457, 112.8, 481.0, 412.8, 73.0, 23.9, 16, 590.6, 16, 45, 160),
    "16-3/4": (426.2, 770, 6, 8.3, 8.33, 478.33, 535, 130.2, 555.6, 485.8, 82.6, 17.5, 19, 676.3, 16, 51, 162),
    "18-3/4": (477, 905, 6, 18.3, 18.26, 563.5, 627, 165.9, 674.7, 568.3, 101.6, 19.1, 16, 803.3, 20, 54, 163),
    "21-1/4": (540.5, 990, 6, 19.1, 19.05, 632.56, 702, 181.0, 758.8, 638.2, 111.1, 22.4, 18, 885.8, 24, 54, 165),
}

# 3K PSI
API_6BX_3K = {
    "26-3/4": (680.2, 1100, 6, 21.4, 21.43, 774.22, 832, 161.2, 870.0, 749.3, 109.5, 0, 16, 1000.1, 24, 54, 168),
    "30": (762.8, 1185, 6, 23.0, 22.62, 862.3, 922, 167.1, 970.0, 835.0, 114.3, 12.7, 16, 1090.6, 32, 51, 303),
}

# 2K PSI
API_6BX_2K = {
    "26-3/4": (680.2, 1040, 6, 21.4, 21.43, 768.33, 805, 126.3, 835.8, 723.9, 93.7, 9.7, 16, 952.5, 20, 48, 167),
    "30": (762.8, 1120, 6, 23.0, 22.62, 862.3, 908, 134.2, 931.9, 811.2, 98.4, 17.5, 16, 1039.8, 32, 45, 303),
}

# Collect all data
ALL_PRESSURE_CLASSES = {
    "2K": API_6BX_2K,
    "3K": API_6BX_3K,
    "5K": API_6BX_5K,
    "10K": API_6BX_10K,
    "15K": API_6BX_15K,
    "20K": API_6BX_20K,
}


# =============================================================================
# GEOMETRY FUNCTIONS
# =============================================================================

def make_cylinder(r, h, z_base=0):
    """Make a cylinder at origin, radius r, height h, base at z_base."""
    ax = gp_Ax2(gp_Pnt(0, 0, z_base), gp_Dir(0, 0, 1))
    return BRepPrimAPI_MakeCylinder(ax, r, h).Shape()


def make_hub_and_bevel(bore_r, hub_base_r, hub_length, land_r, z_back):
    """
    Make the hub taper + land + weld bevel for WN flanges.
    Hub extends from z=0 (back of flange) downward into negative Z.
    """
    bevel_rad = math.radians(BEVEL_ANGLE)
    
    z_hub_start = z_back        # Start of hub at z=0
    z_hub_end = z_back - hub_length  # End of hub taper
    z_land_bottom = z_hub_end - LAND_HEIGHT
    
    # Bevel geometry
    bevel_height = (land_r - bore_r) / math.tan(bevel_rad)
    z_bevel_tip = z_land_bottom - bevel_height
    
    # Profile points (counterclockwise from bore at back)
    points = [
        gp_Pnt(bore_r, 0, z_hub_start),      # Bore at back of flange
        gp_Pnt(hub_base_r, 0, z_hub_start),  # Hub base (widest) 
        gp_Pnt(land_r, 0, z_hub_end),        # Hub tapers to land
        gp_Pnt(land_r, 0, z_land_bottom),    # Bottom of land
        gp_Pnt(bore_r, 0, z_bevel_tip),      # Bevel tip at bore
    ]
    
    wire = BRepBuilderAPI_MakeWire()
    for i in range(len(points) - 1):
        wire.Add(BRepBuilderAPI_MakeEdge(points[i], points[i+1]).Edge())
    wire.Add(BRepBuilderAPI_MakeEdge(points[-1], points[0]).Edge())
    
    face = BRepBuilderAPI_MakeFace(wire.Wire()).Face()
    axis = gp_Ax1(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1))
    
    return BRepPrimAPI_MakeRevol(face, axis, 2 * math.pi).Shape()


def make_tapered_back_protrusion(j1_r, height, z_bottom):
    """
    Create the back protrusion with 15° taper.
    J1 = diameter at TOP (where it meets main disc, closest to flange) - LARGEST
    Tapers OUTWARD at 15° going toward back face (away from flange)
    Back face diameter = J1 - 2 × J4 × tan(15°) - SMALLER
    
    Profile (cross-section):
    z=0 (back face, farthest from flange): smaller radius
    z=J4 (top, meets main disc):           J1 radius (largest)
    """
    angle_15 = math.radians(15.0)
    tan_15 = math.tan(angle_15)
    
    z_top = z_bottom + height
    back_face_r = j1_r - height * tan_15  # Smaller at back face
    
    # Profile: center -> smaller at back face -> J1 at top -> center
    pts = [
        gp_Pnt(0, 0, z_bottom),            # Center at back face
        gp_Pnt(back_face_r, 0, z_bottom),  # Smaller at back face (farthest)
        gp_Pnt(j1_r, 0, z_top),            # J1 at top (LARGEST, meets main disc)
        gp_Pnt(0, 0, z_top),               # Center at top
    ]
    
    wire = BRepBuilderAPI_MakeWire()
    for i in range(len(pts) - 1):
        wire.Add(BRepBuilderAPI_MakeEdge(pts[i], pts[i+1]).Edge())
    wire.Add(BRepBuilderAPI_MakeEdge(pts[-1], pts[0]).Edge())
    
    face = BRepBuilderAPI_MakeFace(wire.Wire()).Face()
    axis = gp_Ax1(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1))
    return BRepPrimAPI_MakeRevol(face, axis, 2 * math.pi).Shape()


def add_od_chamfers(shape, od_r, z_bottom, z_top, chamfer=6.0):
    """Add chamfers at OD edges (front and back)."""
    # Front chamfer (at z_bottom)
    front_cham_pts = [
        gp_Pnt(od_r + 1, 0, z_bottom - 1),
        gp_Pnt(od_r + 1, 0, z_bottom + chamfer),
        gp_Pnt(od_r, 0, z_bottom + chamfer),
        gp_Pnt(od_r - chamfer, 0, z_bottom),
        gp_Pnt(od_r - chamfer, 0, z_bottom - 1),
    ]
    wire_fc = BRepBuilderAPI_MakeWire()
    for i in range(len(front_cham_pts) - 1):
        wire_fc.Add(BRepBuilderAPI_MakeEdge(front_cham_pts[i], front_cham_pts[i+1]).Edge())
    wire_fc.Add(BRepBuilderAPI_MakeEdge(front_cham_pts[-1], front_cham_pts[0]).Edge())
    fc_face = BRepBuilderAPI_MakeFace(wire_fc.Wire()).Face()
    front_cut = BRepPrimAPI_MakeRevol(fc_face, gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 2*math.pi).Shape()
    shape = BRepAlgoAPI_Cut(shape, front_cut).Shape()
    
    # Back chamfer (at z_top)
    back_cham_pts = [
        gp_Pnt(od_r + 1, 0, z_top - chamfer),
        gp_Pnt(od_r + 1, 0, z_top + 1),
        gp_Pnt(od_r - chamfer, 0, z_top + 1),
        gp_Pnt(od_r - chamfer, 0, z_top),
        gp_Pnt(od_r, 0, z_top - chamfer),
    ]
    wire_bc = BRepBuilderAPI_MakeWire()
    for i in range(len(back_cham_pts) - 1):
        wire_bc.Add(BRepBuilderAPI_MakeEdge(back_cham_pts[i], back_cham_pts[i+1]).Edge())
    wire_bc.Add(BRepBuilderAPI_MakeEdge(back_cham_pts[-1], back_cham_pts[0]).Edge())
    bc_face = BRepBuilderAPI_MakeFace(wire_bc.Wire()).Face()
    back_cut = BRepPrimAPI_MakeRevol(bc_face, gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), 2*math.pi).Shape()
    shape = BRepAlgoAPI_Cut(shape, back_cut).Shape()
    
    return shape


def cut_ring_groove(shape, g_r, ring, Q, z_face, z_base_top, bore_r=None):
    """
    Cut the BX ring groove with 23° walls.
    
    Controlling dimensions (outside-in):
    - G = outer taper starts here at face
    - 23° taper down to flat at groove depth Q
    - Ring flat width determines flat at bottom (critical seating surface)
    - 23° taper back up from flat to face
    - Horizontal section from where taper meets face over to B (bore)
    
    B is just the bore - it doesn't control the groove geometry.
    The ring flat is the critical dimension - work outside to inside.
    """
    angle_rad = math.radians(RING_GROOVE_ANGLE)
    tan_23 = math.tan(angle_rad)
    
    # Outer taper: from G/2 at face, 23° inward, down to flat at depth Q
    flat_outer_r = g_r - Q * tan_23
    
    # Ring flat width determines flat at bottom (ALWAYS use ring flat)
    flat_inner_r = flat_outer_r - ring['flat']
    
    # Inner taper: from flat_inner back up 23° to face level
    inner_face_r = flat_inner_r - Q * tan_23
    
    ext = 1.0
    
    if bore_r is not None:
        # WN or large Blind: horizontal section from inner taper to bore
        # Profile: G → taper down → flat → taper up → horizontal → B
        p1 = gp_Pnt(g_r + ext, 0, z_face + ext)
        p2 = gp_Pnt(g_r, 0, z_face)                    # G at face (outer taper starts)
        p3 = gp_Pnt(flat_outer_r, 0, z_base_top)       # Outer flat edge at bottom
        p4 = gp_Pnt(flat_inner_r, 0, z_base_top)       # Inner flat edge at bottom
        p5 = gp_Pnt(inner_face_r, 0, z_face)           # Inner taper meets face
        p6 = gp_Pnt(bore_r, 0, z_face)                 # B at face (bore edge)
        p7 = gp_Pnt(bore_r - ext, 0, z_face + ext)
        
        wire = BRepBuilderAPI_MakeWire()
        wire.Add(BRepBuilderAPI_MakeEdge(p1, p2).Edge())
        wire.Add(BRepBuilderAPI_MakeEdge(p2, p3).Edge())
        wire.Add(BRepBuilderAPI_MakeEdge(p3, p4).Edge())
        wire.Add(BRepBuilderAPI_MakeEdge(p4, p5).Edge())
        wire.Add(BRepBuilderAPI_MakeEdge(p5, p6).Edge())
        wire.Add(BRepBuilderAPI_MakeEdge(p6, p7).Edge())
        wire.Add(BRepBuilderAPI_MakeEdge(p7, p1).Edge())
    else:
        # Small Blind: no bore, inner taper just ends where it meets face
        p1 = gp_Pnt(g_r + ext, 0, z_face + ext)
        p2 = gp_Pnt(g_r, 0, z_face)                    # G at face
        p3 = gp_Pnt(flat_outer_r, 0, z_base_top)       # Outer flat at bottom
        p4 = gp_Pnt(flat_inner_r, 0, z_base_top)       # Inner flat at bottom
        p5 = gp_Pnt(inner_face_r, 0, z_face)           # Inner taper meets face
        p6 = gp_Pnt(inner_face_r - ext, 0, z_face + ext)
        
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
    
    return BRepAlgoAPI_Cut(shape, groove_cutter).Shape()


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


def cut_front_pocket(shape, pocket_r, pocket_depth, z_face):
    """Cut front pocket (E1 depth, J1 diameter) for blind flanges."""
    pocket = make_cylinder(pocket_r, pocket_depth + 1, z_face - pocket_depth)
    return BRepAlgoAPI_Cut(shape, pocket).Shape()


def cut_back_relief(shape, relief_r, relief_depth, z_bottom):
    """Cut back relief (J4 depth, K diameter raised ring) for blind flanges."""
    # Relief is an annular cut - from relief_r outward
    # Actually it's a pocket from the back that leaves a raised ring at K dia
    relief = make_cylinder(relief_r, relief_depth + 1, z_bottom - 1)
    return BRepAlgoAPI_Cut(shape, relief).Shape()


def save_step(shape, filename):
    """Save shape to STEP file."""
    writer = STEPControl_Writer()
    Interface_Static.SetCVal("write.step.schema", "AP214")
    writer.Transfer(shape, STEPControl_AsIs)
    writer.Write(filename)
    print(f"    Saved: {filename}")


# =============================================================================
# WN FLANGE GENERATOR
# =============================================================================

def generate_wn_flange(pressure_class, size, data, output_dir):
    """Generate a WN flange."""
    B, OD, C, E1, Q, G, K, T, J1, J2, J3, J4, R, BC, N, H, ring_no = data
    ring = BX_RINGS.get(ring_no, {"od": 100, "h": 10, "flat": 8})
    
    size_clean = size.replace("/", "-")
    filename = os.path.join(output_dir, f"API-6BX-{pressure_class}-{size_clean}-WN.step")
    
    print(f"\n  Generating {pressure_class} {size} WN")
    print(f"    B={B}, OD={OD}, T={T}, Q={Q}, G={G}, K={K}")
    print(f"    Ring {ring_no}: flat={ring['flat']}")
    
    # Radii
    od_r = OD / 2
    bore_r = B / 2
    k_r = K / 2
    g_r = G / 2
    j2_r = J2 / 2 if J2 else bore_r + 10  # Hub outer at back
    land_r = bore_r + 4  # Land OD
    
    # Z coordinates
    z_base_bottom = 0
    z_base_top = T - Q  # Top of base disc = bottom of ring groove
    z_face = T          # Top surface (ring sealing face)
    
    # Layer 1: Base disc
    layer1 = make_cylinder(od_r, T - Q, z_base_bottom)
    bore_cut = make_cylinder(bore_r, T - Q + 2, z_base_bottom - 1)
    layer1 = BRepAlgoAPI_Cut(layer1, bore_cut).Shape()
    layer1 = add_od_chamfers(layer1, od_r, z_base_bottom, z_base_top)
    
    # Layer 2: Ring face (K diameter)
    layer2 = make_cylinder(k_r, Q, z_base_top)
    bore_cut2 = make_cylinder(bore_r, Q + 2, z_base_top - 1)
    layer2 = BRepAlgoAPI_Cut(layer2, bore_cut2).Shape()
    
    # Fuse layers
    body = BRepAlgoAPI_Fuse(layer1, layer2).Shape()
    
    # Cut ring groove - pass ring object for OTD-based flat position
    body = cut_ring_groove(body, g_r, ring, Q, z_face, z_base_top, bore_r=bore_r)
    
    # Add hub + bevel (uses J2 for hub base, J3 for length)
    if J3:
        hub = make_hub_and_bevel(bore_r, j2_r, J3, land_r, z_base_bottom)
        body = BRepAlgoAPI_Fuse(body, hub).Shape()
    
    # Add bolt holes
    z_min = -J3 if J3 else z_base_bottom
    body = add_bolt_holes(body, BC, N, H, z_min - 20, z_face + 5)
    
    save_step(body, filename)
    return body


# =============================================================================
# BLIND FLANGE GENERATOR
# =============================================================================

def generate_blind_flange(pressure_class, size, data, output_dir):
    """
    Generate a Blind flange.
    
    For sizes WITH E1/J4 (larger sizes):
        - Main disc: OD diameter, thickness = T - J4 - E1
        - Back protrusion: K diameter, height = J4 (protrudes from back, NOT a pocket)
        - Front ring face: K diameter, height = E1 (ring groove cut with 23° walls, flat at depth E1)
        
    For sizes WITHOUT E1/J4 (smaller sizes):
        - Main disc: OD diameter, thickness = T - Q
        - Ring face: K diameter, height = Q (standard ring groove)
        - No back protrusion
    """
    B, OD, C, E1, Q, G, K, T, J1, J2, J3, J4, R, BC, N, H, ring_no = data
    ring = BX_RINGS.get(ring_no, {"od": 100, "h": 10, "flat": 8})
    
    size_clean = size.replace("/", "-")
    filename = os.path.join(output_dir, f"API-6BX-{pressure_class}-{size_clean}-BLIND.step")
    
    has_e1 = E1 is not None and E1 > 0
    has_j4 = J4 is not None and J4 > 0
    
    print(f"\n  Generating {pressure_class} {size} BLIND")
    print(f"    B={B}, OD={OD}, T={T}, Q={Q}, G={G}, K={K}")
    print(f"    E1={E1}, J4={J4}")
    print(f"    Ring {ring_no}: flat={ring['flat']}")
    
    # Radii
    od_r = OD / 2
    k_r = K / 2
    g_r = G / 2
    
    if has_e1 and has_j4:
        # =====================================================================
        # LARGE SIZE BLIND: Main disc + back protrusion + front ring face
        # =====================================================================
        print(f"    Type: Large (with E1={E1}, J4={J4})")
        
        # Main disc thickness (between the two protrusions)
        main_disc_thickness = T - J4 - E1
        print(f"    Main disc: OD={OD}, thickness={main_disc_thickness:.1f}")
        print(f"    Back protrusion: J1={J1} tapered to K={K}, height={J4}, 15° taper")
        print(f"    Front ring face: K={K}, height={E1}")
        
        # Z coordinates:
        # z=0 is at the bottom of the back protrusion
        # Back protrusion: z=0 to z=J4
        # Main disc: z=J4 to z=J4+main_disc_thickness = z=T-E1
        # Front ring face: z=T-E1 to z=T
        z_back_protrusion_bottom = 0
        z_back_protrusion_top = J4  # Also bottom of main disc
        z_main_disc_top = T - E1    # Also bottom of front ring face
        z_face = T                   # Top surface
        
        # Layer 1: Back protrusion with 15° taper (J1 at base, tapers inward)
        j1_r = J1 / 2
        layer1 = make_tapered_back_protrusion(j1_r, J4, z_back_protrusion_bottom)
        print(f"    Layer 1: Back protrusion J1={J1} tapered 15° over {J4}mm, z=0 to z={J4}")
        
        # Layer 2: Main disc (OD diameter, from J4 to T-E1)
        layer2 = make_cylinder(od_r, main_disc_thickness, z_back_protrusion_top)
        layer2 = add_od_chamfers(layer2, od_r, z_back_protrusion_top, z_main_disc_top)
        print(f"    Layer 2: Main disc OD={OD}, z={J4} to z={T-E1:.1f}")
        
        # Layer 3: Front ring face (K diameter, E1 height)
        layer3 = make_cylinder(k_r, E1, z_main_disc_top)
        print(f"    Layer 3: Front ring face K={K}, z={T-E1:.1f} to z={T}")
        
        # Fuse all layers
        body = BRepAlgoAPI_Fuse(layer1, layer2).Shape()
        body = BRepAlgoAPI_Fuse(body, layer3).Shape()
        
        # Cut ring groove into front face
        # Controlling dimensions (outside-in): K, G, B
        # Outer taper starts at G, goes down 23° to flat
        # Inner taper goes from flat up 23° to B (pocket edge)
        
        bore_r = B / 2  # Inner wall at B (pocket edge)
        flat_top_width = (K - G) / 2  # Width of flat top between K and G
        
        # Calculate flat positions from G, B, and taper geometry
        angle_rad = math.radians(23.0)
        tan_23 = math.tan(angle_rad)
        
        # Outer taper: from G/2 at face, 23° inward, down to flat at depth E1
        flat_outer_r = g_r - E1 * tan_23
        
        # Inner taper: from B/2 at face, 23° outward, down to flat at depth E1
        flat_inner_r = bore_r + E1 * tan_23
        
        # Flat width is whatever geometry gives us
        flat_width = flat_outer_r - flat_inner_r
        
        print(f"    Cutting ring groove (Blind BX geometry):")
        print(f"      K/2={k_r}, G/2={g_r}, B/2={bore_r}")
        print(f"      Flat top width (K-G)/2 = {flat_top_width:.2f}")
        print(f"      Groove depth E1 = {E1}")
        print(f"      Flat at bottom: outer_r={flat_outer_r:.2f}, inner_r={flat_inner_r:.2f}, width={flat_width:.2f}")
        
        # Build groove cutter profile (in XZ plane, will revolve around Z)
        ext = 1.0
        
        # Groove bottom z = z_face - E1 (groove depth = E1)
        z_groove_bottom = z_face - E1
        
        # The groove profile for large Blind:
        # - G at face (outer taper starts)
        # - 23° taper down to flat_outer at bottom
        # - Flat at bottom from flat_outer to flat_inner
        # - 23° taper up to B at face (pocket edge)
        
        p1 = gp_Pnt(g_r + ext, 0, z_face + ext)       # Above face, outside G
        p2 = gp_Pnt(g_r, 0, z_face)                    # G at face (outer taper starts)
        p3 = gp_Pnt(flat_outer_r, 0, z_groove_bottom)  # Outer flat edge at bottom
        p4 = gp_Pnt(flat_inner_r, 0, z_groove_bottom)  # Inner flat edge at bottom
        p5 = gp_Pnt(bore_r, 0, z_face)                 # B at face (pocket edge)
        p6 = gp_Pnt(bore_r - ext, 0, z_face + ext)     # Above face, inside B
        
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
        
        # Cut center pocket (B diameter, E1 deep from face)
        print(f"    Cutting center pocket: B={B} (r={bore_r}), depth={E1}")
        center_pocket = make_cylinder(bore_r, E1 + 1, z_groove_bottom)
        body = BRepAlgoAPI_Cut(body, center_pocket).Shape()
        
        # Add bolt holes (through full thickness)
        body = add_bolt_holes(body, BC, N, H, z_back_protrusion_bottom - 5, z_face + 5)
        
    else:
        # =====================================================================
        # SMALL SIZE BLIND: Simple disc + ring face (like WN but solid)
        # B is still controlling dimension for inner groove wall
        # =====================================================================
        print(f"    Type: Small (no E1/J4, standard Q={Q})")
        
        bore_r = B / 2  # B is controlling dimension even for solid blind
        
        # Z coordinates
        z_base_bottom = 0
        z_base_top = T - Q  # Top of base disc = bottom of ring groove
        z_face = T          # Top surface
        
        # Layer 1: Base disc (OD diameter, solid)
        layer1 = make_cylinder(od_r, T - Q, z_base_bottom)
        layer1 = add_od_chamfers(layer1, od_r, z_base_bottom, z_base_top)
        
        # Layer 2: Ring face (K diameter)
        layer2 = make_cylinder(k_r, Q, z_base_top)
        
        # Fuse layers
        body = BRepAlgoAPI_Fuse(layer1, layer2).Shape()
        
        # Cut ring groove - B controls inner wall position
        body = cut_ring_groove(body, g_r, ring, Q, z_face, z_base_top, bore_r=bore_r)
        
        # Add bolt holes
        body = add_bolt_holes(body, BC, N, H, z_base_bottom - 10, z_face + 5)
    
    save_step(body, filename)
    return body


# =============================================================================
# TEST SUITE - Generate test flanges for each pressure class
# =============================================================================

def run_test_suite(output_dir="test_flanges"):
    """Generate test flanges for each pressure class."""
    os.makedirs(output_dir, exist_ok=True)
    
    print("=" * 60)
    print("API 6BX Flange Test Suite")
    print("=" * 60)
    
    # Test matrix - small and large sizes for each class
    test_sizes = {
        "20K": ["4-1/16", "7-1/16"],    # Small (no pocket), Large (with pocket)
        "15K": ["4-1/16", "7-1/16"],
        "10K": ["4-1/16", "7-1/16"],
        "5K": ["13-5/8", "16-3/4"],     # 5K only has larger sizes
        "3K": ["26-3/4", "30"],          # 3K only has 26-3/4" and 30"
        "2K": ["26-3/4", "30"],          # 2K only has 26-3/4" and 30"
    }
    
    generated = []
    
    for pressure_class, sizes in test_sizes.items():
        print(f"\n{'='*60}")
        print(f"PRESSURE CLASS: {pressure_class}")
        print("="*60)
        
        data_dict = ALL_PRESSURE_CLASSES[pressure_class]
        
        for size in sizes:
            if size in data_dict:
                data = data_dict[size]
                
                # Generate WN
                try:
                    generate_wn_flange(pressure_class, size, data, output_dir)
                    generated.append(f"{pressure_class} {size} WN")
                except Exception as e:
                    print(f"    ERROR generating WN: {e}")
                
                # Generate Blind
                try:
                    generate_blind_flange(pressure_class, size, data, output_dir)
                    generated.append(f"{pressure_class} {size} BLIND")
                except Exception as e:
                    print(f"    ERROR generating BLIND: {e}")
            else:
                print(f"\n  SKIP: {size} not in {pressure_class} data")
    
    print("\n" + "=" * 60)
    print(f"GENERATED {len(generated)} FLANGES:")
    for item in generated:
        print(f"  ✓ {item}")
    print("=" * 60)
    
    return generated


# =============================================================================
# GUI WRAPPER FUNCTION
# =============================================================================
def generate_flange(size, pressure_class, output_path):
    """
    Wrapper function for GUI to generate API 6BX WN flanges.
    
    Args:
        size: Flange size (e.g., "4-1/16", "2-1/16")
        pressure_class: Pressure class (e.g., "5K", "10K", "20K")
        output_path: Directory or full path where to save the file
        
    Returns:
        (success: bool, message: str)
    """
    try:
        # Convert size format: "2-1/16" -> "2-1/16", "4" -> "4"
        size_key = size  # Already in correct format from GUI
        
        # Get pressure class data
        data_dict = ALL_PRESSURE_CLASSES.get(pressure_class)
        if not data_dict:
            return False, f"Unknown pressure class: {pressure_class}. Available: {list(ALL_PRESSURE_CLASSES.keys())}"
        
        if size_key not in data_dict:
            return False, f"Size {size_key} not found in {pressure_class}. Available: {list(data_dict.keys())}"
        
        # Get flange data
        data = data_dict[size_key]
        
        # Determine output directory
        if os.path.isdir(output_path):
            output_dir = output_path
        else:
            output_dir = os.path.dirname(output_path)
        
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate WN flange
        generate_wn_flange(pressure_class, size_key, data, output_dir)
        
        return True, f"Successfully generated API 6BX {pressure_class} {size_key} WN flange"
        
    except Exception as e:
        return False, f"Error generating flange: {str(e)}"


# =============================================================================
# MAIN
# =============================================================================
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate API 6BX flanges")
    parser.add_argument("--class", dest="pressure_class", help="Pressure class (2K, 3K, 5K, 10K, 15K, 20K)")
    parser.add_argument("--size", help="Size (e.g., 26-3/4, 4-1/16)")
    parser.add_argument("--type", dest="flange_type", help="Flange type (WN, Blind)")
    args = parser.parse_args()
    
    output_dir = r"C:\ParadiseSuite\test_flanges"
    os.makedirs(output_dir, exist_ok=True)
    
    if args.pressure_class and args.size and args.flange_type:
        # Generate single flange
        size_key = args.size.replace("-", "/")  # Convert 26-3-4 back to 26/3/4 or 26-3/4
        # Handle various formats: "26-3-4" -> "26-3/4", "4-1-16" -> "4-1/16"
        if size_key.count("/") == 2:
            parts = size_key.split("/")
            size_key = f"{parts[0]}-{parts[1]}/{parts[2]}"
        
        data_dict = ALL_PRESSURE_CLASSES.get(args.pressure_class)
        if not data_dict:
            print(f"Unknown pressure class: {args.pressure_class}")
            exit(1)
        
        if size_key not in data_dict:
            print(f"Size {size_key} not found in {args.pressure_class}")
            print(f"Available sizes: {list(data_dict.keys())}")
            exit(1)
        
        data = data_dict[size_key]
        if args.flange_type.upper() == "WN":
            generate_wn_flange(args.pressure_class, size_key, data, output_dir)
        elif args.flange_type.upper() == "BLIND":
            generate_blind_flange(args.pressure_class, size_key, data, output_dir)
        else:
            print(f"Unknown flange type: {args.flange_type}")
    else:
        # Run full test suite
        run_test_suite(output_dir)
