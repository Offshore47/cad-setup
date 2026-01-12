"""
Gasket Dimensions Database
ASME B16.5 and API Standards

All dimensions in inches unless otherwise noted.

Gasket Types:
- Full Face: Covers entire flange face, used with flat face flanges or Class 150 RF
- Flat Ring: Seals on raised face only, smaller OD than full face
- Ring: Seals on raised face only, used with Classes 300+
- Spiral Wound: Metallic gasket with filler, ASME B16.20
- Ring Joint: For RTJ flanges, oval or octagonal profiles
"""

# ASME B16.5 Class 150 Flat Ring Gaskets
B165_CLASS150_FLAT_RING_GASKETS = {
    '1/2': {'nps': '1/2', 'class': 150, 'gasket_type': 'flat_ring', 'id_inches': 0.84, 'id_mm': 21, 'od_inches': 1.88, 'od_mm': 48},
    '3/4': {'nps': '3/4', 'class': 150, 'gasket_type': 'flat_ring', 'id_inches': 1.06, 'id_mm': 27, 'od_inches': 2.25, 'od_mm': 57},
    '1': {'nps': '1', 'class': 150, 'gasket_type': 'flat_ring', 'id_inches': 1.31, 'id_mm': 33, 'od_inches': 2.62, 'od_mm': 67},
    '1-1/4': {'nps': '1-1/4', 'class': 150, 'gasket_type': 'flat_ring', 'id_inches': 1.66, 'id_mm': 42, 'od_inches': 3.00, 'od_mm': 76},
    '1-1/2': {'nps': '1-1/2', 'class': 150, 'gasket_type': 'flat_ring', 'id_inches': 1.91, 'id_mm': 49, 'od_inches': 3.38, 'od_mm': 86},
    '2': {'nps': '2', 'class': 150, 'gasket_type': 'flat_ring', 'id_inches': 2.38, 'id_mm': 60, 'od_inches': 4.12, 'od_mm': 105},
    '2-1/2': {'nps': '2-1/2', 'class': 150, 'gasket_type': 'flat_ring', 'id_inches': 2.88, 'id_mm': 73, 'od_inches': 4.88, 'od_mm': 124},
    '3': {'nps': '3', 'class': 150, 'gasket_type': 'flat_ring', 'id_inches': 3.50, 'id_mm': 89, 'od_inches': 5.38, 'od_mm': 137},
    '3-1/2': {'nps': '3-1/2', 'class': 150, 'gasket_type': 'flat_ring', 'id_inches': 4.00, 'id_mm': 102, 'od_inches': 6.38, 'od_mm': 162},
    '4': {'nps': '4', 'class': 150, 'gasket_type': 'flat_ring', 'id_inches': 4.50, 'id_mm': 114, 'od_inches': 6.88, 'od_mm': 175},
    '5': {'nps': '5', 'class': 150, 'gasket_type': 'flat_ring', 'id_inches': 5.56, 'id_mm': 141, 'od_inches': 7.75, 'od_mm': 197},
    '6': {'nps': '6', 'class': 150, 'gasket_type': 'flat_ring', 'id_inches': 6.62, 'id_mm': 168, 'od_inches': 8.75, 'od_mm': 222},
    '8': {'nps': '8', 'class': 150, 'gasket_type': 'flat_ring', 'id_inches': 8.62, 'id_mm': 219, 'od_inches': 11.00, 'od_mm': 279},
    '10': {'nps': '10', 'class': 150, 'gasket_type': 'flat_ring', 'id_inches': 10.75, 'id_mm': 273, 'od_inches': 13.38, 'od_mm': 340},
    '12': {'nps': '12', 'class': 150, 'gasket_type': 'flat_ring', 'id_inches': 12.75, 'id_mm': 324, 'od_inches': 16.13, 'od_mm': 410},
    '14': {'nps': '14', 'class': 150, 'gasket_type': 'flat_ring', 'id_inches': 14.00, 'id_mm': 356, 'od_inches': 17.75, 'od_mm': 451},
    '16': {'nps': '16', 'class': 150, 'gasket_type': 'flat_ring', 'id_inches': 16.00, 'id_mm': 406, 'od_inches': 20.25, 'od_mm': 514},
    '18': {'nps': '18', 'class': 150, 'gasket_type': 'flat_ring', 'id_inches': 18.00, 'id_mm': 457, 'od_inches': 21.62, 'od_mm': 549},
    '20': {'nps': '20', 'class': 150, 'gasket_type': 'flat_ring', 'id_inches': 20.00, 'id_mm': 508, 'od_inches': 23.88, 'od_mm': 607},
    '24': {'nps': '24', 'class': 150, 'gasket_type': 'flat_ring', 'id_inches': 24.00, 'id_mm': 610, 'od_inches': 28.25, 'od_mm': 718},
}

# ASME B16.5 Class 300 Flat Ring Gaskets
B165_CLASS300_FLAT_RING_GASKETS = {
    '1/2': {'nps': '1/2', 'class': 300, 'gasket_type': 'flat_ring', 'id_inches': 0.84, 'id_mm': 21, 'od_inches': 2.12, 'od_mm': 54},
    '3/4': {'nps': '3/4', 'class': 300, 'gasket_type': 'flat_ring', 'id_inches': 1.06, 'id_mm': 27, 'od_inches': 2.62, 'od_mm': 67},
    '1': {'nps': '1', 'class': 300, 'gasket_type': 'flat_ring', 'id_inches': 1.31, 'id_mm': 33, 'od_inches': 2.88, 'od_mm': 73},
    '1-1/4': {'nps': '1-1/4', 'class': 300, 'gasket_type': 'flat_ring', 'id_inches': 1.66, 'id_mm': 42, 'od_inches': 3.25, 'od_mm': 83},
    '1-1/2': {'nps': '1-1/2', 'class': 300, 'gasket_type': 'flat_ring', 'id_inches': 1.91, 'id_mm': 49, 'od_inches': 3.75, 'od_mm': 95},
    '2': {'nps': '2', 'class': 300, 'gasket_type': 'flat_ring', 'id_inches': 2.38, 'id_mm': 60, 'od_inches': 4.38, 'od_mm': 111},
    '2-1/2': {'nps': '2-1/2', 'class': 300, 'gasket_type': 'flat_ring', 'id_inches': 2.88, 'id_mm': 73, 'od_inches': 5.12, 'od_mm': 130},
    '3': {'nps': '3', 'class': 300, 'gasket_type': 'flat_ring', 'id_inches': 3.50, 'id_mm': 89, 'od_inches': 5.88, 'od_mm': 149},
    '3-1/2': {'nps': '3-1/2', 'class': 300, 'gasket_type': 'flat_ring', 'id_inches': 4.00, 'id_mm': 102, 'od_inches': 6.50, 'od_mm': 165},
    '4': {'nps': '4', 'class': 300, 'gasket_type': 'flat_ring', 'id_inches': 4.50, 'id_mm': 114, 'od_inches': 7.12, 'od_mm': 181},
    '5': {'nps': '5', 'class': 300, 'gasket_type': 'flat_ring', 'id_inches': 5.56, 'id_mm': 141, 'od_inches': 8.50, 'od_mm': 216},
    '6': {'nps': '6', 'class': 300, 'gasket_type': 'flat_ring', 'id_inches': 6.62, 'id_mm': 168, 'od_inches': 9.88, 'od_mm': 251},
    '8': {'nps': '8', 'class': 300, 'gasket_type': 'flat_ring', 'id_inches': 8.62, 'id_mm': 219, 'od_inches': 12.12, 'od_mm': 308},
    '10': {'nps': '10', 'class': 300, 'gasket_type': 'flat_ring', 'id_inches': 10.75, 'id_mm': 273, 'od_inches': 14.25, 'od_mm': 362},
    '12': {'nps': '12', 'class': 300, 'gasket_type': 'flat_ring', 'id_inches': 12.75, 'id_mm': 324, 'od_inches': 16.62, 'od_mm': 422},
    '14': {'nps': '14', 'class': 300, 'gasket_type': 'flat_ring', 'id_inches': 14.00, 'id_mm': 356, 'od_inches': 19.12, 'od_mm': 486},
    '16': {'nps': '16', 'class': 300, 'gasket_type': 'flat_ring', 'id_inches': 16.00, 'id_mm': 406, 'od_inches': 21.25, 'od_mm': 540},
    '18': {'nps': '18', 'class': 300, 'gasket_type': 'flat_ring', 'id_inches': 18.00, 'id_mm': 457, 'od_inches': 23.50, 'od_mm': 597},
    '20': {'nps': '20', 'class': 300, 'gasket_type': 'flat_ring', 'id_inches': 20.00, 'id_mm': 508, 'od_inches': 25.75, 'od_mm': 654},
    '24': {'nps': '24', 'class': 300, 'gasket_type': 'flat_ring', 'id_inches': 24.00, 'id_mm': 610, 'od_inches': 30.50, 'od_mm': 775},
}

# ASME B16.5 Class 400 Flat Ring Gaskets
B165_CLASS400_FLAT_RING_GASKETS = {
    '1/2': {'nps': '1/2', 'class': 400, 'gasket_type': 'flat_ring', 'id_inches': 0.84, 'id_mm': 21, 'od_inches': 2.12, 'od_mm': 54},
    '3/4': {'nps': '3/4', 'class': 400, 'gasket_type': 'flat_ring', 'id_inches': 1.06, 'id_mm': 27, 'od_inches': 2.62, 'od_mm': 67},
    '1': {'nps': '1', 'class': 400, 'gasket_type': 'flat_ring', 'id_inches': 1.31, 'id_mm': 33, 'od_inches': 2.88, 'od_mm': 73},
    '1-1/4': {'nps': '1-1/4', 'class': 400, 'gasket_type': 'flat_ring', 'id_inches': 1.66, 'id_mm': 42, 'od_inches': 3.25, 'od_mm': 83},
    '1-1/2': {'nps': '1-1/2', 'class': 400, 'gasket_type': 'flat_ring', 'id_inches': 1.91, 'id_mm': 49, 'od_inches': 3.75, 'od_mm': 95},
    '2': {'nps': '2', 'class': 400, 'gasket_type': 'flat_ring', 'id_inches': 2.38, 'id_mm': 60, 'od_inches': 4.38, 'od_mm': 111},
    '2-1/2': {'nps': '2-1/2', 'class': 400, 'gasket_type': 'flat_ring', 'id_inches': 2.88, 'id_mm': 73, 'od_inches': 5.12, 'od_mm': 130},
    '3': {'nps': '3', 'class': 400, 'gasket_type': 'flat_ring', 'id_inches': 3.50, 'id_mm': 89, 'od_inches': 5.88, 'od_mm': 149},
    '3-1/2': {'nps': '3-1/2', 'class': 400, 'gasket_type': 'flat_ring', 'id_inches': 4.00, 'id_mm': 102, 'od_inches': 6.38, 'od_mm': 162},
    '4': {'nps': '4', 'class': 400, 'gasket_type': 'flat_ring', 'id_inches': 4.50, 'id_mm': 114, 'od_inches': 7.00, 'od_mm': 178},
    '5': {'nps': '5', 'class': 400, 'gasket_type': 'flat_ring', 'id_inches': 5.56, 'id_mm': 141, 'od_inches': 8.38, 'od_mm': 213},
    '6': {'nps': '6', 'class': 400, 'gasket_type': 'flat_ring', 'id_inches': 6.62, 'id_mm': 168, 'od_inches': 9.75, 'od_mm': 248},
    '8': {'nps': '8', 'class': 400, 'gasket_type': 'flat_ring', 'id_inches': 8.62, 'id_mm': 219, 'od_inches': 12.00, 'od_mm': 305},
    '10': {'nps': '10', 'class': 400, 'gasket_type': 'flat_ring', 'id_inches': 10.75, 'id_mm': 273, 'od_inches': 14.12, 'od_mm': 359},
    '12': {'nps': '12', 'class': 400, 'gasket_type': 'flat_ring', 'id_inches': 12.75, 'id_mm': 324, 'od_inches': 16.50, 'od_mm': 419},
    '14': {'nps': '14', 'class': 400, 'gasket_type': 'flat_ring', 'id_inches': 14.00, 'id_mm': 356, 'od_inches': 19.00, 'od_mm': 483},
    '16': {'nps': '16', 'class': 400, 'gasket_type': 'flat_ring', 'id_inches': 16.00, 'id_mm': 406, 'od_inches': 21.12, 'od_mm': 536},
    '18': {'nps': '18', 'class': 400, 'gasket_type': 'flat_ring', 'id_inches': 18.00, 'id_mm': 457, 'od_inches': 23.38, 'od_mm': 594},
    '20': {'nps': '20', 'class': 400, 'gasket_type': 'flat_ring', 'id_inches': 20.00, 'id_mm': 508, 'od_inches': 25.50, 'od_mm': 648},
    '24': {'nps': '24', 'class': 400, 'gasket_type': 'flat_ring', 'id_inches': 24.00, 'id_mm': 610, 'od_inches': 30.25, 'od_mm': 768},
}

# ASME B16.5 Class 600 Flat Ring Gaskets
B165_CLASS600_FLAT_RING_GASKETS = {
    '1/2': {'nps': '1/2', 'class': 600, 'gasket_type': 'flat_ring', 'id_inches': 0.84, 'id_mm': 21, 'od_inches': 2.12, 'od_mm': 54},
    '3/4': {'nps': '3/4', 'class': 600, 'gasket_type': 'flat_ring', 'id_inches': 1.06, 'id_mm': 27, 'od_inches': 2.62, 'od_mm': 67},
    '1': {'nps': '1', 'class': 600, 'gasket_type': 'flat_ring', 'id_inches': 1.31, 'id_mm': 33, 'od_inches': 2.88, 'od_mm': 73},
    '1-1/4': {'nps': '1-1/4', 'class': 600, 'gasket_type': 'flat_ring', 'id_inches': 1.66, 'id_mm': 42, 'od_inches': 3.25, 'od_mm': 83},
    '1-1/2': {'nps': '1-1/2', 'class': 600, 'gasket_type': 'flat_ring', 'id_inches': 1.91, 'id_mm': 49, 'od_inches': 3.75, 'od_mm': 95},
    '2': {'nps': '2', 'class': 600, 'gasket_type': 'flat_ring', 'id_inches': 2.38, 'id_mm': 60, 'od_inches': 4.38, 'od_mm': 111},
    '2-1/2': {'nps': '2-1/2', 'class': 600, 'gasket_type': 'flat_ring', 'id_inches': 2.88, 'id_mm': 73, 'od_inches': 5.12, 'od_mm': 130},
    '3': {'nps': '3', 'class': 600, 'gasket_type': 'flat_ring', 'id_inches': 3.50, 'id_mm': 89, 'od_inches': 5.88, 'od_mm': 149},
    '3-1/2': {'nps': '3-1/2', 'class': 600, 'gasket_type': 'flat_ring', 'id_inches': 4.00, 'id_mm': 102, 'od_inches': 6.38, 'od_mm': 162},
    '4': {'nps': '4', 'class': 600, 'gasket_type': 'flat_ring', 'id_inches': 4.50, 'id_mm': 114, 'od_inches': 7.62, 'od_mm': 194},
    '5': {'nps': '5', 'class': 600, 'gasket_type': 'flat_ring', 'id_inches': 5.56, 'id_mm': 141, 'od_inches': 9.50, 'od_mm': 241},
    '6': {'nps': '6', 'class': 600, 'gasket_type': 'flat_ring', 'id_inches': 6.62, 'id_mm': 168, 'od_inches': 10.50, 'od_mm': 267},
    '8': {'nps': '8', 'class': 600, 'gasket_type': 'flat_ring', 'id_inches': 8.62, 'id_mm': 219, 'od_inches': 12.62, 'od_mm': 321},
    '10': {'nps': '10', 'class': 600, 'gasket_type': 'flat_ring', 'id_inches': 10.75, 'id_mm': 273, 'od_inches': 15.75, 'od_mm': 400},
    '12': {'nps': '12', 'class': 600, 'gasket_type': 'flat_ring', 'id_inches': 12.75, 'id_mm': 324, 'od_inches': 18.00, 'od_mm': 457},
    '14': {'nps': '14', 'class': 600, 'gasket_type': 'flat_ring', 'id_inches': 14.00, 'id_mm': 356, 'od_inches': 19.38, 'od_mm': 492},
    '16': {'nps': '16', 'class': 600, 'gasket_type': 'flat_ring', 'id_inches': 16.00, 'id_mm': 406, 'od_inches': 22.25, 'od_mm': 565},
    '18': {'nps': '18', 'class': 600, 'gasket_type': 'flat_ring', 'id_inches': 18.00, 'id_mm': 457, 'od_inches': 24.12, 'od_mm': 613},
    '20': {'nps': '20', 'class': 600, 'gasket_type': 'flat_ring', 'id_inches': 20.00, 'id_mm': 508, 'od_inches': 26.88, 'od_mm': 683},
    '24': {'nps': '24', 'class': 600, 'gasket_type': 'flat_ring', 'id_inches': 24.00, 'id_mm': 610, 'od_inches': 31.12, 'od_mm': 791},
}

# ASME B16.5 Class 900 Flat Ring Gaskets (Note: NPS 3-1/2 not available)
B165_CLASS900_FLAT_RING_GASKETS = {
    '1/2': {'nps': '1/2', 'class': 900, 'gasket_type': 'flat_ring', 'id_inches': 0.84, 'id_mm': 21, 'od_inches': 2.50, 'od_mm': 64},
    '3/4': {'nps': '3/4', 'class': 900, 'gasket_type': 'flat_ring', 'id_inches': 1.06, 'id_mm': 27, 'od_inches': 2.75, 'od_mm': 70},
    '1': {'nps': '1', 'class': 900, 'gasket_type': 'flat_ring', 'id_inches': 1.31, 'id_mm': 33, 'od_inches': 3.12, 'od_mm': 79},
    '1-1/4': {'nps': '1-1/4', 'class': 900, 'gasket_type': 'flat_ring', 'id_inches': 1.66, 'id_mm': 42, 'od_inches': 3.50, 'od_mm': 89},
    '1-1/2': {'nps': '1-1/2', 'class': 900, 'gasket_type': 'flat_ring', 'id_inches': 1.91, 'id_mm': 49, 'od_inches': 3.88, 'od_mm': 99},
    '2': {'nps': '2', 'class': 900, 'gasket_type': 'flat_ring', 'id_inches': 2.38, 'id_mm': 60, 'od_inches': 5.62, 'od_mm': 143},
    '2-1/2': {'nps': '2-1/2', 'class': 900, 'gasket_type': 'flat_ring', 'id_inches': 2.88, 'id_mm': 73, 'od_inches': 6.50, 'od_mm': 165},
    '3': {'nps': '3', 'class': 900, 'gasket_type': 'flat_ring', 'id_inches': 3.50, 'id_mm': 89, 'od_inches': 6.62, 'od_mm': 168},
    '4': {'nps': '4', 'class': 900, 'gasket_type': 'flat_ring', 'id_inches': 4.50, 'id_mm': 114, 'od_inches': 8.12, 'od_mm': 206},
    '5': {'nps': '5', 'class': 900, 'gasket_type': 'flat_ring', 'id_inches': 5.56, 'id_mm': 141, 'od_inches': 9.75, 'od_mm': 248},
    '6': {'nps': '6', 'class': 900, 'gasket_type': 'flat_ring', 'id_inches': 6.62, 'id_mm': 168, 'od_inches': 11.38, 'od_mm': 289},
    '8': {'nps': '8', 'class': 900, 'gasket_type': 'flat_ring', 'id_inches': 8.62, 'id_mm': 219, 'od_inches': 14.12, 'od_mm': 359},
    '10': {'nps': '10', 'class': 900, 'gasket_type': 'flat_ring', 'id_inches': 10.75, 'id_mm': 273, 'od_inches': 17.12, 'od_mm': 435},
    '12': {'nps': '12', 'class': 900, 'gasket_type': 'flat_ring', 'id_inches': 12.75, 'id_mm': 324, 'od_inches': 19.62, 'od_mm': 498},
    '14': {'nps': '14', 'class': 900, 'gasket_type': 'flat_ring', 'id_inches': 14.00, 'id_mm': 356, 'od_inches': 20.50, 'od_mm': 521},
    '16': {'nps': '16', 'class': 900, 'gasket_type': 'flat_ring', 'id_inches': 16.00, 'id_mm': 406, 'od_inches': 22.62, 'od_mm': 575},
    '18': {'nps': '18', 'class': 900, 'gasket_type': 'flat_ring', 'id_inches': 18.00, 'id_mm': 457, 'od_inches': 25.12, 'od_mm': 638},
    '20': {'nps': '20', 'class': 900, 'gasket_type': 'flat_ring', 'id_inches': 20.00, 'id_mm': 508, 'od_inches': 27.50, 'od_mm': 699},
    '24': {'nps': '24', 'class': 900, 'gasket_type': 'flat_ring', 'id_inches': 24.00, 'id_mm': 610, 'od_inches': 33.00, 'od_mm': 838},
}

