"""
Heavy Hex Nut Dimensions Database
ASME B18.2.2 Heavy Hex Nuts

All dimensions in inches unless otherwise noted.

CAD Modeling Notes:
- Total nut thickness = H (overall height from base to top)
- Washer face OD = Width across flats (F)
- Washer face height = 0.016" (INCLUDED in thickness H, not additional)
- Main hex body height = H - 0.016"
- Washer face location = Bottom face (bearing surface against flange)
- Chamfer = Top face ONLY (opposite side from washer face)
- Chamfer height = ~0.020" (slight edge break, approximately washer thickness)
- Chamfer angle = 15° (shallow edge break)
- Bottom face = Flat washer surface (no chamfer)
"""

# Geometric constants for CAD modeling
NUT_WASHER_FACE_HEIGHT = 0.016  # inches, raised bearing surface (included in total thickness H)
NUT_CHAMFER_HEIGHT = 0.020  # inches, shallow edge break on top face (~0.016-0.020")
NUT_CHAMFER_ANGLE = 15  # degrees, shallow edge break chamfer
NUT_CHAMFER_LOCATION = 'top'  # Chamfer only on top, opposite washer face

# Heavy Hex Nut Dimensions by Thread Size
HEAVY_HEX_NUTS = {
    '1/4': {
        'size': '1/4',
        'thread_diameter': 0.2500,
        'width_across_flats_basic': 0.500,
        'width_across_flats_max': 0.500,
        'width_across_flats_min': 0.488,
        'width_across_corners_max': 0.577,
        'width_across_corners_min': 0.556,
        'thickness_basic': 0.250,
        'thickness_max': 0.250,
        'thickness_min': 0.218
    },
    '5/16': {
        'size': '5/16',
        'thread_diameter': 0.3125,
        'width_across_flats_basic': 0.562,
        'width_across_flats_max': 0.562,
        'width_across_flats_min': 0.546,
        'width_across_corners_max': 0.650,
        'width_across_corners_min': 0.622,
        'thickness_basic': 0.314,
        'thickness_max': 0.314,
        'thickness_min': 0.280
    },
    '3/8': {
        'size': '3/8',
        'thread_diameter': 0.3750,
        'width_across_flats_basic': 0.688,
        'width_across_flats_max': 0.688,
        'width_across_flats_min': 0.669,
        'width_across_corners_max': 0.794,
        'width_across_corners_min': 0.763,
        'thickness_basic': 0.377,
        'thickness_max': 0.377,
        'thickness_min': 0.341
    },
    '7/16': {
        'size': '7/16',
        'thread_diameter': 0.4375,
        'width_across_flats_basic': 0.750,
        'width_across_flats_max': 0.750,
        'width_across_flats_min': 0.728,
        'width_across_corners_max': 0.866,
        'width_across_corners_min': 0.830,
        'thickness_basic': 0.441,
        'thickness_max': 0.441,
        'thickness_min': 0.403
    },
    '1/2': {
        'size': '1/2',
        'thread_diameter': 0.5000,
        'width_across_flats_basic': 0.875,
        'width_across_flats_max': 0.875,
        'width_across_flats_min': 0.850,
        'width_across_corners_max': 1.010,
        'width_across_corners_min': 0.969,
        'thickness_basic': 0.504,
        'thickness_max': 0.504,
        'thickness_min': 0.464
    },
    '9/16': {
        'size': '9/16',
        'thread_diameter': 0.5625,
        'width_across_flats_basic': 0.938,
        'width_across_flats_max': 0.938,
        'width_across_flats_min': 0.909,
        'width_across_corners_max': 1.083,
        'width_across_corners_min': 1.037,
        'thickness_basic': 0.568,
        'thickness_max': 0.568,
        'thickness_min': 0.526
    },
    '5/8': {
        'size': '5/8',
        'thread_diameter': 0.6250,
        'width_across_flats_basic': 1.062,
        'width_across_flats_max': 1.062,
        'width_across_flats_min': 1.031,
        'width_across_corners_max': 1.227,
        'width_across_corners_min': 1.175,
        'thickness_basic': 0.631,
        'thickness_max': 0.631,
        'thickness_min': 0.587
    },
    '3/4': {
        'size': '3/4',
        'thread_diameter': 0.7500,
        'width_across_flats_basic': 1.250,
        'width_across_flats_max': 1.250,
        'width_across_flats_min': 1.212,
        'width_across_corners_max': 1.443,
        'width_across_corners_min': 1.382,
        'thickness_basic': 0.758,
        'thickness_max': 0.758,
        'thickness_min': 0.710
    },
    '7/8': {
        'size': '7/8',
        'thread_diameter': 0.8750,
        'width_across_flats_basic': 1.438,
        'width_across_flats_max': 1.438,
        'width_across_flats_min': 1.394,
        'width_across_corners_max': 1.660,
        'width_across_corners_min': 1.589,
        'thickness_basic': 0.885,
        'thickness_max': 0.885,
        'thickness_min': 0.833
    },
    '1': {
        'size': '1',
        'thread_diameter': 1.0000,
        'width_across_flats_basic': 1.625,
        'width_across_flats_max': 1.625,
        'width_across_flats_min': 1.575,
        'width_across_corners_max': 1.876,
        'width_across_corners_min': 1.796,
        'thickness_basic': 1.012,
        'thickness_max': 1.012,
        'thickness_min': 0.956
    },
    '1-1/8': {
        'size': '1-1/8',
        'thread_diameter': 1.1250,
        'width_across_flats_basic': 1.812,
        'width_across_flats_max': 1.812,
        'width_across_flats_min': 1.756,
        'width_across_corners_max': 2.093,
        'width_across_corners_min': 2.002,
        'thickness_basic': 1.139,
        'thickness_max': 1.139,
        'thickness_min': 1.079
    },
    '1-1/4': {
        'size': '1-1/4',
        'thread_diameter': 1.2500,
        'width_across_flats_basic': 2.000,
        'width_across_flats_max': 2.000,
        'width_across_flats_min': 1.938,
        'width_across_corners_max': 2.309,
        'width_across_corners_min': 2.209,
        'thickness_basic': 1.251,
        'thickness_max': 1.251,
        'thickness_min': 1.187
    },
    '1-3/8': {
        'size': '1-3/8',
        'thread_diameter': 1.3750,
        'width_across_flats_basic': 2.188,
        'width_across_flats_max': 2.188,
        'width_across_flats_min': 2.119,
        'width_across_corners_max': 2.526,
        'width_across_corners_min': 2.416,
        'thickness_basic': 1.378,
        'thickness_max': 1.378,
        'thickness_min': 1.310
    },
    '1-1/2': {
        'size': '1-1/2',
        'thread_diameter': 1.5000,
        'width_across_flats_basic': 2.375,
        'width_across_flats_max': 2.375,
        'width_across_flats_min': 2.300,
        'width_across_corners_max': 2.742,
        'width_across_corners_min': 2.622,
        'thickness_basic': 1.505,
        'thickness_max': 1.505,
        'thickness_min': 1.433
    },
    '1-5/8': {
        'size': '1-5/8',
        'thread_diameter': 1.6250,
        'width_across_flats_basic': 2.562,
        'width_across_flats_max': 2.562,
        'width_across_flats_min': 2.481,
        'width_across_corners_max': 2.959,
        'width_across_corners_min': 2.828,
        'thickness_basic': 1.632,
        'thickness_max': 1.632,
        'thickness_min': 1.556
    },
    '1-3/4': {
        'size': '1-3/4',
        'thread_diameter': 1.7500,
        'width_across_flats_basic': 2.750,
        'width_across_flats_max': 2.750,
        'width_across_flats_min': 2.662,
        'width_across_corners_max': 3.175,
        'width_across_corners_min': 3.035,
        'thickness_basic': 1.759,
        'thickness_max': 1.759,
        'thickness_min': 1.679
    },
    '2': {
        'size': '2',
        'thread_diameter': 2.0000,
        'width_across_flats_basic': 3.125,
        'width_across_flats_max': 3.125,
        'width_across_flats_min': 3.025,
        'width_across_corners_max': 3.608,
        'width_across_corners_min': 3.449,
        'thickness_basic': 2.013,
        'thickness_max': 2.013,
        'thickness_min': 1.925
    },
    '2-1/4': {
        'size': '2-1/4',
        'thread_diameter': 2.2500,
        'width_across_flats_basic': 3.500,
        'width_across_flats_max': 3.500,
        'width_across_flats_min': 3.388,
        'width_across_corners_max': 4.041,
        'width_across_corners_min': 3.862,
        'thickness_basic': 2.251,
        'thickness_max': 2.251,
        'thickness_min': 2.155
    },
    '2-1/2': {
        'size': '2-1/2',
        'thread_diameter': 2.5000,
        'width_across_flats_basic': 3.875,
        'width_across_flats_max': 3.875,
        'width_across_flats_min': 3.750,
        'width_across_corners_max': 4.474,
        'width_across_corners_min': 4.275,
        'thickness_basic': 2.505,
        'thickness_max': 2.505,
        'thickness_min': 2.401
    },
    '2-3/4': {
        'size': '2-3/4',
        'thread_diameter': 2.7500,
        'width_across_flats_basic': 4.250,
        'width_across_flats_max': 4.250,
        'width_across_flats_min': 4.112,
        'width_across_corners_max': 4.907,
        'width_across_corners_min': 4.688,
        'thickness_basic': 2.759,
        'thickness_max': 2.759,
        'thickness_min': 2.647
    },
    '3': {
        'size': '3',
        'thread_diameter': 3.0000,
        'width_across_flats_basic': 4.625,
        'width_across_flats_max': 4.625,
        'width_across_flats_min': 4.475,
        'width_across_corners_max': 5.340,
        'width_across_corners_min': 5.102,
        'thickness_basic': 3.013,
        'thickness_max': 3.013,
        'thickness_min': 2.893
    },
    '3-1/4': {
        'size': '3-1/4',
        'thread_diameter': 3.2500,
        'width_across_flats_basic': 5.000,
        'width_across_flats_max': 5.000,
        'width_across_flats_min': 4.838,
        'width_across_corners_max': 5.774,
        'width_across_corners_min': 5.515,
        'thickness_basic': 3.252,
        'thickness_max': 3.252,
        'thickness_min': 3.124
    },
    '3-1/2': {
        'size': '3-1/2',
        'thread_diameter': 3.5000,
        'width_across_flats_basic': 5.375,
        'width_across_flats_max': 5.375,
        'width_across_flats_min': 5.200,
        'width_across_corners_max': 6.207,
        'width_across_corners_min': 5.928,
        'thickness_basic': 3.506,
        'thickness_max': 3.506,
        'thickness_min': 3.370
    },
    '3-3/4': {
        'size': '3-3/4',
        'thread_diameter': 3.7500,
        'width_across_flats_basic': 5.750,
        'width_across_flats_max': 5.750,
        'width_across_flats_min': 5.562,
        'width_across_corners_max': 6.640,
        'width_across_corners_min': 6.341,
        'thickness_basic': 3.760,
        'thickness_max': 3.760,
        'thickness_min': 3.616
    },
    '4': {
        'size': '4',
        'thread_diameter': 4.0000,
        'width_across_flats_basic': 6.125,
        'width_across_flats_max': 6.125,
        'width_across_flats_min': 5.925,
        'width_across_corners_max': 7.073,
        'width_across_corners_min': 6.755,
        'thickness_basic': 4.014,
        'thickness_max': 4.014,
        'thickness_min': 3.862
    },
}