# ASME B16.5 Class 150 Spiral Wound Gaskets (with inner and outer rings)
B165_CLASS150_SPIRAL_WOUND_GASKETS = {
    '1/2': {'nps': '1/2', 'class': 150, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 14.2, 'sealing_element_id_mm': 19.1, 'sealing_element_od_mm': 31.8, 'outer_ring_od_mm': 47.8},
    '3/4': {'nps': '3/4', 'class': 150, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 20.6, 'sealing_element_id_mm': 25.4, 'sealing_element_od_mm': 39.6, 'outer_ring_od_mm': 57.2},
    '1': {'nps': '1', 'class': 150, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 26.9, 'sealing_element_id_mm': 31.8, 'sealing_element_od_mm': 47.8, 'outer_ring_od_mm': 66.8},
    '1-1/4': {'nps': '1-1/4', 'class': 150, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 38.1, 'sealing_element_id_mm': 47.8, 'sealing_element_od_mm': 60.5, 'outer_ring_od_mm': 76.2},
    '1-1/2': {'nps': '1-1/2', 'class': 150, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 44.5, 'sealing_element_id_mm': 54.1, 'sealing_element_od_mm': 69.9, 'outer_ring_od_mm': 85.9},
    '2': {'nps': '2', 'class': 150, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 55.6, 'sealing_element_id_mm': 69.9, 'sealing_element_od_mm': 85.9, 'outer_ring_od_mm': 104.9},
    '2-1/2': {'nps': '2-1/2', 'class': 150, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 66.5, 'sealing_element_id_mm': 82.6, 'sealing_element_od_mm': 98.6, 'outer_ring_od_mm': 124.0},
    '3': {'nps': '3', 'class': 150, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 81.0, 'sealing_element_id_mm': 101.6, 'sealing_element_od_mm': 120.7, 'outer_ring_od_mm': 136.7},
    '3-1/2': {'nps': '3-1/2', 'class': 150, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': None, 'sealing_element_id_mm': 114.3, 'sealing_element_od_mm': 133.4, 'outer_ring_od_mm': 161.9},
    '4': {'nps': '4', 'class': 150, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 106.4, 'sealing_element_id_mm': 127.0, 'sealing_element_od_mm': 149.4, 'outer_ring_od_mm': 174.8},
    '4-1/2': {'nps': '4-1/2', 'class': 150, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': None, 'sealing_element_id_mm': 139.7, 'sealing_element_od_mm': 165.1, 'outer_ring_od_mm': 177.8},
    '5': {'nps': '5', 'class': 150, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 131.8, 'sealing_element_id_mm': 155.7, 'sealing_element_od_mm': 177.8, 'outer_ring_od_mm': 196.9},
    '6': {'nps': '6', 'class': 150, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 157.2, 'sealing_element_id_mm': 182.6, 'sealing_element_od_mm': 209.6, 'outer_ring_od_mm': 222.3},
    '8': {'nps': '8', 'class': 150, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 215.9, 'sealing_element_id_mm': 233.4, 'sealing_element_od_mm': 263.7, 'outer_ring_od_mm': 279.4},
    '10': {'nps': '10', 'class': 150, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 268.2, 'sealing_element_id_mm': 287.3, 'sealing_element_od_mm': 317.5, 'outer_ring_od_mm': 339.9},
    '12': {'nps': '12', 'class': 150, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 317.5, 'sealing_element_id_mm': 339.9, 'sealing_element_od_mm': 374.7, 'outer_ring_od_mm': 409.7},
    '14': {'nps': '14', 'class': 150, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 349.3, 'sealing_element_id_mm': 371.6, 'sealing_element_od_mm': 406.4, 'outer_ring_od_mm': 450.9},
    '16': {'nps': '16', 'class': 150, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 400.1, 'sealing_element_id_mm': 422.4, 'sealing_element_od_mm': 463.6, 'outer_ring_od_mm': 514.4},
    '18': {'nps': '18', 'class': 150, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 449.3, 'sealing_element_id_mm': 474.7, 'sealing_element_od_mm': 527.1, 'outer_ring_od_mm': 549.4},
    '20': {'nps': '20', 'class': 150, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 500.1, 'sealing_element_id_mm': 525.5, 'sealing_element_od_mm': 577.9, 'outer_ring_od_mm': 606.6},
    '24': {'nps': '24', 'class': 150, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 603.3, 'sealing_element_id_mm': 628.7, 'sealing_element_od_mm': 685.8, 'outer_ring_od_mm': 717.6},
}

# ASME B16.5 Class 300 Spiral Wound Gaskets (with inner and outer rings)
B165_CLASS300_SPIRAL_WOUND_GASKETS = {
    '1/2': {'nps': '1/2', 'class': 300, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 14.2, 'sealing_element_id_mm': 19.1, 'sealing_element_od_mm': 31.8, 'outer_ring_od_mm': 54.1},
    '3/4': {'nps': '3/4', 'class': 300, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 20.6, 'sealing_element_id_mm': 25.4, 'sealing_element_od_mm': 39.6, 'outer_ring_od_mm': 66.8},
    '1': {'nps': '1', 'class': 300, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 26.9, 'sealing_element_id_mm': 31.8, 'sealing_element_od_mm': 47.8, 'outer_ring_od_mm': 73.2},
    '1-1/4': {'nps': '1-1/4', 'class': 300, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 38.1, 'sealing_element_id_mm': 47.8, 'sealing_element_od_mm': 60.5, 'outer_ring_od_mm': 82.6},
    '1-1/2': {'nps': '1-1/2', 'class': 300, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 44.5, 'sealing_element_id_mm': 54.1, 'sealing_element_od_mm': 69.9, 'outer_ring_od_mm': 95.3},
    '2': {'nps': '2', 'class': 300, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 55.6, 'sealing_element_id_mm': 69.9, 'sealing_element_od_mm': 85.9, 'outer_ring_od_mm': 111.3},
    '2-1/2': {'nps': '2-1/2', 'class': 300, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 66.5, 'sealing_element_id_mm': 82.6, 'sealing_element_od_mm': 98.6, 'outer_ring_od_mm': 130.3},
    '3': {'nps': '3', 'class': 300, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 81.0, 'sealing_element_id_mm': 101.6, 'sealing_element_od_mm': 120.7, 'outer_ring_od_mm': 149.4},
    '3-1/2': {'nps': '3-1/2', 'class': 300, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': None, 'sealing_element_id_mm': 114.3, 'sealing_element_od_mm': 133.4, 'outer_ring_od_mm': 165.1},
    '4': {'nps': '4', 'class': 300, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 106.4, 'sealing_element_id_mm': 127.0, 'sealing_element_od_mm': 149.4, 'outer_ring_od_mm': 181.1},
    '4-1/2': {'nps': '4-1/2', 'class': 300, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': None, 'sealing_element_id_mm': 139.7, 'sealing_element_od_mm': 165.1, 'outer_ring_od_mm': 196.9},
    '5': {'nps': '5', 'class': 300, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 131.8, 'sealing_element_id_mm': 155.7, 'sealing_element_od_mm': 177.8, 'outer_ring_od_mm': 215.9},
    '6': {'nps': '6', 'class': 300, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 157.2, 'sealing_element_id_mm': 182.6, 'sealing_element_od_mm': 209.6, 'outer_ring_od_mm': 251.0},
    '8': {'nps': '8', 'class': 300, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 215.9, 'sealing_element_id_mm': 233.4, 'sealing_element_od_mm': 263.7, 'outer_ring_od_mm': 308.1},
    '10': {'nps': '10', 'class': 300, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 268.2, 'sealing_element_id_mm': 287.3, 'sealing_element_od_mm': 317.5, 'outer_ring_od_mm': 362.0},
    '12': {'nps': '12', 'class': 300, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 317.5, 'sealing_element_id_mm': 339.9, 'sealing_element_od_mm': 374.7, 'outer_ring_od_mm': 422.4},
    '14': {'nps': '14', 'class': 300, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 349.3, 'sealing_element_id_mm': 371.6, 'sealing_element_od_mm': 406.4, 'outer_ring_od_mm': 485.9},
    '16': {'nps': '16', 'class': 300, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 400.1, 'sealing_element_id_mm': 422.4, 'sealing_element_od_mm': 463.6, 'outer_ring_od_mm': 539.8},
    '18': {'nps': '18', 'class': 300, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 449.3, 'sealing_element_id_mm': 474.7, 'sealing_element_od_mm': 527.1, 'outer_ring_od_mm': 596.9},
    '20': {'nps': '20', 'class': 300, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 500.1, 'sealing_element_id_mm': 525.5, 'sealing_element_od_mm': 577.9, 'outer_ring_od_mm': 654.1},
    '24': {'nps': '24', 'class': 300, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 603.3, 'sealing_element_id_mm': 628.7, 'sealing_element_od_mm': 685.8, 'outer_ring_od_mm': 774.7},
}

# ASME B16.5 Class 400 Spiral Wound Gaskets (with inner and outer rings)
B165_CLASS400_SPIRAL_WOUND_GASKETS = {
    '1/2': {'nps': '1/2', 'class': 400, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 14.2, 'sealing_element_id_mm': 19.1, 'sealing_element_od_mm': 31.8, 'outer_ring_od_mm': 54.1},
    '3/4': {'nps': '3/4', 'class': 400, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 20.6, 'sealing_element_id_mm': 25.4, 'sealing_element_od_mm': 39.6, 'outer_ring_od_mm': 66.8},
    '1': {'nps': '1', 'class': 400, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 26.9, 'sealing_element_id_mm': 31.8, 'sealing_element_od_mm': 47.8, 'outer_ring_od_mm': 73.2},
    '1-1/4': {'nps': '1-1/4', 'class': 400, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 38.1, 'sealing_element_id_mm': 47.8, 'sealing_element_od_mm': 60.5, 'outer_ring_od_mm': 82.6},
    '1-1/2': {'nps': '1-1/2', 'class': 400, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 44.5, 'sealing_element_id_mm': 54.1, 'sealing_element_od_mm': 69.9, 'outer_ring_od_mm': 95.3},
    '2': {'nps': '2', 'class': 400, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 55.6, 'sealing_element_id_mm': 69.9, 'sealing_element_od_mm': 85.9, 'outer_ring_od_mm': 111.3},
    '2-1/2': {'nps': '2-1/2', 'class': 400, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 66.5, 'sealing_element_id_mm': 82.6, 'sealing_element_od_mm': 98.6, 'outer_ring_od_mm': 130.3},
    '3': {'nps': '3', 'class': 400, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 81.0, 'sealing_element_id_mm': 101.6, 'sealing_element_od_mm': 120.7, 'outer_ring_od_mm': 149.4},
    '3-1/2': {'nps': '3-1/2', 'class': 400, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': None, 'sealing_element_id_mm': 104.8, 'sealing_element_od_mm': 133.4, 'outer_ring_od_mm': 161.9},
    '4': {'nps': '4', 'class': 400, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 102.6, 'sealing_element_id_mm': 120.7, 'sealing_element_od_mm': 149.4, 'outer_ring_od_mm': 177.8},
    '4-1/2': {'nps': '4-1/2', 'class': 400, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': None, 'sealing_element_id_mm': 134.9, 'sealing_element_od_mm': 165.1, 'outer_ring_od_mm': 193.7},
    '5': {'nps': '5', 'class': 400, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 128.3, 'sealing_element_id_mm': 147.6, 'sealing_element_od_mm': 177.8, 'outer_ring_od_mm': 212.9},
    '6': {'nps': '6', 'class': 400, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 154.9, 'sealing_element_id_mm': 174.8, 'sealing_element_od_mm': 209.6, 'outer_ring_od_mm': 247.7},
    '8': {'nps': '8', 'class': 400, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 205.7, 'sealing_element_id_mm': 225.6, 'sealing_element_od_mm': 263.7, 'outer_ring_od_mm': 304.8},
    '10': {'nps': '10', 'class': 400, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 255.3, 'sealing_element_id_mm': 274.6, 'sealing_element_od_mm': 317.5, 'outer_ring_od_mm': 358.9},
    '12': {'nps': '12', 'class': 400, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 307.3, 'sealing_element_id_mm': 327.2, 'sealing_element_od_mm': 374.7, 'outer_ring_od_mm': 419.1},
    '14': {'nps': '14', 'class': 400, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 342.9, 'sealing_element_id_mm': 362.0, 'sealing_element_od_mm': 406.4, 'outer_ring_od_mm': 482.6},
    '16': {'nps': '16', 'class': 400, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 389.9, 'sealing_element_id_mm': 412.8, 'sealing_element_od_mm': 463.6, 'outer_ring_od_mm': 536.7},
    '18': {'nps': '18', 'class': 400, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 438.2, 'sealing_element_id_mm': 469.9, 'sealing_element_od_mm': 527.1, 'outer_ring_od_mm': 593.9},
    '20': {'nps': '20', 'class': 400, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 489.0, 'sealing_element_id_mm': 520.7, 'sealing_element_od_mm': 577.9, 'outer_ring_od_mm': 647.7},
    '24': {'nps': '24', 'class': 400, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 590.6, 'sealing_element_id_mm': 628.7, 'sealing_element_od_mm': 685.8, 'outer_ring_od_mm': 768.4},
}

# ASME B16.5 Class 600 Spiral Wound Gaskets (with inner and outer rings)
B165_CLASS600_SPIRAL_WOUND_GASKETS = {
    '1/2': {'nps': '1/2', 'class': 600, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 14.2, 'sealing_element_id_mm': 19.1, 'sealing_element_od_mm': 31.8, 'outer_ring_od_mm': 54.1},
    '3/4': {'nps': '3/4', 'class': 600, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 20.6, 'sealing_element_id_mm': 25.4, 'sealing_element_od_mm': 39.6, 'outer_ring_od_mm': 66.8},
    '1': {'nps': '1', 'class': 600, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 26.9, 'sealing_element_id_mm': 31.8, 'sealing_element_od_mm': 47.8, 'outer_ring_od_mm': 73.2},
    '1-1/4': {'nps': '1-1/4', 'class': 600, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 38.1, 'sealing_element_id_mm': 47.8, 'sealing_element_od_mm': 60.5, 'outer_ring_od_mm': 82.6},
    '1-1/2': {'nps': '1-1/2', 'class': 600, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 44.5, 'sealing_element_id_mm': 54.1, 'sealing_element_od_mm': 69.9, 'outer_ring_od_mm': 95.3},
    '2': {'nps': '2', 'class': 600, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 55.6, 'sealing_element_id_mm': 69.9, 'sealing_element_od_mm': 85.9, 'outer_ring_od_mm': 111.3},
    '2-1/2': {'nps': '2-1/2', 'class': 600, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 66.5, 'sealing_element_id_mm': 82.6, 'sealing_element_od_mm': 98.6, 'outer_ring_od_mm': 130.3},
    '3': {'nps': '3', 'class': 600, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 78.7, 'sealing_element_id_mm': 101.6, 'sealing_element_od_mm': 120.7, 'outer_ring_od_mm': 149.4},
    '3-1/2': {'nps': '3-1/2', 'class': 600, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': None, 'sealing_element_id_mm': 104.8, 'sealing_element_od_mm': 133.4, 'outer_ring_od_mm': 161.9},
    '4': {'nps': '4', 'class': 600, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 102.6, 'sealing_element_id_mm': 120.7, 'sealing_element_od_mm': 149.4, 'outer_ring_od_mm': 193.8},
    '4-1/2': {'nps': '4-1/2', 'class': 600, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': None, 'sealing_element_id_mm': 134.9, 'sealing_element_od_mm': 165.1, 'outer_ring_od_mm': 209.6},
    '5': {'nps': '5', 'class': 600, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 128.3, 'sealing_element_id_mm': 147.6, 'sealing_element_od_mm': 177.8, 'outer_ring_od_mm': 241.3},
    '6': {'nps': '6', 'class': 600, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 154.9, 'sealing_element_id_mm': 174.8, 'sealing_element_od_mm': 209.6, 'outer_ring_od_mm': 266.7},
    '8': {'nps': '8', 'class': 600, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 205.7, 'sealing_element_id_mm': 225.6, 'sealing_element_od_mm': 263.7, 'outer_ring_od_mm': 320.8},
    '10': {'nps': '10', 'class': 600, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 255.3, 'sealing_element_id_mm': 274.6, 'sealing_element_od_mm': 317.5, 'outer_ring_od_mm': 400.1},
    '12': {'nps': '12', 'class': 600, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 307.3, 'sealing_element_id_mm': 327.2, 'sealing_element_od_mm': 374.7, 'outer_ring_od_mm': 457.2},
    '14': {'nps': '14', 'class': 600, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 342.9, 'sealing_element_id_mm': 362.0, 'sealing_element_od_mm': 406.4, 'outer_ring_od_mm': 492.3},
    '16': {'nps': '16', 'class': 600, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 389.9, 'sealing_element_id_mm': 412.8, 'sealing_element_od_mm': 463.6, 'outer_ring_od_mm': 565.2},
    '18': {'nps': '18', 'class': 600, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 438.2, 'sealing_element_id_mm': 469.9, 'sealing_element_od_mm': 527.1, 'outer_ring_od_mm': 612.9},
    '20': {'nps': '20', 'class': 600, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 489.0, 'sealing_element_id_mm': 520.7, 'sealing_element_od_mm': 577.9, 'outer_ring_od_mm': 682.8},
    '24': {'nps': '24', 'class': 600, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 590.6, 'sealing_element_id_mm': 628.7, 'sealing_element_od_mm': 685.8, 'outer_ring_od_mm': 790.7},
}

# ASME B16.5 Class 900 Spiral Wound Gaskets (with inner and outer rings)
B165_CLASS900_SPIRAL_WOUND_GASKETS = {
    '1/2': {'nps': '1/2', 'class': 900, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 14.2, 'sealing_element_id_mm': 19.1, 'sealing_element_od_mm': 31.8, 'outer_ring_od_mm': 63.5},
    '3/4': {'nps': '3/4', 'class': 900, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 20.6, 'sealing_element_id_mm': 25.4, 'sealing_element_od_mm': 39.6, 'outer_ring_od_mm': 69.9},
    '1': {'nps': '1', 'class': 900, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 26.9, 'sealing_element_id_mm': 31.8, 'sealing_element_od_mm': 47.8, 'outer_ring_od_mm': 79.5},
    '1-1/4': {'nps': '1-1/4', 'class': 900, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 33.4, 'sealing_element_id_mm': 39.6, 'sealing_element_od_mm': 60.5, 'outer_ring_od_mm': 88.9},
    '1-1/2': {'nps': '1-1/2', 'class': 900, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 41.4, 'sealing_element_id_mm': 47.8, 'sealing_element_od_mm': 69.9, 'outer_ring_od_mm': 98.6},
    '2': {'nps': '2', 'class': 900, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 52.3, 'sealing_element_id_mm': 58.7, 'sealing_element_od_mm': 85.9, 'outer_ring_od_mm': 143.0},
    '2-1/2': {'nps': '2-1/2', 'class': 900, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 63.5, 'sealing_element_id_mm': 69.9, 'sealing_element_od_mm': 98.6, 'outer_ring_od_mm': 165.1},
    '3': {'nps': '3', 'class': 900, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 78.7, 'sealing_element_id_mm': 95.3, 'sealing_element_od_mm': 120.7, 'outer_ring_od_mm': 168.4},
    '3-1/2': {'nps': '3-1/2', 'class': 900, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': None, 'sealing_element_id_mm': 104.8, 'sealing_element_od_mm': 133.4, 'outer_ring_od_mm': 190.5},
    '4': {'nps': '4', 'class': 900, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 102.6, 'sealing_element_id_mm': 120.7, 'sealing_element_od_mm': 149.4, 'outer_ring_od_mm': 206.5},
    '4-1/2': {'nps': '4-1/2', 'class': 900, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': None, 'sealing_element_id_mm': 134.9, 'sealing_element_od_mm': 165.1, 'outer_ring_od_mm': 238.1},
    '5': {'nps': '5', 'class': 900, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 128.3, 'sealing_element_id_mm': 147.6, 'sealing_element_od_mm': 177.8, 'outer_ring_od_mm': 247.7},
    '6': {'nps': '6', 'class': 900, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 154.9, 'sealing_element_id_mm': 174.8, 'sealing_element_od_mm': 209.6, 'outer_ring_od_mm': 289.1},
    '8': {'nps': '8', 'class': 900, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 196.9, 'sealing_element_id_mm': 222.3, 'sealing_element_od_mm': 257.3, 'outer_ring_od_mm': 358.9},
    '10': {'nps': '10', 'class': 900, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 246.1, 'sealing_element_id_mm': 276.4, 'sealing_element_od_mm': 311.2, 'outer_ring_od_mm': 435.1},
    '12': {'nps': '12', 'class': 900, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 292.1, 'sealing_element_id_mm': 323.9, 'sealing_element_od_mm': 368.3, 'outer_ring_od_mm': 498.6},
    '14': {'nps': '14', 'class': 900, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 320.8, 'sealing_element_id_mm': 355.6, 'sealing_element_od_mm': 400.1, 'outer_ring_od_mm': 520.7},
    '16': {'nps': '16', 'class': 900, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 374.7, 'sealing_element_id_mm': 412.8, 'sealing_element_od_mm': 457.2, 'outer_ring_od_mm': 574.8},
    '18': {'nps': '18', 'class': 900, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 425.5, 'sealing_element_id_mm': 463.6, 'sealing_element_od_mm': 520.7, 'outer_ring_od_mm': 638.3},
    '20': {'nps': '20', 'class': 900, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 482.6, 'sealing_element_id_mm': 520.7, 'sealing_element_od_mm': 571.5, 'outer_ring_od_mm': 698.5},
    '24': {'nps': '24', 'class': 900, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 590.6, 'sealing_element_id_mm': 628.7, 'sealing_element_od_mm': 679.5, 'outer_ring_od_mm': 838.2},
}

# ASME B16.5 Class 1500 Spiral Wound Gaskets (with inner and outer rings)
B165_CLASS1500_SPIRAL_WOUND_GASKETS = {
    '1/2': {'nps': '1/2', 'class': 1500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 14.2, 'sealing_element_id_mm': 19.1, 'sealing_element_od_mm': 31.8, 'outer_ring_od_mm': 63.5},
    '3/4': {'nps': '3/4', 'class': 1500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 20.6, 'sealing_element_id_mm': 25.4, 'sealing_element_od_mm': 39.6, 'outer_ring_od_mm': 69.9},
    '1': {'nps': '1', 'class': 1500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 26.9, 'sealing_element_id_mm': 31.8, 'sealing_element_od_mm': 47.8, 'outer_ring_od_mm': 79.5},
    '1-1/4': {'nps': '1-1/4', 'class': 1500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 33.3, 'sealing_element_id_mm': 39.6, 'sealing_element_od_mm': 60.5, 'outer_ring_od_mm': 88.9},
    '1-1/2': {'nps': '1-1/2', 'class': 1500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 41.4, 'sealing_element_id_mm': 47.8, 'sealing_element_od_mm': 69.9, 'outer_ring_od_mm': 98.6},
    '2': {'nps': '2', 'class': 1500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 52.3, 'sealing_element_id_mm': 58.7, 'sealing_element_od_mm': 85.9, 'outer_ring_od_mm': 143.0},
    '2-1/2': {'nps': '2-1/2', 'class': 1500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 63.5, 'sealing_element_id_mm': 69.9, 'sealing_element_od_mm': 98.6, 'outer_ring_od_mm': 165.1},
    '3': {'nps': '3', 'class': 1500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 78.7, 'sealing_element_id_mm': 92.2, 'sealing_element_od_mm': 120.7, 'outer_ring_od_mm': 174.8},
    '3-1/2': {'nps': '3-1/2', 'class': 1500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': None, 'sealing_element_id_mm': 104.8, 'sealing_element_od_mm': 133.4, 'outer_ring_od_mm': 187.3},
    '4': {'nps': '4', 'class': 1500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 97.8, 'sealing_element_id_mm': 117.6, 'sealing_element_od_mm': 149.4, 'outer_ring_od_mm': 209.6},
    '4-1/2': {'nps': '4-1/2', 'class': 1500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': None, 'sealing_element_id_mm': 134.9, 'sealing_element_od_mm': 165.1, 'outer_ring_od_mm': 231.8},
    '5': {'nps': '5', 'class': 1500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 124.5, 'sealing_element_id_mm': 143.0, 'sealing_element_od_mm': 177.8, 'outer_ring_od_mm': 254.0},
    '6': {'nps': '6', 'class': 1500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 147.3, 'sealing_element_id_mm': 171.5, 'sealing_element_od_mm': 209.6, 'outer_ring_od_mm': 282.7},
    '8': {'nps': '8', 'class': 1500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 196.9, 'sealing_element_id_mm': 215.9, 'sealing_element_od_mm': 257.3, 'outer_ring_od_mm': 352.6},
    '10': {'nps': '10', 'class': 1500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 246.1, 'sealing_element_id_mm': 266.7, 'sealing_element_od_mm': 311.2, 'outer_ring_od_mm': 435.1},
    '12': {'nps': '12', 'class': 1500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 292.1, 'sealing_element_id_mm': 323.9, 'sealing_element_od_mm': 368.3, 'outer_ring_od_mm': 520.7},
    '14': {'nps': '14', 'class': 1500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 320.8, 'sealing_element_id_mm': 362.0, 'sealing_element_od_mm': 400.1, 'outer_ring_od_mm': 577.9},
    '16': {'nps': '16', 'class': 1500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 374.7, 'sealing_element_id_mm': 406.4, 'sealing_element_od_mm': 457.2, 'outer_ring_od_mm': 641.4},
    '18': {'nps': '18', 'class': 1500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 425.5, 'sealing_element_id_mm': 463.6, 'sealing_element_od_mm': 520.7, 'outer_ring_od_mm': 704.9},
    '20': {'nps': '20', 'class': 1500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 476.3, 'sealing_element_id_mm': 514.4, 'sealing_element_od_mm': 571.5, 'outer_ring_od_mm': 755.7},
    '24': {'nps': '24', 'class': 1500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 577.9, 'sealing_element_id_mm': 616.0, 'sealing_element_od_mm': 679.5, 'outer_ring_od_mm': 901.7},
}

# ASME B16.5 Class 2500 Spiral Wound Gaskets (with inner and outer rings)
# Note: Class 2500 available only through NPS 12", and NPS 3-1/2" and 4-1/2" not available (incomplete specifications)
B165_CLASS2500_SPIRAL_WOUND_GASKETS = {
    '1/2': {'nps': '1/2', 'class': 2500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 14.2, 'sealing_element_id_mm': 19.1, 'sealing_element_od_mm': 31.8, 'outer_ring_od_mm': 69.9},
    '3/4': {'nps': '3/4', 'class': 2500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 20.6, 'sealing_element_id_mm': 25.4, 'sealing_element_od_mm': 39.6, 'outer_ring_od_mm': 76.2},
    '1': {'nps': '1', 'class': 2500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 26.9, 'sealing_element_id_mm': 31.8, 'sealing_element_od_mm': 47.8, 'outer_ring_od_mm': 85.9},
    '1-1/4': {'nps': '1-1/4', 'class': 2500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 33.3, 'sealing_element_id_mm': 39.6, 'sealing_element_od_mm': 60.5, 'outer_ring_od_mm': 104.9},
    '1-1/2': {'nps': '1-1/2', 'class': 2500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 41.4, 'sealing_element_id_mm': 47.8, 'sealing_element_od_mm': 69.9, 'outer_ring_od_mm': 117.6},
    '2': {'nps': '2', 'class': 2500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 52.3, 'sealing_element_id_mm': 58.7, 'sealing_element_od_mm': 85.9, 'outer_ring_od_mm': 146.1},
    '2-1/2': {'nps': '2-1/2', 'class': 2500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 63.5, 'sealing_element_id_mm': 69.9, 'sealing_element_od_mm': 98.6, 'outer_ring_od_mm': 168.4},
    '3': {'nps': '3', 'class': 2500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 78.7, 'sealing_element_id_mm': 92.2, 'sealing_element_od_mm': 120.7, 'outer_ring_od_mm': 196.9},
    '4': {'nps': '4', 'class': 2500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 97.8, 'sealing_element_id_mm': 117.6, 'sealing_element_od_mm': 149.4, 'outer_ring_od_mm': 235.0},
    '5': {'nps': '5', 'class': 2500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 124.5, 'sealing_element_id_mm': 143.0, 'sealing_element_od_mm': 177.8, 'outer_ring_od_mm': 279.4},
    '6': {'nps': '6', 'class': 2500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 147.3, 'sealing_element_id_mm': 171.5, 'sealing_element_od_mm': 209.6, 'outer_ring_od_mm': 317.5},
    '8': {'nps': '8', 'class': 2500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 196.9, 'sealing_element_id_mm': 215.9, 'sealing_element_od_mm': 257.3, 'outer_ring_od_mm': 387.4},
    '10': {'nps': '10', 'class': 2500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 246.1, 'sealing_element_id_mm': 270.0, 'sealing_element_od_mm': 311.2, 'outer_ring_od_mm': 476.3},
    '12': {'nps': '12', 'class': 2500, 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 292.1, 'sealing_element_id_mm': 317.5, 'sealing_element_od_mm': 368.3, 'outer_ring_od_mm': 549.4},
}

# ASME B16.47 Series A Class 150 Spiral Wound Gaskets (with inner and outer rings)
B1647A_CLASS150_SPIRAL_WOUND_GASKETS = {
    '26': {'nps': '26', 'class': 150, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 654.1, 'sealing_element_id_mm': 673.1, 'sealing_element_od_mm': 704.9, 'outer_ring_od_mm': 774.7},
    '28': {'nps': '28', 'class': 150, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 704.9, 'sealing_element_id_mm': 723.9, 'sealing_element_od_mm': 755.7, 'outer_ring_od_mm': 831.9},
    '30': {'nps': '30', 'class': 150, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 755.7, 'sealing_element_id_mm': 774.7, 'sealing_element_od_mm': 806.5, 'outer_ring_od_mm': 882.7},
    '32': {'nps': '32', 'class': 150, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 806.5, 'sealing_element_id_mm': 825.5, 'sealing_element_od_mm': 860.6, 'outer_ring_od_mm': 939.8},
    '34': {'nps': '34', 'class': 150, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 857.3, 'sealing_element_id_mm': 876.3, 'sealing_element_od_mm': 911.4, 'outer_ring_od_mm': 990.6},
    '36': {'nps': '36', 'class': 150, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 908.1, 'sealing_element_id_mm': 927.1, 'sealing_element_od_mm': 968.5, 'outer_ring_od_mm': 1047.8},
    '38': {'nps': '38', 'class': 150, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 958.9, 'sealing_element_id_mm': 977.9, 'sealing_element_od_mm': 1019.3, 'outer_ring_od_mm': 1111.3},
    '40': {'nps': '40', 'class': 150, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1009.7, 'sealing_element_id_mm': 1028.7, 'sealing_element_od_mm': 1070.1, 'outer_ring_od_mm': 1162.1},
    '42': {'nps': '42', 'class': 150, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1060.5, 'sealing_element_id_mm': 1079.5, 'sealing_element_od_mm': 1124.0, 'outer_ring_od_mm': 1219.2},
    '44': {'nps': '44', 'class': 150, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1111.3, 'sealing_element_id_mm': 1130.3, 'sealing_element_od_mm': 1178.1, 'outer_ring_od_mm': 1276.4},
    '46': {'nps': '46', 'class': 150, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1162.1, 'sealing_element_id_mm': 1181.1, 'sealing_element_od_mm': 1228.9, 'outer_ring_od_mm': 1327.2},
    '48': {'nps': '48', 'class': 150, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1212.9, 'sealing_element_id_mm': 1231.9, 'sealing_element_od_mm': 1279.7, 'outer_ring_od_mm': 1384.3},
    '50': {'nps': '50', 'class': 150, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1263.7, 'sealing_element_id_mm': 1282.7, 'sealing_element_od_mm': 1333.5, 'outer_ring_od_mm': 1435.1},
    '52': {'nps': '52', 'class': 150, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1314.5, 'sealing_element_id_mm': 1333.5, 'sealing_element_od_mm': 1384.3, 'outer_ring_od_mm': 1492.3},
    '54': {'nps': '54', 'class': 150, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1358.9, 'sealing_element_id_mm': 1384.3, 'sealing_element_od_mm': 1435.1, 'outer_ring_od_mm': 1549.4},
    '56': {'nps': '56', 'class': 150, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1409.7, 'sealing_element_id_mm': 1435.1, 'sealing_element_od_mm': 1485.9, 'outer_ring_od_mm': 1606.6},
    '58': {'nps': '58', 'class': 150, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1460.5, 'sealing_element_id_mm': 1485.9, 'sealing_element_od_mm': 1536.7, 'outer_ring_od_mm': 1663.7},
    '60': {'nps': '60', 'class': 150, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1511.3, 'sealing_element_id_mm': 1536.7, 'sealing_element_od_mm': 1587.5, 'outer_ring_od_mm': 1714.5},
}

# ASME B16.47 Series A Class 300 Spiral Wound Gaskets (with inner and outer rings)
B1647A_CLASS300_SPIRAL_WOUND_GASKETS = {
    '26': {'nps': '26', 'class': 300, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 654.1, 'sealing_element_id_mm': 673.1, 'sealing_element_od_mm': 711.2, 'outer_ring_od_mm': 771.7},
    '28': {'nps': '28', 'class': 300, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 704.9, 'sealing_element_id_mm': 723.9, 'sealing_element_od_mm': 762.0, 'outer_ring_od_mm': 825.5},
    '30': {'nps': '30', 'class': 300, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 755.7, 'sealing_element_id_mm': 774.7, 'sealing_element_od_mm': 812.8, 'outer_ring_od_mm': 886.0},
    '32': {'nps': '32', 'class': 300, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 806.5, 'sealing_element_id_mm': 825.5, 'sealing_element_od_mm': 863.6, 'outer_ring_od_mm': 939.8},
    '34': {'nps': '34', 'class': 300, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 857.3, 'sealing_element_id_mm': 876.3, 'sealing_element_od_mm': 914.4, 'outer_ring_od_mm': 993.9},
    '36': {'nps': '36', 'class': 300, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 908.1, 'sealing_element_id_mm': 927.1, 'sealing_element_od_mm': 965.2, 'outer_ring_od_mm': 1047.8},
    '38': {'nps': '38', 'class': 300, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 971.6, 'sealing_element_id_mm': 1009.7, 'sealing_element_od_mm': 1047.8, 'outer_ring_od_mm': 1098.6},
    '40': {'nps': '40', 'class': 300, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1022.4, 'sealing_element_id_mm': 1060.5, 'sealing_element_od_mm': 1098.6, 'outer_ring_od_mm': 1149.4},
    '42': {'nps': '42', 'class': 300, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1085.9, 'sealing_element_id_mm': 1111.3, 'sealing_element_od_mm': 1149.4, 'outer_ring_od_mm': 1200.2},
    '44': {'nps': '44', 'class': 300, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1124.0, 'sealing_element_id_mm': 1162.1, 'sealing_element_od_mm': 1200.2, 'outer_ring_od_mm': 1251.0},
    '46': {'nps': '46', 'class': 300, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1178.1, 'sealing_element_id_mm': 1216.2, 'sealing_element_od_mm': 1254.3, 'outer_ring_od_mm': 1317.8},
    '48': {'nps': '48', 'class': 300, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1231.9, 'sealing_element_id_mm': 1263.7, 'sealing_element_od_mm': 1311.4, 'outer_ring_od_mm': 1368.6},
    '50': {'nps': '50', 'class': 300, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1267.0, 'sealing_element_id_mm': 1317.8, 'sealing_element_od_mm': 1355.9, 'outer_ring_od_mm': 1419.4},
    '52': {'nps': '52', 'class': 300, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1317.8, 'sealing_element_id_mm': 1368.6, 'sealing_element_od_mm': 1406.7, 'outer_ring_od_mm': 1470.2},
    '54': {'nps': '54', 'class': 300, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1365.3, 'sealing_element_id_mm': 1403.4, 'sealing_element_od_mm': 1454.2, 'outer_ring_od_mm': 1530.4},
    '56': {'nps': '56', 'class': 300, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1428.8, 'sealing_element_id_mm': 1479.6, 'sealing_element_od_mm': 1524.0, 'outer_ring_od_mm': 1593.9},
    '58': {'nps': '58', 'class': 300, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1484.4, 'sealing_element_id_mm': 1535.2, 'sealing_element_od_mm': 1573.3, 'outer_ring_od_mm': 1655.8},
    '60': {'nps': '60', 'class': 300, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1557.3, 'sealing_element_id_mm': 1589.0, 'sealing_element_od_mm': 1630.4, 'outer_ring_od_mm': 1706.6},
}

# ASME B16.47 Series A Class 400 Spiral Wound Gaskets (with inner and outer rings)
B1647A_CLASS400_SPIRAL_WOUND_GASKETS = {
    '26': {'nps': '26', 'class': 400, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 660.4, 'sealing_element_id_mm': 685.8, 'sealing_element_od_mm': 736.6, 'outer_ring_od_mm': 831.9},
    '28': {'nps': '28', 'class': 400, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 711.2, 'sealing_element_id_mm': 736.6, 'sealing_element_od_mm': 787.4, 'outer_ring_od_mm': 892.3},
    '30': {'nps': '30', 'class': 400, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 755.7, 'sealing_element_id_mm': 793.8, 'sealing_element_od_mm': 844.6, 'outer_ring_od_mm': 946.2},
    '32': {'nps': '32', 'class': 400, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 812.8, 'sealing_element_id_mm': 850.9, 'sealing_element_od_mm': 901.7, 'outer_ring_od_mm': 1003.3},
    '34': {'nps': '34', 'class': 400, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 863.6, 'sealing_element_id_mm': 901.7, 'sealing_element_od_mm': 952.5, 'outer_ring_od_mm': 1054.1},
    '36': {'nps': '36', 'class': 400, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 917.7, 'sealing_element_id_mm': 955.8, 'sealing_element_od_mm': 1006.6, 'outer_ring_od_mm': 1117.6},
    '38': {'nps': '38', 'class': 400, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 952.5, 'sealing_element_id_mm': 971.6, 'sealing_element_od_mm': 1022.4, 'outer_ring_od_mm': 1073.2},
    '40': {'nps': '40', 'class': 400, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1000.3, 'sealing_element_id_mm': 1025.7, 'sealing_element_od_mm': 1076.5, 'outer_ring_od_mm': 1127.3},
    '42': {'nps': '42', 'class': 400, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1051.1, 'sealing_element_id_mm': 1076.5, 'sealing_element_od_mm': 1127.3, 'outer_ring_od_mm': 1178.1},
    '44': {'nps': '44', 'class': 400, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1104.9, 'sealing_element_id_mm': 1130.3, 'sealing_element_od_mm': 1181.1, 'outer_ring_od_mm': 1231.9},
    '46': {'nps': '46', 'class': 400, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1168.4, 'sealing_element_id_mm': 1193.8, 'sealing_element_od_mm': 1244.6, 'outer_ring_od_mm': 1289.1},
    '48': {'nps': '48', 'class': 400, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1206.5, 'sealing_element_id_mm': 1244.6, 'sealing_element_od_mm': 1295.4, 'outer_ring_od_mm': 1346.2},
    '50': {'nps': '50', 'class': 400, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1257.3, 'sealing_element_id_mm': 1295.4, 'sealing_element_od_mm': 1346.2, 'outer_ring_od_mm': 1403.4},
    '52': {'nps': '52', 'class': 400, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1308.1, 'sealing_element_id_mm': 1346.2, 'sealing_element_od_mm': 1397.0, 'outer_ring_od_mm': 1454.2},
    '54': {'nps': '54', 'class': 400, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1352.6, 'sealing_element_id_mm': 1403.4, 'sealing_element_od_mm': 1454.2, 'outer_ring_od_mm': 1517.7},
    '56': {'nps': '56', 'class': 400, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1403.4, 'sealing_element_id_mm': 1454.2, 'sealing_element_od_mm': 1505.0, 'outer_ring_od_mm': 1568.5},
    '58': {'nps': '58', 'class': 400, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1454.2, 'sealing_element_id_mm': 1505.0, 'sealing_element_od_mm': 1555.8, 'outer_ring_od_mm': 1619.3},
    '60': {'nps': '60', 'class': 400, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1517.7, 'sealing_element_id_mm': 1568.5, 'sealing_element_od_mm': 1619.3, 'outer_ring_od_mm': 1682.8},
}

# ASME B16.47 Series A Class 600 Spiral Wound Gaskets (with inner and outer rings)
B1647A_CLASS600_SPIRAL_WOUND_GASKETS = {
    '26': {'nps': '26', 'class': 600, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 647.7, 'sealing_element_id_mm': 685.8, 'sealing_element_od_mm': 736.6, 'outer_ring_od_mm': 866.9},
    '28': {'nps': '28', 'class': 600, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 698.5, 'sealing_element_id_mm': 736.6, 'sealing_element_od_mm': 787.4, 'outer_ring_od_mm': 914.4},
    '30': {'nps': '30', 'class': 600, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 755.7, 'sealing_element_id_mm': 793.8, 'sealing_element_od_mm': 844.6, 'outer_ring_od_mm': 971.6},
    '32': {'nps': '32', 'class': 600, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 812.8, 'sealing_element_id_mm': 850.9, 'sealing_element_od_mm': 901.7, 'outer_ring_od_mm': 1022.4},
    '34': {'nps': '34', 'class': 600, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 863.6, 'sealing_element_id_mm': 901.7, 'sealing_element_od_mm': 952.5, 'outer_ring_od_mm': 1073.2},
    '36': {'nps': '36', 'class': 600, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 917.7, 'sealing_element_id_mm': 955.8, 'sealing_element_od_mm': 1006.6, 'outer_ring_od_mm': 1130.3},
    '38': {'nps': '38', 'class': 600, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 952.5, 'sealing_element_id_mm': 990.6, 'sealing_element_od_mm': 1041.4, 'outer_ring_od_mm': 1104.9},
    '40': {'nps': '40', 'class': 600, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1009.7, 'sealing_element_id_mm': 1047.8, 'sealing_element_od_mm': 1098.6, 'outer_ring_od_mm': 1155.7},
    '42': {'nps': '42', 'class': 600, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1066.8, 'sealing_element_id_mm': 1104.9, 'sealing_element_od_mm': 1155.7, 'outer_ring_od_mm': 1219.2},
    '44': {'nps': '44', 'class': 600, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1111.3, 'sealing_element_id_mm': 1162.1, 'sealing_element_od_mm': 1212.9, 'outer_ring_od_mm': 1270.0},
    '46': {'nps': '46', 'class': 600, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1162.1, 'sealing_element_id_mm': 1212.9, 'sealing_element_od_mm': 1263.7, 'outer_ring_od_mm': 1327.2},
    '48': {'nps': '48', 'class': 600, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1219.2, 'sealing_element_id_mm': 1270.0, 'sealing_element_od_mm': 1320.8, 'outer_ring_od_mm': 1390.7},
    '50': {'nps': '50', 'class': 600, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1270.0, 'sealing_element_id_mm': 1320.8, 'sealing_element_od_mm': 1371.6, 'outer_ring_od_mm': 1447.8},
    '52': {'nps': '52', 'class': 600, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1320.8, 'sealing_element_id_mm': 1371.6, 'sealing_element_od_mm': 1422.4, 'outer_ring_od_mm': 1498.6},
    '54': {'nps': '54', 'class': 600, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1378.0, 'sealing_element_id_mm': 1428.8, 'sealing_element_od_mm': 1479.6, 'outer_ring_od_mm': 1555.8},
    '56': {'nps': '56', 'class': 600, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1428.8, 'sealing_element_id_mm': 1479.6, 'sealing_element_od_mm': 1530.4, 'outer_ring_od_mm': 1612.9},
    '58': {'nps': '58', 'class': 600, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1473.2, 'sealing_element_id_mm': 1536.7, 'sealing_element_od_mm': 1587.5, 'outer_ring_od_mm': 1663.7},
    '60': {'nps': '60', 'class': 600, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1530.4, 'sealing_element_id_mm': 1593.9, 'sealing_element_od_mm': 1644.7, 'outer_ring_od_mm': 1733.6},
}

# ASME B16.47 Series A Class 900 Spiral Wound Gaskets (with inner and outer rings)
# Note: Class 900 available only through NPS 48"
B1647A_CLASS900_SPIRAL_WOUND_GASKETS = {
    '26': {'nps': '26', 'class': 900, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 660.4, 'sealing_element_id_mm': 685.8, 'sealing_element_od_mm': 736.6, 'outer_ring_od_mm': 882.7},
    '28': {'nps': '28', 'class': 900, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 711.2, 'sealing_element_id_mm': 736.6, 'sealing_element_od_mm': 787.4, 'outer_ring_od_mm': 946.2},
    '30': {'nps': '30', 'class': 900, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 768.4, 'sealing_element_id_mm': 793.8, 'sealing_element_od_mm': 844.6, 'outer_ring_od_mm': 1009.7},
    '32': {'nps': '32', 'class': 900, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 812.8, 'sealing_element_id_mm': 850.9, 'sealing_element_od_mm': 901.7, 'outer_ring_od_mm': 1073.2},
    '34': {'nps': '34', 'class': 900, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 863.6, 'sealing_element_id_mm': 901.7, 'sealing_element_od_mm': 952.5, 'outer_ring_od_mm': 1136.7},
    '36': {'nps': '36', 'class': 900, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 920.8, 'sealing_element_id_mm': 958.9, 'sealing_element_od_mm': 1009.7, 'outer_ring_od_mm': 1200.2},
    '38': {'nps': '38', 'class': 900, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1009.7, 'sealing_element_id_mm': 1035.1, 'sealing_element_od_mm': 1085.9, 'outer_ring_od_mm': 1200.2},
    '40': {'nps': '40', 'class': 900, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1060.5, 'sealing_element_id_mm': 1098.6, 'sealing_element_od_mm': 1149.4, 'outer_ring_od_mm': 1251.0},
    '42': {'nps': '42', 'class': 900, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1111.3, 'sealing_element_id_mm': 1149.4, 'sealing_element_od_mm': 1200.2, 'outer_ring_od_mm': 1301.8},
    '44': {'nps': '44', 'class': 900, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1155.7, 'sealing_element_id_mm': 1206.5, 'sealing_element_od_mm': 1257.3, 'outer_ring_od_mm': 1368.6},
    '46': {'nps': '46', 'class': 900, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1219.2, 'sealing_element_id_mm': 1270.0, 'sealing_element_od_mm': 1320.8, 'outer_ring_od_mm': 1435.1},
    '48': {'nps': '48', 'class': 900, 'series': 'A', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1270.0, 'sealing_element_id_mm': 1320.8, 'sealing_element_od_mm': 1371.6, 'outer_ring_od_mm': 1485.9},
}

# ASME B16.47 Series B Class 150 Spiral Wound Gaskets (with inner and outer rings)
B1647B_CLASS150_SPIRAL_WOUND_GASKETS = {
    '26': {'nps': '26', 'class': 150, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 654.1, 'sealing_element_id_mm': 673.1, 'sealing_element_od_mm': 698.5, 'outer_ring_od_mm': 725.4},
    '28': {'nps': '28', 'class': 150, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 704.9, 'sealing_element_id_mm': 723.9, 'sealing_element_od_mm': 749.3, 'outer_ring_od_mm': 776.2},
    '30': {'nps': '30', 'class': 150, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 755.7, 'sealing_element_id_mm': 774.7, 'sealing_element_od_mm': 800.1, 'outer_ring_od_mm': 827.0},
    '32': {'nps': '32', 'class': 150, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 806.5, 'sealing_element_id_mm': 825.5, 'sealing_element_od_mm': 850.9, 'outer_ring_od_mm': 881.1},
    '34': {'nps': '34', 'class': 150, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 857.3, 'sealing_element_id_mm': 876.3, 'sealing_element_od_mm': 908.1, 'outer_ring_od_mm': 935.0},
    '36': {'nps': '36', 'class': 150, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 908.1, 'sealing_element_id_mm': 927.1, 'sealing_element_od_mm': 958.9, 'outer_ring_od_mm': 987.6},
    '38': {'nps': '38', 'class': 150, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 958.9, 'sealing_element_id_mm': 974.9, 'sealing_element_od_mm': 1009.7, 'outer_ring_od_mm': 1044.7},
    '40': {'nps': '40', 'class': 150, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1009.7, 'sealing_element_id_mm': 1022.4, 'sealing_element_od_mm': 1063.8, 'outer_ring_od_mm': 1095.5},
    '42': {'nps': '42', 'class': 150, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1060.5, 'sealing_element_id_mm': 1079.5, 'sealing_element_od_mm': 1114.6, 'outer_ring_od_mm': 1146.3},
    '44': {'nps': '44', 'class': 150, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1111.3, 'sealing_element_id_mm': 1124.0, 'sealing_element_od_mm': 1165.4, 'outer_ring_od_mm': 1197.1},
    '46': {'nps': '46', 'class': 150, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1162.1, 'sealing_element_id_mm': 1181.1, 'sealing_element_od_mm': 1224.0, 'outer_ring_od_mm': 1255.8},
    '48': {'nps': '48', 'class': 150, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1212.9, 'sealing_element_id_mm': 1231.9, 'sealing_element_od_mm': 1270.0, 'outer_ring_od_mm': 1306.6},
    '50': {'nps': '50', 'class': 150, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1263.7, 'sealing_element_id_mm': 1282.7, 'sealing_element_od_mm': 1325.6, 'outer_ring_od_mm': 1357.4},
    '52': {'nps': '52', 'class': 150, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1314.5, 'sealing_element_id_mm': 1333.5, 'sealing_element_od_mm': 1376.4, 'outer_ring_od_mm': 1408.2},
    '54': {'nps': '54', 'class': 150, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1365.3, 'sealing_element_id_mm': 1384.3, 'sealing_element_od_mm': 1422.4, 'outer_ring_od_mm': 1463.8},
    '56': {'nps': '56', 'class': 150, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1422.4, 'sealing_element_id_mm': 1444.8, 'sealing_element_od_mm': 1478.0, 'outer_ring_od_mm': 1514.6},
    '58': {'nps': '58', 'class': 150, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1478.0, 'sealing_element_id_mm': 1500.0, 'sealing_element_od_mm': 1528.8, 'outer_ring_od_mm': 1579.6},
    '60': {'nps': '60', 'class': 150, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1535.2, 'sealing_element_id_mm': 1557.3, 'sealing_element_od_mm': 1586.0, 'outer_ring_od_mm': 1630.4},
}

# ASME B16.47 Series B Class 300 Spiral Wound Gaskets (with inner and outer rings)
B1647B_CLASS300_SPIRAL_WOUND_GASKETS = {
    '26': {'nps': '26', 'class': 300, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 654.1, 'sealing_element_id_mm': 673.1, 'sealing_element_od_mm': 711.2, 'outer_ring_od_mm': 771.7},
    '28': {'nps': '28', 'class': 300, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 704.9, 'sealing_element_id_mm': 723.9, 'sealing_element_od_mm': 762.0, 'outer_ring_od_mm': 825.5},
    '30': {'nps': '30', 'class': 300, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 755.7, 'sealing_element_id_mm': 774.7, 'sealing_element_od_mm': 812.8, 'outer_ring_od_mm': 886.0},
    '32': {'nps': '32', 'class': 300, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 806.5, 'sealing_element_id_mm': 825.5, 'sealing_element_od_mm': 863.6, 'outer_ring_od_mm': 939.8},
    '34': {'nps': '34', 'class': 300, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 857.3, 'sealing_element_id_mm': 876.3, 'sealing_element_od_mm': 914.4, 'outer_ring_od_mm': 993.9},
    '36': {'nps': '36', 'class': 300, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 908.1, 'sealing_element_id_mm': 927.1, 'sealing_element_od_mm': 965.2, 'outer_ring_od_mm': 1047.8},
    '38': {'nps': '38', 'class': 300, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 971.6, 'sealing_element_id_mm': 1009.7, 'sealing_element_od_mm': 1047.8, 'outer_ring_od_mm': 1098.6},
    '40': {'nps': '40', 'class': 300, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1022.4, 'sealing_element_id_mm': 1060.5, 'sealing_element_od_mm': 1098.6, 'outer_ring_od_mm': 1149.4},
    '42': {'nps': '42', 'class': 300, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1085.9, 'sealing_element_id_mm': 1111.3, 'sealing_element_od_mm': 1149.4, 'outer_ring_od_mm': 1200.2},
    '44': {'nps': '44', 'class': 300, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1124.0, 'sealing_element_id_mm': 1162.1, 'sealing_element_od_mm': 1200.2, 'outer_ring_od_mm': 1251.0},
    '46': {'nps': '46', 'class': 300, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1178.1, 'sealing_element_id_mm': 1216.2, 'sealing_element_od_mm': 1254.3, 'outer_ring_od_mm': 1317.8},
    '48': {'nps': '48', 'class': 300, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1231.9, 'sealing_element_id_mm': 1263.7, 'sealing_element_od_mm': 1311.4, 'outer_ring_od_mm': 1368.6},
    '50': {'nps': '50', 'class': 300, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1267.0, 'sealing_element_id_mm': 1317.8, 'sealing_element_od_mm': 1355.9, 'outer_ring_od_mm': 1419.4},
    '52': {'nps': '52', 'class': 300, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1317.8, 'sealing_element_id_mm': 1368.6, 'sealing_element_od_mm': 1406.7, 'outer_ring_od_mm': 1470.2},
    '54': {'nps': '54', 'class': 300, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1365.3, 'sealing_element_id_mm': 1403.4, 'sealing_element_od_mm': 1454.2, 'outer_ring_od_mm': 1530.4},
    '56': {'nps': '56', 'class': 300, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1428.8, 'sealing_element_id_mm': 1479.6, 'sealing_element_od_mm': 1524.0, 'outer_ring_od_mm': 1593.9},
    '58': {'nps': '58', 'class': 300, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1484.4, 'sealing_element_id_mm': 1535.2, 'sealing_element_od_mm': 1573.3, 'outer_ring_od_mm': 1655.8},
    '60': {'nps': '60', 'class': 300, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1557.3, 'sealing_element_id_mm': 1589.0, 'sealing_element_od_mm': 1630.4, 'outer_ring_od_mm': 1706.6},
}

# ASME B16.47 Series B Class 400 Spiral Wound Gaskets (with inner and outer rings)
B1647B_CLASS400_SPIRAL_WOUND_GASKETS = {
    '26': {'nps': '26', 'class': 400, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 654.1, 'sealing_element_id_mm': 666.8, 'sealing_element_od_mm': 698.5, 'outer_ring_od_mm': 746.3},
    '28': {'nps': '28', 'class': 400, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 701.8, 'sealing_element_id_mm': 714.5, 'sealing_element_od_mm': 749.3, 'outer_ring_od_mm': 800.1},
    '30': {'nps': '30', 'class': 400, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 752.6, 'sealing_element_id_mm': 765.3, 'sealing_element_od_mm': 806.5, 'outer_ring_od_mm': 857.3},
    '32': {'nps': '32', 'class': 400, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 800.1, 'sealing_element_id_mm': 812.8, 'sealing_element_od_mm': 860.6, 'outer_ring_od_mm': 911.4},
    '34': {'nps': '34', 'class': 400, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 850.9, 'sealing_element_id_mm': 866.9, 'sealing_element_od_mm': 911.4, 'outer_ring_od_mm': 962.2},
    '36': {'nps': '36', 'class': 400, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 898.7, 'sealing_element_id_mm': 917.7, 'sealing_element_od_mm': 965.2, 'outer_ring_od_mm': 1022.4},
    '38': {'nps': '38', 'class': 400, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 952.5, 'sealing_element_id_mm': 971.6, 'sealing_element_od_mm': 1022.4, 'outer_ring_od_mm': 1073.2},
    '40': {'nps': '40', 'class': 400, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1000.3, 'sealing_element_id_mm': 1025.7, 'sealing_element_od_mm': 1076.5, 'outer_ring_od_mm': 1127.3},
    '42': {'nps': '42', 'class': 400, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1051.1, 'sealing_element_id_mm': 1076.5, 'sealing_element_od_mm': 1127.3, 'outer_ring_od_mm': 1178.1},
    '44': {'nps': '44', 'class': 400, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1104.9, 'sealing_element_id_mm': 1130.3, 'sealing_element_od_mm': 1181.1, 'outer_ring_od_mm': 1231.9},
    '46': {'nps': '46', 'class': 400, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1168.4, 'sealing_element_id_mm': 1193.8, 'sealing_element_od_mm': 1244.6, 'outer_ring_od_mm': 1289.1},
    '48': {'nps': '48', 'class': 400, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1206.5, 'sealing_element_id_mm': 1244.6, 'sealing_element_od_mm': 1295.4, 'outer_ring_od_mm': 1346.2},
    '50': {'nps': '50', 'class': 400, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1257.3, 'sealing_element_id_mm': 1295.4, 'sealing_element_od_mm': 1346.2, 'outer_ring_od_mm': 1403.4},
    '52': {'nps': '52', 'class': 400, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1308.1, 'sealing_element_id_mm': 1346.2, 'sealing_element_od_mm': 1397.0, 'outer_ring_od_mm': 1454.2},
    '54': {'nps': '54', 'class': 400, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1352.6, 'sealing_element_id_mm': 1403.4, 'sealing_element_od_mm': 1454.2, 'outer_ring_od_mm': 1517.7},
    '56': {'nps': '56', 'class': 400, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1403.4, 'sealing_element_id_mm': 1454.2, 'sealing_element_od_mm': 1505.0, 'outer_ring_od_mm': 1568.5},
    '58': {'nps': '58', 'class': 400, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1454.2, 'sealing_element_id_mm': 1505.0, 'sealing_element_od_mm': 1555.8, 'outer_ring_od_mm': 1619.3},
    '60': {'nps': '60', 'class': 400, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1517.7, 'sealing_element_id_mm': 1568.5, 'sealing_element_od_mm': 1619.3, 'outer_ring_od_mm': 1682.8},
}

# ASME B16.47 Series B Class 600 Spiral Wound Gaskets (with inner and outer rings)
B1647B_CLASS600_SPIRAL_WOUND_GASKETS = {
    '26': {'nps': '26', 'class': 600, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 644.7, 'sealing_element_id_mm': 663.7, 'sealing_element_od_mm': 714.5, 'outer_ring_od_mm': 765.3},
    '28': {'nps': '28', 'class': 600, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 685.8, 'sealing_element_id_mm': 704.9, 'sealing_element_od_mm': 755.7, 'outer_ring_od_mm': 819.2},
    '30': {'nps': '30', 'class': 600, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 752.6, 'sealing_element_id_mm': 778.0, 'sealing_element_od_mm': 828.8, 'outer_ring_od_mm': 879.6},
    '32': {'nps': '32', 'class': 600, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 793.8, 'sealing_element_id_mm': 831.9, 'sealing_element_od_mm': 882.7, 'outer_ring_od_mm': 933.5},
    '34': {'nps': '34', 'class': 600, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 850.9, 'sealing_element_id_mm': 889.0, 'sealing_element_od_mm': 939.8, 'outer_ring_od_mm': 997.0},
    '36': {'nps': '36', 'class': 600, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 901.7, 'sealing_element_id_mm': 939.8, 'sealing_element_od_mm': 990.6, 'outer_ring_od_mm': 1047.8},
    '38': {'nps': '38', 'class': 600, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 952.5, 'sealing_element_id_mm': 990.6, 'sealing_element_od_mm': 1041.4, 'outer_ring_od_mm': 1104.9},
    '40': {'nps': '40', 'class': 600, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1009.7, 'sealing_element_id_mm': 1047.8, 'sealing_element_od_mm': 1098.6, 'outer_ring_od_mm': 1155.7},
    '42': {'nps': '42', 'class': 600, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1066.8, 'sealing_element_id_mm': 1104.9, 'sealing_element_od_mm': 1155.7, 'outer_ring_od_mm': 1219.2},
    '44': {'nps': '44', 'class': 600, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1111.3, 'sealing_element_id_mm': 1162.1, 'sealing_element_od_mm': 1212.9, 'outer_ring_od_mm': 1270.0},
    '46': {'nps': '46', 'class': 600, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1162.1, 'sealing_element_id_mm': 1212.9, 'sealing_element_od_mm': 1263.7, 'outer_ring_od_mm': 1327.2},
    '48': {'nps': '48', 'class': 600, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1219.2, 'sealing_element_id_mm': 1270.0, 'sealing_element_od_mm': 1320.8, 'outer_ring_od_mm': 1390.7},
    '50': {'nps': '50', 'class': 600, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1270.0, 'sealing_element_id_mm': 1320.8, 'sealing_element_od_mm': 1371.6, 'outer_ring_od_mm': 1447.8},
    '52': {'nps': '52', 'class': 600, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1320.8, 'sealing_element_id_mm': 1371.6, 'sealing_element_od_mm': 1422.4, 'outer_ring_od_mm': 1498.6},
    '54': {'nps': '54', 'class': 600, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1378.0, 'sealing_element_id_mm': 1428.8, 'sealing_element_od_mm': 1479.6, 'outer_ring_od_mm': 1555.8},
    '56': {'nps': '56', 'class': 600, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1428.8, 'sealing_element_id_mm': 1479.6, 'sealing_element_od_mm': 1530.4, 'outer_ring_od_mm': 1612.9},
    '58': {'nps': '58', 'class': 600, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1473.2, 'sealing_element_id_mm': 1536.7, 'sealing_element_od_mm': 1587.5, 'outer_ring_od_mm': 1663.7},
    '60': {'nps': '60', 'class': 600, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1530.4, 'sealing_element_id_mm': 1593.9, 'sealing_element_od_mm': 1644.7, 'outer_ring_od_mm': 1733.6},
}

# ASME B16.47 Series B Class 900 Spiral Wound Gaskets (with inner and outer rings)
# Note: Series B Class 900 limited to NPS 48" maximum (12 sizes)
B1647B_CLASS900_SPIRAL_WOUND_GASKETS = {
    '26': {'nps': '26', 'class': 900, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 666.8, 'sealing_element_id_mm': 692.2, 'sealing_element_od_mm': 749.3, 'outer_ring_od_mm': 838.2},
    '28': {'nps': '28', 'class': 900, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 717.6, 'sealing_element_id_mm': 743.0, 'sealing_element_od_mm': 800.1, 'outer_ring_od_mm': 901.7},
    '30': {'nps': '30', 'class': 900, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 781.1, 'sealing_element_id_mm': 806.5, 'sealing_element_od_mm': 857.3, 'outer_ring_od_mm': 958.9},
    '32': {'nps': '32', 'class': 900, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 838.2, 'sealing_element_id_mm': 863.6, 'sealing_element_od_mm': 914.4, 'outer_ring_od_mm': 1016.0},
    '34': {'nps': '34', 'class': 900, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 895.4, 'sealing_element_id_mm': 920.8, 'sealing_element_od_mm': 971.6, 'outer_ring_od_mm': 1073.2},
    '36': {'nps': '36', 'class': 900, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 920.8, 'sealing_element_id_mm': 946.2, 'sealing_element_od_mm': 997.0, 'outer_ring_od_mm': 1124.0},
    '38': {'nps': '38', 'class': 900, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1009.7, 'sealing_element_id_mm': 1035.1, 'sealing_element_od_mm': 1085.9, 'outer_ring_od_mm': 1200.2},
    '40': {'nps': '40', 'class': 900, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1060.5, 'sealing_element_id_mm': 1098.6, 'sealing_element_od_mm': 1149.4, 'outer_ring_od_mm': 1251.0},
    '42': {'nps': '42', 'class': 900, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1111.3, 'sealing_element_id_mm': 1149.4, 'sealing_element_od_mm': 1200.2, 'outer_ring_od_mm': 1301.8},
    '44': {'nps': '44', 'class': 900, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1155.7, 'sealing_element_id_mm': 1206.5, 'sealing_element_od_mm': 1257.3, 'outer_ring_od_mm': 1368.6},
    '46': {'nps': '46', 'class': 900, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1219.2, 'sealing_element_id_mm': 1270.0, 'sealing_element_od_mm': 1320.8, 'outer_ring_od_mm': 1435.1},
    '48': {'nps': '48', 'class': 900, 'series': 'B', 'gasket_type': 'spiral_wound', 'inner_ring_id_mm': 1270.0, 'sealing_element_id_mm': 1320.8, 'sealing_element_od_mm': 1371.6, 'outer_ring_od_mm': 1485.9},
}

# API Ring Joint Gaskets - Type R (Oval and Octagonal profiles)
# For RTJ (Ring Type Joint) flanges per API 6A and ASME B16.20
RING_JOINT_TYPE_R_GASKETS = {
    'R-11': {'ring_number': 'R-11', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 1.344, 'pitch_diameter_mm': 34.14, 'width_inches': 0.250, 'width_mm': 6.35, 'oval_height_inches': 0.440, 'oval_height_mm': 11.2, 'octagonal_height_inches': 0.380, 'octagonal_height_mm': 9.7, 'flat_width_inches': 0.170, 'flat_width_mm': 4.32, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-12': {'ring_number': 'R-12', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 1.563, 'pitch_diameter_mm': 39.70, 'width_inches': 0.313, 'width_mm': 7.95, 'oval_height_inches': 0.560, 'oval_height_mm': 14.2, 'octagonal_height_inches': 0.500, 'octagonal_height_mm': 12.7, 'flat_width_inches': 0.206, 'flat_width_mm': 5.23, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-13': {'ring_number': 'R-13', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 1.688, 'pitch_diameter_mm': 42.88, 'width_inches': 0.313, 'width_mm': 7.95, 'oval_height_inches': 0.560, 'oval_height_mm': 14.2, 'octagonal_height_inches': 0.500, 'octagonal_height_mm': 12.7, 'flat_width_inches': 0.206, 'flat_width_mm': 5.23, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-14': {'ring_number': 'R-14', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 1.750, 'pitch_diameter_mm': 44.45, 'width_inches': 0.313, 'width_mm': 7.95, 'oval_height_inches': 0.560, 'oval_height_mm': 14.2, 'octagonal_height_inches': 0.500, 'octagonal_height_mm': 12.7, 'flat_width_inches': 0.206, 'flat_width_mm': 5.23, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-15': {'ring_number': 'R-15', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 1.875, 'pitch_diameter_mm': 47.63, 'width_inches': 0.313, 'width_mm': 7.95, 'oval_height_inches': 0.560, 'oval_height_mm': 14.2, 'octagonal_height_inches': 0.500, 'octagonal_height_mm': 12.7, 'flat_width_inches': 0.206, 'flat_width_mm': 5.23, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-16': {'ring_number': 'R-16', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 2.000, 'pitch_diameter_mm': 50.80, 'width_inches': 0.313, 'width_mm': 7.95, 'oval_height_inches': 0.560, 'oval_height_mm': 14.2, 'octagonal_height_inches': 0.500, 'octagonal_height_mm': 12.7, 'flat_width_inches': 0.206, 'flat_width_mm': 5.23, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-17': {'ring_number': 'R-17', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 2.250, 'pitch_diameter_mm': 57.15, 'width_inches': 0.313, 'width_mm': 7.95, 'oval_height_inches': 0.560, 'oval_height_mm': 14.2, 'octagonal_height_inches': 0.500, 'octagonal_height_mm': 12.7, 'flat_width_inches': 0.206, 'flat_width_mm': 5.23, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-18': {'ring_number': 'R-18', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 2.375, 'pitch_diameter_mm': 60.33, 'width_inches': 0.313, 'width_mm': 7.95, 'oval_height_inches': 0.560, 'oval_height_mm': 14.2, 'octagonal_height_inches': 0.500, 'octagonal_height_mm': 12.7, 'flat_width_inches': 0.206, 'flat_width_mm': 5.23, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-19': {'ring_number': 'R-19', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 2.563, 'pitch_diameter_mm': 65.10, 'width_inches': 0.313, 'width_mm': 7.95, 'oval_height_inches': 0.560, 'oval_height_mm': 14.2, 'octagonal_height_inches': 0.500, 'octagonal_height_mm': 12.7, 'flat_width_inches': 0.206, 'flat_width_mm': 5.23, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-20': {'ring_number': 'R-20', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 2.688, 'pitch_diameter_mm': 68.28, 'width_inches': 0.313, 'width_mm': 7.95, 'oval_height_inches': 0.560, 'oval_height_mm': 14.2, 'octagonal_height_inches': 0.500, 'octagonal_height_mm': 12.7, 'flat_width_inches': 0.206, 'flat_width_mm': 5.23, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-21': {'ring_number': 'R-21', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 2.844, 'pitch_diameter_mm': 72.24, 'width_inches': 0.438, 'width_mm': 11.13, 'oval_height_inches': 0.690, 'oval_height_mm': 17.5, 'octagonal_height_inches': 0.630, 'octagonal_height_mm': 16.0, 'flat_width_inches': 0.305, 'flat_width_mm': 7.75, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-22': {'ring_number': 'R-22', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 3.250, 'pitch_diameter_mm': 82.55, 'width_inches': 0.313, 'width_mm': 7.95, 'oval_height_inches': 0.560, 'oval_height_mm': 14.2, 'octagonal_height_inches': 0.500, 'octagonal_height_mm': 12.7, 'flat_width_inches': 0.206, 'flat_width_mm': 5.23, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-23': {'ring_number': 'R-23', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 3.250, 'pitch_diameter_mm': 82.55, 'width_inches': 0.438, 'width_mm': 11.13, 'oval_height_inches': 0.690, 'oval_height_mm': 17.5, 'octagonal_height_inches': 0.630, 'octagonal_height_mm': 16.0, 'flat_width_inches': 0.305, 'flat_width_mm': 7.75, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-24': {'ring_number': 'R-24', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 3.750, 'pitch_diameter_mm': 95.25, 'width_inches': 0.438, 'width_mm': 11.13, 'oval_height_inches': 0.690, 'oval_height_mm': 17.5, 'octagonal_height_inches': 0.630, 'octagonal_height_mm': 16.0, 'flat_width_inches': 0.305, 'flat_width_mm': 7.75, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-25': {'ring_number': 'R-25', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 4.000, 'pitch_diameter_mm': 101.60, 'width_inches': 0.313, 'width_mm': 7.95, 'oval_height_inches': 0.560, 'oval_height_mm': 14.2, 'octagonal_height_inches': 0.500, 'octagonal_height_mm': 12.7, 'flat_width_inches': 0.206, 'flat_width_mm': 5.23, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-26': {'ring_number': 'R-26', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 4.000, 'pitch_diameter_mm': 101.60, 'width_inches': 0.438, 'width_mm': 11.13, 'oval_height_inches': 0.690, 'oval_height_mm': 17.5, 'octagonal_height_inches': 0.630, 'octagonal_height_mm': 16.0, 'flat_width_inches': 0.305, 'flat_width_mm': 7.75, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-27': {'ring_number': 'R-27', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 4.250, 'pitch_diameter_mm': 107.95, 'width_inches': 0.438, 'width_mm': 11.13, 'oval_height_inches': 0.690, 'oval_height_mm': 17.5, 'octagonal_height_inches': 0.630, 'octagonal_height_mm': 16.0, 'flat_width_inches': 0.305, 'flat_width_mm': 7.75, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-28': {'ring_number': 'R-28', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 4.375, 'pitch_diameter_mm': 111.13, 'width_inches': 0.500, 'width_mm': 12.70, 'oval_height_inches': 0.750, 'oval_height_mm': 19.1, 'octagonal_height_inches': 0.690, 'octagonal_height_mm': 17.5, 'flat_width_inches': 0.341, 'flat_width_mm': 8.66, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-29': {'ring_number': 'R-29', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 4.500, 'pitch_diameter_mm': 114.30, 'width_inches': 0.313, 'width_mm': 7.95, 'oval_height_inches': 0.560, 'oval_height_mm': 14.2, 'octagonal_height_inches': 0.500, 'octagonal_height_mm': 12.7, 'flat_width_inches': 0.206, 'flat_width_mm': 5.23, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-30': {'ring_number': 'R-30', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 4.625, 'pitch_diameter_mm': 117.48, 'width_inches': 0.438, 'width_mm': 11.13, 'oval_height_inches': 0.690, 'oval_height_mm': 17.5, 'octagonal_height_inches': 0.630, 'octagonal_height_mm': 16.0, 'flat_width_inches': 0.305, 'flat_width_mm': 7.75, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-31': {'ring_number': 'R-31', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 4.875, 'pitch_diameter_mm': 123.83, 'width_inches': 0.438, 'width_mm': 11.13, 'oval_height_inches': 0.690, 'oval_height_mm': 17.5, 'octagonal_height_inches': 0.630, 'octagonal_height_mm': 16.0, 'flat_width_inches': 0.305, 'flat_width_mm': 7.75, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-32': {'ring_number': 'R-32', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 5.000, 'pitch_diameter_mm': 127.00, 'width_inches': 0.500, 'width_mm': 12.70, 'oval_height_inches': 0.750, 'oval_height_mm': 19.1, 'octagonal_height_inches': 0.690, 'octagonal_height_mm': 17.5, 'flat_width_inches': 0.341, 'flat_width_mm': 8.66, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-33': {'ring_number': 'R-33', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 5.188, 'pitch_diameter_mm': 131.78, 'width_inches': 0.313, 'width_mm': 7.95, 'oval_height_inches': 0.560, 'oval_height_mm': 14.2, 'octagonal_height_inches': 0.500, 'octagonal_height_mm': 12.7, 'flat_width_inches': 0.206, 'flat_width_mm': 5.23, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-34': {'ring_number': 'R-34', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 5.188, 'pitch_diameter_mm': 131.78, 'width_inches': 0.438, 'width_mm': 11.13, 'oval_height_inches': 0.690, 'oval_height_mm': 17.5, 'octagonal_height_inches': 0.630, 'octagonal_height_mm': 16.0, 'flat_width_inches': 0.305, 'flat_width_mm': 7.75, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-35': {'ring_number': 'R-35', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 5.375, 'pitch_diameter_mm': 136.53, 'width_inches': 0.438, 'width_mm': 11.13, 'oval_height_inches': 0.690, 'oval_height_mm': 17.5, 'octagonal_height_inches': 0.630, 'octagonal_height_mm': 16.0, 'flat_width_inches': 0.305, 'flat_width_mm': 7.75, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-36': {'ring_number': 'R-36', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 5.875, 'pitch_diameter_mm': 149.23, 'width_inches': 0.313, 'width_mm': 7.95, 'oval_height_inches': 0.560, 'oval_height_mm': 14.2, 'octagonal_height_inches': 0.500, 'octagonal_height_mm': 12.7, 'flat_width_inches': 0.206, 'flat_width_mm': 5.23, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-37': {'ring_number': 'R-37', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 5.875, 'pitch_diameter_mm': 149.23, 'width_inches': 0.438, 'width_mm': 11.13, 'oval_height_inches': 0.690, 'oval_height_mm': 17.5, 'octagonal_height_inches': 0.630, 'octagonal_height_mm': 16.0, 'flat_width_inches': 0.305, 'flat_width_mm': 7.75, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-38': {'ring_number': 'R-38', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 6.188, 'pitch_diameter_mm': 157.18, 'width_inches': 0.625, 'width_mm': 15.88, 'oval_height_inches': 0.880, 'oval_height_mm': 22.4, 'octagonal_height_inches': 0.810, 'octagonal_height_mm': 20.6, 'flat_width_inches': 0.413, 'flat_width_mm': 10.49, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-39': {'ring_number': 'R-39', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 6.375, 'pitch_diameter_mm': 161.93, 'width_inches': 0.438, 'width_mm': 11.13, 'oval_height_inches': 0.690, 'oval_height_mm': 17.5, 'octagonal_height_inches': 0.630, 'octagonal_height_mm': 16.0, 'flat_width_inches': 0.305, 'flat_width_mm': 7.75, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-40': {'ring_number': 'R-40', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 6.750, 'pitch_diameter_mm': 171.45, 'width_inches': 0.313, 'width_mm': 7.95, 'oval_height_inches': 0.560, 'oval_height_mm': 14.2, 'octagonal_height_inches': 0.500, 'octagonal_height_mm': 12.7, 'flat_width_inches': 0.206, 'flat_width_mm': 5.23, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-41': {'ring_number': 'R-41', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 7.125, 'pitch_diameter_mm': 180.98, 'width_inches': 0.438, 'width_mm': 11.13, 'oval_height_inches': 0.690, 'oval_height_mm': 17.5, 'octagonal_height_inches': 0.630, 'octagonal_height_mm': 16.0, 'flat_width_inches': 0.305, 'flat_width_mm': 7.75, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-42': {'ring_number': 'R-42', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 7.500, 'pitch_diameter_mm': 190.50, 'width_inches': 0.750, 'width_mm': 19.05, 'oval_height_inches': 1.000, 'oval_height_mm': 25.4, 'octagonal_height_inches': 0.940, 'octagonal_height_mm': 23.9, 'flat_width_inches': 0.485, 'flat_width_mm': 12.32, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-43': {'ring_number': 'R-43', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 7.625, 'pitch_diameter_mm': 193.68, 'width_inches': 0.313, 'width_mm': 7.95, 'oval_height_inches': 0.560, 'oval_height_mm': 14.2, 'octagonal_height_inches': 0.500, 'octagonal_height_mm': 12.7, 'flat_width_inches': 0.206, 'flat_width_mm': 5.23, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-44': {'ring_number': 'R-44', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 7.625, 'pitch_diameter_mm': 193.68, 'width_inches': 0.438, 'width_mm': 11.13, 'oval_height_inches': 0.690, 'oval_height_mm': 17.5, 'octagonal_height_inches': 0.630, 'octagonal_height_mm': 16.0, 'flat_width_inches': 0.305, 'flat_width_mm': 7.75, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-45': {'ring_number': 'R-45', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 8.313, 'pitch_diameter_mm': 211.15, 'width_inches': 0.438, 'width_mm': 11.13, 'oval_height_inches': 0.690, 'oval_height_mm': 17.5, 'octagonal_height_inches': 0.630, 'octagonal_height_mm': 16.0, 'flat_width_inches': 0.305, 'flat_width_mm': 7.75, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-46': {'ring_number': 'R-46', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 8.313, 'pitch_diameter_mm': 211.15, 'width_inches': 0.500, 'width_mm': 12.70, 'oval_height_inches': 0.750, 'oval_height_mm': 19.1, 'octagonal_height_inches': 0.690, 'octagonal_height_mm': 17.5, 'flat_width_inches': 0.341, 'flat_width_mm': 8.66, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-47': {'ring_number': 'R-47', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 9.000, 'pitch_diameter_mm': 228.60, 'width_inches': 0.750, 'width_mm': 19.05, 'oval_height_inches': 1.000, 'oval_height_mm': 25.4, 'octagonal_height_inches': 0.940, 'octagonal_height_mm': 23.9, 'flat_width_inches': 0.485, 'flat_width_mm': 12.32, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-48': {'ring_number': 'R-48', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 9.750, 'pitch_diameter_mm': 247.65, 'width_inches': 0.313, 'width_mm': 7.95, 'oval_height_inches': 0.560, 'oval_height_mm': 14.2, 'octagonal_height_inches': 0.500, 'octagonal_height_mm': 12.7, 'flat_width_inches': 0.206, 'flat_width_mm': 5.23, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-49': {'ring_number': 'R-49', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 10.625, 'pitch_diameter_mm': 269.88, 'width_inches': 0.438, 'width_mm': 11.13, 'oval_height_inches': 0.690, 'oval_height_mm': 17.5, 'octagonal_height_inches': 0.630, 'octagonal_height_mm': 16.0, 'flat_width_inches': 0.305, 'flat_width_mm': 7.75, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-50': {'ring_number': 'R-50', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 10.625, 'pitch_diameter_mm': 269.88, 'width_inches': 0.625, 'width_mm': 15.88, 'oval_height_inches': 0.880, 'oval_height_mm': 22.4, 'octagonal_height_inches': 0.810, 'octagonal_height_mm': 20.6, 'flat_width_inches': 0.413, 'flat_width_mm': 10.49, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-51': {'ring_number': 'R-51', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 11.000, 'pitch_diameter_mm': 279.40, 'width_inches': 0.875, 'width_mm': 22.23, 'oval_height_inches': 1.130, 'oval_height_mm': 28.7, 'octagonal_height_inches': 1.060, 'octagonal_height_mm': 26.9, 'flat_width_inches': 0.583, 'flat_width_mm': 14.81, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-52': {'ring_number': 'R-52', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 12.000, 'pitch_diameter_mm': 304.80, 'width_inches': 0.313, 'width_mm': 7.95, 'oval_height_inches': 0.560, 'oval_height_mm': 14.2, 'octagonal_height_inches': 0.500, 'octagonal_height_mm': 12.7, 'flat_width_inches': 0.206, 'flat_width_mm': 5.23, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-53': {'ring_number': 'R-53', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 12.750, 'pitch_diameter_mm': 323.85, 'width_inches': 0.438, 'width_mm': 11.13, 'oval_height_inches': 0.690, 'oval_height_mm': 17.5, 'octagonal_height_inches': 0.630, 'octagonal_height_mm': 16.0, 'flat_width_inches': 0.305, 'flat_width_mm': 7.75, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-54': {'ring_number': 'R-54', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 12.750, 'pitch_diameter_mm': 323.85, 'width_inches': 0.625, 'width_mm': 15.88, 'oval_height_inches': 0.880, 'oval_height_mm': 22.4, 'octagonal_height_inches': 0.810, 'octagonal_height_mm': 20.6, 'flat_width_inches': 0.413, 'flat_width_mm': 10.49, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-55': {'ring_number': 'R-55', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 13.500, 'pitch_diameter_mm': 342.90, 'width_inches': 1.125, 'width_mm': 28.58, 'oval_height_inches': 1.440, 'oval_height_mm': 36.6, 'octagonal_height_inches': 1.380, 'octagonal_height_mm': 35.1, 'flat_width_inches': 0.750, 'flat_width_mm': 19.05, 'radius_inches': 0.090, 'radius_mm': 2.3},
    'R-56': {'ring_number': 'R-56', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 15.000, 'pitch_diameter_mm': 381.00, 'width_inches': 0.313, 'width_mm': 7.95, 'oval_height_inches': 0.560, 'oval_height_mm': 14.2, 'octagonal_height_inches': 0.500, 'octagonal_height_mm': 12.7, 'flat_width_inches': 0.206, 'flat_width_mm': 5.23, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-57': {'ring_number': 'R-57', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 15.000, 'pitch_diameter_mm': 381.00, 'width_inches': 0.438, 'width_mm': 11.13, 'oval_height_inches': 0.690, 'oval_height_mm': 17.5, 'octagonal_height_inches': 0.630, 'octagonal_height_mm': 16.0, 'flat_width_inches': 0.305, 'flat_width_mm': 7.75, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-58': {'ring_number': 'R-58', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 15.000, 'pitch_diameter_mm': 381.00, 'width_inches': 0.875, 'width_mm': 22.23, 'oval_height_inches': 1.130, 'oval_height_mm': 28.7, 'octagonal_height_inches': 1.060, 'octagonal_height_mm': 26.9, 'flat_width_inches': 0.583, 'flat_width_mm': 14.81, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-59': {'ring_number': 'R-59', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 15.625, 'pitch_diameter_mm': 396.88, 'width_inches': 0.313, 'width_mm': 7.95, 'oval_height_inches': 0.560, 'oval_height_mm': 14.2, 'octagonal_height_inches': 0.500, 'octagonal_height_mm': 12.7, 'flat_width_inches': 0.206, 'flat_width_mm': 5.23, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-60': {'ring_number': 'R-60', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 16.000, 'pitch_diameter_mm': 406.40, 'width_inches': 1.250, 'width_mm': 31.75, 'oval_height_inches': 1.560, 'oval_height_mm': 39.6, 'octagonal_height_inches': 1.500, 'octagonal_height_mm': 38.1, 'flat_width_inches': 0.879, 'flat_width_mm': 22.33, 'radius_inches': 0.090, 'radius_mm': 2.3},
    'R-61': {'ring_number': 'R-61', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 16.500, 'pitch_diameter_mm': 419.10, 'width_inches': 0.438, 'width_mm': 11.13, 'oval_height_inches': 0.690, 'oval_height_mm': 17.5, 'octagonal_height_inches': 0.630, 'octagonal_height_mm': 16.0, 'flat_width_inches': 0.305, 'flat_width_mm': 7.75, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-62': {'ring_number': 'R-62', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 16.500, 'pitch_diameter_mm': 419.10, 'width_inches': 0.625, 'width_mm': 15.88, 'oval_height_inches': 0.880, 'oval_height_mm': 22.4, 'octagonal_height_inches': 0.810, 'octagonal_height_mm': 20.6, 'flat_width_inches': 0.413, 'flat_width_mm': 10.49, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-63': {'ring_number': 'R-63', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 16.500, 'pitch_diameter_mm': 419.10, 'width_inches': 1.000, 'width_mm': 25.40, 'oval_height_inches': 1.310, 'oval_height_mm': 33.3, 'octagonal_height_inches': 1.250, 'octagonal_height_mm': 31.8, 'flat_width_inches': 0.681, 'flat_width_mm': 17.30, 'radius_inches': 0.090, 'radius_mm': 2.3},
    'R-64': {'ring_number': 'R-64', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 17.875, 'pitch_diameter_mm': 454.03, 'width_inches': 0.313, 'width_mm': 7.95, 'oval_height_inches': 0.560, 'oval_height_mm': 14.2, 'octagonal_height_inches': 0.500, 'octagonal_height_mm': 12.7, 'flat_width_inches': 0.206, 'flat_width_mm': 5.23, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-65': {'ring_number': 'R-65', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 18.500, 'pitch_diameter_mm': 469.90, 'width_inches': 0.438, 'width_mm': 11.13, 'oval_height_inches': 0.690, 'oval_height_mm': 17.5, 'octagonal_height_inches': 0.630, 'octagonal_height_mm': 16.0, 'flat_width_inches': 0.305, 'flat_width_mm': 7.75, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-66': {'ring_number': 'R-66', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 18.500, 'pitch_diameter_mm': 469.90, 'width_inches': 0.625, 'width_mm': 15.88, 'oval_height_inches': 0.880, 'oval_height_mm': 22.4, 'octagonal_height_inches': 0.810, 'octagonal_height_mm': 20.6, 'flat_width_inches': 0.413, 'flat_width_mm': 10.49, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-67': {'ring_number': 'R-67', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 18.500, 'pitch_diameter_mm': 469.90, 'width_inches': 1.125, 'width_mm': 28.58, 'oval_height_inches': 1.440, 'oval_height_mm': 36.6, 'octagonal_height_inches': 1.380, 'octagonal_height_mm': 35.1, 'flat_width_inches': 0.780, 'flat_width_mm': 19.81, 'radius_inches': 0.090, 'radius_mm': 2.3},
    'R-68': {'ring_number': 'R-68', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 20.375, 'pitch_diameter_mm': 517.53, 'width_inches': 0.313, 'width_mm': 7.95, 'oval_height_inches': 0.560, 'oval_height_mm': 14.2, 'octagonal_height_inches': 0.500, 'octagonal_height_mm': 12.7, 'flat_width_inches': 0.206, 'flat_width_mm': 5.23, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-69': {'ring_number': 'R-69', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 21.000, 'pitch_diameter_mm': 533.40, 'width_inches': 0.438, 'width_mm': 11.13, 'oval_height_inches': 0.690, 'oval_height_mm': 17.5, 'octagonal_height_inches': 0.630, 'octagonal_height_mm': 16.0, 'flat_width_inches': 0.305, 'flat_width_mm': 7.75, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-70': {'ring_number': 'R-70', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 21.000, 'pitch_diameter_mm': 533.40, 'width_inches': 0.750, 'width_mm': 19.05, 'oval_height_inches': 1.000, 'oval_height_mm': 25.4, 'octagonal_height_inches': 0.940, 'octagonal_height_mm': 23.9, 'flat_width_inches': 0.485, 'flat_width_mm': 12.32, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-71': {'ring_number': 'R-71', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 21.000, 'pitch_diameter_mm': 533.40, 'width_inches': 1.125, 'width_mm': 28.58, 'oval_height_inches': 1.440, 'oval_height_mm': 36.6, 'octagonal_height_inches': 1.380, 'octagonal_height_mm': 35.1, 'flat_width_inches': 0.780, 'flat_width_mm': 19.81, 'radius_inches': 0.090, 'radius_mm': 2.3},
    'R-72': {'ring_number': 'R-72', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 22.000, 'pitch_diameter_mm': 558.80, 'width_inches': 0.313, 'width_mm': 7.95, 'oval_height_inches': 0.560, 'oval_height_mm': 14.2, 'octagonal_height_inches': 0.500, 'octagonal_height_mm': 12.7, 'flat_width_inches': 0.206, 'flat_width_mm': 5.23, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-73': {'ring_number': 'R-73', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 23.000, 'pitch_diameter_mm': 584.20, 'width_inches': 0.500, 'width_mm': 12.70, 'oval_height_inches': 0.750, 'oval_height_mm': 19.1, 'octagonal_height_inches': 0.690, 'octagonal_height_mm': 17.5, 'flat_width_inches': 0.341, 'flat_width_mm': 8.66, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-74': {'ring_number': 'R-74', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 23.000, 'pitch_diameter_mm': 584.20, 'width_inches': 0.750, 'width_mm': 19.05, 'oval_height_inches': 1.000, 'oval_height_mm': 25.4, 'octagonal_height_inches': 0.940, 'octagonal_height_mm': 23.9, 'flat_width_inches': 0.485, 'flat_width_mm': 12.32, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-75': {'ring_number': 'R-75', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 23.000, 'pitch_diameter_mm': 584.20, 'width_inches': 1.250, 'width_mm': 31.75, 'oval_height_inches': 1.560, 'oval_height_mm': 39.6, 'octagonal_height_inches': 1.500, 'octagonal_height_mm': 38.1, 'flat_width_inches': 0.879, 'flat_width_mm': 22.33, 'radius_inches': 0.090, 'radius_mm': 2.3},
    'R-76': {'ring_number': 'R-76', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 26.500, 'pitch_diameter_mm': 673.10, 'width_inches': 0.313, 'width_mm': 7.95, 'oval_height_inches': 0.560, 'oval_height_mm': 14.2, 'octagonal_height_inches': 0.500, 'octagonal_height_mm': 12.7, 'flat_width_inches': 0.206, 'flat_width_mm': 5.23, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-77': {'ring_number': 'R-77', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 27.250, 'pitch_diameter_mm': 692.15, 'width_inches': 0.625, 'width_mm': 15.88, 'oval_height_inches': 0.880, 'oval_height_mm': 22.4, 'octagonal_height_inches': 0.810, 'octagonal_height_mm': 20.6, 'flat_width_inches': 0.413, 'flat_width_mm': 10.49, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-78': {'ring_number': 'R-78', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 27.250, 'pitch_diameter_mm': 692.15, 'width_inches': 1.000, 'width_mm': 25.40, 'oval_height_inches': 1.310, 'oval_height_mm': 33.3, 'octagonal_height_inches': 1.250, 'octagonal_height_mm': 31.8, 'flat_width_inches': 0.681, 'flat_width_mm': 17.30, 'radius_inches': 0.090, 'radius_mm': 2.3},
    'R-79': {'ring_number': 'R-79', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 27.250, 'pitch_diameter_mm': 692.15, 'width_inches': 1.375, 'width_mm': 34.93, 'oval_height_inches': 1.750, 'oval_height_mm': 44.5, 'octagonal_height_inches': 1.630, 'octagonal_height_mm': 41.4, 'flat_width_inches': 0.977, 'flat_width_mm': 24.82, 'radius_inches': 0.090, 'radius_mm': 2.3},
    'R-80': {'ring_number': 'R-80', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 24.250, 'pitch_diameter_mm': 615.95, 'width_inches': 0.313, 'width_mm': 7.95, 'oval_height_inches': None, 'oval_height_mm': None, 'octagonal_height_inches': 0.500, 'octagonal_height_mm': 12.7, 'flat_width_inches': 0.206, 'flat_width_mm': 5.23, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-81': {'ring_number': 'R-81', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 25.000, 'pitch_diameter_mm': 635.00, 'width_inches': 0.563, 'width_mm': 14.30, 'oval_height_inches': None, 'oval_height_mm': None, 'octagonal_height_inches': 0.750, 'octagonal_height_mm': 19.1, 'flat_width_inches': 0.377, 'flat_width_mm': 9.58, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-82': {'ring_number': 'R-82', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 2.250, 'pitch_diameter_mm': 57.15, 'width_inches': 0.438, 'width_mm': 11.13, 'oval_height_inches': None, 'oval_height_mm': None, 'octagonal_height_inches': 0.630, 'octagonal_height_mm': 16.0, 'flat_width_inches': 0.305, 'flat_width_mm': 7.75, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-84': {'ring_number': 'R-84', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 2.500, 'pitch_diameter_mm': 63.50, 'width_inches': 0.438, 'width_mm': 11.13, 'oval_height_inches': None, 'oval_height_mm': None, 'octagonal_height_inches': 0.630, 'octagonal_height_mm': 16.0, 'flat_width_inches': 0.305, 'flat_width_mm': 7.75, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-85': {'ring_number': 'R-85', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 3.125, 'pitch_diameter_mm': 79.38, 'width_inches': 0.500, 'width_mm': 12.70, 'oval_height_inches': None, 'oval_height_mm': None, 'octagonal_height_inches': 0.690, 'octagonal_height_mm': 17.5, 'flat_width_inches': 0.341, 'flat_width_mm': 8.66, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-86': {'ring_number': 'R-86', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 3.563, 'pitch_diameter_mm': 90.50, 'width_inches': 0.625, 'width_mm': 15.88, 'oval_height_inches': None, 'oval_height_mm': None, 'octagonal_height_inches': 0.810, 'octagonal_height_mm': 20.6, 'flat_width_inches': 0.413, 'flat_width_mm': 10.49, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-87': {'ring_number': 'R-87', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 3.938, 'pitch_diameter_mm': 100.03, 'width_inches': 0.625, 'width_mm': 15.88, 'oval_height_inches': None, 'oval_height_mm': None, 'octagonal_height_inches': 0.810, 'octagonal_height_mm': 20.6, 'flat_width_inches': 0.413, 'flat_width_mm': 10.49, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-88': {'ring_number': 'R-88', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 4.875, 'pitch_diameter_mm': 123.83, 'width_inches': 0.750, 'width_mm': 19.05, 'oval_height_inches': None, 'oval_height_mm': None, 'octagonal_height_inches': 0.940, 'octagonal_height_mm': 23.9, 'flat_width_inches': 0.485, 'flat_width_mm': 12.32, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-89': {'ring_number': 'R-89', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 4.500, 'pitch_diameter_mm': 114.30, 'width_inches': 0.750, 'width_mm': 19.05, 'oval_height_inches': None, 'oval_height_mm': None, 'octagonal_height_inches': 0.940, 'octagonal_height_mm': 23.9, 'flat_width_inches': 0.485, 'flat_width_mm': 12.32, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-90': {'ring_number': 'R-90', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 6.125, 'pitch_diameter_mm': 155.58, 'width_inches': 0.875, 'width_mm': 22.23, 'oval_height_inches': None, 'oval_height_mm': None, 'octagonal_height_inches': 1.060, 'octagonal_height_mm': 26.9, 'flat_width_inches': 0.583, 'flat_width_mm': 14.81, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-91': {'ring_number': 'R-91', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 10.250, 'pitch_diameter_mm': 260.35, 'width_inches': 1.250, 'width_mm': 31.75, 'oval_height_inches': None, 'oval_height_mm': None, 'octagonal_height_inches': 1.500, 'octagonal_height_mm': 38.1, 'flat_width_inches': 0.879, 'flat_width_mm': 22.33, 'radius_inches': 0.090, 'radius_mm': 2.3},
    'R-92': {'ring_number': 'R-92', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 9.000, 'pitch_diameter_mm': 228.60, 'width_inches': 0.438, 'width_mm': 11.13, 'oval_height_inches': 0.690, 'oval_height_mm': None, 'octagonal_height_inches': 0.630, 'octagonal_height_mm': 16.0, 'flat_width_inches': 0.305, 'flat_width_mm': 7.75, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-93': {'ring_number': 'R-93', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 29.500, 'pitch_diameter_mm': 749.30, 'width_inches': 0.750, 'width_mm': 19.05, 'oval_height_inches': None, 'oval_height_mm': None, 'octagonal_height_inches': 0.940, 'octagonal_height_mm': 23.9, 'flat_width_inches': 0.485, 'flat_width_mm': 12.32, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-94': {'ring_number': 'R-94', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 31.500, 'pitch_diameter_mm': 800.10, 'width_inches': 0.750, 'width_mm': 19.05, 'oval_height_inches': None, 'oval_height_mm': None, 'octagonal_height_inches': 0.940, 'octagonal_height_mm': 23.9, 'flat_width_inches': 0.485, 'flat_width_mm': 12.32, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-95': {'ring_number': 'R-95', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 33.750, 'pitch_diameter_mm': 857.25, 'width_inches': 0.750, 'width_mm': 19.05, 'oval_height_inches': None, 'oval_height_mm': None, 'octagonal_height_inches': 0.940, 'octagonal_height_mm': 23.9, 'flat_width_inches': 0.485, 'flat_width_mm': 12.32, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-96': {'ring_number': 'R-96', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 36.000, 'pitch_diameter_mm': 914.40, 'width_inches': 0.875, 'width_mm': 22.23, 'oval_height_inches': None, 'oval_height_mm': None, 'octagonal_height_inches': 1.060, 'octagonal_height_mm': 26.9, 'flat_width_inches': 0.583, 'flat_width_mm': 14.81, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-97': {'ring_number': 'R-97', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 38.000, 'pitch_diameter_mm': 965.20, 'width_inches': 0.875, 'width_mm': 22.23, 'oval_height_inches': None, 'oval_height_mm': None, 'octagonal_height_inches': 1.060, 'octagonal_height_mm': 26.9, 'flat_width_inches': 0.583, 'flat_width_mm': 14.81, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-98': {'ring_number': 'R-98', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 40.250, 'pitch_diameter_mm': 1022.35, 'width_inches': 0.875, 'width_mm': 22.23, 'oval_height_inches': None, 'oval_height_mm': None, 'octagonal_height_inches': 1.060, 'octagonal_height_mm': 26.9, 'flat_width_inches': 0.583, 'flat_width_mm': 14.81, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-99': {'ring_number': 'R-99', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 9.250, 'pitch_diameter_mm': 234.95, 'width_inches': 0.438, 'width_mm': 11.13, 'oval_height_inches': None, 'oval_height_mm': None, 'octagonal_height_inches': 0.630, 'octagonal_height_mm': 16.0, 'flat_width_inches': 0.305, 'flat_width_mm': 7.75, 'radius_inches': 0.060, 'radius_mm': 1.5},
    'R-100': {'ring_number': 'R-100', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 29.500, 'pitch_diameter_mm': 749.30, 'width_inches': 1.125, 'width_mm': 28.58, 'oval_height_inches': None, 'oval_height_mm': None, 'octagonal_height_inches': 1.380, 'octagonal_height_mm': 35.1, 'flat_width_inches': 0.780, 'flat_width_mm': 19.81, 'radius_inches': 0.090, 'radius_mm': 2.3},
    'R-101': {'ring_number': 'R-101', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 31.500, 'pitch_diameter_mm': 800.10, 'width_inches': 1.250, 'width_mm': 31.75, 'oval_height_inches': None, 'oval_height_mm': None, 'octagonal_height_inches': 1.500, 'octagonal_height_mm': 38.1, 'flat_width_inches': 0.879, 'flat_width_mm': 22.33, 'radius_inches': 0.090, 'radius_mm': 2.3},
    'R-102': {'ring_number': 'R-102', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 33.750, 'pitch_diameter_mm': 857.25, 'width_inches': 1.250, 'width_mm': 31.75, 'oval_height_inches': None, 'oval_height_mm': None, 'octagonal_height_inches': 1.500, 'octagonal_height_mm': 38.1, 'flat_width_inches': 0.879, 'flat_width_mm': 22.33, 'radius_inches': 0.090, 'radius_mm': 2.3},
    'R-103': {'ring_number': 'R-103', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 36.000, 'pitch_diameter_mm': 914.40, 'width_inches': 1.250, 'width_mm': 31.75, 'oval_height_inches': None, 'oval_height_mm': None, 'octagonal_height_inches': 1.500, 'octagonal_height_mm': 38.1, 'flat_width_inches': 0.879, 'flat_width_mm': 22.33, 'radius_inches': 0.090, 'radius_mm': 2.3},
    'R-104': {'ring_number': 'R-104', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 38.000, 'pitch_diameter_mm': 965.20, 'width_inches': 1.375, 'width_mm': 34.93, 'oval_height_inches': None, 'oval_height_mm': None, 'octagonal_height_inches': 1.630, 'octagonal_height_mm': 41.4, 'flat_width_inches': 0.977, 'flat_width_mm': 24.82, 'radius_inches': 0.090, 'radius_mm': 2.3},
    'R-105': {'ring_number': 'R-105', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 40.250, 'pitch_diameter_mm': 1022.35, 'width_inches': 1.375, 'width_mm': 34.93, 'oval_height_inches': None, 'oval_height_mm': None, 'octagonal_height_inches': 1.630, 'octagonal_height_mm': 41.4, 'flat_width_inches': 0.977, 'flat_width_mm': 24.82, 'radius_inches': 0.090, 'radius_mm': 2.3},
}

# API 6A Type RX Ring Joint Gaskets (for ASME B16.5 and API 6A Type 6B Flanges)
# Octagonal profile only, improved design over Type R
RING_JOINT_TYPE_RX_GASKETS = {
    'RX-20': {'ring_number': 'RX-20', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 3.000, 'pitch_diameter_mm': 76.20, 'width_inches': 0.344, 'width_mm': 8.74, 'flat_width_inches': 0.182, 'flat_width_mm': 4.62, 'outside_bevel_height_inches': 0.125, 'outside_bevel_height_mm': 3.18, 'ring_height_inches': 0.750, 'ring_height_mm': 19.05, 'radius_inches': 0.060, 'radius_mm': 1.5, 'hole_size_inches': None, 'hole_size_mm': None},
    'RX-23': {'ring_number': 'RX-23', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 3.672, 'pitch_diameter_mm': 93.27, 'width_inches': 0.469, 'width_mm': 11.91, 'flat_width_inches': 0.254, 'flat_width_mm': 6.45, 'outside_bevel_height_inches': 0.167, 'outside_bevel_height_mm': 4.24, 'ring_height_inches': 1.000, 'ring_height_mm': 25.40, 'radius_inches': 0.060, 'radius_mm': 1.5, 'hole_size_inches': None, 'hole_size_mm': None},
    'RX-24': {'ring_number': 'RX-24', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 4.172, 'pitch_diameter_mm': 105.97, 'width_inches': 0.469, 'width_mm': 11.91, 'flat_width_inches': 0.254, 'flat_width_mm': 6.45, 'outside_bevel_height_inches': 0.167, 'outside_bevel_height_mm': 4.24, 'ring_height_inches': 1.000, 'ring_height_mm': 25.40, 'radius_inches': 0.060, 'radius_mm': 1.5, 'hole_size_inches': None, 'hole_size_mm': None},
    'RX-25': {'ring_number': 'RX-25', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 4.313, 'pitch_diameter_mm': 109.55, 'width_inches': 0.344, 'width_mm': 8.74, 'flat_width_inches': 0.182, 'flat_width_mm': 4.62, 'outside_bevel_height_inches': 0.125, 'outside_bevel_height_mm': 3.18, 'ring_height_inches': 0.750, 'ring_height_mm': 19.05, 'radius_inches': 0.060, 'radius_mm': 1.5, 'hole_size_inches': None, 'hole_size_mm': None},
    'RX-26': {'ring_number': 'RX-26', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 4.406, 'pitch_diameter_mm': 111.91, 'width_inches': 0.469, 'width_mm': 11.91, 'flat_width_inches': 0.254, 'flat_width_mm': 6.45, 'outside_bevel_height_inches': 0.167, 'outside_bevel_height_mm': 4.24, 'ring_height_inches': 1.000, 'ring_height_mm': 25.40, 'radius_inches': 0.060, 'radius_mm': 1.5, 'hole_size_inches': None, 'hole_size_mm': None},
    'RX-27': {'ring_number': 'RX-27', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 4.656, 'pitch_diameter_mm': 118.26, 'width_inches': 0.469, 'width_mm': 11.91, 'flat_width_inches': 0.254, 'flat_width_mm': 6.45, 'outside_bevel_height_inches': 0.167, 'outside_bevel_height_mm': 4.24, 'ring_height_inches': 1.000, 'ring_height_mm': 25.40, 'radius_inches': 0.060, 'radius_mm': 1.5, 'hole_size_inches': None, 'hole_size_mm': None},
    'RX-31': {'ring_number': 'RX-31', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 5.297, 'pitch_diameter_mm': 134.54, 'width_inches': 0.469, 'width_mm': 11.91, 'flat_width_inches': 0.254, 'flat_width_mm': 6.45, 'outside_bevel_height_inches': 0.167, 'outside_bevel_height_mm': 4.24, 'ring_height_inches': 1.000, 'ring_height_mm': 25.40, 'radius_inches': 0.060, 'radius_mm': 1.5, 'hole_size_inches': None, 'hole_size_mm': None},
    'RX-35': {'ring_number': 'RX-35', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 5.797, 'pitch_diameter_mm': 147.24, 'width_inches': 0.469, 'width_mm': 11.91, 'flat_width_inches': 0.254, 'flat_width_mm': 6.45, 'outside_bevel_height_inches': 0.167, 'outside_bevel_height_mm': 4.24, 'ring_height_inches': 1.000, 'ring_height_mm': 25.40, 'radius_inches': 0.060, 'radius_mm': 1.5, 'hole_size_inches': None, 'hole_size_mm': None},
    'RX-37': {'ring_number': 'RX-37', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 6.297, 'pitch_diameter_mm': 159.94, 'width_inches': 0.469, 'width_mm': 11.91, 'flat_width_inches': 0.254, 'flat_width_mm': 6.45, 'outside_bevel_height_inches': 0.167, 'outside_bevel_height_mm': 4.24, 'ring_height_inches': 1.000, 'ring_height_mm': 25.40, 'radius_inches': 0.060, 'radius_mm': 1.5, 'hole_size_inches': None, 'hole_size_mm': None},
    'RX-39': {'ring_number': 'RX-39', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 6.797, 'pitch_diameter_mm': 172.64, 'width_inches': 0.469, 'width_mm': 11.91, 'flat_width_inches': 0.254, 'flat_width_mm': 6.45, 'outside_bevel_height_inches': 0.167, 'outside_bevel_height_mm': 4.24, 'ring_height_inches': 1.000, 'ring_height_mm': 25.40, 'radius_inches': 0.060, 'radius_mm': 1.5, 'hole_size_inches': None, 'hole_size_mm': None},
    'RX-41': {'ring_number': 'RX-41', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 7.547, 'pitch_diameter_mm': 191.69, 'width_inches': 0.469, 'width_mm': 11.91, 'flat_width_inches': 0.254, 'flat_width_mm': 6.45, 'outside_bevel_height_inches': 0.167, 'outside_bevel_height_mm': 4.24, 'ring_height_inches': 1.000, 'ring_height_mm': 25.40, 'radius_inches': 0.060, 'radius_mm': 1.5, 'hole_size_inches': None, 'hole_size_mm': None},
    'RX-44': {'ring_number': 'RX-44', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 8.047, 'pitch_diameter_mm': 204.39, 'width_inches': 0.469, 'width_mm': 11.91, 'flat_width_inches': 0.254, 'flat_width_mm': 6.45, 'outside_bevel_height_inches': 0.167, 'outside_bevel_height_mm': 4.24, 'ring_height_inches': 1.000, 'ring_height_mm': 25.40, 'radius_inches': 0.060, 'radius_mm': 1.5, 'hole_size_inches': None, 'hole_size_mm': None},
    'RX-45': {'ring_number': 'RX-45', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 8.734, 'pitch_diameter_mm': 221.84, 'width_inches': 0.469, 'width_mm': 11.91, 'flat_width_inches': 0.254, 'flat_width_mm': 6.45, 'outside_bevel_height_inches': 0.167, 'outside_bevel_height_mm': 4.24, 'ring_height_inches': 1.000, 'ring_height_mm': 25.40, 'radius_inches': 0.060, 'radius_mm': 1.5, 'hole_size_inches': None, 'hole_size_mm': None},
    'RX-46': {'ring_number': 'RX-46', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 8.750, 'pitch_diameter_mm': 222.25, 'width_inches': 0.531, 'width_mm': 13.49, 'flat_width_inches': 0.263, 'flat_width_mm': 6.68, 'outside_bevel_height_inches': 0.188, 'outside_bevel_height_mm': 4.78, 'ring_height_inches': 1.125, 'ring_height_mm': 28.58, 'radius_inches': 0.060, 'radius_mm': 1.5, 'hole_size_inches': None, 'hole_size_mm': None},
    'RX-47': {'ring_number': 'RX-47', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 9.656, 'pitch_diameter_mm': 245.26, 'width_inches': 0.781, 'width_mm': 19.84, 'flat_width_inches': 0.407, 'flat_width_mm': 10.34, 'outside_bevel_height_inches': 0.271, 'outside_bevel_height_mm': 6.88, 'ring_height_inches': 1.625, 'ring_height_mm': 41.28, 'radius_inches': 0.090, 'radius_mm': 2.3, 'hole_size_inches': None, 'hole_size_mm': None},
    'RX-49': {'ring_number': 'RX-49', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 11.047, 'pitch_diameter_mm': 280.59, 'width_inches': 0.469, 'width_mm': 11.91, 'flat_width_inches': 0.254, 'flat_width_mm': 6.45, 'outside_bevel_height_inches': 0.167, 'outside_bevel_height_mm': 4.24, 'ring_height_inches': 1.000, 'ring_height_mm': 25.40, 'radius_inches': 0.060, 'radius_mm': 1.5, 'hole_size_inches': None, 'hole_size_mm': None},
    'RX-50': {'ring_number': 'RX-50', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 11.156, 'pitch_diameter_mm': 283.36, 'width_inches': 0.656, 'width_mm': 16.66, 'flat_width_inches': 0.335, 'flat_width_mm': 8.51, 'outside_bevel_height_inches': 0.208, 'outside_bevel_height_mm': 5.28, 'ring_height_inches': 1.250, 'ring_height_mm': 31.75, 'radius_inches': 0.060, 'radius_mm': 1.5, 'hole_size_inches': None, 'hole_size_mm': None},
    'RX-53': {'ring_number': 'RX-53', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 13.172, 'pitch_diameter_mm': 334.57, 'width_inches': 0.469, 'width_mm': 11.91, 'flat_width_inches': 0.254, 'flat_width_mm': 6.45, 'outside_bevel_height_inches': 0.167, 'outside_bevel_height_mm': 4.24, 'ring_height_inches': 1.000, 'ring_height_mm': 25.40, 'radius_inches': 0.060, 'radius_mm': 1.5, 'hole_size_inches': None, 'hole_size_mm': None},
    'RX-54': {'ring_number': 'RX-54', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 13.281, 'pitch_diameter_mm': 337.34, 'width_inches': 0.656, 'width_mm': 16.66, 'flat_width_inches': 0.335, 'flat_width_mm': 8.51, 'outside_bevel_height_inches': 0.208, 'outside_bevel_height_mm': 5.28, 'ring_height_inches': 1.250, 'ring_height_mm': 31.75, 'radius_inches': 0.060, 'radius_mm': 1.5, 'hole_size_inches': None, 'hole_size_mm': None},
    'RX-57': {'ring_number': 'RX-57', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 15.422, 'pitch_diameter_mm': 391.72, 'width_inches': 0.469, 'width_mm': 11.91, 'flat_width_inches': 0.254, 'flat_width_mm': 6.45, 'outside_bevel_height_inches': 0.167, 'outside_bevel_height_mm': 4.24, 'ring_height_inches': 1.000, 'ring_height_mm': 25.40, 'radius_inches': 0.060, 'radius_mm': 1.5, 'hole_size_inches': None, 'hole_size_mm': None},
    'RX-63': {'ring_number': 'RX-63', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 17.391, 'pitch_diameter_mm': 441.73, 'width_inches': 1.063, 'width_mm': 27.00, 'flat_width_inches': 0.582, 'flat_width_mm': 14.78, 'outside_bevel_height_inches': 0.333, 'outside_bevel_height_mm': 8.46, 'ring_height_inches': 2.000, 'ring_height_mm': 50.80, 'radius_inches': 0.090, 'radius_mm': 2.3, 'hole_size_inches': None, 'hole_size_mm': None},
    'RX-65': {'ring_number': 'RX-65', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 18.922, 'pitch_diameter_mm': 480.62, 'width_inches': 0.469, 'width_mm': 11.91, 'flat_width_inches': 0.254, 'flat_width_mm': 6.45, 'outside_bevel_height_inches': 0.167, 'outside_bevel_height_mm': 4.24, 'ring_height_inches': 1.000, 'ring_height_mm': 25.40, 'radius_inches': 0.060, 'radius_mm': 1.5, 'hole_size_inches': None, 'hole_size_mm': None},
    'RX-66': {'ring_number': 'RX-66', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 18.031, 'pitch_diameter_mm': 457.99, 'width_inches': 0.656, 'width_mm': 16.66, 'flat_width_inches': 0.335, 'flat_width_mm': 8.51, 'outside_bevel_height_inches': 0.208, 'outside_bevel_height_mm': 5.28, 'ring_height_inches': 1.250, 'ring_height_mm': 31.75, 'radius_inches': 0.060, 'radius_mm': 1.5, 'hole_size_inches': None, 'hole_size_mm': None},
    'RX-69': {'ring_number': 'RX-69', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 21.422, 'pitch_diameter_mm': 544.12, 'width_inches': 0.469, 'width_mm': 11.91, 'flat_width_inches': 0.254, 'flat_width_mm': 6.45, 'outside_bevel_height_inches': 0.167, 'outside_bevel_height_mm': 4.24, 'ring_height_inches': 1.000, 'ring_height_mm': 25.40, 'radius_inches': 0.060, 'radius_mm': 1.5, 'hole_size_inches': None, 'hole_size_mm': None},
    'RX-70': {'ring_number': 'RX-70', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 21.656, 'pitch_diameter_mm': 550.06, 'width_inches': 0.781, 'width_mm': 19.84, 'flat_width_inches': 0.407, 'flat_width_mm': 10.34, 'outside_bevel_height_inches': 0.271, 'outside_bevel_height_mm': 6.88, 'ring_height_inches': 1.625, 'ring_height_mm': 41.28, 'radius_inches': 0.090, 'radius_mm': 2.3, 'hole_size_inches': None, 'hole_size_mm': None},
    'RX-73': {'ring_number': 'RX-73', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 23.469, 'pitch_diameter_mm': 596.11, 'width_inches': 0.531, 'width_mm': 13.49, 'flat_width_inches': 0.263, 'flat_width_mm': 6.68, 'outside_bevel_height_inches': 0.208, 'outside_bevel_height_mm': 5.28, 'ring_height_inches': 1.250, 'ring_height_mm': 31.75, 'radius_inches': 0.060, 'radius_mm': 1.5, 'hole_size_inches': None, 'hole_size_mm': None},
    'RX-74': {'ring_number': 'RX-74', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 23.656, 'pitch_diameter_mm': 600.86, 'width_inches': 0.781, 'width_mm': 19.84, 'flat_width_inches': 0.407, 'flat_width_mm': 10.34, 'outside_bevel_height_inches': 0.271, 'outside_bevel_height_mm': 6.88, 'ring_height_inches': 1.625, 'ring_height_mm': 41.28, 'radius_inches': 0.090, 'radius_mm': 2.3, 'hole_size_inches': None, 'hole_size_mm': None},
    'RX-82': {'ring_number': 'RX-82', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 2.672, 'pitch_diameter_mm': 67.87, 'width_inches': 0.469, 'width_mm': 11.91, 'flat_width_inches': 0.254, 'flat_width_mm': 6.45, 'outside_bevel_height_inches': 0.167, 'outside_bevel_height_mm': 4.24, 'ring_height_inches': 1.000, 'ring_height_mm': 25.40, 'radius_inches': 0.060, 'radius_mm': 1.5, 'hole_size_inches': 0.060, 'hole_size_mm': 1.5},
    'RX-84': {'ring_number': 'RX-84', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 2.922, 'pitch_diameter_mm': 74.22, 'width_inches': 0.469, 'width_mm': 11.91, 'flat_width_inches': 0.254, 'flat_width_mm': 6.45, 'outside_bevel_height_inches': 0.167, 'outside_bevel_height_mm': 4.24, 'ring_height_inches': 1.000, 'ring_height_mm': 25.40, 'radius_inches': 0.060, 'radius_mm': 1.5, 'hole_size_inches': 0.060, 'hole_size_mm': 1.5},
    'RX-85': {'ring_number': 'RX-85', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 3.547, 'pitch_diameter_mm': 90.09, 'width_inches': 0.531, 'width_mm': 13.49, 'flat_width_inches': 0.263, 'flat_width_mm': 6.68, 'outside_bevel_height_inches': 0.167, 'outside_bevel_height_mm': 4.24, 'ring_height_inches': 1.000, 'ring_height_mm': 25.40, 'radius_inches': 0.060, 'radius_mm': 1.5, 'hole_size_inches': 0.060, 'hole_size_mm': 1.5},
    'RX-86': {'ring_number': 'RX-86', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 4.078, 'pitch_diameter_mm': 103.58, 'width_inches': 0.594, 'width_mm': 15.09, 'flat_width_inches': 0.335, 'flat_width_mm': 8.51, 'outside_bevel_height_inches': 0.188, 'outside_bevel_height_mm': 4.78, 'ring_height_inches': 1.125, 'ring_height_mm': 28.58, 'radius_inches': 0.060, 'radius_mm': 1.5, 'hole_size_inches': 0.090, 'hole_size_mm': 2.3},
    'RX-87': {'ring_number': 'RX-87', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 4.453, 'pitch_diameter_mm': 113.11, 'width_inches': 0.594, 'width_mm': 15.09, 'flat_width_inches': 0.335, 'flat_width_mm': 8.51, 'outside_bevel_height_inches': 0.188, 'outside_bevel_height_mm': 4.78, 'ring_height_inches': 1.125, 'ring_height_mm': 28.58, 'radius_inches': 0.060, 'radius_mm': 1.5, 'hole_size_inches': 0.090, 'hole_size_mm': 2.3},
    'RX-88': {'ring_number': 'RX-88', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 5.484, 'pitch_diameter_mm': 139.29, 'width_inches': 0.688, 'width_mm': 17.48, 'flat_width_inches': 0.407, 'flat_width_mm': 10.34, 'outside_bevel_height_inches': 0.208, 'outside_bevel_height_mm': 5.28, 'ring_height_inches': 1.250, 'ring_height_mm': 31.75, 'radius_inches': 0.060, 'radius_mm': 1.5, 'hole_size_inches': 0.120, 'hole_size_mm': 3.0},
    'RX-89': {'ring_number': 'RX-89', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 5.109, 'pitch_diameter_mm': 129.77, 'width_inches': 0.719, 'width_mm': 18.26, 'flat_width_inches': 0.407, 'flat_width_mm': 10.34, 'outside_bevel_height_inches': 0.208, 'outside_bevel_height_mm': 5.28, 'ring_height_inches': 1.250, 'ring_height_mm': 31.75, 'radius_inches': 0.060, 'radius_mm': 1.5, 'hole_size_inches': 0.120, 'hole_size_mm': 3.0},
    'RX-90': {'ring_number': 'RX-90', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 6.875, 'pitch_diameter_mm': 174.63, 'width_inches': 0.781, 'width_mm': 19.84, 'flat_width_inches': 0.479, 'flat_width_mm': 12.17, 'outside_bevel_height_inches': 0.292, 'outside_bevel_height_mm': 7.42, 'ring_height_inches': 1.750, 'ring_height_mm': 44.45, 'radius_inches': 0.090, 'radius_mm': 2.3, 'hole_size_inches': 0.120, 'hole_size_mm': 3.0},
    'RX-91': {'ring_number': 'RX-91', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 11.297, 'pitch_diameter_mm': 286.94, 'width_inches': 1.188, 'width_mm': 30.18, 'flat_width_inches': 0.780, 'flat_width_mm': 19.81, 'outside_bevel_height_inches': 0.297, 'outside_bevel_height_mm': 7.54, 'ring_height_inches': 1.781, 'ring_height_mm': 45.24, 'radius_inches': 0.090, 'radius_mm': 2.3, 'hole_size_inches': 0.120, 'hole_size_mm': 3.0},
    'RX-99': {'ring_number': 'RX-99', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 9.672, 'pitch_diameter_mm': 245.67, 'width_inches': 0.469, 'width_mm': 11.91, 'flat_width_inches': 0.254, 'flat_width_mm': 6.45, 'outside_bevel_height_inches': 0.167, 'outside_bevel_height_mm': 4.24, 'ring_height_inches': 1.000, 'ring_height_mm': 25.40, 'radius_inches': 0.060, 'radius_mm': 1.5, 'hole_size_inches': None, 'hole_size_mm': None},
    'RX-201': {'ring_number': 'RX-201', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 2.026, 'pitch_diameter_mm': 51.46, 'width_inches': 0.226, 'width_mm': 5.74, 'flat_width_inches': 0.126, 'flat_width_mm': 3.20, 'outside_bevel_height_inches': 0.057, 'outside_bevel_height_mm': 1.45, 'ring_height_inches': 0.445, 'ring_height_mm': 11.30, 'radius_inches': 0.020, 'radius_mm': 0.5, 'hole_size_inches': None, 'hole_size_mm': None},
    'RX-205': {'ring_number': 'RX-205', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 2.453, 'pitch_diameter_mm': 62.31, 'width_inches': 0.219, 'width_mm': 5.56, 'flat_width_inches': 0.120, 'flat_width_mm': 3.05, 'outside_bevel_height_inches': 0.072, 'outside_bevel_height_mm': 1.83, 'ring_height_inches': 0.437, 'ring_height_mm': 11.10, 'radius_inches': 0.020, 'radius_mm': 0.5, 'hole_size_inches': None, 'hole_size_mm': None},
    'RX-210': {'ring_number': 'RX-210', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 3.844, 'pitch_diameter_mm': 97.64, 'width_inches': 0.375, 'width_mm': 9.53, 'flat_width_inches': 0.231, 'flat_width_mm': 5.87, 'outside_bevel_height_inches': 0.125, 'outside_bevel_height_mm': 3.18, 'ring_height_inches': 0.750, 'ring_height_mm': 19.05, 'radius_inches': 0.030, 'radius_mm': 0.8, 'hole_size_inches': None, 'hole_size_mm': None},
    'RX-215': {'ring_number': 'RX-215', 'gasket_type': 'ring_joint', 'pitch_diameter_inches': 5.547, 'pitch_diameter_mm': 140.89, 'width_inches': 0.469, 'width_mm': 11.91, 'flat_width_inches': 0.210, 'flat_width_mm': 5.33, 'outside_bevel_height_inches': 0.167, 'outside_bevel_height_mm': 4.24, 'ring_height_inches': 1.000, 'ring_height_mm': 25.40, 'radius_inches': 0.060, 'radius_mm': 1.5, 'hole_size_inches': None, 'hole_size_mm': None},
}

# ASME B16.47 Series A Class 150 Flat Ring Gaskets (for RF Flanges)
B1647A_CLASS150_FLAT_RING_GASKETS = {
    '26': {'nps': '26', 'class': 150, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 25.98, 'id_mm': 660, 'od_inches': 30.51, 'od_mm': 775},
    '28': {'nps': '28', 'class': 150, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 27.99, 'id_mm': 711, 'od_inches': 32.76, 'od_mm': 832},
    '30': {'nps': '30', 'class': 150, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 30.00, 'id_mm': 762, 'od_inches': 34.76, 'od_mm': 883},
    '32': {'nps': '32', 'class': 150, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 32.01, 'id_mm': 813, 'od_inches': 37.01, 'od_mm': 940},
    '34': {'nps': '34', 'class': 150, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 34.02, 'id_mm': 864, 'od_inches': 39.02, 'od_mm': 991},
    '36': {'nps': '36', 'class': 150, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 35.98, 'id_mm': 914, 'od_inches': 41.26, 'od_mm': 1048},
    '38': {'nps': '38', 'class': 150, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 37.99, 'id_mm': 965, 'od_inches': 43.74, 'od_mm': 1111},
    '40': {'nps': '40', 'class': 150, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 40.00, 'id_mm': 1016, 'od_inches': 45.75, 'od_mm': 1162},
    '42': {'nps': '42', 'class': 150, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 42.01, 'id_mm': 1067, 'od_inches': 48.00, 'od_mm': 1219},
    '44': {'nps': '44', 'class': 150, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 44.02, 'id_mm': 1118, 'od_inches': 50.24, 'od_mm': 1276},
    '46': {'nps': '46', 'class': 150, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 45.98, 'id_mm': 1168, 'od_inches': 52.24, 'od_mm': 1327},
    '48': {'nps': '48', 'class': 150, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 48.00, 'id_mm': 1219, 'od_inches': 54.49, 'od_mm': 1384},
    '50': {'nps': '50', 'class': 150, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 50.00, 'id_mm': 1270, 'od_inches': 56.50, 'od_mm': 1435},
    '52': {'nps': '52', 'class': 150, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 52.01, 'id_mm': 1321, 'od_inches': 58.74, 'od_mm': 1492},
    '54': {'nps': '54', 'class': 150, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 54.02, 'id_mm': 1372, 'od_inches': 60.98, 'od_mm': 1549},
    '56': {'nps': '56', 'class': 150, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 55.98, 'id_mm': 1422, 'od_inches': 63.27, 'od_mm': 1607},
    '58': {'nps': '58', 'class': 150, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 58.00, 'id_mm': 1473, 'od_inches': 65.51, 'od_mm': 1664},
    '60': {'nps': '60', 'class': 150, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 60.00, 'id_mm': 1524, 'od_inches': 67.52, 'od_mm': 1715},
}

# ASME B16.47 Series A Class 300 Flat Ring Gaskets (for RF Flanges)
B1647A_CLASS300_FLAT_RING_GASKETS = {
    '26': {'nps': '26', 'class': 300, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 25.98, 'id_mm': 660, 'od_inches': 32.87, 'od_mm': 835},
    '28': {'nps': '28', 'class': 300, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 27.99, 'id_mm': 711, 'od_inches': 35.39, 'od_mm': 899},
    '30': {'nps': '30', 'class': 300, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 30.00, 'id_mm': 762, 'od_inches': 37.52, 'od_mm': 953},
    '32': {'nps': '32', 'class': 300, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 32.01, 'id_mm': 813, 'od_inches': 39.61, 'od_mm': 1006},
    '34': {'nps': '34', 'class': 300, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 34.02, 'id_mm': 864, 'od_inches': 41.61, 'od_mm': 1057},
    '36': {'nps': '36', 'class': 300, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 35.98, 'id_mm': 914, 'od_inches': 44.02, 'od_mm': 1118},
    '38': {'nps': '38', 'class': 300, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 37.99, 'id_mm': 965, 'od_inches': 41.50, 'od_mm': 1054},
    '40': {'nps': '40', 'class': 300, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 40.00, 'id_mm': 1016, 'od_inches': 43.86, 'od_mm': 1114},
    '42': {'nps': '42', 'class': 300, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 42.01, 'id_mm': 1067, 'od_inches': 45.87, 'od_mm': 1165},
    '44': {'nps': '44', 'class': 300, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 44.02, 'id_mm': 1118, 'od_inches': 48.00, 'od_mm': 1219},
    '46': {'nps': '46', 'class': 300, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 45.98, 'id_mm': 1168, 'od_inches': 50.12, 'od_mm': 1273},
    '48': {'nps': '48', 'class': 300, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 48.00, 'id_mm': 1219, 'od_inches': 52.13, 'od_mm': 1324},
    '50': {'nps': '50', 'class': 300, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 50.00, 'id_mm': 1270, 'od_inches': 54.25, 'od_mm': 1378},
    '52': {'nps': '52', 'class': 300, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 52.01, 'id_mm': 1321, 'od_inches': 56.26, 'od_mm': 1429},
    '54': {'nps': '54', 'class': 300, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 54.02, 'id_mm': 1372, 'od_inches': 58.74, 'od_mm': 1492},
    '56': {'nps': '56', 'class': 300, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 55.98, 'id_mm': 1422, 'od_inches': 60.75, 'od_mm': 1543},
    '58': {'nps': '58', 'class': 300, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 58.00, 'id_mm': 1473, 'od_inches': 62.76, 'od_mm': 1594},
    '60': {'nps': '60', 'class': 300, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 60.00, 'id_mm': 1524, 'od_inches': 64.76, 'od_mm': 1645},
}

# ASME B16.47 Series A Class 400 Flat Ring Gaskets (for RF Flanges)
B1647A_CLASS400_FLAT_RING_GASKETS = {
    '26': {'nps': '26', 'class': 400, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 25.98, 'id_mm': 660, 'od_inches': 32.76, 'od_mm': 832},
    '28': {'nps': '28', 'class': 400, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 27.99, 'id_mm': 711, 'od_inches': 35.12, 'od_mm': 892},
    '30': {'nps': '30', 'class': 400, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 30.00, 'id_mm': 762, 'od_inches': 37.24, 'od_mm': 946},
    '32': {'nps': '32', 'class': 400, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 32.01, 'id_mm': 813, 'od_inches': 39.49, 'od_mm': 1003},
    '34': {'nps': '34', 'class': 400, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 34.02, 'id_mm': 864, 'od_inches': 41.50, 'od_mm': 1054},
    '36': {'nps': '36', 'class': 400, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 35.98, 'id_mm': 914, 'od_inches': 44.02, 'od_mm': 1118},
    '38': {'nps': '38', 'class': 400, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 37.99, 'id_mm': 965, 'od_inches': 42.24, 'od_mm': 1073},
    '40': {'nps': '40', 'class': 400, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 40.00, 'id_mm': 1016, 'od_inches': 44.37, 'od_mm': 1127},
    '42': {'nps': '42', 'class': 400, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 42.01, 'id_mm': 1067, 'od_inches': 46.38, 'od_mm': 1178},
    '44': {'nps': '44', 'class': 400, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 44.02, 'id_mm': 1118, 'od_inches': 48.50, 'od_mm': 1232},
    '46': {'nps': '46', 'class': 400, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 45.98, 'id_mm': 1168, 'od_inches': 50.75, 'od_mm': 1289},
    '48': {'nps': '48', 'class': 400, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 48.00, 'id_mm': 1219, 'od_inches': 53.00, 'od_mm': 1346},
    '50': {'nps': '50', 'class': 400, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 50.00, 'id_mm': 1270, 'od_inches': 55.24, 'od_mm': 1403},
    '52': {'nps': '52', 'class': 400, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 52.01, 'id_mm': 1321, 'od_inches': 57.24, 'od_mm': 1454},
    '54': {'nps': '54', 'class': 400, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 54.02, 'id_mm': 1372, 'od_inches': 59.76, 'od_mm': 1518},
    '56': {'nps': '56', 'class': 400, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 55.98, 'id_mm': 1422, 'od_inches': 61.74, 'od_mm': 1568},
    '58': {'nps': '58', 'class': 400, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 58.00, 'id_mm': 1473, 'od_inches': 63.74, 'od_mm': 1619},
    '60': {'nps': '60', 'class': 400, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 60.00, 'id_mm': 1524, 'od_inches': 66.26, 'od_mm': 1683},
}

# ASME B16.47 Series A Class 600 Flat Ring Gaskets (for RF Flanges)
B1647A_CLASS600_FLAT_RING_GASKETS = {
    '26': {'nps': '26', 'class': 600, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 25.98, 'id_mm': 660, 'od_inches': 34.13, 'od_mm': 867},
    '28': {'nps': '28', 'class': 600, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 27.99, 'id_mm': 711, 'od_inches': 35.98, 'od_mm': 914},
    '30': {'nps': '30', 'class': 600, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 30.00, 'id_mm': 762, 'od_inches': 38.27, 'od_mm': 972},
    '32': {'nps': '32', 'class': 600, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 32.01, 'id_mm': 813, 'od_inches': 40.24, 'od_mm': 1022},
    '34': {'nps': '34', 'class': 600, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 34.02, 'id_mm': 864, 'od_inches': 42.24, 'od_mm': 1073},
    '36': {'nps': '36', 'class': 600, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 35.98, 'id_mm': 914, 'od_inches': 44.49, 'od_mm': 1130},
    '38': {'nps': '38', 'class': 600, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 37.99, 'id_mm': 965, 'od_inches': 43.50, 'od_mm': 1105},
    '40': {'nps': '40', 'class': 600, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 40.00, 'id_mm': 1016, 'od_inches': 45.51, 'od_mm': 1156},
    '42': {'nps': '42', 'class': 600, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 42.01, 'id_mm': 1067, 'od_inches': 48.00, 'od_mm': 1219},
    '44': {'nps': '44', 'class': 600, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 44.02, 'id_mm': 1118, 'od_inches': 50.00, 'od_mm': 1270},
    '46': {'nps': '46', 'class': 600, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 45.98, 'id_mm': 1168, 'od_inches': 52.24, 'od_mm': 1327},
    '48': {'nps': '48', 'class': 600, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 48.00, 'id_mm': 1219, 'od_inches': 54.76, 'od_mm': 1391},
    '50': {'nps': '50', 'class': 600, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 50.00, 'id_mm': 1270, 'od_inches': 57.01, 'od_mm': 1448},
    '52': {'nps': '52', 'class': 600, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 52.01, 'id_mm': 1321, 'od_inches': 59.02, 'od_mm': 1499},
    '54': {'nps': '54', 'class': 600, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 54.02, 'id_mm': 1372, 'od_inches': 61.26, 'od_mm': 1556},
    '56': {'nps': '56', 'class': 600, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 55.98, 'id_mm': 1422, 'od_inches': 63.50, 'od_mm': 1613},
    '58': {'nps': '58', 'class': 600, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 58.00, 'id_mm': 1473, 'od_inches': 65.51, 'od_mm': 1664},
    '60': {'nps': '60', 'class': 600, 'series': 'A', 'gasket_type': 'flat_ring', 'id_inches': 60.00, 'id_mm': 1524, 'od_inches': 67.76, 'od_mm': 1721},
}

# ASME B16.5 Class 150 Full Face Gaskets
B165_CLASS150_FULL_FACE_GASKETS = {
    '1/2': {
        'nps': '1/2',
        'class': 150,
        'gasket_type': 'full_face',
        'id_inches': 0.84,
        'id_mm': 21,
        'od_inches': 3.50,
        'od_mm': 89,
        'number_of_holes': 4,
        'bolt_hole_diameter_inches': 0.62,
        'bolt_circle_diameter_inches': 2.38,
        'bolt_circle_diameter_mm': 60.3
    },
    '3/4': {
        'nps': '3/4',
        'class': 150,
        'gasket_type': 'full_face',
        'id_inches': 1.06,
        'id_mm': 27,
        'od_inches': 3.88,
        'od_mm': 99,
        'number_of_holes': 4,
        'bolt_hole_diameter_inches': 0.62,
        'bolt_circle_diameter_inches': 2.75,
        'bolt_circle_diameter_mm': 69.9
    },
    '1': {
        'nps': '1',
        'class': 150,
        'gasket_type': 'full_face',
        'id_inches': 1.31,
        'id_mm': 33,
        'od_inches': 4.25,
        'od_mm': 108,
        'number_of_holes': 4,
        'bolt_hole_diameter_inches': 0.62,
        'bolt_circle_diameter_inches': 3.12,
        'bolt_circle_diameter_mm': 79.4
    },
    '1-1/4': {
        'nps': '1-1/4',
        'class': 150,
        'gasket_type': 'full_face',
        'id_inches': 1.66,
        'id_mm': 42,
        'od_inches': 4.63,
        'od_mm': 118,
        'number_of_holes': 4,
        'bolt_hole_diameter_inches': 0.62,
        'bolt_circle_diameter_inches': 3.50,
        'bolt_circle_diameter_mm': 88.9
    },
    '1-1/2': {
        'nps': '1-1/2',
        'class': 150,
        'gasket_type': 'full_face',
        'id_inches': 1.91,
        'id_mm': 49,
        'od_inches': 5.00,
        'od_mm': 127,
        'number_of_holes': 4,
        'bolt_hole_diameter_inches': 0.62,
        'bolt_circle_diameter_inches': 3.88,
        'bolt_circle_diameter_mm': 98.4
    },
    '2': {
        'nps': '2',
        'class': 150,
        'gasket_type': 'full_face',
        'id_inches': 2.38,
        'id_mm': 60,
        'od_inches': 6.00,
        'od_mm': 152,
        'number_of_holes': 4,
        'bolt_hole_diameter_inches': 0.75,
        'bolt_circle_diameter_inches': 4.75,
        'bolt_circle_diameter_mm': 120.7
    },
    '2-1/2': {
        'nps': '2-1/2',
        'class': 150,
        'gasket_type': 'full_face',
        'id_inches': 2.88,
        'id_mm': 73,
        'od_inches': 7.00,
        'od_mm': 178,
        'number_of_holes': 4,
        'bolt_hole_diameter_inches': 0.75,
        'bolt_circle_diameter_inches': 5.50,
        'bolt_circle_diameter_mm': 139.7
    },
    '3': {
        'nps': '3',
        'class': 150,
        'gasket_type': 'full_face',
        'id_inches': 3.50,
        'id_mm': 89,
        'od_inches': 7.50,
        'od_mm': 191,
        'number_of_holes': 4,
        'bolt_hole_diameter_inches': 0.75,
        'bolt_circle_diameter_inches': 6.00,
        'bolt_circle_diameter_mm': 152.4
    },
    '3-1/2': {
        'nps': '3-1/2',
        'class': 150,
        'gasket_type': 'full_face',
        'id_inches': 4.00,
        'id_mm': 102,
        'od_inches': 8.50,
        'od_mm': 216,
        'number_of_holes': 8,
        'bolt_hole_diameter_inches': 0.75,
        'bolt_circle_diameter_inches': 7.00,
        'bolt_circle_diameter_mm': 177.8
    },
    '4': {
        'nps': '4',
        'class': 150,
        'gasket_type': 'full_face',
        'id_inches': 4.50,
        'id_mm': 114,
        'od_inches': 9.00,
        'od_mm': 229,
        'number_of_holes': 8,
        'bolt_hole_diameter_inches': 0.75,
        'bolt_circle_diameter_inches': 7.50,
        'bolt_circle_diameter_mm': 190.5
    },
    '5': {
        'nps': '5',
        'class': 150,
        'gasket_type': 'full_face',
        'id_inches': 5.56,
        'id_mm': 141,
        'od_inches': 10.00,
        'od_mm': 254,
        'number_of_holes': 8,
        'bolt_hole_diameter_inches': 0.88,
        'bolt_circle_diameter_inches': 8.50,
        'bolt_circle_diameter_mm': 215.9
    },
    '6': {
        'nps': '6',
        'class': 150,
        'gasket_type': 'full_face',
        'id_inches': 6.62,
        'id_mm': 168,
        'od_inches': 11.00,
        'od_mm': 279,
        'number_of_holes': 8,
        'bolt_hole_diameter_inches': 0.88,
        'bolt_circle_diameter_inches': 9.50,
        'bolt_circle_diameter_mm': 241.3
    },
    '8': {
        'nps': '8',
        'class': 150,
        'gasket_type': 'full_face',
        'id_inches': 8.62,
        'id_mm': 219,
        'od_inches': 13.50,
        'od_mm': 343,
        'number_of_holes': 8,
        'bolt_hole_diameter_inches': 0.88,
        'bolt_circle_diameter_inches': 11.75,
        'bolt_circle_diameter_mm': 298.5
    },
    '10': {
        'nps': '10',
        'class': 150,
        'gasket_type': 'full_face',
        'id_inches': 10.75,
        'id_mm': 273,
        'od_inches': 16.00,
        'od_mm': 406,
        'number_of_holes': 12,
        'bolt_hole_diameter_inches': 1.00,
        'bolt_circle_diameter_inches': 14.25,
        'bolt_circle_diameter_mm': 362.0
    },
    '12': {
        'nps': '12',
        'class': 150,
        'gasket_type': 'full_face',
        'id_inches': 12.75,
        'id_mm': 324,
        'od_inches': 19.00,
        'od_mm': 483,
        'number_of_holes': 12,
        'bolt_hole_diameter_inches': 1.00,
        'bolt_circle_diameter_inches': 17.00,
        'bolt_circle_diameter_mm': 431.8
    },
    '14': {
        'nps': '14',
        'class': 150,
        'gasket_type': 'full_face',
        'id_inches': 14.00,
        'id_mm': 356,
        'od_inches': 21.00,
        'od_mm': 533,
        'number_of_holes': 12,
        'bolt_hole_diameter_inches': 1.12,
        'bolt_circle_diameter_inches': 18.75,
        'bolt_circle_diameter_mm': 476.3
    },
    '16': {
        'nps': '16',
        'class': 150,
        'gasket_type': 'full_face',
        'id_inches': 16.00,
        'id_mm': 406,
        'od_inches': 23.50,
        'od_mm': 597,
        'number_of_holes': 16,
        'bolt_hole_diameter_inches': 1.12,
        'bolt_circle_diameter_inches': 21.25,
        'bolt_circle_diameter_mm': 539.8
    },
    '18': {
        'nps': '18',
        'class': 150,
        'gasket_type': 'full_face',
        'id_inches': 18.00,
        'id_mm': 457,
        'od_inches': 25.00,
        'od_mm': 635,
        'number_of_holes': 16,
        'bolt_hole_diameter_inches': 1.25,
        'bolt_circle_diameter_inches': 22.75,
        'bolt_circle_diameter_mm': 577.9
    },
    '20': {
        'nps': '20',
        'class': 150,
        'gasket_type': 'full_face',
        'id_inches': 20.00,
        'id_mm': 508,
        'od_inches': 27.50,
        'od_mm': 699,
        'number_of_holes': 20,
        'bolt_hole_diameter_inches': 1.25,
        'bolt_circle_diameter_inches': 25.00,
        'bolt_circle_diameter_mm': 635.0
    },
    '24': {
        'nps': '24',
        'class': 150,
        'gasket_type': 'full_face',
        'id_inches': 24.00,
        'id_mm': 610,
        'od_inches': 32.00,
        'od_mm': 813,
        'number_of_holes': 20,
        'bolt_hole_diameter_inches': 1.38,
        'bolt_circle_diameter_inches': 29.50,
        'bolt_circle_diameter_mm': 749.3
    },
}

# ASME B16.5 Class 300 Full Face Gaskets
B165_CLASS300_FULL_FACE_GASKETS = {
    '1/2': {
        'nps': '1/2',
        'class': 300,
        'gasket_type': 'full_face',
        'id_inches': 0.84,
        'id_mm': 21,
        'od_inches': 3.75,
        'od_mm': 95,
        'number_of_holes': 4,
        'bolt_hole_diameter_inches': 0.63,
        'bolt_circle_diameter_inches': 2.63,
        'bolt_circle_diameter_mm': 66.8
    },
    '3/4': {
        'nps': '3/4',
        'class': 300,
        'gasket_type': 'full_face',
        'id_inches': 1.06,
        'id_mm': 27,
        'od_inches': 4.62,
        'od_mm': 117,
        'number_of_holes': 4,
        'bolt_hole_diameter_inches': 0.75,
        'bolt_circle_diameter_inches': 3.25,
        'bolt_circle_diameter_mm': 82.6
    },
    '1': {
        'nps': '1',
        'class': 300,
        'gasket_type': 'full_face',
        'id_inches': 1.31,
        'id_mm': 33,
        'od_inches': 4.88,
        'od_mm': 124,
        'number_of_holes': 4,
        'bolt_hole_diameter_inches': 0.75,
        'bolt_circle_diameter_inches': 3.50,
        'bolt_circle_diameter_mm': 88.9
    },
    '1-1/4': {
        'nps': '1-1/4',
        'class': 300,
        'gasket_type': 'full_face',
        'id_inches': 1.66,
        'id_mm': 42,
        'od_inches': 5.25,
        'od_mm': 133,
        'number_of_holes': 4,
        'bolt_hole_diameter_inches': 0.75,
        'bolt_circle_diameter_inches': 3.88,
        'bolt_circle_diameter_mm': 98.4
    },
    '1-1/2': {
        'nps': '1-1/2',
        'class': 300,
        'gasket_type': 'full_face',
        'id_inches': 1.91,
        'id_mm': 49,
        'od_inches': 6.12,
        'od_mm': 155,
        'number_of_holes': 4,
        'bolt_hole_diameter_inches': 0.88,
        'bolt_circle_diameter_inches': 4.50,
        'bolt_circle_diameter_mm': 114.3
    },
    '2': {
        'nps': '2',
        'class': 300,
        'gasket_type': 'full_face',
        'id_inches': 2.38,
        'id_mm': 60,
        'od_inches': 6.50,
        'od_mm': 165,
        'number_of_holes': 8,
        'bolt_hole_diameter_inches': 0.75,
        'bolt_circle_diameter_inches': 5.00,
        'bolt_circle_diameter_mm': 127.0
    },
    '2-1/2': {
        'nps': '2-1/2',
        'class': 300,
        'gasket_type': 'full_face',
        'id_inches': 2.88,
        'id_mm': 73,
        'od_inches': 7.50,
        'od_mm': 191,
        'number_of_holes': 8,
        'bolt_hole_diameter_inches': 0.88,
        'bolt_circle_diameter_inches': 5.88,
        'bolt_circle_diameter_mm': 149.2
    },
    '3': {
        'nps': '3',
        'class': 300,
        'gasket_type': 'full_face',
        'id_inches': 3.50,
        'id_mm': 89,
        'od_inches': 8.25,
        'od_mm': 210,
        'number_of_holes': 8,
        'bolt_hole_diameter_inches': 0.88,
        'bolt_circle_diameter_inches': 6.63,
        'bolt_circle_diameter_mm': 168.3
    },
    '3-1/2': {
        'nps': '3-1/2',
        'class': 300,
        'gasket_type': 'full_face',
        'id_inches': 4.00,
        'id_mm': 102,
        'od_inches': 9.00,
        'od_mm': 229,
        'number_of_holes': 8,
        'bolt_hole_diameter_inches': 0.88,
        'bolt_circle_diameter_inches': 7.25,
        'bolt_circle_diameter_mm': 184.2
    },
    '4': {
        'nps': '4',
        'class': 300,
        'gasket_type': 'full_face',
        'id_inches': 4.50,
        'id_mm': 114,
        'od_inches': 10.00,
        'od_mm': 254,
        'number_of_holes': 8,
        'bolt_hole_diameter_inches': 0.88,
        'bolt_circle_diameter_inches': 7.88,
        'bolt_circle_diameter_mm': 200.0
    },
    '5': {
        'nps': '5',
        'class': 300,
        'gasket_type': 'full_face',
        'id_inches': 5.56,
        'id_mm': 141,
        'od_inches': 11.00,
        'od_mm': 279,
        'number_of_holes': 8,
        'bolt_hole_diameter_inches': 0.88,
        'bolt_circle_diameter_inches': 9.25,
        'bolt_circle_diameter_mm': 235.0
    },
    '6': {
        'nps': '6',
        'class': 300,
        'gasket_type': 'full_face',
        'id_inches': 6.62,
        'id_mm': 168,
        'od_inches': 12.50,
        'od_mm': 318,
        'number_of_holes': 12,
        'bolt_hole_diameter_inches': 0.88,
        'bolt_circle_diameter_inches': 10.63,
        'bolt_circle_diameter_mm': 269.9
    },
    '8': {
        'nps': '8',
        'class': 300,
        'gasket_type': 'full_face',
        'id_inches': 8.62,
        'id_mm': 219,
        'od_inches': 15.00,
        'od_mm': 381,
        'number_of_holes': 12,
        'bolt_hole_diameter_inches': 1.00,
        'bolt_circle_diameter_inches': 13.00,
        'bolt_circle_diameter_mm': 330.2
    },
    '10': {
        'nps': '10',
        'class': 300,
        'gasket_type': 'full_face',
        'id_inches': 10.75,
        'id_mm': 273,
        'od_inches': 17.50,
        'od_mm': 445,
        'number_of_holes': 16,
        'bolt_hole_diameter_inches': 1.13,
        'bolt_circle_diameter_inches': 15.25,
        'bolt_circle_diameter_mm': 387.4
    },
    '12': {
        'nps': '12',
        'class': 300,
        'gasket_type': 'full_face',
        'id_inches': 12.75,
        'id_mm': 324,
        'od_inches': 20.50,
        'od_mm': 521,
        'number_of_holes': 16,
        'bolt_hole_diameter_inches': 1.25,
        'bolt_circle_diameter_inches': 17.75,
        'bolt_circle_diameter_mm': 450.9
    },
    '14': {
        'nps': '14',
        'class': 300,
        'gasket_type': 'full_face',
        'id_inches': 14.00,
        'id_mm': 356,
        'od_inches': 23.00,
        'od_mm': 584,
        'number_of_holes': 20,
        'bolt_hole_diameter_inches': 1.25,
        'bolt_circle_diameter_inches': 20.25,
        'bolt_circle_diameter_mm': 514.4
    },
    '16': {
        'nps': '16',
        'class': 300,
        'gasket_type': 'full_face',
        'id_inches': 16.00,
        'id_mm': 406,
        'od_inches': 25.50,
        'od_mm': 648,
        'number_of_holes': 20,
        'bolt_hole_diameter_inches': 1.38,
        'bolt_circle_diameter_inches': 22.50,
        'bolt_circle_diameter_mm': 571.5
    },
    '18': {
        'nps': '18',
        'class': 300,
        'gasket_type': 'full_face',
        'id_inches': 18.00,
        'id_mm': 457,
        'od_inches': 28.00,
        'od_mm': 711,
        'number_of_holes': 24,
        'bolt_hole_diameter_inches': 1.38,
        'bolt_circle_diameter_inches': 24.75,
        'bolt_circle_diameter_mm': 628.7
    },
    '20': {
        'nps': '20',
        'class': 300,
        'gasket_type': 'full_face',
        'id_inches': 20.00,
        'id_mm': 508,
        'od_inches': 30.50,
        'od_mm': 775,
        'number_of_holes': 24,
        'bolt_hole_diameter_inches': 1.38,
        'bolt_circle_diameter_inches': 27.00,
        'bolt_circle_diameter_mm': 685.8
    },
    '24': {
        'nps': '24',
        'class': 300,
        'gasket_type': 'full_face',
        'id_inches': 24.00,
        'id_mm': 610,
        'od_inches': 36.00,
        'od_mm': 914,
        'number_of_holes': 24,
        'bolt_hole_diameter_inches': 1.63,
        'bolt_circle_diameter_inches': 32.00,
        'bolt_circle_diameter_mm': 812.8
    },
}

# ASME B16.5 Class 400 Full Face Gaskets
B165_CLASS400_FULL_FACE_GASKETS = {
    '1/2': {
        'nps': '1/2',
        'class': 400,
        'gasket_type': 'full_face',
        'id_inches': 0.84,
        'id_mm': 21,
        'od_inches': 3.75,
        'od_mm': 95,
        'number_of_holes': 4,
        'bolt_hole_diameter_inches': 0.63,
        'bolt_circle_diameter_inches': 2.62,
        'bolt_circle_diameter_mm': 66.5
    },
    '3/4': {
        'nps': '3/4',
        'class': 400,
        'gasket_type': 'full_face',
        'id_inches': 1.06,
        'id_mm': 27,
        'od_inches': 4.63,
        'od_mm': 117,
        'number_of_holes': 4,
        'bolt_hole_diameter_inches': 0.75,
        'bolt_circle_diameter_inches': 3.25,
        'bolt_circle_diameter_mm': 82.6
    },
    '1': {
        'nps': '1',
        'class': 400,
        'gasket_type': 'full_face',
        'id_inches': 1.31,
        'id_mm': 33,
        'od_inches': 4.88,
        'od_mm': 124,
        'number_of_holes': 4,
        'bolt_hole_diameter_inches': 0.75,
        'bolt_circle_diameter_inches': 3.50,
        'bolt_circle_diameter_mm': 88.9
    },
    '1-1/4': {
        'nps': '1-1/4',
        'class': 400,
        'gasket_type': 'full_face',
        'id_inches': 1.66,
        'id_mm': 42,
        'od_inches': 5.25,
        'od_mm': 133,
        'number_of_holes': 4,
        'bolt_hole_diameter_inches': 0.75,
        'bolt_circle_diameter_inches': 3.88,
        'bolt_circle_diameter_mm': 98.4
    },
    '1-1/2': {
        'nps': '1-1/2',
        'class': 400,
        'gasket_type': 'full_face',
        'id_inches': 1.91,
        'id_mm': 49,
        'od_inches': 6.13,
        'od_mm': 156,
        'number_of_holes': 4,
        'bolt_hole_diameter_inches': 0.88,
        'bolt_circle_diameter_inches': 4.50,
        'bolt_circle_diameter_mm': 114.3
    },
    '2': {
        'nps': '2',
        'class': 400,
        'gasket_type': 'full_face',
        'id_inches': 2.38,
        'id_mm': 60,
        'od_inches': 6.50,
        'od_mm': 165,
        'number_of_holes': 8,
        'bolt_hole_diameter_inches': 0.75,
        'bolt_circle_diameter_inches': 5.00,
        'bolt_circle_diameter_mm': 127.0
    },
    '2-1/2': {
        'nps': '2-1/2',
        'class': 400,
        'gasket_type': 'full_face',
        'id_inches': 2.88,
        'id_mm': 73,
        'od_inches': 7.50,
        'od_mm': 191,
        'number_of_holes': 8,
        'bolt_hole_diameter_inches': 0.88,
        'bolt_circle_diameter_inches': 5.88,
        'bolt_circle_diameter_mm': 149.2
    },
    '3': {
        'nps': '3',
        'class': 400,
        'gasket_type': 'full_face',
        'id_inches': 3.50,
        'id_mm': 89,
        'od_inches': 8.25,
        'od_mm': 210,
        'number_of_holes': 8,
        'bolt_hole_diameter_inches': 0.88,
        'bolt_circle_diameter_inches': 6.63,
        'bolt_circle_diameter_mm': 168.3
    },
    '3-1/2': {
        'nps': '3-1/2',
        'class': 400,
        'gasket_type': 'full_face',
        'id_inches': 4.00,
        'id_mm': 102,
        'od_inches': 9.00,
        'od_mm': 229,
        'number_of_holes': 8,
        'bolt_hole_diameter_inches': 1.00,
        'bolt_circle_diameter_inches': 7.25,
        'bolt_circle_diameter_mm': 184.2
    },
    '4': {
        'nps': '4',
        'class': 400,
        'gasket_type': 'full_face',
        'id_inches': 4.50,
        'id_mm': 114,
        'od_inches': 10.00,
        'od_mm': 254,
        'number_of_holes': 8,
        'bolt_hole_diameter_inches': 1.00,
        'bolt_circle_diameter_inches': 7.88,
        'bolt_circle_diameter_mm': 200.0
    },
    '5': {
        'nps': '5',
        'class': 400,
        'gasket_type': 'full_face',
        'id_inches': 5.56,
        'id_mm': 141,
        'od_inches': 11.00,
        'od_mm': 279,
        'number_of_holes': 8,
        'bolt_hole_diameter_inches': 1.00,
        'bolt_circle_diameter_inches': 9.25,
        'bolt_circle_diameter_mm': 235.0
    },
    '6': {
        'nps': '6',
        'class': 400,
        'gasket_type': 'full_face',
        'id_inches': 6.62,
        'id_mm': 168,
        'od_inches': 12.50,
        'od_mm': 318,
        'number_of_holes': 12,
        'bolt_hole_diameter_inches': 1.00,
        'bolt_circle_diameter_inches': 10.63,
        'bolt_circle_diameter_mm': 269.9
    },
    '8': {
        'nps': '8',
        'class': 400,
        'gasket_type': 'full_face',
        'id_inches': 8.62,
        'id_mm': 219,
        'od_inches': 15.00,
        'od_mm': 381,
        'number_of_holes': 12,
        'bolt_hole_diameter_inches': 1.13,
        'bolt_circle_diameter_inches': 13.00,
        'bolt_circle_diameter_mm': 330.2
    },
    '10': {
        'nps': '10',
        'class': 400,
        'gasket_type': 'full_face',
        'id_inches': 10.75,
        'id_mm': 273,
        'od_inches': 17.50,
        'od_mm': 445,
        'number_of_holes': 16,
        'bolt_hole_diameter_inches': 1.25,
        'bolt_circle_diameter_inches': 15.25,
        'bolt_circle_diameter_mm': 387.4
    },
    '12': {
        'nps': '12',
        'class': 400,
        'gasket_type': 'full_face',
        'id_inches': 12.75,
        'id_mm': 324,
        'od_inches': 20.50,
        'od_mm': 521,
        'number_of_holes': 16,
        'bolt_hole_diameter_inches': 1.38,
        'bolt_circle_diameter_inches': 17.75,
        'bolt_circle_diameter_mm': 450.9
    },
    '14': {
        'nps': '14',
        'class': 400,
        'gasket_type': 'full_face',
        'id_inches': 14.00,
        'id_mm': 356,
        'od_inches': 23.00,
        'od_mm': 584,
        'number_of_holes': 20,
        'bolt_hole_diameter_inches': 1.38,
        'bolt_circle_diameter_inches': 20.25,
        'bolt_circle_diameter_mm': 514.4
    },
    '16': {
        'nps': '16',
        'class': 400,
        'gasket_type': 'full_face',
        'id_inches': 16.00,
        'id_mm': 406,
        'od_inches': 25.50,
        'od_mm': 648,
        'number_of_holes': 20,
        'bolt_hole_diameter_inches': 1.50,
        'bolt_circle_diameter_inches': 22.50,
        'bolt_circle_diameter_mm': 571.5
    },
    '18': {
        'nps': '18',
        'class': 400,
        'gasket_type': 'full_face',
        'id_inches': 18.00,
        'id_mm': 457,
        'od_inches': 28.00,
        'od_mm': 711,
        'number_of_holes': 24,
        'bolt_hole_diameter_inches': 1.50,
        'bolt_circle_diameter_inches': 24.75,
        'bolt_circle_diameter_mm': 628.7
    },
    '20': {
        'nps': '20',
        'class': 400,
        'gasket_type': 'full_face',
        'id_inches': 20.00,
        'id_mm': 508,
        'od_inches': 30.50,
        'od_mm': 775,
        'number_of_holes': 24,
        'bolt_hole_diameter_inches': 1.63,
        'bolt_circle_diameter_inches': 27.00,
        'bolt_circle_diameter_mm': 685.8
    },
    '24': {
        'nps': '24',
        'class': 400,
        'gasket_type': 'full_face',
        'id_inches': 24.00,
        'id_mm': 610,
        'od_inches': 36.00,
        'od_mm': 914,
        'number_of_holes': 24,
        'bolt_hole_diameter_inches': 1.88,
        'bolt_circle_diameter_inches': 32.00,
        'bolt_circle_diameter_mm': 812.8
    },
}

# ASME B16.5 Class 600 Full Face Gaskets
B165_CLASS600_FULL_FACE_GASKETS = {
    '1/2': {
        'nps': '1/2',
        'class': 600,
        'gasket_type': 'full_face',
        'id_inches': 0.84,
        'id_mm': 21,
        'od_inches': 3.75,
        'od_mm': 95,
        'number_of_holes': 4,
        'bolt_hole_diameter_inches': 0.63,
        'bolt_circle_diameter_inches': 2.63,
        'bolt_circle_diameter_mm': 66.8
    },
    '3/4': {
        'nps': '3/4',
        'class': 600,
        'gasket_type': 'full_face',
        'id_inches': 1.06,
        'id_mm': 27,
        'od_inches': 4.63,
        'od_mm': 117,
        'number_of_holes': 4,
        'bolt_hole_diameter_inches': 0.75,
        'bolt_circle_diameter_inches': 3.25,
        'bolt_circle_diameter_mm': 82.6
    },
    '1': {
        'nps': '1',
        'class': 600,
        'gasket_type': 'full_face',
        'id_inches': 1.31,
        'id_mm': 33,
        'od_inches': 4.88,
        'od_mm': 124,
        'number_of_holes': 4,
        'bolt_hole_diameter_inches': 0.75,
        'bolt_circle_diameter_inches': 3.50,
        'bolt_circle_diameter_mm': 88.9
    },
    '1-1/4': {
        'nps': '1-1/4',
        'class': 600,
        'gasket_type': 'full_face',
        'id_inches': 1.66,
        'id_mm': 42,
        'od_inches': 5.25,
        'od_mm': 133,
        'number_of_holes': 4,
        'bolt_hole_diameter_inches': 0.75,
        'bolt_circle_diameter_inches': 3.88,
        'bolt_circle_diameter_mm': 98.4
    },
    '1-1/2': {
        'nps': '1-1/2',
        'class': 600,
        'gasket_type': 'full_face',
        'id_inches': 1.91,
        'id_mm': 49,
        'od_inches': 6.13,
        'od_mm': 156,
        'number_of_holes': 4,
        'bolt_hole_diameter_inches': 0.88,
        'bolt_circle_diameter_inches': 4.50,
        'bolt_circle_diameter_mm': 114.3
    },
    '2': {
        'nps': '2',
        'class': 600,
        'gasket_type': 'full_face',
        'id_inches': 2.38,
        'id_mm': 60,
        'od_inches': 6.50,
        'od_mm': 165,
        'number_of_holes': 8,
        'bolt_hole_diameter_inches': 0.75,
        'bolt_circle_diameter_inches': 5.00,
        'bolt_circle_diameter_mm': 127.0
    },
    '2-1/2': {
        'nps': '2-1/2',
        'class': 600,
        'gasket_type': 'full_face',
        'id_inches': 2.88,
        'id_mm': 73,
        'od_inches': 7.50,
        'od_mm': 191,
        'number_of_holes': 8,
        'bolt_hole_diameter_inches': 0.88,
        'bolt_circle_diameter_inches': 5.88,
        'bolt_circle_diameter_mm': 149.2
    },
    '3': {
        'nps': '3',
        'class': 600,
        'gasket_type': 'full_face',
        'id_inches': 3.50,
        'id_mm': 89,
        'od_inches': 8.25,
        'od_mm': 210,
        'number_of_holes': 8,
        'bolt_hole_diameter_inches': 0.88,
        'bolt_circle_diameter_inches': 6.63,
        'bolt_circle_diameter_mm': 168.3
    },
    '3-1/2': {
        'nps': '3-1/2',
        'class': 600,
        'gasket_type': 'full_face',
        'id_inches': 4.00,
        'id_mm': 102,
        'od_inches': 9.00,
        'od_mm': 229,
        'number_of_holes': 8,
        'bolt_hole_diameter_inches': 1.00,
        'bolt_circle_diameter_inches': 7.25,
        'bolt_circle_diameter_mm': 184.2
    },
    '4': {
        'nps': '4',
        'class': 600,
        'gasket_type': 'full_face',
        'id_inches': 4.50,
        'id_mm': 114,
        'od_inches': 10.75,
        'od_mm': 273,
        'number_of_holes': 8,
        'bolt_hole_diameter_inches': 1.00,
        'bolt_circle_diameter_inches': 8.50,
        'bolt_circle_diameter_mm': 215.9
    },
    '5': {
        'nps': '5',
        'class': 600,
        'gasket_type': 'full_face',
        'id_inches': 5.56,
        'id_mm': 141,
        'od_inches': 13.00,
        'od_mm': 330,
        'number_of_holes': 8,
        'bolt_hole_diameter_inches': 1.13,
        'bolt_circle_diameter_inches': 10.50,
        'bolt_circle_diameter_mm': 266.7
    },
    '6': {
        'nps': '6',
        'class': 600,
        'gasket_type': 'full_face',
        'id_inches': 6.62,
        'id_mm': 168,
        'od_inches': 14.00,
        'od_mm': 356,
        'number_of_holes': 12,
        'bolt_hole_diameter_inches': 1.13,
        'bolt_circle_diameter_inches': 11.50,
        'bolt_circle_diameter_mm': 292.1
    },
    '8': {
        'nps': '8',
        'class': 600,
        'gasket_type': 'full_face',
        'id_inches': 8.62,
        'id_mm': 219,
        'od_inches': 16.50,
        'od_mm': 419,
        'number_of_holes': 12,
        'bolt_hole_diameter_inches': 1.25,
        'bolt_circle_diameter_inches': 13.75,
        'bolt_circle_diameter_mm': 349.3
    },
    '10': {
        'nps': '10',
        'class': 600,
        'gasket_type': 'full_face',
        'id_inches': 10.75,
        'id_mm': 273,
        'od_inches': 20.00,
        'od_mm': 508,
        'number_of_holes': 16,
        'bolt_hole_diameter_inches': 1.38,
        'bolt_circle_diameter_inches': 17.00,
        'bolt_circle_diameter_mm': 431.8
    },
    '12': {
        'nps': '12',
        'class': 600,
        'gasket_type': 'full_face',
        'id_inches': 12.75,
        'id_mm': 324,
        'od_inches': 22.00,
        'od_mm': 559,
        'number_of_holes': 20,
        'bolt_hole_diameter_inches': 1.38,
        'bolt_circle_diameter_inches': 19.25,
        'bolt_circle_diameter_mm': 489.0
    },
    '14': {
        'nps': '14',
        'class': 600,
        'gasket_type': 'full_face',
        'id_inches': 14.00,
        'id_mm': 356,
        'od_inches': 23.75,
        'od_mm': 603,
        'number_of_holes': 20,
        'bolt_hole_diameter_inches': 1.50,
        'bolt_circle_diameter_inches': 20.75,
        'bolt_circle_diameter_mm': 527.1
    },
    '16': {
        'nps': '16',
        'class': 600,
        'gasket_type': 'full_face',
        'id_inches': 16.00,
        'id_mm': 406,
        'od_inches': 27.00,
        'od_mm': 686,
        'number_of_holes': 20,
        'bolt_hole_diameter_inches': 1.63,
        'bolt_circle_diameter_inches': 23.75,
        'bolt_circle_diameter_mm': 603.3
    },
    '18': {
        'nps': '18',
        'class': 600,
        'gasket_type': 'full_face',
        'id_inches': 18.00,
        'id_mm': 457,
        'od_inches': 29.25,
        'od_mm': 743,
        'number_of_holes': 20,
        'bolt_hole_diameter_inches': 1.75,
        'bolt_circle_diameter_inches': 25.75,
        'bolt_circle_diameter_mm': 654.1
    },
    '20': {
        'nps': '20',
        'class': 600,
        'gasket_type': 'full_face',
        'id_inches': 20.00,
        'id_mm': 508,
        'od_inches': 32.00,
        'od_mm': 813,
        'number_of_holes': 24,
        'bolt_hole_diameter_inches': 1.75,
        'bolt_circle_diameter_inches': 28.50,
        'bolt_circle_diameter_mm': 723.9
    },
    '24': {
        'nps': '24',
        'class': 600,
        'gasket_type': 'full_face',
        'id_inches': 24.00,
        'id_mm': 610,
        'od_inches': 37.00,
        'od_mm': 940,
        'number_of_holes': 24,
        'bolt_hole_diameter_inches': 2.00,
        'bolt_circle_diameter_inches': 33.00,
        'bolt_circle_diameter_mm': 838.2
    },
}

# ASME B16.5 Class 900 Full Face Gaskets
B165_CLASS900_FULL_FACE_GASKETS = {
    '1/2': {
        'nps': '1/2',
        'class': 900,
        'gasket_type': 'full_face',
        'id_inches': 0.84,
        'id_mm': 21,
        'od_inches': 4.75,
        'od_mm': 121,
        'number_of_holes': 4,
        'bolt_hole_diameter_inches': 0.88,
        'bolt_circle_diameter_inches': 3.25,
        'bolt_circle_diameter_mm': 82.6
    },
    '3/4': {
        'nps': '3/4',
        'class': 900,
        'gasket_type': 'full_face',
        'id_inches': 1.06,
        'id_mm': 27,
        'od_inches': 5.13,
        'od_mm': 130,
        'number_of_holes': 4,
        'bolt_hole_diameter_inches': 0.88,
        'bolt_circle_diameter_inches': 3.50,
        'bolt_circle_diameter_mm': 88.9
    },
    '1': {
        'nps': '1',
        'class': 900,
        'gasket_type': 'full_face',
        'id_inches': 1.31,
        'id_mm': 33,
        'od_inches': 5.88,
        'od_mm': 149,
        'number_of_holes': 4,
        'bolt_hole_diameter_inches': 1.00,
        'bolt_circle_diameter_inches': 4.00,
        'bolt_circle_diameter_mm': 101.6
    },
    '1-1/4': {
        'nps': '1-1/4',
        'class': 900,
        'gasket_type': 'full_face',
        'id_inches': 1.66,
        'id_mm': 42,
        'od_inches': 6.25,
        'od_mm': 159,
        'number_of_holes': 4,
        'bolt_hole_diameter_inches': 1.00,
        'bolt_circle_diameter_inches': 4.38,
        'bolt_circle_diameter_mm': 111.3
    },
    '1-1/2': {
        'nps': '1-1/2',
        'class': 900,
        'gasket_type': 'full_face',
        'id_inches': 1.91,
        'id_mm': 49,
        'od_inches': 7.00,
        'od_mm': 178,
        'number_of_holes': 4,
        'bolt_hole_diameter_inches': 1.13,
        'bolt_circle_diameter_inches': 4.88,
        'bolt_circle_diameter_mm': 124.0
    },
    '2': {
        'nps': '2',
        'class': 900,
        'gasket_type': 'full_face',
        'id_inches': 2.38,
        'id_mm': 60,
        'od_inches': 8.50,
        'od_mm': 216,
        'number_of_holes': 8,
        'bolt_hole_diameter_inches': 1.00,
        'bolt_circle_diameter_inches': 6.50,
        'bolt_circle_diameter_mm': 165.1
    },
    '2-1/2': {
        'nps': '2-1/2',
        'class': 900,
        'gasket_type': 'full_face',
        'id_inches': 2.88,
        'id_mm': 73,
        'od_inches': 9.63,
        'od_mm': 245,
        'number_of_holes': 8,
        'bolt_hole_diameter_inches': 1.13,
        'bolt_circle_diameter_inches': 7.50,
        'bolt_circle_diameter_mm': 190.5
    },
    '3': {
        'nps': '3',
        'class': 900,
        'gasket_type': 'full_face',
        'id_inches': 3.50,
        'id_mm': 89,
        'od_inches': 9.50,
        'od_mm': 241,
        'number_of_holes': 8,
        'bolt_hole_diameter_inches': 1.00,
        'bolt_circle_diameter_inches': 7.50,
        'bolt_circle_diameter_mm': 190.5
    },
    '3-1/2': {
        'nps': '3-1/2',
        'class': 900,
        'gasket_type': 'full_face',
        'id_inches': 4.00,
        'id_mm': 102,
        'od_inches': 11.50,
        'od_mm': 292,
        'number_of_holes': None,
        'bolt_hole_diameter_inches': None,
        'bolt_circle_diameter_inches': None,
        'bolt_circle_diameter_mm': None
    },
    '4': {
        'nps': '4',
        'class': 900,
        'gasket_type': 'full_face',
        'id_inches': 4.50,
        'id_mm': 114,
        'od_inches': 11.50,
        'od_mm': 292,
        'number_of_holes': 8,
        'bolt_hole_diameter_inches': 1.25,
        'bolt_circle_diameter_inches': 9.25,
        'bolt_circle_diameter_mm': 235.0
    },
    '5': {
        'nps': '5',
        'class': 900,
        'gasket_type': 'full_face',
        'id_inches': 5.56,
        'id_mm': 141,
        'od_inches': 13.75,
        'od_mm': 349,
        'number_of_holes': 8,
        'bolt_hole_diameter_inches': 1.38,
        'bolt_circle_diameter_inches': 11.00,
        'bolt_circle_diameter_mm': 279.4
    },
    '6': {
        'nps': '6',
        'class': 900,
        'gasket_type': 'full_face',
        'id_inches': 6.62,
        'id_mm': 168,
        'od_inches': 15.00,
        'od_mm': 381,
        'number_of_holes': 12,
        'bolt_hole_diameter_inches': 1.25,
        'bolt_circle_diameter_inches': 12.50,
        'bolt_circle_diameter_mm': 317.5
    },
    '8': {
        'nps': '8',
        'class': 900,
        'gasket_type': 'full_face',
        'id_inches': 8.62,
        'id_mm': 219,
        'od_inches': 18.50,
        'od_mm': 470,
        'number_of_holes': 12,
        'bolt_hole_diameter_inches': 1.50,
        'bolt_circle_diameter_inches': 15.50,
        'bolt_circle_diameter_mm': 393.7
    },
    '10': {
        'nps': '10',
        'class': 900,
        'gasket_type': 'full_face',
        'id_inches': 10.75,
        'id_mm': 273,
        'od_inches': 21.50,
        'od_mm': 546,
        'number_of_holes': 16,
        'bolt_hole_diameter_inches': 1.50,
        'bolt_circle_diameter_inches': 18.50,
        'bolt_circle_diameter_mm': 469.9
    },
    '12': {
        'nps': '12',
        'class': 900,
        'gasket_type': 'full_face',
        'id_inches': 12.75,
        'id_mm': 324,
        'od_inches': 24.00,
        'od_mm': 610,
        'number_of_holes': 20,
        'bolt_hole_diameter_inches': 1.50,
        'bolt_circle_diameter_inches': 21.00,
        'bolt_circle_diameter_mm': 533.4
    },
    '14': {
        'nps': '14',
        'class': 900,
        'gasket_type': 'full_face',
        'id_inches': 14.00,
        'id_mm': 356,
        'od_inches': 25.25,
        'od_mm': 641,
        'number_of_holes': 20,
        'bolt_hole_diameter_inches': 1.63,
        'bolt_circle_diameter_inches': 22.00,
        'bolt_circle_diameter_mm': 558.8
    },
    '16': {
        'nps': '16',
        'class': 900,
        'gasket_type': 'full_face',
        'id_inches': 16.00,
        'id_mm': 406,
        'od_inches': 27.75,
        'od_mm': 705,
        'number_of_holes': 20,
        'bolt_hole_diameter_inches': 1.75,
        'bolt_circle_diameter_inches': 24.25,
        'bolt_circle_diameter_mm': 616.0
    },
    '18': {
        'nps': '18',
        'class': 900,
        'gasket_type': 'full_face',
        'id_inches': 18.00,
        'id_mm': 457,
        'od_inches': 31.00,
        'od_mm': 787,
        'number_of_holes': 20,
        'bolt_hole_diameter_inches': 2.00,
        'bolt_circle_diameter_inches': 27.00,
        'bolt_circle_diameter_mm': 685.8
    },
    '20': {
        'nps': '20',
        'class': 900,
        'gasket_type': 'full_face',
        'id_inches': 20.00,
        'id_mm': 508,
        'od_inches': 33.75,
        'od_mm': 857,
        'number_of_holes': 20,
        'bolt_hole_diameter_inches': 2.13,
        'bolt_circle_diameter_inches': 29.50,
        'bolt_circle_diameter_mm': 749.3
    },
    '24': {
        'nps': '24',
        'class': 900,
        'gasket_type': 'full_face',
        'id_inches': 24.00,
        'id_mm': 610,
        'od_inches': 41.00,
        'od_mm': 1041,
        'number_of_holes': 20,
        'bolt_hole_diameter_inches': 2.63,
        'bolt_circle_diameter_inches': 35.50,
        'bolt_circle_diameter_mm': 901.7
    },
}

# ASME B16.47 Series A Class 150 Full Face Gaskets
B1647A_CLASS150_FULL_FACE_GASKETS = {
    '26': {
        'nps': '26',
        'class': 150,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 26.00,
        'id_mm': 660,
        'od_inches': 34.25,
        'od_mm': 870,
        'number_of_holes': 24,
        'bolt_hole_diameter_inches': 1.38,
        'bolt_circle_diameter_inches': 31.75,
        'bolt_circle_diameter_mm': 806.5
    },
    '28': {
        'nps': '28',
        'class': 150,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 28.00,
        'id_mm': 711,
        'od_inches': 36.50,
        'od_mm': 927,
        'number_of_holes': 28,
        'bolt_hole_diameter_inches': 1.38,
        'bolt_circle_diameter_inches': 34.00,
        'bolt_circle_diameter_mm': 863.6
    },
    '30': {
        'nps': '30',
        'class': 150,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 30.00,
        'id_mm': 762,
        'od_inches': 38.75,
        'od_mm': 984,
        'number_of_holes': 28,
        'bolt_hole_diameter_inches': 1.38,
        'bolt_circle_diameter_inches': 36.00,
        'bolt_circle_diameter_mm': 914.4
    },
    '32': {
        'nps': '32',
        'class': 150,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 32.00,
        'id_mm': 813,
        'od_inches': 41.75,
        'od_mm': 1060,
        'number_of_holes': 28,
        'bolt_hole_diameter_inches': 1.63,
        'bolt_circle_diameter_inches': 38.50,
        'bolt_circle_diameter_mm': 977.9
    },
    '34': {
        'nps': '34',
        'class': 150,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 34.00,
        'id_mm': 864,
        'od_inches': 43.75,
        'od_mm': 1111,
        'number_of_holes': 32,
        'bolt_hole_diameter_inches': 1.63,
        'bolt_circle_diameter_inches': 40.50,
        'bolt_circle_diameter_mm': 1028.7
    },
    '36': {
        'nps': '36',
        'class': 150,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 36.00,
        'id_mm': 914,
        'od_inches': 46.00,
        'od_mm': 1168,
        'number_of_holes': 32,
        'bolt_hole_diameter_inches': 1.63,
        'bolt_circle_diameter_inches': 42.75,
        'bolt_circle_diameter_mm': 1085.9
    },
    '38': {
        'nps': '38',
        'class': 150,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 38.00,
        'id_mm': 965,
        'od_inches': 48.75,
        'od_mm': 1238,
        'number_of_holes': 32,
        'bolt_hole_diameter_inches': 1.63,
        'bolt_circle_diameter_inches': 45.25,
        'bolt_circle_diameter_mm': 1149.4
    },
    '40': {
        'nps': '40',
        'class': 150,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 40.00,
        'id_mm': 1016,
        'od_inches': 50.75,
        'od_mm': 1289,
        'number_of_holes': 36,
        'bolt_hole_diameter_inches': 1.63,
        'bolt_circle_diameter_inches': 47.25,
        'bolt_circle_diameter_mm': 1200.2
    },
    '42': {
        'nps': '42',
        'class': 150,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 42.00,
        'id_mm': 1067,
        'od_inches': 53.00,
        'od_mm': 1346,
        'number_of_holes': 36,
        'bolt_hole_diameter_inches': 1.63,
        'bolt_circle_diameter_inches': 49.50,
        'bolt_circle_diameter_mm': 1257.3
    },
    '44': {
        'nps': '44',
        'class': 150,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 44.00,
        'id_mm': 1118,
        'od_inches': 55.25,
        'od_mm': 1403,
        'number_of_holes': 40,
        'bolt_hole_diameter_inches': 1.63,
        'bolt_circle_diameter_inches': 51.75,
        'bolt_circle_diameter_mm': 1314.5
    },
    '46': {
        'nps': '46',
        'class': 150,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 46.00,
        'id_mm': 1168,
        'od_inches': 57.25,
        'od_mm': 1454,
        'number_of_holes': 40,
        'bolt_hole_diameter_inches': 1.63,
        'bolt_circle_diameter_inches': 53.75,
        'bolt_circle_diameter_mm': 1365.3
    },
    '48': {
        'nps': '48',
        'class': 150,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 48.00,
        'id_mm': 1219,
        'od_inches': 59.50,
        'od_mm': 1511,
        'number_of_holes': 44,
        'bolt_hole_diameter_inches': 1.63,
        'bolt_circle_diameter_inches': 56.00,
        'bolt_circle_diameter_mm': 1422.4
    },
    '50': {
        'nps': '50',
        'class': 150,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 50.00,
        'id_mm': 1270,
        'od_inches': 61.75,
        'od_mm': 1568,
        'number_of_holes': 44,
        'bolt_hole_diameter_inches': 1.88,
        'bolt_circle_diameter_inches': 58.25,
        'bolt_circle_diameter_mm': 1479.6
    },
    '52': {
        'nps': '52',
        'class': 150,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 52.00,
        'id_mm': 1321,
        'od_inches': 64.00,
        'od_mm': 1626,
        'number_of_holes': 44,
        'bolt_hole_diameter_inches': 1.88,
        'bolt_circle_diameter_inches': 60.50,
        'bolt_circle_diameter_mm': 1536.7
    },
    '54': {
        'nps': '54',
        'class': 150,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 54.00,
        'id_mm': 1372,
        'od_inches': 66.25,
        'od_mm': 1683,
        'number_of_holes': 44,
        'bolt_hole_diameter_inches': 1.88,
        'bolt_circle_diameter_inches': 62.75,
        'bolt_circle_diameter_mm': 1593.9
    },
    '56': {
        'nps': '56',
        'class': 150,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 56.00,
        'id_mm': 1422,
        'od_inches': 68.75,
        'od_mm': 1746,
        'number_of_holes': 48,
        'bolt_hole_diameter_inches': 1.88,
        'bolt_circle_diameter_inches': 65.00,
        'bolt_circle_diameter_mm': 1651.0
    },
    '58': {
        'nps': '58',
        'class': 150,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 58.00,
        'id_mm': 1473,
        'od_inches': 71.00,
        'od_mm': 1803,
        'number_of_holes': 48,
        'bolt_hole_diameter_inches': 1.88,
        'bolt_circle_diameter_inches': 67.25,
        'bolt_circle_diameter_mm': 1708.2
    },
    '60': {
        'nps': '60',
        'class': 150,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 60.00,
        'id_mm': 1524,
        'od_inches': 73.00,
        'od_mm': 1854,
        'number_of_holes': 52,
        'bolt_hole_diameter_inches': 1.88,
        'bolt_circle_diameter_inches': 69.25,
        'bolt_circle_diameter_mm': 1759.0
    },
}

# ASME B16.47 Series A Class 300 Full Face Gaskets
B1647A_CLASS300_FULL_FACE_GASKETS = {
    '26': {
        'nps': '26',
        'class': 300,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 26.00,
        'id_mm': 662,
        'od_inches': 38.25,
        'od_mm': 972,
        'number_of_holes': 28,
        'bolt_hole_diameter_inches': 1.75,
        'bolt_circle_diameter_inches': 34.50,
        'bolt_circle_diameter_mm': 876.3
    },
    '28': {
        'nps': '28',
        'class': 300,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 28.00,
        'id_mm': 713,
        'od_inches': 40.75,
        'od_mm': 1035,
        'number_of_holes': 28,
        'bolt_hole_diameter_inches': 1.75,
        'bolt_circle_diameter_inches': 37.00,
        'bolt_circle_diameter_mm': 939.8
    },
    '30': {
        'nps': '30',
        'class': 300,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 30.00,
        'id_mm': 764,
        'od_inches': 43.00,
        'od_mm': 1092,
        'number_of_holes': 28,
        'bolt_hole_diameter_inches': 1.88,
        'bolt_circle_diameter_inches': 39.25,
        'bolt_circle_diameter_mm': 997.0
    },
    '32': {
        'nps': '32',
        'class': 300,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 32.00,
        'id_mm': 815,
        'od_inches': 45.25,
        'od_mm': 1149,
        'number_of_holes': 28,
        'bolt_hole_diameter_inches': 2.00,
        'bolt_circle_diameter_inches': 41.50,
        'bolt_circle_diameter_mm': 1054.1
    },
    '34': {
        'nps': '34',
        'class': 300,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 34.00,
        'id_mm': 866,
        'od_inches': 47.50,
        'od_mm': 1207,
        'number_of_holes': 28,
        'bolt_hole_diameter_inches': 2.00,
        'bolt_circle_diameter_inches': 43.50,
        'bolt_circle_diameter_mm': 1104.9
    },
    '36': {
        'nps': '36',
        'class': 300,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 36.00,
        'id_mm': 917,
        'od_inches': 50.00,
        'od_mm': 1270,
        'number_of_holes': 32,
        'bolt_hole_diameter_inches': 2.13,
        'bolt_circle_diameter_inches': 46.00,
        'bolt_circle_diameter_mm': 1168.4
    },
    '38': {
        'nps': '38',
        'class': 300,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 38.00,
        'id_mm': 968,
        'od_inches': 46.00,
        'od_mm': 1168,
        'number_of_holes': 32,
        'bolt_hole_diameter_inches': 1.63,
        'bolt_circle_diameter_inches': 43.00,
        'bolt_circle_diameter_mm': 1092.2
    },
    '40': {
        'nps': '40',
        'class': 300,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 40.00,
        'id_mm': 1019,
        'od_inches': 48.75,
        'od_mm': 1238,
        'number_of_holes': 32,
        'bolt_hole_diameter_inches': 1.75,
        'bolt_circle_diameter_inches': 45.50,
        'bolt_circle_diameter_mm': 1155.7
    },
    '42': {
        'nps': '42',
        'class': 300,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 42.00,
        'id_mm': 1070,
        'od_inches': 50.75,
        'od_mm': 1289,
        'number_of_holes': 32,
        'bolt_hole_diameter_inches': 1.75,
        'bolt_circle_diameter_inches': 47.50,
        'bolt_circle_diameter_mm': 1206.5
    },
    '44': {
        'nps': '44',
        'class': 300,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 44.00,
        'id_mm': 1121,
        'od_inches': 53.25,
        'od_mm': 1353,
        'number_of_holes': 32,
        'bolt_hole_diameter_inches': 1.88,
        'bolt_circle_diameter_inches': 49.75,
        'bolt_circle_diameter_mm': 1263.7
    },
    '46': {
        'nps': '46',
        'class': 300,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 46.00,
        'id_mm': 1172,
        'od_inches': 55.75,
        'od_mm': 1416,
        'number_of_holes': 28,
        'bolt_hole_diameter_inches': 2.00,
        'bolt_circle_diameter_inches': 52.00,
        'bolt_circle_diameter_mm': 1320.8
    },
    '48': {
        'nps': '48',
        'class': 300,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 48.00,
        'id_mm': 1223,
        'od_inches': 57.75,
        'od_mm': 1467,
        'number_of_holes': 32,
        'bolt_hole_diameter_inches': 2.00,
        'bolt_circle_diameter_inches': 54.00,
        'bolt_circle_diameter_mm': 1371.6
    },
    '50': {
        'nps': '50',
        'class': 300,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 50.00,
        'id_mm': 1274,
        'od_inches': 60.25,
        'od_mm': 1530,
        'number_of_holes': 32,
        'bolt_hole_diameter_inches': 2.13,
        'bolt_circle_diameter_inches': 56.25,
        'bolt_circle_diameter_mm': 1428.8
    },
    '52': {
        'nps': '52',
        'class': 300,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 52.00,
        'id_mm': 1324,
        'od_inches': 62.25,
        'od_mm': 1581,
        'number_of_holes': 32,
        'bolt_hole_diameter_inches': 2.13,
        'bolt_circle_diameter_inches': 58.25,
        'bolt_circle_diameter_mm': 1479.6
    },
    '54': {
        'nps': '54',
        'class': 300,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 54.00,
        'id_mm': 1375,
        'od_inches': 65.25,
        'od_mm': 1657,
        'number_of_holes': 28,
        'bolt_hole_diameter_inches': 2.38,
        'bolt_circle_diameter_inches': 61.00,
        'bolt_circle_diameter_mm': 1549.4
    },
    '56': {
        'nps': '56',
        'class': 300,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 56.00,
        'id_mm': 1426,
        'od_inches': 67.25,
        'od_mm': 1708,
        'number_of_holes': 28,
        'bolt_hole_diameter_inches': 2.38,
        'bolt_circle_diameter_inches': 63.00,
        'bolt_circle_diameter_mm': 1600.2
    },
    '58': {
        'nps': '58',
        'class': 300,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 58.00,
        'id_mm': 1477,
        'od_inches': 69.25,
        'od_mm': 1759,
        'number_of_holes': 32,
        'bolt_hole_diameter_inches': 2.38,
        'bolt_circle_diameter_inches': 65.00,
        'bolt_circle_diameter_mm': 1651.0
    },
    '60': {
        'nps': '60',
        'class': 300,
        'series': 'A',
        'gasket_type': 'full_face',
        'id_inches': 60.00,
        'id_mm': 1528,
        'od_inches': 71.25,
        'od_mm': 1810,
        'number_of_holes': 32,
        'bolt_hole_diameter_inches': 2.38,
        'bolt_circle_diameter_inches': 67.00,
        'bolt_circle_diameter_mm': 1701.8
    },
}

# ASME B16.47 Series B Class 150 Full Face Gaskets
B1647B_CLASS150_FULL_FACE_GASKETS = {
    '26': {
        'nps': '26',
        'class': 150,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 26.00,
        'id_mm': 660,
        'od_inches': 30.94,
        'od_mm': 786,
        'number_of_holes': 36,
        'bolt_hole_diameter_inches': 0.88,
        'bolt_circle_diameter_inches': 29.31,
        'bolt_circle_diameter_mm': 744.5
    },
    '28': {
        'nps': '28',
        'class': 150,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 28.00,
        'id_mm': 711,
        'od_inches': 32.94,
        'od_mm': 837,
        'number_of_holes': 40,
        'bolt_hole_diameter_inches': 0.88,
        'bolt_circle_diameter_inches': 31.31,
        'bolt_circle_diameter_mm': 795.3
    },
    '30': {
        'nps': '30',
        'class': 150,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 30.00,
        'id_mm': 762,
        'od_inches': 34.94,
        'od_mm': 887,
        'number_of_holes': 44,
        'bolt_hole_diameter_inches': 0.88,
        'bolt_circle_diameter_inches': 33.31,
        'bolt_circle_diameter_mm': 846.1
    },
    '32': {
        'nps': '32',
        'class': 150,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 32.00,
        'id_mm': 813,
        'od_inches': 37.06,
        'od_mm': 941,
        'number_of_holes': 48,
        'bolt_hole_diameter_inches': 0.88,
        'bolt_circle_diameter_inches': 35.44,
        'bolt_circle_diameter_mm': 900.2
    },
    '34': {
        'nps': '34',
        'class': 150,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 34.00,
        'id_mm': 864,
        'od_inches': 39.56,
        'od_mm': 1005,
        'number_of_holes': 40,
        'bolt_hole_diameter_inches': 1.00,
        'bolt_circle_diameter_inches': 37.69,
        'bolt_circle_diameter_mm': 957.3
    },
    '36': {
        'nps': '36',
        'class': 150,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 36.00,
        'id_mm': 914,
        'od_inches': 41.63,
        'od_mm': 1057,
        'number_of_holes': 44,
        'bolt_hole_diameter_inches': 1.00,
        'bolt_circle_diameter_inches': 39.75,
        'bolt_circle_diameter_mm': 1009.7
    },
    '38': {
        'nps': '38',
        'class': 150,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 38.00,
        'id_mm': 965,
        'od_inches': 44.25,
        'od_mm': 1124,
        'number_of_holes': 40,
        'bolt_hole_diameter_inches': 1.13,
        'bolt_circle_diameter_inches': 42.13,
        'bolt_circle_diameter_mm': 1070.1
    },
    '40': {
        'nps': '40',
        'class': 150,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 40.00,
        'id_mm': 1016,
        'od_inches': 46.25,
        'od_mm': 1175,
        'number_of_holes': 44,
        'bolt_hole_diameter_inches': 1.13,
        'bolt_circle_diameter_inches': 44.13,
        'bolt_circle_diameter_mm': 1120.9
    },
    '42': {
        'nps': '42',
        'class': 150,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 42.00,
        'id_mm': 1067,
        'od_inches': 48.25,
        'od_mm': 1226,
        'number_of_holes': 48,
        'bolt_hole_diameter_inches': 1.13,
        'bolt_circle_diameter_inches': 46.13,
        'bolt_circle_diameter_mm': 1171.7
    },
    '44': {
        'nps': '44',
        'class': 150,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 44.00,
        'id_mm': 1118,
        'od_inches': 50.25,
        'od_mm': 1276,
        'number_of_holes': 52,
        'bolt_hole_diameter_inches': 1.13,
        'bolt_circle_diameter_inches': 48.13,
        'bolt_circle_diameter_mm': 1222.5
    },
    '46': {
        'nps': '46',
        'class': 150,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 46.00,
        'id_mm': 1168,
        'od_inches': 52.81,
        'od_mm': 1341,
        'number_of_holes': 40,
        'bolt_hole_diameter_inches': 1.25,
        'bolt_circle_diameter_inches': 50.56,
        'bolt_circle_diameter_mm': 1284.2
    },
    '48': {
        'nps': '48',
        'class': 150,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 48.00,
        'id_mm': 1219,
        'od_inches': 54.81,
        'od_mm': 1392,
        'number_of_holes': 44,
        'bolt_hole_diameter_inches': 1.25,
        'bolt_circle_diameter_inches': 52.56,
        'bolt_circle_diameter_mm': 1335.0
    },
    '50': {
        'nps': '50',
        'class': 150,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 50.00,
        'id_mm': 1270,
        'od_inches': 56.81,
        'od_mm': 1443,
        'number_of_holes': 48,
        'bolt_hole_diameter_inches': 1.25,
        'bolt_circle_diameter_inches': 54.56,
        'bolt_circle_diameter_mm': 1385.8
    },
    '52': {
        'nps': '52',
        'class': 150,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 52.00,
        'id_mm': 1321,
        'od_inches': 58.81,
        'od_mm': 1494,
        'number_of_holes': 52,
        'bolt_hole_diameter_inches': 1.25,
        'bolt_circle_diameter_inches': 56.56,
        'bolt_circle_diameter_mm': 1436.6
    },
    '54': {
        'nps': '54',
        'class': 150,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 54.00,
        'id_mm': 1372,
        'od_inches': 61.00,
        'od_mm': 1549,
        'number_of_holes': 56,
        'bolt_hole_diameter_inches': 1.25,
        'bolt_circle_diameter_inches': 58.75,
        'bolt_circle_diameter_mm': 1492.3
    },
    '56': {
        'nps': '56',
        'class': 150,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 56.00,
        'id_mm': 1422,
        'od_inches': 63.00,
        'od_mm': 1600,
        'number_of_holes': 60,
        'bolt_hole_diameter_inches': 1.25,
        'bolt_circle_diameter_inches': 60.75,
        'bolt_circle_diameter_mm': 1543.1
    },
    '58': {
        'nps': '58',
        'class': 150,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 58.00,
        'id_mm': 1473,
        'od_inches': 65.94,
        'od_mm': 1675,
        'number_of_holes': 48,
        'bolt_hole_diameter_inches': 1.38,
        'bolt_circle_diameter_inches': 63.44,
        'bolt_circle_diameter_mm': 1611.4
    },
    '60': {
        'nps': '60',
        'class': 150,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 60.00,
        'id_mm': 1524,
        'od_inches': 67.94,
        'od_mm': 1726,
        'number_of_holes': 52,
        'bolt_hole_diameter_inches': 1.38,
        'bolt_circle_diameter_inches': 65.44,
        'bolt_circle_diameter_mm': 1662.2
    },
}

# ASME B16.47 Series B Class 300 Full Face Gaskets
B1647B_CLASS300_FULL_FACE_GASKETS = {
    '26': {
        'nps': '26',
        'class': 300,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 26.00,
        'id_mm': 660,
        'od_inches': 34.13,
        'od_mm': 867,
        'number_of_holes': 32,
        'bolt_hole_diameter_inches': 1.38,
        'bolt_circle_diameter_inches': 31.63,
        'bolt_circle_diameter_mm': 803.4
    },
    '28': {
        'nps': '28',
        'class': 300,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 28.00,
        'id_mm': 711,
        'od_inches': 36.25,
        'od_mm': 921,
        'number_of_holes': 36,
        'bolt_hole_diameter_inches': 1.38,
        'bolt_circle_diameter_inches': 33.75,
        'bolt_circle_diameter_mm': 857.3
    },
    '30': {
        'nps': '30',
        'class': 300,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 30.00,
        'id_mm': 762,
        'od_inches': 39.00,
        'od_mm': 991,
        'number_of_holes': 36,
        'bolt_hole_diameter_inches': 1.50,
        'bolt_circle_diameter_inches': 36.25,
        'bolt_circle_diameter_mm': 920.8
    },
    '32': {
        'nps': '32',
        'class': 300,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 32.00,
        'id_mm': 813,
        'od_inches': 41.50,
        'od_mm': 1054,
        'number_of_holes': 32,
        'bolt_hole_diameter_inches': 1.63,
        'bolt_circle_diameter_inches': 38.50,
        'bolt_circle_diameter_mm': 977.9
    },
    '34': {
        'nps': '34',
        'class': 300,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 34.00,
        'id_mm': 864,
        'od_inches': 43.63,
        'od_mm': 1108,
        'number_of_holes': 36,
        'bolt_hole_diameter_inches': 1.63,
        'bolt_circle_diameter_inches': 40.63,
        'bolt_circle_diameter_mm': 1032.0
    },
    '36': {
        'nps': '36',
        'class': 300,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 36.00,
        'id_mm': 914,
        'od_inches': 46.13,
        'od_mm': 1172,
        'number_of_holes': 32,
        'bolt_hole_diameter_inches': 1.75,
        'bolt_circle_diameter_inches': 42.88,
        'bolt_circle_diameter_mm': 1089.2
    },
    '38': {
        'nps': '38',
        'class': 300,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 38.00,
        'id_mm': 965,
        'od_inches': 48.13,
        'od_mm': 1223,
        'number_of_holes': 36,
        'bolt_hole_diameter_inches': 1.75,
        'bolt_circle_diameter_inches': 44.88,
        'bolt_circle_diameter_mm': 1140.0
    },
    '40': {
        'nps': '40',
        'class': 300,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 40.00,
        'id_mm': 1016,
        'od_inches': 50.13,
        'od_mm': 1273,
        'number_of_holes': 40,
        'bolt_hole_diameter_inches': 1.75,
        'bolt_circle_diameter_inches': 46.88,
        'bolt_circle_diameter_mm': 1190.8
    },
    '42': {
        'nps': '42',
        'class': 300,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 42.00,
        'id_mm': 1067,
        'od_inches': 52.50,
        'od_mm': 1334,
        'number_of_holes': 36,
        'bolt_hole_diameter_inches': 1.88,
        'bolt_circle_diameter_inches': 49.00,
        'bolt_circle_diameter_mm': 1244.6
    },
    '44': {
        'nps': '44',
        'class': 300,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 44.00,
        'id_mm': 1118,
        'od_inches': 54.50,
        'od_mm': 1384,
        'number_of_holes': 40,
        'bolt_hole_diameter_inches': 1.88,
        'bolt_circle_diameter_inches': 51.00,
        'bolt_circle_diameter_mm': 1295.4
    },
    '46': {
        'nps': '46',
        'class': 300,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 46.00,
        'id_mm': 1168,
        'od_inches': 57.50,
        'od_mm': 1461,
        'number_of_holes': 36,
        'bolt_hole_diameter_inches': 2.00,
        'bolt_circle_diameter_inches': 53.75,
        'bolt_circle_diameter_mm': 1365.3
    },
    '48': {
        'nps': '48',
        'class': 300,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 48.00,
        'id_mm': 1219,
        'od_inches': 59.50,
        'od_mm': 1511,
        'number_of_holes': 40,
        'bolt_hole_diameter_inches': 2.00,
        'bolt_circle_diameter_inches': 55.75,
        'bolt_circle_diameter_mm': 1416.1
    },
    '50': {
        'nps': '50',
        'class': 300,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 50.00,
        'id_mm': 1270,
        'od_inches': 61.50,
        'od_mm': 1562,
        'number_of_holes': 44,
        'bolt_hole_diameter_inches': 2.00,
        'bolt_circle_diameter_inches': 57.75,
        'bolt_circle_diameter_mm': 1466.9
    },
    '52': {
        'nps': '52',
        'class': 300,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 52.00,
        'id_mm': 1321,
        'od_inches': 63.50,
        'od_mm': 1613,
        'number_of_holes': 48,
        'bolt_hole_diameter_inches': 2.00,
        'bolt_circle_diameter_inches': 59.75,
        'bolt_circle_diameter_mm': 1517.7
    },
    '54': {
        'nps': '54',
        'class': 300,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 54.00,
        'id_mm': 1372,
        'od_inches': 65.88,
        'od_mm': 1673,
        'number_of_holes': 48,
        'bolt_hole_diameter_inches': 2.00,
        'bolt_circle_diameter_inches': 62.13,
        'bolt_circle_diameter_mm': 1578.1
    },
    '56': {
        'nps': '56',
        'class': 300,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 56.00,
        'id_mm': 1422,
        'od_inches': 69.50,
        'od_mm': 1765,
        'number_of_holes': 36,
        'bolt_hole_diameter_inches': 2.38,
        'bolt_circle_diameter_inches': 65.00,
        'bolt_circle_diameter_mm': 1651.0
    },
    '58': {
        'nps': '58',
        'class': 300,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 58.00,
        'id_mm': 1473,
        'od_inches': 71.94,
        'od_mm': 1827,
        'number_of_holes': 40,
        'bolt_hole_diameter_inches': 2.38,
        'bolt_circle_diameter_inches': 67.44,
        'bolt_circle_diameter_mm': 1713.0
    },
    '60': {
        'nps': '60',
        'class': 300,
        'series': 'B',
        'gasket_type': 'full_face',
        'id_inches': 60.00,
        'id_mm': 1524,
        'od_inches': 73.94,
        'od_mm': 1878,
        'number_of_holes': 40,
        'bolt_hole_diameter_inches': 2.38,
        'bolt_circle_diameter_inches': 69.44,
        'bolt_circle_diameter_mm': 1763.8
    },
}


def get_gasket_info(nps, pressure_class, gasket_type='full_face', series=None):
    """
    Get gasket dimensions for a specific NPS, pressure class, and gasket type.
    
    Args:
        nps (str): Nominal pipe size (e.g., '1/2', '1', '1-1/4')
        pressure_class (int): Pressure class (150, 300, 600, etc.)
        gasket_type (str): 'full_face', 'ring', 'spiral_wound', 'ring_joint'
        series (str): For B16.47 flanges, specify 'A' or 'B'. None for B16.5 flanges.
    
    Returns:
        dict: Gasket dimensions or None if not found
    """
    # Map to appropriate gasket dictionary
    if pressure_class == 150 and gasket_type == 'full_face':
        if series == 'A':
            return B1647A_CLASS150_FULL_FACE_GASKETS.get(nps)
        elif series == 'B':
            return B1647B_CLASS150_FULL_FACE_GASKETS.get(nps)
        return B165_CLASS150_FULL_FACE_GASKETS.get(nps)
    elif pressure_class == 300 and gasket_type == 'full_face':
        if series == 'A':
            return B1647A_CLASS300_FULL_FACE_GASKETS.get(nps)
        elif series == 'B':
            return B1647B_CLASS300_FULL_FACE_GASKETS.get(nps)
        return B165_CLASS300_FULL_FACE_GASKETS.get(nps)
    elif pressure_class == 400 and gasket_type == 'full_face':
        return B165_CLASS400_FULL_FACE_GASKETS.get(nps)
    elif pressure_class == 600 and gasket_type == 'full_face':
        return B165_CLASS600_FULL_FACE_GASKETS.get(nps)
    elif pressure_class == 900 and gasket_type == 'full_face':
        return B165_CLASS900_FULL_FACE_GASKETS.get(nps)
    elif pressure_class == 150 and gasket_type == 'flat_ring':
        if series == 'A':
            return B1647A_CLASS150_FLAT_RING_GASKETS.get(nps)
        return B165_CLASS150_FLAT_RING_GASKETS.get(nps)
    elif pressure_class == 300 and gasket_type == 'flat_ring':
        if series == 'A':
            return B1647A_CLASS300_FLAT_RING_GASKETS.get(nps)
        return B165_CLASS300_FLAT_RING_GASKETS.get(nps)
    elif pressure_class == 400 and gasket_type == 'flat_ring':
        if series == 'A':
            return B1647A_CLASS400_FLAT_RING_GASKETS.get(nps)
        return B165_CLASS400_FLAT_RING_GASKETS.get(nps)
    elif pressure_class == 600 and gasket_type == 'flat_ring':
        if series == 'A':
            return B1647A_CLASS600_FLAT_RING_GASKETS.get(nps)
        return B165_CLASS600_FLAT_RING_GASKETS.get(nps)
    elif pressure_class == 900 and gasket_type == 'flat_ring':
        return B165_CLASS900_FLAT_RING_GASKETS.get(nps)
    elif pressure_class == 150 and gasket_type == 'spiral_wound':
        if series == 'A':
            return B1647A_CLASS150_SPIRAL_WOUND_GASKETS.get(nps)
        elif series == 'B':
            return B1647B_CLASS150_SPIRAL_WOUND_GASKETS.get(nps)
        return B165_CLASS150_SPIRAL_WOUND_GASKETS.get(nps)
    elif pressure_class == 300 and gasket_type == 'spiral_wound':
        if series == 'A':
            return B1647A_CLASS300_SPIRAL_WOUND_GASKETS.get(nps)
        elif series == 'B':
            return B1647B_CLASS300_SPIRAL_WOUND_GASKETS.get(nps)
        return B165_CLASS300_SPIRAL_WOUND_GASKETS.get(nps)
    elif pressure_class == 400 and gasket_type == 'spiral_wound':
        if series == 'A':
            return B1647A_CLASS400_SPIRAL_WOUND_GASKETS.get(nps)
        elif series == 'B':
            return B1647B_CLASS400_SPIRAL_WOUND_GASKETS.get(nps)
        return B165_CLASS400_SPIRAL_WOUND_GASKETS.get(nps)
    elif pressure_class == 600 and gasket_type == 'spiral_wound':
        if series == 'A':
            return B1647A_CLASS600_SPIRAL_WOUND_GASKETS.get(nps)
        elif series == 'B':
            return B1647B_CLASS600_SPIRAL_WOUND_GASKETS.get(nps)
        return B165_CLASS600_SPIRAL_WOUND_GASKETS.get(nps)
    elif pressure_class == 900 and gasket_type == 'spiral_wound':
        if series == 'A':
            return B1647A_CLASS900_SPIRAL_WOUND_GASKETS.get(nps)
        elif series == 'B':
            return B1647B_CLASS900_SPIRAL_WOUND_GASKETS.get(nps)
        return B165_CLASS900_SPIRAL_WOUND_GASKETS.get(nps)
    elif pressure_class == 1500 and gasket_type == 'spiral_wound':
        return B165_CLASS1500_SPIRAL_WOUND_GASKETS.get(nps)
    elif pressure_class == 2500 and gasket_type == 'spiral_wound':
        return B165_CLASS2500_SPIRAL_WOUND_GASKETS.get(nps)
    elif gasket_type == 'ring_joint':
        # Check if RX series (starts with 'RX-') or Type R (starts with 'R-')
        if nps.startswith('RX-'):
            return RING_JOINT_TYPE_RX_GASKETS.get(nps)
        else:
            return RING_JOINT_TYPE_R_GASKETS.get(nps)
    
    return None


def list_gasket_sizes(pressure_class, gasket_type='full_face', series=None):
    """
    List all available gasket sizes for a given pressure class and type.
    
    Args:
        pressure_class (int): Pressure class (150, 300, 600, etc.)
        gasket_type (str): 'full_face', 'ring', 'spiral_wound', 'ring_joint'
        series (str): For B16.47 flanges, specify 'A' or 'B'. None for B16.5 flanges.
    
    Returns:
        list: Available sizes sorted
    """
    def nps_to_float(nps_str):
        """Convert fractional NPS string to float for sorting."""
        if '-' in nps_str and '/' in nps_str:
            parts = nps_str.split('-')
            whole = float(parts[0])
            frac_parts = parts[1].split('/')
            frac = float(frac_parts[0]) / float(frac_parts[1])
            return whole + frac
        elif '/' in nps_str:
            parts = nps_str.split('/')
            return float(parts[0]) / float(parts[1])
        else:
            return float(nps_str)
    
    if pressure_class == 150 and gasket_type == 'full_face':
        if series == 'A':
            return sorted(B1647A_CLASS150_FULL_FACE_GASKETS.keys(), key=nps_to_float)
        elif series == 'B':
            return sorted(B1647B_CLASS150_FULL_FACE_GASKETS.keys(), key=nps_to_float)
        return sorted(B165_CLASS150_FULL_FACE_GASKETS.keys(), key=nps_to_float)
    elif pressure_class == 300 and gasket_type == 'full_face':
        if series == 'A':
            return sorted(B1647A_CLASS300_FULL_FACE_GASKETS.keys(), key=nps_to_float)
        elif series == 'B':
            return sorted(B1647B_CLASS300_FULL_FACE_GASKETS.keys(), key=nps_to_float)
        return sorted(B165_CLASS300_FULL_FACE_GASKETS.keys(), key=nps_to_float)
    elif pressure_class == 400 and gasket_type == 'full_face':
        return sorted(B165_CLASS400_FULL_FACE_GASKETS.keys(), key=nps_to_float)
    elif pressure_class == 600 and gasket_type == 'full_face':
        return sorted(B165_CLASS600_FULL_FACE_GASKETS.keys(), key=nps_to_float)
    elif pressure_class == 900 and gasket_type == 'full_face':
        return sorted(B165_CLASS900_FULL_FACE_GASKETS.keys(), key=nps_to_float)
    elif pressure_class == 150 and gasket_type == 'flat_ring':
        if series == 'A':
            return sorted(B1647A_CLASS150_FLAT_RING_GASKETS.keys(), key=nps_to_float)
        return sorted(B165_CLASS150_FLAT_RING_GASKETS.keys(), key=nps_to_float)
    elif pressure_class == 300 and gasket_type == 'flat_ring':
        if series == 'A':
            return sorted(B1647A_CLASS300_FLAT_RING_GASKETS.keys(), key=nps_to_float)
        return sorted(B165_CLASS300_FLAT_RING_GASKETS.keys(), key=nps_to_float)
    elif pressure_class == 400 and gasket_type == 'flat_ring':
        if series == 'A':
            return sorted(B1647A_CLASS400_FLAT_RING_GASKETS.keys(), key=nps_to_float)
        return sorted(B165_CLASS400_FLAT_RING_GASKETS.keys(), key=nps_to_float)
    elif pressure_class == 600 and gasket_type == 'flat_ring':
        if series == 'A':
            return sorted(B1647A_CLASS600_FLAT_RING_GASKETS.keys(), key=nps_to_float)
        return sorted(B165_CLASS600_FLAT_RING_GASKETS.keys(), key=nps_to_float)
    elif pressure_class == 900 and gasket_type == 'flat_ring':
        return sorted(B165_CLASS900_FLAT_RING_GASKETS.keys(), key=nps_to_float)
    elif pressure_class == 150 and gasket_type == 'spiral_wound':
        if series == 'A':
            return sorted(B1647A_CLASS150_SPIRAL_WOUND_GASKETS.keys(), key=nps_to_float)
        elif series == 'B':
            return sorted(B1647B_CLASS150_SPIRAL_WOUND_GASKETS.keys(), key=nps_to_float)
        return sorted(B165_CLASS150_SPIRAL_WOUND_GASKETS.keys(), key=nps_to_float)
    elif pressure_class == 300 and gasket_type == 'spiral_wound':
        if series == 'A':
            return sorted(B1647A_CLASS300_SPIRAL_WOUND_GASKETS.keys(), key=nps_to_float)
        elif series == 'B':
            return sorted(B1647B_CLASS300_SPIRAL_WOUND_GASKETS.keys(), key=nps_to_float)
        return sorted(B165_CLASS300_SPIRAL_WOUND_GASKETS.keys(), key=nps_to_float)
    elif pressure_class == 400 and gasket_type == 'spiral_wound':
        if series == 'A':
            return sorted(B1647A_CLASS400_SPIRAL_WOUND_GASKETS.keys(), key=nps_to_float)
        elif series == 'B':
            return sorted(B1647B_CLASS400_SPIRAL_WOUND_GASKETS.keys(), key=nps_to_float)
        return sorted(B165_CLASS400_SPIRAL_WOUND_GASKETS.keys(), key=nps_to_float)
    elif pressure_class == 600 and gasket_type == 'spiral_wound':
        if series == 'A':
            return sorted(B1647A_CLASS600_SPIRAL_WOUND_GASKETS.keys(), key=nps_to_float)
        elif series == 'B':
            return sorted(B1647B_CLASS600_SPIRAL_WOUND_GASKETS.keys(), key=nps_to_float)
        return sorted(B165_CLASS600_SPIRAL_WOUND_GASKETS.keys(), key=nps_to_float)
    elif pressure_class == 900 and gasket_type == 'spiral_wound':
        if series == 'A':
            return sorted(B1647A_CLASS900_SPIRAL_WOUND_GASKETS.keys(), key=nps_to_float)
        elif series == 'B':
            return sorted(B1647B_CLASS900_SPIRAL_WOUND_GASKETS.keys(), key=nps_to_float)
        return sorted(B165_CLASS900_SPIRAL_WOUND_GASKETS.keys(), key=nps_to_float)
    elif pressure_class == 1500 and gasket_type == 'spiral_wound':
        return sorted(B165_CLASS1500_SPIRAL_WOUND_GASKETS.keys(), key=nps_to_float)
    elif pressure_class == 2500 and gasket_type == 'spiral_wound':
        return sorted(B165_CLASS2500_SPIRAL_WOUND_GASKETS.keys(), key=nps_to_float)
    elif gasket_type == 'ring_joint':
        # Combine both Type R and Type RX rings
        all_rings = list(RING_JOINT_TYPE_R_GASKETS.keys()) + list(RING_JOINT_TYPE_RX_GASKETS.keys())
        return sorted(all_rings)
    
    return []


# Example usage and testing
if __name__ == "__main__":
    print("ASME B16.5 Gasket Dimensions Database")
    print("=" * 70)
    
    # Test Class 150 Full Face gaskets
    test_sizes = ['1/2', '2', '6', '12', '24']
    
    print("\nClass 150 Full Face Gasket Specifications:")
    for size in test_sizes:
        info = get_gasket_info(size, 150, 'full_face')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}):")
            print(f"    ID: {info['id_inches']}\" ({info['id_mm']}mm)")
            print(f"    OD: {info['od_inches']}\" ({info['od_mm']}mm)")
            print(f"    Bolt Holes: {info['number_of_holes']} x {info['bolt_hole_diameter_inches']}\" dia")
            print(f"    Bolt Circle: {info['bolt_circle_diameter_inches']}\" ({info['bolt_circle_diameter_mm']}mm)")
    
    # Test Class 300 Full Face gaskets
    print("\n" + "=" * 70)
    print("\nClass 300 Full Face Gasket Specifications:")
    for size in test_sizes:
        info = get_gasket_info(size, 300, 'full_face')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}):")
            print(f"    ID: {info['id_inches']}\" ({info['id_mm']}mm)")
            print(f"    OD: {info['od_inches']}\" ({info['od_mm']}mm)")
            print(f"    Bolt Holes: {info['number_of_holes']} x {info['bolt_hole_diameter_inches']}\" dia")
            print(f"    Bolt Circle: {info['bolt_circle_diameter_inches']}\" ({info['bolt_circle_diameter_mm']}mm)")
    
    # Test Class 400 Full Face gaskets
    print("\n" + "=" * 70)
    print("\nClass 400 Full Face Gasket Specifications:")
    for size in test_sizes:
        info = get_gasket_info(size, 400, 'full_face')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}):")
            print(f"    ID: {info['id_inches']}\" ({info['id_mm']}mm)")
            print(f"    OD: {info['od_inches']}\" ({info['od_mm']}mm)")
            print(f"    Bolt Holes: {info['number_of_holes']} x {info['bolt_hole_diameter_inches']}\" dia")
            print(f"    Bolt Circle: {info['bolt_circle_diameter_inches']}\" ({info['bolt_circle_diameter_mm']}mm)")
    
    # Test Class 600 Full Face gaskets
    print("\n" + "=" * 70)
    print("\nClass 600 Full Face Gasket Specifications:")
    for size in test_sizes:
        info = get_gasket_info(size, 600, 'full_face')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}):")
            print(f"    ID: {info['id_inches']}\" ({info['id_mm']}mm)")
            print(f"    OD: {info['od_inches']}\" ({info['od_mm']}mm)")
            print(f"    Bolt Holes: {info['number_of_holes']} x {info['bolt_hole_diameter_inches']}\" dia")
            print(f"    Bolt Circle: {info['bolt_circle_diameter_inches']}\" ({info['bolt_circle_diameter_mm']}mm)")
    
    # Test Class 900 Full Face gaskets
    print("\n" + "=" * 70)
    print("\nClass 900 Full Face Gasket Specifications:")
    for size in test_sizes:
        info = get_gasket_info(size, 900, 'full_face')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}):")
            print(f"    ID: {info['id_inches']}\" ({info['id_mm']}mm)")
            print(f"    OD: {info['od_inches']}\" ({info['od_mm']}mm)")
            if info['number_of_holes'] is not None:
                print(f"    Bolt Holes: {info['number_of_holes']} x {info['bolt_hole_diameter_inches']}\" dia")
                print(f"    Bolt Circle: {info['bolt_circle_diameter_inches']}\" ({info['bolt_circle_diameter_mm']}mm)")
            else:
                print(f"    Bolt Holes: Data not available")
    
    # List all available sizes
    print("\n" + "=" * 70)
    print("Available sizes:")
    sizes_150 = list_gasket_sizes(150, 'full_face')
    print(f"  Class 150 Full Face (B16.5): {', '.join(sizes_150)} ({len(sizes_150)} sizes)")
    sizes_300 = list_gasket_sizes(300, 'full_face')
    print(f"  Class 300 Full Face: {', '.join(sizes_300)} ({len(sizes_300)} sizes)")
    sizes_400 = list_gasket_sizes(400, 'full_face')
    print(f"  Class 400 Full Face: {', '.join(sizes_400)} ({len(sizes_400)} sizes)")
    sizes_600 = list_gasket_sizes(600, 'full_face')
    print(f"  Class 600 Full Face: {', '.join(sizes_600)} ({len(sizes_600)} sizes)")
    sizes_900 = list_gasket_sizes(900, 'full_face')
    print(f"  Class 900 Full Face: {', '.join(sizes_900)} ({len(sizes_900)} sizes)")
    
    # Test B16.47 Series A Class 150 Full Face gaskets
    print("\n" + "=" * 70)
    print("\nB16.47 Series A Class 150 Full Face Gasket Specifications:")
    b1647_test_sizes = ['26', '36', '48', '60']
    for size in b1647_test_sizes:
        info = get_gasket_info(size, 150, 'full_face', series='A')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}, Series {info['series']}):")
            print(f"    ID: {info['id_inches']}\" ({info['id_mm']}mm)")
            print(f"    OD: {info['od_inches']}\" ({info['od_mm']}mm)")
            print(f"    Bolt Holes: {info['number_of_holes']} x {info['bolt_hole_diameter_inches']}\" dia")
            print(f"    Bolt Circle: {info['bolt_circle_diameter_inches']}\" ({info['bolt_circle_diameter_mm']}mm)")
    
    sizes_b1647a_150 = list_gasket_sizes(150, 'full_face', series='A')
    print(f"\n  B16.47 Series A Class 150 Full Face: {', '.join(sizes_b1647a_150)} ({len(sizes_b1647a_150)} sizes)")
    
    # Test B16.47 Series A Class 300 Full Face gaskets
    print("\n" + "=" * 70)
    print("\nB16.47 Series A Class 300 Full Face Gasket Specifications:")
    for size in b1647_test_sizes:
        info = get_gasket_info(size, 300, 'full_face', series='A')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}, Series {info['series']}):")
            print(f"    ID: {info['id_inches']}\" ({info['id_mm']}mm)")
            print(f"    OD: {info['od_inches']}\" ({info['od_mm']}mm)")
            print(f"    Bolt Holes: {info['number_of_holes']} x {info['bolt_hole_diameter_inches']}\" dia")
            print(f"    Bolt Circle: {info['bolt_circle_diameter_inches']}\" ({info['bolt_circle_diameter_mm']}mm)")
    
    sizes_b1647a_300 = list_gasket_sizes(300, 'full_face', series='A')
    print(f"\n  B16.47 Series A Class 300 Full Face: {', '.join(sizes_b1647a_300)} ({len(sizes_b1647a_300)} sizes)")
    
    # Test B16.47 Series B Class 150 Full Face gaskets
    print("\n" + "=" * 70)
    print("\nB16.47 Series B Class 150 Full Face Gasket Specifications:")
    for size in b1647_test_sizes:
        info = get_gasket_info(size, 150, 'full_face', series='B')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}, Series {info['series']}):")
            print(f"    ID: {info['id_inches']}\" ({info['id_mm']}mm)")
            print(f"    OD: {info['od_inches']}\" ({info['od_mm']}mm)")
            print(f"    Bolt Holes: {info['number_of_holes']} x {info['bolt_hole_diameter_inches']}\" dia")
            print(f"    Bolt Circle: {info['bolt_circle_diameter_inches']}\" ({info['bolt_circle_diameter_mm']}mm)")
    
    sizes_b1647b_150 = list_gasket_sizes(150, 'full_face', series='B')
    print(f"\n  B16.47 Series B Class 150 Full Face: {', '.join(sizes_b1647b_150)} ({len(sizes_b1647b_150)} sizes)")
    
    # Test B16.47 Series B Class 300 Full Face gaskets
    print("\n" + "=" * 70)
    print("\nB16.47 Series B Class 300 Full Face Gasket Specifications:")
    for size in b1647_test_sizes:
        info = get_gasket_info(size, 300, 'full_face', series='B')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}, Series {info['series']}):")
            print(f"    ID: {info['id_inches']}\" ({info['id_mm']}mm)")
            print(f"    OD: {info['od_inches']}\" ({info['od_mm']}mm)")
            print(f"    Bolt Holes: {info['number_of_holes']} x {info['bolt_hole_diameter_inches']}\" dia")
            print(f"    Bolt Circle: {info['bolt_circle_diameter_inches']}\" ({info['bolt_circle_diameter_mm']}mm)")
    
    sizes_b1647b_300 = list_gasket_sizes(300, 'full_face', series='B')
    print(f"\n  B16.47 Series B Class 300 Full Face: {', '.join(sizes_b1647b_300)} ({len(sizes_b1647b_300)} sizes)")
    
    # Test Class 150 Flat Ring gaskets
    print("\n" + "=" * 70)
    print("\nClass 150 Flat Ring Gasket Specifications:")
    for size in test_sizes:
        info = get_gasket_info(size, 150, 'flat_ring')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}, Type: {info['gasket_type']}):")
            print(f"    ID: {info['id_inches']}\" ({info['id_mm']}mm)")
            print(f"    OD: {info['od_inches']}\" ({info['od_mm']}mm)")
    
    sizes_flat_ring_150 = list_gasket_sizes(150, 'flat_ring')
    print(f"\n  Class 150 Flat Ring: {', '.join(sizes_flat_ring_150)} ({len(sizes_flat_ring_150)} sizes)")
    
    # Test Class 300 Flat Ring gaskets
    print("\n" + "=" * 70)
    print("\nClass 300 Flat Ring Gasket Specifications:")
    for size in test_sizes:
        info = get_gasket_info(size, 300, 'flat_ring')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}, Type: {info['gasket_type']}):")
            print(f"    ID: {info['id_inches']}\" ({info['id_mm']}mm)")
            print(f"    OD: {info['od_inches']}\" ({info['od_mm']}mm)")
    
    sizes_flat_ring_300 = list_gasket_sizes(300, 'flat_ring')
    print(f"\n  Class 300 Flat Ring: {', '.join(sizes_flat_ring_300)} ({len(sizes_flat_ring_300)} sizes)")
    
    # Test Class 400 Flat Ring gaskets
    print("\n" + "=" * 70)
    print("\nClass 400 Flat Ring Gasket Specifications:")
    for size in test_sizes:
        info = get_gasket_info(size, 400, 'flat_ring')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}, Type: {info['gasket_type']}):")
            print(f"    ID: {info['id_inches']}\" ({info['id_mm']}mm)")
            print(f"    OD: {info['od_inches']}\" ({info['od_mm']}mm)")
    
    sizes_flat_ring_400 = list_gasket_sizes(400, 'flat_ring')
    print(f"\n  Class 400 Flat Ring: {', '.join(sizes_flat_ring_400)} ({len(sizes_flat_ring_400)} sizes)")
    
    # Test Class 600 Flat Ring gaskets
    print("\n" + "=" * 70)
    print("\nClass 600 Flat Ring Gasket Specifications:")
    for size in test_sizes:
        info = get_gasket_info(size, 600, 'flat_ring')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}, Type: {info['gasket_type']}):")
            print(f"    ID: {info['id_inches']}\" ({info['id_mm']}mm)")
            print(f"    OD: {info['od_inches']}\" ({info['od_mm']}mm)")
    
    sizes_flat_ring_600 = list_gasket_sizes(600, 'flat_ring')
    print(f"\n  Class 600 Flat Ring: {', '.join(sizes_flat_ring_600)} ({len(sizes_flat_ring_600)} sizes)")
    
    # Test Class 900 Flat Ring gaskets
    print("\n" + "=" * 70)
    print("\nClass 900 Flat Ring Gasket Specifications:")
    for size in test_sizes:
        info = get_gasket_info(size, 900, 'flat_ring')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}, Type: {info['gasket_type']}):")
            print(f"    ID: {info['id_inches']}\" ({info['id_mm']}mm)")
            print(f"    OD: {info['od_inches']}\" ({info['od_mm']}mm)")
    
    sizes_flat_ring_900 = list_gasket_sizes(900, 'flat_ring')
    print(f"\n  Class 900 Flat Ring: {', '.join(sizes_flat_ring_900)} ({len(sizes_flat_ring_900)} sizes)")
    
    # Test B16.47 Series A Flat Ring gaskets
    b1647_test_sizes = ['26', '36', '48', '60']
    
    print("\n" + "=" * 70)
    print("\nB16.47 Series A Class 150 Flat Ring Gasket Specifications:")
    for size in b1647_test_sizes:
        info = get_gasket_info(size, 150, 'flat_ring', series='A')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}, Series {info['series']}, Type: {info['gasket_type']}):")
            print(f"    ID: {info['id_inches']}\" ({info['id_mm']}mm)")
            print(f"    OD: {info['od_inches']}\" ({info['od_mm']}mm)")
    
    sizes_b1647a_150_fr = list_gasket_sizes(150, 'flat_ring', series='A')
    print(f"\n  B16.47 Series A Class 150 Flat Ring: {', '.join(sizes_b1647a_150_fr)} ({len(sizes_b1647a_150_fr)} sizes)")
    
    print("\n" + "=" * 70)
    print("\nB16.47 Series A Class 300 Flat Ring Gasket Specifications:")
    for size in b1647_test_sizes:
        info = get_gasket_info(size, 300, 'flat_ring', series='A')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}, Series {info['series']}, Type: {info['gasket_type']}):")
            print(f"    ID: {info['id_inches']}\" ({info['id_mm']}mm)")
            print(f"    OD: {info['od_inches']}\" ({info['od_mm']}mm)")
    
    sizes_b1647a_300_fr = list_gasket_sizes(300, 'flat_ring', series='A')
    print(f"\n  B16.47 Series A Class 300 Flat Ring: {', '.join(sizes_b1647a_300_fr)} ({len(sizes_b1647a_300_fr)} sizes)")
    
    print("\n" + "=" * 70)
    print("\nB16.47 Series A Class 400 Flat Ring Gasket Specifications:")
    for size in b1647_test_sizes:
        info = get_gasket_info(size, 400, 'flat_ring', series='A')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}, Series {info['series']}, Type: {info['gasket_type']}):")
            print(f"    ID: {info['id_inches']}\" ({info['id_mm']}mm)")
            print(f"    OD: {info['od_inches']}\" ({info['od_mm']}mm)")
    
    sizes_b1647a_400_fr = list_gasket_sizes(400, 'flat_ring', series='A')
    print(f"\n  B16.47 Series A Class 400 Flat Ring: {', '.join(sizes_b1647a_400_fr)} ({len(sizes_b1647a_400_fr)} sizes)")
    
    print("\n" + "=" * 70)
    print("\nB16.47 Series A Class 600 Flat Ring Gasket Specifications:")
    for size in b1647_test_sizes:
        info = get_gasket_info(size, 600, 'flat_ring', series='A')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}, Series {info['series']}, Type: {info['gasket_type']}):")
            print(f"    ID: {info['id_inches']}\" ({info['id_mm']}mm)")
            print(f"    OD: {info['od_inches']}\" ({info['od_mm']}mm)")
    
    sizes_b1647a_600_fr = list_gasket_sizes(600, 'flat_ring', series='A')
    print(f"\n  B16.47 Series A Class 600 Flat Ring: {', '.join(sizes_b1647a_600_fr)} ({len(sizes_b1647a_600_fr)} sizes)")
    
    # Test Class 150 Spiral Wound gaskets
    print("\n" + "=" * 70)
    print("\nClass 150 Spiral Wound Gasket Specifications:")
    for size in test_sizes:
        info = get_gasket_info(size, 150, 'spiral_wound')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}, Type: {info['gasket_type']}):")
            if info['inner_ring_id_mm'] is not None:
                print(f"    Inner Ring ID: {info['inner_ring_id_mm']}mm")
            else:
                print(f"    Inner Ring ID: N/A")
            print(f"    Sealing Element ID: {info['sealing_element_id_mm']}mm")
            print(f"    Sealing Element OD: {info['sealing_element_od_mm']}mm")
            print(f"    Outer Ring OD: {info['outer_ring_od_mm']}mm")
    
    sizes_spiral_150 = list_gasket_sizes(150, 'spiral_wound')
    print(f"\n  Class 150 Spiral Wound: {', '.join(sizes_spiral_150)} ({len(sizes_spiral_150)} sizes)")
    
    # Test Class 300 Spiral Wound gaskets
    print("\n" + "=" * 70)
    print("\nClass 300 Spiral Wound Gasket Specifications:")
    for size in test_sizes:
        info = get_gasket_info(size, 300, 'spiral_wound')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}, Type: {info['gasket_type']}):")
            if info['inner_ring_id_mm'] is not None:
                print(f"    Inner Ring ID: {info['inner_ring_id_mm']}mm")
            else:
                print(f"    Inner Ring ID: N/A")
            print(f"    Sealing Element ID: {info['sealing_element_id_mm']}mm")
            print(f"    Sealing Element OD: {info['sealing_element_od_mm']}mm")
            print(f"    Outer Ring OD: {info['outer_ring_od_mm']}mm")
    
    sizes_spiral_300 = list_gasket_sizes(300, 'spiral_wound')
    print(f"\n  Class 300 Spiral Wound: {', '.join(sizes_spiral_300)} ({len(sizes_spiral_300)} sizes)")
    
    # Test Class 400 Spiral Wound gaskets
    print("\n" + "=" * 70)
    print("\nClass 400 Spiral Wound Gasket Specifications:")
    for size in test_sizes:
        info = get_gasket_info(size, 400, 'spiral_wound')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}, Type: {info['gasket_type']}):")
            if info['inner_ring_id_mm'] is not None:
                print(f"    Inner Ring ID: {info['inner_ring_id_mm']}mm")
            else:
                print(f"    Inner Ring ID: N/A")
            print(f"    Sealing Element ID: {info['sealing_element_id_mm']}mm")
            print(f"    Sealing Element OD: {info['sealing_element_od_mm']}mm")
            print(f"    Outer Ring OD: {info['outer_ring_od_mm']}mm")
    
    sizes_spiral_400 = list_gasket_sizes(400, 'spiral_wound')
    print(f"\n  Class 400 Spiral Wound: {', '.join(sizes_spiral_400)} ({len(sizes_spiral_400)} sizes)")
    
    # Test Class 600 Spiral Wound gaskets
    print("\n" + "=" * 70)
    print("\nClass 600 Spiral Wound Gasket Specifications:")
    for size in test_sizes:
        info = get_gasket_info(size, 600, 'spiral_wound')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}, Type: {info['gasket_type']}):")
            if info['inner_ring_id_mm'] is not None:
                print(f"    Inner Ring ID: {info['inner_ring_id_mm']}mm")
            else:
                print(f"    Inner Ring ID: N/A")
            print(f"    Sealing Element ID: {info['sealing_element_id_mm']}mm")
            print(f"    Sealing Element OD: {info['sealing_element_od_mm']}mm")
            print(f"    Outer Ring OD: {info['outer_ring_od_mm']}mm")
    
    sizes_spiral_600 = list_gasket_sizes(600, 'spiral_wound')
    print(f"\n  Class 600 Spiral Wound: {', '.join(sizes_spiral_600)} ({len(sizes_spiral_600)} sizes)")
    
    # Test Class 900 Spiral Wound gaskets
    print("\n" + "=" * 70)
    print("\nClass 900 Spiral Wound Gasket Specifications:")
    for size in test_sizes:
        info = get_gasket_info(size, 900, 'spiral_wound')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}, Type: {info['gasket_type']}):")
            if info['inner_ring_id_mm'] is not None:
                print(f"    Inner Ring ID: {info['inner_ring_id_mm']}mm")
            else:
                print(f"    Inner Ring ID: N/A")
            print(f"    Sealing Element ID: {info['sealing_element_id_mm']}mm")
            print(f"    Sealing Element OD: {info['sealing_element_od_mm']}mm")
            print(f"    Outer Ring OD: {info['outer_ring_od_mm']}mm")
    
    sizes_spiral_900 = list_gasket_sizes(900, 'spiral_wound')
    print(f"\n  Class 900 Spiral Wound: {', '.join(sizes_spiral_900)} ({len(sizes_spiral_900)} sizes)")
    
    # Test Class 1500 Spiral Wound gaskets
    print("\n" + "=" * 70)
    print("\nClass 1500 Spiral Wound Gasket Specifications:")
    for size in test_sizes:
        info = get_gasket_info(size, 1500, 'spiral_wound')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}, Type: {info['gasket_type']}):")
            if info['inner_ring_id_mm'] is not None:
                print(f"    Inner Ring ID: {info['inner_ring_id_mm']}mm")
            else:
                print(f"    Inner Ring ID: N/A")
            print(f"    Sealing Element ID: {info['sealing_element_id_mm']}mm")
            print(f"    Sealing Element OD: {info['sealing_element_od_mm']}mm")
            print(f"    Outer Ring OD: {info['outer_ring_od_mm']}mm")
    
    sizes_spiral_1500 = list_gasket_sizes(1500, 'spiral_wound')
    print(f"\n  Class 1500 Spiral Wound: {', '.join(sizes_spiral_1500)} ({len(sizes_spiral_1500)} sizes)")
    
    # Test Class 2500 Spiral Wound gaskets (limited to NPS 12" and below, no 3-1/2" or 4-1/2")
    print("\n" + "=" * 70)
    print("\nClass 2500 Spiral Wound Gasket Specifications:")
    test_sizes_2500 = ['1/2', '2', '6', '10', '12']
    for size in test_sizes_2500:
        info = get_gasket_info(size, 2500, 'spiral_wound')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}, Type: {info['gasket_type']}):")
            if info['inner_ring_id_mm'] is not None:
                print(f"    Inner Ring ID: {info['inner_ring_id_mm']}mm")
            else:
                print(f"    Inner Ring ID: N/A")
            print(f"    Sealing Element ID: {info['sealing_element_id_mm']}mm")
            print(f"    Sealing Element OD: {info['sealing_element_od_mm']}mm")
            print(f"    Outer Ring OD: {info['outer_ring_od_mm']}mm")
    
    sizes_spiral_2500 = list_gasket_sizes(2500, 'spiral_wound')
    print(f"\n  Class 2500 Spiral Wound: {', '.join(sizes_spiral_2500)} ({len(sizes_spiral_2500)} sizes)")
    print("  Note: Class 2500 available only through NPS 12\", excludes 3-1/2\" and 4-1/2\"")
    
    # Test B16.47 Series A Class 150 Spiral Wound gaskets
    print("\n" + "=" * 70)
    print("\nB16.47 Series A Class 150 Spiral Wound Gasket Specifications:")
    test_sizes_series_a = ['26', '36', '48', '60']
    for size in test_sizes_series_a:
        info = get_gasket_info(size, 150, 'spiral_wound', series='A')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}, Series {info['series']}, Type: {info['gasket_type']}):")
            print(f"    Inner Ring ID: {info['inner_ring_id_mm']}mm")
            print(f"    Sealing Element ID: {info['sealing_element_id_mm']}mm")
            print(f"    Sealing Element OD: {info['sealing_element_od_mm']}mm")
            print(f"    Outer Ring OD: {info['outer_ring_od_mm']}mm")
    
    sizes_spiral_series_a_150 = list_gasket_sizes(150, 'spiral_wound', series='A')
    print(f"\n  B16.47 Series A Class 150 Spiral Wound: {', '.join(sizes_spiral_series_a_150)} ({len(sizes_spiral_series_a_150)} sizes)")
    
    # Test B16.47 Series A Class 300 Spiral Wound gaskets
    print("\n" + "=" * 70)
    print("\nB16.47 Series A Class 300 Spiral Wound Gasket Specifications:")
    for size in test_sizes_series_a:
        info = get_gasket_info(size, 300, 'spiral_wound', series='A')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}, Series {info['series']}, Type: {info['gasket_type']}):")
            print(f"    Inner Ring ID: {info['inner_ring_id_mm']}mm")
            print(f"    Sealing Element ID: {info['sealing_element_id_mm']}mm")
            print(f"    Sealing Element OD: {info['sealing_element_od_mm']}mm")
            print(f"    Outer Ring OD: {info['outer_ring_od_mm']}mm")
    
    sizes_spiral_series_a_300 = list_gasket_sizes(300, 'spiral_wound', series='A')
    print(f"\n  B16.47 Series A Class 300 Spiral Wound: {', '.join(sizes_spiral_series_a_300)} ({len(sizes_spiral_series_a_300)} sizes)")
    
    # Test B16.47 Series A Class 400 Spiral Wound gaskets
    print("\n" + "=" * 70)
    print("\nB16.47 Series A Class 400 Spiral Wound Gasket Specifications:")
    for size in test_sizes_series_a:
        info = get_gasket_info(size, 400, 'spiral_wound', series='A')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}, Series {info['series']}, Type: {info['gasket_type']}):")
            print(f"    Inner Ring ID: {info['inner_ring_id_mm']}mm")
            print(f"    Sealing Element ID: {info['sealing_element_id_mm']}mm")
            print(f"    Sealing Element OD: {info['sealing_element_od_mm']}mm")
            print(f"    Outer Ring OD: {info['outer_ring_od_mm']}mm")
    
    sizes_spiral_series_a_400 = list_gasket_sizes(400, 'spiral_wound', series='A')
    print(f"\n  B16.47 Series A Class 400 Spiral Wound: {', '.join(sizes_spiral_series_a_400)} ({len(sizes_spiral_series_a_400)} sizes)")
    
    # Test B16.47 Series A Class 600 Spiral Wound gaskets
    print("\n" + "=" * 70)
    print("\nB16.47 Series A Class 600 Spiral Wound Gasket Specifications:")
    for size in test_sizes_series_a:
        info = get_gasket_info(size, 600, 'spiral_wound', series='A')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}, Series {info['series']}, Type: {info['gasket_type']}):")
            print(f"    Inner Ring ID: {info['inner_ring_id_mm']}mm")
            print(f"    Sealing Element ID: {info['sealing_element_id_mm']}mm")
            print(f"    Sealing Element OD: {info['sealing_element_od_mm']}mm")
            print(f"    Outer Ring OD: {info['outer_ring_od_mm']}mm")
    
    sizes_spiral_series_a_600 = list_gasket_sizes(600, 'spiral_wound', series='A')
    print(f"\n  B16.47 Series A Class 600 Spiral Wound: {', '.join(sizes_spiral_series_a_600)} ({len(sizes_spiral_series_a_600)} sizes)")
    
    # Test B16.47 Series A Class 900 Spiral Wound gaskets (limited to NPS 48" and below)
    print("\n" + "=" * 70)
    print("\nB16.47 Series A Class 900 Spiral Wound Gasket Specifications:")
    test_sizes_series_a_900 = ['26', '36', '44', '48']
    for size in test_sizes_series_a_900:
        info = get_gasket_info(size, 900, 'spiral_wound', series='A')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}, Series {info['series']}, Type: {info['gasket_type']}):")
            print(f"    Inner Ring ID: {info['inner_ring_id_mm']}mm")
            print(f"    Sealing Element ID: {info['sealing_element_id_mm']}mm")
            print(f"    Sealing Element OD: {info['sealing_element_od_mm']}mm")
            print(f"    Outer Ring OD: {info['outer_ring_od_mm']}mm")
    
    sizes_spiral_series_a_900 = list_gasket_sizes(900, 'spiral_wound', series='A')
    print(f"\n  B16.47 Series A Class 900 Spiral Wound: {', '.join(sizes_spiral_series_a_900)} ({len(sizes_spiral_series_a_900)} sizes)")
    print("  Note: Class 900 available only through NPS 48\"")
    
    # Test B16.47 Series B Class 150 Spiral Wound gaskets
    print("\n" + "=" * 70)
    print("\nB16.47 Series B Class 150 Spiral Wound Gasket Specifications:")
    for size in test_sizes_series_a:
        info = get_gasket_info(size, 150, 'spiral_wound', series='B')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}, Series {info['series']}, Type: {info['gasket_type']}):")
            print(f"    Inner Ring ID: {info['inner_ring_id_mm']}mm")
            print(f"    Sealing Element ID: {info['sealing_element_id_mm']}mm")
            print(f"    Sealing Element OD: {info['sealing_element_od_mm']}mm")
            print(f"    Outer Ring OD: {info['outer_ring_od_mm']}mm")
    
    sizes_spiral_series_b_150 = list_gasket_sizes(150, 'spiral_wound', series='B')
    print(f"\n  B16.47 Series B Class 150 Spiral Wound: {', '.join(sizes_spiral_series_b_150)} ({len(sizes_spiral_series_b_150)} sizes)")
    
    # Test B16.47 Series B Class 300 Spiral Wound gaskets
    print("\n" + "=" * 70)
    print("\nB16.47 Series B Class 300 Spiral Wound Gasket Specifications:")
    for size in test_sizes_series_a:
        info = get_gasket_info(size, 300, 'spiral_wound', series='B')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}, Series {info['series']}, Type: {info['gasket_type']}):")
            print(f"    Inner Ring ID: {info['inner_ring_id_mm']}mm")
            print(f"    Sealing Element ID: {info['sealing_element_id_mm']}mm")
            print(f"    Sealing Element OD: {info['sealing_element_od_mm']}mm")
            print(f"    Outer Ring OD: {info['outer_ring_od_mm']}mm")
    
    sizes_spiral_series_b_300 = list_gasket_sizes(300, 'spiral_wound', series='B')
    print(f"\n  B16.47 Series B Class 300 Spiral Wound: {', '.join(sizes_spiral_series_b_300)} ({len(sizes_spiral_series_b_300)} sizes)")
    
    # Test B16.47 Series B Class 400 Spiral Wound gaskets
    print("\n" + "=" * 70)
    print("\nB16.47 Series B Class 400 Spiral Wound Gasket Specifications:")
    for size in test_sizes_series_a:
        info = get_gasket_info(size, 400, 'spiral_wound', series='B')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}, Series {info['series']}, Type: {info['gasket_type']}):")
            print(f"    Inner Ring ID: {info['inner_ring_id_mm']}mm")
            print(f"    Sealing Element ID: {info['sealing_element_id_mm']}mm")
            print(f"    Sealing Element OD: {info['sealing_element_od_mm']}mm")
            print(f"    Outer Ring OD: {info['outer_ring_od_mm']}mm")
    
    sizes_spiral_series_b_400 = list_gasket_sizes(400, 'spiral_wound', series='B')
    print(f"\n  B16.47 Series B Class 400 Spiral Wound: {', '.join(sizes_spiral_series_b_400)} ({len(sizes_spiral_series_b_400)} sizes)")
    
    # Test B16.47 Series B Class 600 Spiral Wound gaskets
    print("\n" + "=" * 70)
    print("\nB16.47 Series B Class 600 Spiral Wound Gasket Specifications:")
    for size in test_sizes_series_a:
        info = get_gasket_info(size, 600, 'spiral_wound', series='B')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}, Series {info['series']}, Type: {info['gasket_type']}):")
            print(f"    Inner Ring ID: {info['inner_ring_id_mm']}mm")
            print(f"    Sealing Element ID: {info['sealing_element_id_mm']}mm")
            print(f"    Sealing Element OD: {info['sealing_element_od_mm']}mm")
            print(f"    Outer Ring OD: {info['outer_ring_od_mm']}mm")
    
    sizes_spiral_series_b_600 = list_gasket_sizes(600, 'spiral_wound', series='B')
    print(f"\n  B16.47 Series B Class 600 Spiral Wound: {', '.join(sizes_spiral_series_b_600)} ({len(sizes_spiral_series_b_600)} sizes)")
    
    # Test B16.47 Series B Class 900 Spiral Wound gaskets (limited to NPS 48")
    print("\n" + "=" * 70)
    print("\nB16.47 Series B Class 900 Spiral Wound Gasket Specifications:")
    test_sizes_series_900 = ['26', '36', '44', '48']
    for size in test_sizes_series_900:
        info = get_gasket_info(size, 900, 'spiral_wound', series='B')
        if info:
            print(f"\n  NPS {size}\" (Class {info['class']}, Series {info['series']}, Type: {info['gasket_type']}):")
            print(f"    Inner Ring ID: {info['inner_ring_id_mm']}mm")
            print(f"    Sealing Element ID: {info['sealing_element_id_mm']}mm")
            print(f"    Sealing Element OD: {info['sealing_element_od_mm']}mm")
            print(f"    Outer Ring OD: {info['outer_ring_od_mm']}mm")
    
    sizes_spiral_series_b_900 = list_gasket_sizes(900, 'spiral_wound', series='B')
    print(f"\n  B16.47 Series B Class 900 Spiral Wound: {', '.join(sizes_spiral_series_b_900)} ({len(sizes_spiral_series_b_900)} sizes)")
    print(f"  Note: Series B Class 900 limited to NPS 48\" maximum")
    
    # Test Ring Joint Type R gaskets
    print("\n" + "=" * 70)
    print("\nRing Joint Type R Gasket Specifications (Oval & Octagonal):")
    test_rings = ['R-11', 'R-16', 'R-23', 'R-28', 'R-30']
    for ring in test_rings:
        info = get_gasket_info(ring, None, 'ring_joint')
        if info:
            print(f"\n  {info['ring_number']} (Type: {info['gasket_type']}):")
            print(f"    Pitch Diameter: {info['pitch_diameter_inches']}\" ({info['pitch_diameter_mm']}mm)")
            print(f"    Width: {info['width_inches']}\" ({info['width_mm']}mm)")
            print(f"    Oval Height: {info['oval_height_inches']}\" ({info['oval_height_mm']}mm)")
            print(f"    Octagonal Height: {info['octagonal_height_inches']}\" ({info['octagonal_height_mm']}mm)")
            print(f"    Flat Width: {info['flat_width_inches']}\" ({info['flat_width_mm']}mm)")
    
    # Test Ring Joint Type RX gaskets
    print("\n" + "=" * 70)
    print("\nRing Joint Type RX Gasket Specifications (Octagonal Only):")
    test_rings_rx = ['RX-23', 'RX-46', 'RX-50']
    for ring in test_rings_rx:
        info = get_gasket_info(ring, None, 'ring_joint')
        if info:
            print(f"\n  {info['ring_number']} (Type: {info['gasket_type']}):")
            print(f"    Pitch Diameter: {info['pitch_diameter_inches']}\" ({info['pitch_diameter_mm']}mm)")
            print(f"    Width: {info['width_inches']}\" ({info['width_mm']}mm)")
            print(f"    Flat Width: {info['flat_width_inches']}\" ({info['flat_width_mm']}mm)")
            print(f"    Outside Bevel Height: {info['outside_bevel_height_inches']}\" ({info['outside_bevel_height_mm']}mm)")
            print(f"    Ring Height: {info['ring_height_inches']}\" ({info['ring_height_mm']}mm)")
            print(f"    Radius: {info['radius_inches']}\" ({info['radius_mm']}mm)")
    
    sizes_ring_joint = list_gasket_sizes(None, 'ring_joint')
    print(f"\n  All Ring Joint Gaskets (Type R + Type RX): {len(sizes_ring_joint)} rings")
    print(f"    Type R rings: {len([r for r in sizes_ring_joint if r.startswith('R-')])}")
    print(f"    Type RX rings: {len([r for r in sizes_ring_joint if r.startswith('RX-')])}")
    
    sizes_600 = list_gasket_sizes(600, 'full_face')
    print(f"\n  Class 600 Full Face: {', '.join(sizes_600)} ({len(sizes_600)} sizes)")
    sizes_900 = list_gasket_sizes(900, 'full_face')
    print(f"  Class 900 Full Face: {', '.join(sizes_900)} ({len(sizes_900)} sizes)")