# 2H Heavy Hex Nut Dimensions by Thread Size
HEAVY_HEX_2H_NUTS = {
    '1/4': {
        'size': '1/4',
        'thread_diameter': 0.250,
        'unc_threads': 20,
        'unf_threads': 28,
        'width_across_flats_basic': 0.500,
        'width_across_flats_max': 0.500,
        'width_across_flats_min': 0.488,
        'width_across_corners_max': 0.577,
        'width_across_corners_min': 0.556,
        'thickness_basic': 0.250,
        'thickness_max': 0.250,
        'thickness_min': 0.218
    },
    '5/16': {
        'size': '5/16',
        'thread_diameter': 0.313,
        'unc_threads': 18,
        'unf_threads': 24,
        'width_across_flats_basic': 0.562,
        'width_across_flats_max': 0.562,
        'width_across_flats_min': 0.546,
        'width_across_corners_max': 0.650,
        'width_across_corners_min': 0.220,
        'thickness_basic': 0.314,
        'thickness_max': 0.314,
        'thickness_min': 0.280
    },
    '3/8': {
        'size': '3/8',
        'thread_diameter': 0.375,
        'unc_threads': 16,
        'unf_threads': 24,
        'width_across_flats_basic': 0.688,
        'width_across_flats_max': 0.688,
        'width_across_flats_min': 0.669,
        'width_across_corners_max': 0.794,
        'width_across_corners_min': 0.763,
        'thickness_basic': 0.377,
        'thickness_max': 0.377,
        'thickness_min': 0.341
    },
    '7/16': {
        'size': '7/16',
        'thread_diameter': 0.438,
        'unc_threads': 14,
        'unf_threads': 20,
        'width_across_flats_basic': 0.750,
        'width_across_flats_max': 0.750,
        'width_across_flats_min': 0.728,
        'width_across_corners_max': 0.866,
        'width_across_corners_min': 0.830,
        'thickness_basic': 0.441,
        'thickness_max': 0.441,
        'thickness_min': 0.403
    },
    '1/2': {
        'size': '1/2',
        'thread_diameter': 0.500,
        'unc_threads': 13,
        'unf_threads': 20,
        'width_across_flats_basic': 0.875,
        'width_across_flats_max': 0.875,
        'width_across_flats_min': 0.850,
        'width_across_corners_max': 1.010,
        'width_across_corners_min': 0.990,
        'thickness_basic': 0.504,
        'thickness_max': 0.504,
        'thickness_min': 0.464
    },
    '9/16': {
        'size': '9/16',
        'thread_diameter': 0.563,
        'unc_threads': 12,
        'unf_threads': 18,
        'width_across_flats_basic': 0.938,
        'width_across_flats_max': 0.938,
        'width_across_flats_min': 0.909,
        'width_across_corners_max': 1.083,
        'width_across_corners_min': 1.037,
        'thickness_basic': 0.568,
        'thickness_max': 0.568,
        'thickness_min': 0.526
    },
    '5/8': {
        'size': '5/8',
        'thread_diameter': 0.625,
        'unc_threads': 11,
        'unf_threads': 18,
        'width_across_flats_basic': 1.062,
        'width_across_flats_max': 1.062,
        'width_across_flats_min': 1.031,
        'width_across_corners_max': 1.227,
        'width_across_corners_min': 1.175,
        'thickness_basic': 0.631,
        'thickness_max': 0.631,
        'thickness_min': 0.587
    },
    '3/4': {
        'size': '3/4',
        'thread_diameter': 0.750,
        'unc_threads': 10,
        'unf_threads': 16,
        'width_across_flats_basic': 1.250,
        'width_across_flats_max': 1.250,
        'width_across_flats_min': 1.212,
        'width_across_corners_max': 1.443,
        'width_across_corners_min': 1.382,
        'thickness_basic': 0.758,
        'thickness_max': 0.758,
        'thickness_min': 0.710
    },
    '7/8': {
        'size': '7/8',
        'thread_diameter': 0.875,
        'unc_threads': 9,
        'unf_threads': 14,
        'width_across_flats_basic': 1.438,
        'width_across_flats_max': 1.438,
        'width_across_flats_min': 1.394,
        'width_across_corners_max': 1.660,
        'width_across_corners_min': 1.589,
        'thickness_basic': 0.885,
        'thickness_max': 0.885,
        'thickness_min': 0.833
    },
    '1': {
        'size': '1',
        'thread_diameter': 1.000,
        'unc_threads': 8,
        'unf_threads': 14,
        'width_across_flats_basic': 1.625,
        'width_across_flats_max': 1.625,
        'width_across_flats_min': 1.575,
        'width_across_corners_max': 1.876,
        'width_across_corners_min': 1.796,
        'thickness_basic': 1.012,
        'thickness_max': 1.012,
        'thickness_min': 0.956
    },
    '1-1/8': {
        'size': '1-1/8',
        'thread_diameter': 1.125,
        'unc_threads': 7,
        'unf_threads': 12,
        'un8_threads': 8,
        'width_across_flats_basic': 1.812,
        'width_across_flats_max': 1.812,
        'width_across_flats_min': 1.756,
        'width_across_corners_max': 2.093,
        'width_across_corners_min': 2.002,
        'thickness_basic': 1.139,
        'thickness_max': 1.139,
        'thickness_min': 1.079
    },
    '1-1/4': {
        'size': '1-1/4',
        'thread_diameter': 1.250,
        'unc_threads': 7,
        'unf_threads': 12,
        'un8_threads': 8,
        'width_across_flats_basic': 2.000,
        'width_across_flats_max': 2.000,
        'width_across_flats_min': 1.380,
        'width_across_corners_max': 2.309,
        'width_across_corners_min': 2.209,
        'thickness_basic': 1.251,
        'thickness_max': 1.251,
        'thickness_min': 1.187
    },
    '1-3/8': {
        'size': '1-3/8',
        'thread_diameter': 1.375,
        'unc_threads': 6,
        'unf_threads': 12,
        'un8_threads': 8,
        'width_across_flats_basic': 2.188,
        'width_across_flats_max': 2.188,
        'width_across_flats_min': 2.119,
        'width_across_corners_max': 2.526,
        'width_across_corners_min': 2.416,
        'thickness_basic': 1.378,
        'thickness_max': 1.378,
        'thickness_min': 1.310
    },
    '1-1/2': {
        'size': '1-1/2',
        'thread_diameter': 1.500,
        'unc_threads': 6,
        'unf_threads': 12,
        'un8_threads': 8,
        'width_across_flats_basic': 2.375,
        'width_across_flats_max': 2.375,
        'width_across_flats_min': 2.300,
        'width_across_corners_max': 2.742,
        'width_across_corners_min': 2.622,
        'thickness_basic': 1.505,
        'thickness_max': 1.505,
        'thickness_min': 1.433
    },
    '1-5/8': {
        'size': '1-5/8',
        'thread_diameter': 1.625,
        'unc_threads': 5.5,
        'unf_threads': 12,
        'un8_threads': 8,
        'width_across_flats_basic': 2.562,
        'width_across_flats_max': 2.562,
        'width_across_flats_min': 2.481,
        'width_across_corners_max': 2.959,
        'width_across_corners_min': 2.828,
        'thickness_basic': 1.632,
        'thickness_max': 1.632,
        'thickness_min': 1.556
    },
    '1-3/4': {
        'size': '1-3/4',
        'thread_diameter': 1.750,
        'unc_threads': 5,
        'unf_threads': 12,
        'un8_threads': 8,
        'width_across_flats_basic': 2.750,
        'width_across_flats_max': 2.750,
        'width_across_flats_min': 2.662,
        'width_across_corners_max': 3.175,
        'width_across_corners_min': 3.035,
        'thickness_basic': 1.759,
        'thickness_max': 1.759,
        'thickness_min': 1.679
    },
    '1-7/8': {
        'size': '1-7/8',
        'thread_diameter': 1.875,
        'unc_threads': 5,
        'unf_threads': 12,
        'un8_threads': 8,
        'width_across_flats_basic': 2.938,
        'width_across_flats_max': 2.938,
        'width_across_flats_min': 2.844,
        'width_across_corners_max': 3.392,
        'width_across_corners_min': 3.242,
        'thickness_basic': 1.886,
        'thickness_max': 1.886,
        'thickness_min': 1.802
    },
    '2': {
        'size': '2',
        'thread_diameter': 2.000,
        'unc_threads': 4.5,
        'unf_threads': 12,
        'un8_threads': 8,
        'width_across_flats_basic': 3.125,
        'width_across_flats_max': 3.125,
        'width_across_flats_min': 3.025,
        'width_across_corners_max': 3.608,
        'width_across_corners_min': 3.449,
        'thickness_basic': 2.013,
        'thickness_max': 2.013,
        'thickness_min': 1.925
    },
    '2-1/4': {
        'size': '2-1/4',
        'thread_diameter': 2.250,
        'unc_threads': 4.5,
        'unf_threads': 12,
        'un8_threads': 8,
        'width_across_flats_basic': 3.500,
        'width_across_flats_max': 3.500,
        'width_across_flats_min': 3.388,
        'width_across_corners_max': 4.041,
        'width_across_corners_min': 3.862,
        'thickness_basic': 2.251,
        'thickness_max': 2.251,
        'thickness_min': 2.155
    },
    '2-1/2': {
        'size': '2-1/2',
        'thread_diameter': 2.500,
        'unc_threads': 4,
        'unf_threads': 12,
        'un8_threads': 8,
        'width_across_flats_basic': 3.875,
        'width_across_flats_max': 3.875,
        'width_across_flats_min': 3.750,
        'width_across_corners_max': 4.474,
        'width_across_corners_min': 4.275,
        'thickness_basic': 2.505,
        'thickness_max': 2.505,
        'thickness_min': 2.401
    },
    '2-3/4': {
        'size': '2-3/4',
        'thread_diameter': 2.750,
        'unc_threads': 4,
        'unf_threads': 12,
        'un8_threads': 8,
        'width_across_flats_basic': 4.250,
        'width_across_flats_max': 4.250,
        'width_across_flats_min': 4.112,
        'width_across_corners_max': 4.907,
        'width_across_corners_min': 4.688,
        'thickness_basic': 2.759,
        'thickness_max': 2.759,
        'thickness_min': 2.647
    },
    '3': {
        'size': '3',
        'thread_diameter': 3.000,
        'unc_threads': 4,
        'unf_threads': 12,
        'un8_threads': 8,
        'width_across_flats_basic': 4.625,
        'width_across_flats_max': 4.625,
        'width_across_flats_min': 4.475,
        'width_across_corners_max': 5.340,
        'width_across_corners_min': 5.102,
        'thickness_basic': 3.013,
        'thickness_max': 3.013,
        'thickness_min': 2.893
    },
    '3-1/4': {
        'size': '3-1/4',
        'thread_diameter': 3.250,
        'unc_threads': 4,
        'unf_threads': 12,
        'un8_threads': 8,
        'width_across_flats_basic': 5.000,
        'width_across_flats_max': 5.000,
        'width_across_flats_min': 4.838,
        'width_across_corners_max': 5.774,
        'width_across_corners_min': 5.515,
        'thickness_basic': 3.252,
        'thickness_max': 3.252,
        'thickness_min': 3.124
    },
    '3-1/2': {
        'size': '3-1/2',
        'thread_diameter': 3.500,
        'unc_threads': 4,
        'unf_threads': 12,
        'un8_threads': 8,
        'width_across_flats_basic': 5.375,
        'width_across_flats_max': 5.375,
        'width_across_flats_min': 5.200,
        'width_across_corners_max': 6.207,
        'width_across_corners_min': 5.928,
        'thickness_basic': 3.506,
        'thickness_max': 3.506,
        'thickness_min': 3.370
    },
    '3-3/4': {
        'size': '3-3/4',
        'thread_diameter': 3.750,
        'unc_threads': 4,
        'unf_threads': 12,
        'un8_threads': 8,
        'width_across_flats_basic': 5.750,
        'width_across_flats_max': 5.750,
        'width_across_flats_min': 5.562,
        'width_across_corners_max': 5.562,
        'width_across_corners_min': 6.341,
        'thickness_basic': 3.670,
        'thickness_max': 3.670,
        'thickness_min': 3.616
    },
    '4': {
        'size': '4',
        'thread_diameter': 4.000,
        'unc_threads': 4,
        'unf_threads': 12,
        'un8_threads': 8,
        'width_across_flats_basic': 6.125,
        'width_across_flats_max': 6.125,
        'width_across_flats_min': 5.925,
        'width_across_corners_max': 5.925,
        'width_across_corners_min': 6.755,
        'thickness_basic': 4.014,
        'thickness_max': 4.014,
        'thickness_min': 3.862
    },
}


def get_heavy_hex_nut_info(size, nut_type='standard'):
    """
    Get Heavy Hex Nut dimensions for a specific thread size.
    
    Args:
        size (str): Thread size (e.g., '1/2', '3/4', '1', '1-1/4')
        nut_type (str): 'standard' or '2h' for double height
    
    Returns:
        dict: Nut dimensions with added CAD modeling info, or None if not found
    """
    if nut_type.lower() in ['2h', 'double', 'double_height']:
        nut_data = HEAVY_HEX_2H_NUTS.get(size)
    else:
        nut_data = HEAVY_HEX_NUTS.get(size)
    
    # Add CAD modeling dimensions if nut found
    if nut_data:
        nut_data = nut_data.copy()  # Don't modify original dict
        nut_data['washer_face_od'] = nut_data['width_across_flats_basic']
        nut_data['washer_face_height'] = NUT_WASHER_FACE_HEIGHT
        nut_data['washer_face_location'] = 'bottom'
        nut_data['chamfer_height'] = NUT_CHAMFER_HEIGHT
        nut_data['chamfer_angle'] = NUT_CHAMFER_ANGLE
        nut_data['chamfer_location'] = NUT_CHAMFER_LOCATION
        nut_data['hex_body_height'] = nut_data['thickness_basic'] - NUT_WASHER_FACE_HEIGHT
    
    return nut_data


def list_heavy_hex_nut_sizes(nut_type='standard'):
    """
    List all available Heavy Hex Nut thread sizes.
    
    Args:
        nut_type (str): 'standard' or '2h' for double height
    
    Returns:
        list: Available sizes sorted
    """
    def size_to_float(size_str):
        """Convert fractional size string to float for sorting."""
        if '-' in size_str and '/' in size_str:
            # Handle '1-1/4' format
            parts = size_str.split('-')
            whole = float(parts[0])
            frac_parts = parts[1].split('/')
            frac = float(frac_parts[0]) / float(frac_parts[1])
            return whole + frac
        elif '/' in size_str:
            # Handle '1/2' format
            parts = size_str.split('/')
            return float(parts[0]) / float(parts[1])
        else:
            # Handle '1', '2', etc.
            return float(size_str)
    
    if nut_type.lower() in ['2h', 'double', 'double_height']:
        return sorted(HEAVY_HEX_2H_NUTS.keys(), key=size_to_float)
    else:
        return sorted(HEAVY_HEX_NUTS.keys(), key=size_to_float)


# Example usage and testing
if __name__ == "__main__":
    print("Heavy Hex Nut Dimensions Database (ASME B18.2.2)")
    print("=" * 70)
    
    # Test standard nuts
    test_sizes = ['1/2', '3/4', '1', '1-1/2', '2', '3', '4']
    
    print("\nStandard Heavy Hex Nut Specifications:")
    for size in test_sizes:
        info = get_heavy_hex_nut_info(size, 'standard')
        if info:
            print(f"\n  {size}\" Thread:")
            print(f"    Width Across Flats: {info['width_across_flats_basic']}\" (nom)")
            print(f"    Width Across Corners: {info['width_across_corners_max']:.3f}\" (max)")
            print(f"    Thickness: {info['thickness_basic']:.3f}\" (nom)")
            print(f"    Washer Face OD: {info['washer_face_od']}\" (= width across flats)")
            print(f"    Washer Face Height: {info['washer_face_height']}\"")
    
    # Test 2H nuts
    print("\n\n2H Heavy Hex Nut Specifications:")
    for size in test_sizes:
        info = get_heavy_hex_nut_info(size, '2h')
        if info:
            print(f"\n  {size}\" Thread:")
            print(f"    Width Across Flats: {info['width_across_flats_basic']}\" (nom)")
            print(f"    Thickness: {info['thickness_basic']:.3f}\" (nom)")
            print(f"    Washer Face OD: {info['washer_face_od']}\"")
            print(f"    Washer Face Height: {info['washer_face_height']}\"")
            if 'unc_threads' in info:
                print(f"    UNC Threads: {info['unc_threads']}")
    
    # List all available sizes
    print("\n" + "=" * 70)
    print("Available sizes:")
    std_sizes = list_heavy_hex_nut_sizes('standard')
    print(f"  Standard: {', '.join(std_sizes)} ({len(std_sizes)} sizes)")
    h2_sizes = list_heavy_hex_nut_sizes('2h')
    print(f"  2H: {', '.join(h2_sizes)} ({len(h2_sizes)} sizes)")

