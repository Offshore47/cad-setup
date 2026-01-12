"""
ASME B16.5 Raised Face Weld Neck Flange Database
All dimensions in millimeters
Data source: ASME B16.5 standard flange dimension tables
"""

# Class 150 RF Weld Neck Flanges
CLASS_150_RF_WN = {
    '1/2': {
        'nps': '1/2',
        'flange_od': 88.9,
        'flange_thickness': 11.2,
        'rf_diameter': 35.1,
        'hub_base_diameter': 30.2,
        'hub_end_diameter': 21.3,
        'hub_length': 47.8,
        'bolt_holes': 4,
        'bolt_hole_diameter': 15.7,
        'bolt_size': '1/2',
        'bolt_circle_diameter': 60.5,
        'weight_kg': 1
    },
    '3/4': {
        'nps': '3/4',
        'flange_od': 98.6,
        'flange_thickness': 12.7,
        'rf_diameter': 42.9,
        'hub_base_diameter': 38.1,
        'hub_end_diameter': 26.7,
        'hub_length': 52.3,
        'bolt_holes': 4,
        'bolt_hole_diameter': 15.7,
        'bolt_size': '1/2',
        'bolt_circle_diameter': 69.9,
        'weight_kg': 1
    },
    '1': {
        'nps': '1',
        'flange_od': 108,
        'flange_thickness': 14.2,
        'rf_diameter': 50.8,
        'hub_base_diameter': 49.3,
        'hub_end_diameter': 33.5,
        'hub_length': 55.6,
        'bolt_holes': 4,
        'bolt_hole_diameter': 15.7,
        'bolt_size': '1/2',
        'bolt_circle_diameter': 79.2,
        'weight_kg': 1
    },
    '1-1/4': {
        'nps': '1-1/4',
        'flange_od': 117.3,
        'flange_thickness': 15.7,
        'rf_diameter': 63.5,
        'hub_base_diameter': 58.7,
        'hub_end_diameter': 42.2,
        'hub_length': 57.2,
        'bolt_holes': 4,
        'bolt_hole_diameter': 15.7,
        'bolt_size': '1/2',
        'bolt_circle_diameter': 88.9,
        'weight_kg': 1
    },
    '1-1/2': {
        'nps': '1-1/2',
        'flange_od': 127,
        'flange_thickness': 17.5,
        'rf_diameter': 73.2,
        'hub_base_diameter': 65,
        'hub_end_diameter': 48.3,
        'hub_length': 62,
        'bolt_holes': 4,
        'bolt_hole_diameter': 15.7,
        'bolt_size': '1/2',
        'bolt_circle_diameter': 98.6,
        'weight_kg': 2
    },
    '2': {
        'nps': '2',
        'flange_od': 152.4,
        'flange_thickness': 19.1,
        'rf_diameter': 91.9,
        'hub_base_diameter': 77.7,
        'hub_end_diameter': 60.5,
        'hub_length': 63.5,
        'bolt_holes': 4,
        'bolt_hole_diameter': 19.1,
        'bolt_size': '5/8',
        'bolt_circle_diameter': 120.7,
        'weight_kg': 3
    },
    '2-1/2': {
        'nps': '2-1/2',
        'flange_od': 177.8,
        'flange_thickness': 22.4,
        'rf_diameter': 104.6,
        'hub_base_diameter': 90.4,
        'hub_end_diameter': 73.2,
        'hub_length': 69.9,
        'bolt_holes': 4,
        'bolt_hole_diameter': 19.1,
        'bolt_size': '5/8',
        'bolt_circle_diameter': 139.7,
        'weight_kg': 4
    },
    '3': {
        'nps': '3',
        'flange_od': 190.5,
        'flange_thickness': 23.9,
        'rf_diameter': 127,
        'hub_base_diameter': 108,
        'hub_end_diameter': 88.9,
        'hub_length': 69.9,
        'bolt_holes': 4,
        'bolt_hole_diameter': 19.1,
        'bolt_size': '5/8',
        'bolt_circle_diameter': 152.4,
        'weight_kg': 5
    },
    '3-1/2': {
        'nps': '3-1/2',
        'flange_od': 215.9,
        'flange_thickness': 23.9,
        'rf_diameter': 139.7,
        'hub_base_diameter': 122.2,
        'hub_end_diameter': 101.6,
        'hub_length': 71.4,
        'bolt_holes': 8,
        'bolt_hole_diameter': 19.1,
        'bolt_size': '5/8',
        'bolt_circle_diameter': 177.8,
        'weight_kg': 5
    },
    '4': {
        'nps': '4',
        'flange_od': 228.6,
        'flange_thickness': 23.9,
        'rf_diameter': 157.2,
        'hub_base_diameter': 134.9,
        'hub_end_diameter': 114.3,
        'hub_length': 76.2,
        'bolt_holes': 8,
        'bolt_hole_diameter': 19.1,
        'bolt_size': '5/8',
        'bolt_circle_diameter': 190.5,
        'weight_kg': 7
    },
    '5': {
        'nps': '5',
        'flange_od': 254,
        'flange_thickness': 23.9,
        'rf_diameter': 185.7,
        'hub_base_diameter': 163.6,
        'hub_end_diameter': 141.2,
        'hub_length': 88.9,
        'bolt_holes': 8,
        'bolt_hole_diameter': 22.4,
        'bolt_size': '3/4',
        'bolt_circle_diameter': 215.9,
        'weight_kg': 9
    },
    '6': {
        'nps': '6',
        'flange_od': 279.4,
        'flange_thickness': 25.4,
        'rf_diameter': 215.9,
        'hub_base_diameter': 192,
        'hub_end_diameter': 168.4,
        'hub_length': 88.9,
        'bolt_holes': 8,
        'bolt_hole_diameter': 22.4,
        'bolt_size': '3/4',
        'bolt_circle_diameter': 241.3,
        'weight_kg': 11
    },
    '8': {
        'nps': '8',
        'flange_od': 342.9,
        'flange_thickness': 28.4,
        'rf_diameter': 269.7,
        'hub_base_diameter': 246.1,
        'hub_end_diameter': 219.2,
        'hub_length': 101.6,
        'bolt_holes': 8,
        'bolt_hole_diameter': 22.4,
        'bolt_size': '3/4',
        'bolt_circle_diameter': 298.5,
        'weight_kg': 18
    },
    '10': {
        'nps': '10',
        'flange_od': 406.4,
        'flange_thickness': 30.2,
        'rf_diameter': 323.9,
        'hub_base_diameter': 304.8,
        'hub_end_diameter': 273.1,
        'hub_length': 101.6,
        'bolt_holes': 12,
        'bolt_hole_diameter': 25.4,
        'bolt_size': '7/8',
        'bolt_circle_diameter': 362,
        'weight_kg': 24
    },
    '12': {
        'nps': '12',
        'flange_od': 482.6,
        'flange_thickness': 31.8,
        'rf_diameter': 381,
        'hub_base_diameter': 365.3,
        'hub_end_diameter': 323.9,
        'hub_length': 114.3,
        'bolt_holes': 12,
        'bolt_hole_diameter': 25.4,
        'bolt_size': '7/8',
        'bolt_circle_diameter': 431.8,
        'weight_kg': 36
    },
    '14': {
        'nps': '14',
        'flange_od': 533.4,
        'flange_thickness': 35.1,
        'rf_diameter': 412.8,
        'hub_base_diameter': 400.1,
        'hub_end_diameter': 355.6,
        'hub_length': 127,
        'bolt_holes': 12,
        'bolt_hole_diameter': 28.4,
        'bolt_size': '1',
        'bolt_circle_diameter': 476.3,
        'weight_kg': 50
    },
    '16': {
        'nps': '16',
        'flange_od': 596.9,
        'flange_thickness': 36.6,
        'rf_diameter': 469.9,
        'hub_base_diameter': 457.2,
        'hub_end_diameter': 406.4,
        'hub_length': 127,
        'bolt_holes': 16,
        'bolt_hole_diameter': 28.4,
        'bolt_size': '1',
        'bolt_circle_diameter': 539.8,
        'weight_kg': 64
    },
    '18': {
        'nps': '18',
        'flange_od': 635,
        'flange_thickness': 39.6,
        'rf_diameter': 533.4,
        'hub_base_diameter': 505,
        'hub_end_diameter': 457.2,
        'hub_length': 139.7,
        'bolt_holes': 16,
        'bolt_hole_diameter': 31.8,
        'bolt_size': '1-1/8',
        'bolt_circle_diameter': 577.9,
        'weight_kg': 68
    },
    '20': {
        'nps': '20',
        'flange_od': 698.5,
        'flange_thickness': 42.9,
        'rf_diameter': 584.2,
        'hub_base_diameter': 558.8,
        'hub_end_diameter': 508,
        'hub_length': 144.5,
        'bolt_holes': 20,
        'bolt_hole_diameter': 31.8,
        'bolt_size': '1-1/8',
        'bolt_circle_diameter': 635,
        'weight_kg': 82
    },
    '24': {
        'nps': '24',
        'flange_od': 812.8,
        'flange_thickness': 47.8,
        'rf_diameter': 692.2,
        'hub_base_diameter': 663.4,
        'hub_end_diameter': 609.6,
        'hub_length': 152.4,
        'bolt_holes': 20,
        'bolt_hole_diameter': 35.1,
        'bolt_size': '1-1/4',
        'bolt_circle_diameter': 749.3,
        'weight_kg': 118
    },
}

# Class 300 RF Weld Neck Flanges
CLASS_300_RF_WN = {
    '1/2': {
        'nps': '1/2',
        'flange_od': 95.3,
        'flange_thickness': 14.2,
        'rf_diameter': 35.1,
        'hub_base_diameter': 38.1,
        'hub_end_diameter': 21.3,
        'hub_length': 52.3,
        'bolt_holes': 4,
        'bolt_hole_diameter': 15.7,
        'bolt_size': '1/2',
        'bolt_circle_diameter': 66.5,
        'weight_kg': 1
    },
    '3/4': {
        'nps': '3/4',
        'flange_od': 117.3,
        'flange_thickness': 15.7,
        'rf_diameter': 42.9,
        'hub_base_diameter': 47.8,
        'hub_end_diameter': 26.7,
        'hub_length': 57.2,
        'bolt_holes': 4,
        'bolt_hole_diameter': 19.1,
        'bolt_size': '5/8',
        'bolt_circle_diameter': 82.6,
        'weight_kg': 1
    },
    '1': {
        'nps': '1',
        'flange_od': 124,
        'flange_thickness': 17.5,
        'rf_diameter': 50.8,
        'hub_base_diameter': 53.8,
        'hub_end_diameter': 33.5,
        'hub_length': 62,
        'bolt_holes': 4,
        'bolt_hole_diameter': 19.1,
        'bolt_size': '5/8',
        'bolt_circle_diameter': 88.9,
        'weight_kg': 2
    },
    '1-1/4': {
        'nps': '1-1/4',
        'flange_od': 133.4,
        'flange_thickness': 19.1,
        'rf_diameter': 63.5,
        'hub_base_diameter': 63.5,
        'hub_end_diameter': 42.2,
        'hub_length': 65,
        'bolt_holes': 4,
        'bolt_hole_diameter': 19.1,
        'bolt_size': '5/8',
        'bolt_circle_diameter': 98.6,
        'weight_kg': 2
    },
    '1-1/2': {
        'nps': '1-1/2',
        'flange_od': 155.4,
        'flange_thickness': 20.6,
        'rf_diameter': 73.2,
        'hub_base_diameter': 69.9,
        'hub_end_diameter': 48.3,
        'hub_length': 68.3,
        'bolt_holes': 4,
        'bolt_hole_diameter': 22.4,
        'bolt_size': '3/4',
        'bolt_circle_diameter': 114.3,
        'weight_kg': 3
    },
    '2': {
        'nps': '2',
        'flange_od': 165.1,
        'flange_thickness': 22.4,
        'rf_diameter': 91.9,
        'hub_base_diameter': 84.1,
        'hub_end_diameter': 60.5,
        'hub_length': 69.9,
        'bolt_holes': 8,
        'bolt_hole_diameter': 19.1,
        'bolt_size': '5/8',
        'bolt_circle_diameter': 127,
        'weight_kg': 4
    },
    '2-1/2': {
        'nps': '2-1/2',
        'flange_od': 190.5,
        'flange_thickness': 25.4,
        'rf_diameter': 104.6,
        'hub_base_diameter': 100.1,
        'hub_end_diameter': 73.2,
        'hub_length': 76.2,
        'bolt_holes': 8,
        'bolt_hole_diameter': 22.4,
        'bolt_size': '3/4',
        'bolt_circle_diameter': 149.4,
        'weight_kg': 5
    },
    '3': {
        'nps': '3',
        'flange_od': 209.6,
        'flange_thickness': 28.4,
        'rf_diameter': 127,
        'hub_base_diameter': 117.3,
        'hub_end_diameter': 88.9,
        'hub_length': 79.2,
        'bolt_holes': 8,
        'bolt_hole_diameter': 22.4,
        'bolt_size': '3/4',
        'bolt_circle_diameter': 168.1,
        'weight_kg': 7
    },
    '3-1/2': {
        'nps': '3-1/2',
        'flange_od': 228.6,
        'flange_thickness': 30.2,
        'rf_diameter': 139.7,
        'hub_base_diameter': 133.4,
        'hub_end_diameter': 101.6,
        'hub_length': 81,
        'bolt_holes': 8,
        'bolt_hole_diameter': 22.4,
        'bolt_size': '3/4',
        'bolt_circle_diameter': 184.2,
        'weight_kg': 8
    },
    '4': {
        'nps': '4',
        'flange_od': 254,
        'flange_thickness': 31.8,
        'rf_diameter': 157.2,
        'hub_base_diameter': 146.1,
        'hub_end_diameter': 114.3,
        'hub_length': 85.9,
        'bolt_holes': 8,
        'bolt_hole_diameter': 22.4,
        'bolt_size': '3/4',
        'bolt_circle_diameter': 200.2,
        'weight_kg': 11
    },
    '5': {
        'nps': '5',
        'flange_od': 279.4,
        'flange_thickness': 35.1,
        'rf_diameter': 185.7,
        'hub_base_diameter': 177.8,
        'hub_end_diameter': 141.2,
        'hub_length': 98.6,
        'bolt_holes': 8,
        'bolt_hole_diameter': 22.4,
        'bolt_size': '3/4',
        'bolt_circle_diameter': 235,
        'weight_kg': 15
    },
    '6': {
        'nps': '6',
        'flange_od': 317.5,
        'flange_thickness': 36.6,
        'rf_diameter': 215.9,
        'hub_base_diameter': 206.2,
        'hub_end_diameter': 168.4,
        'hub_length': 98.6,
        'bolt_holes': 12,
        'bolt_hole_diameter': 22.4,
        'bolt_size': '3/4',
        'bolt_circle_diameter': 269.7,
        'weight_kg': 19
    },
    '8': {
        'nps': '8',
        'flange_od': 381,
        'flange_thickness': 41.1,
        'rf_diameter': 269.7,
        'hub_base_diameter': 260.4,
        'hub_end_diameter': 219.2,
        'hub_length': 111.3,
        'bolt_holes': 12,
        'bolt_hole_diameter': 25.4,
        'bolt_size': '7/8',
        'bolt_circle_diameter': 330.2,
        'weight_kg': 30
    },
    '10': {
        'nps': '10',
        'flange_od': 444.5,
        'flange_thickness': 47.8,
        'rf_diameter': 323.9,
        'hub_base_diameter': 320.5,
        'hub_end_diameter': 273.1,
        'hub_length': 117.3,
        'bolt_holes': 16,
        'bolt_hole_diameter': 28.4,
        'bolt_size': '1',
        'bolt_circle_diameter': 387.4,
        'weight_kg': 41
    },
    '12': {
        'nps': '12',
        'flange_od': 520.7,
        'flange_thickness': 50.8,
        'rf_diameter': 381,
        'hub_base_diameter': 374.7,
        'hub_end_diameter': 323.9,
        'hub_length': 130,
        'bolt_holes': 16,
        'bolt_hole_diameter': 31.8,
        'bolt_size': '1-1/8',
        'bolt_circle_diameter': 450.9,
        'weight_kg': 64
    },
    '14': {
        'nps': '14',
        'flange_od': 584.2,
        'flange_thickness': 53.8,
        'rf_diameter': 412.8,
        'hub_base_diameter': 425.5,
        'hub_end_diameter': 355.6,
        'hub_length': 142.7,
        'bolt_holes': 20,
        'bolt_hole_diameter': 31.8,
        'bolt_size': '1-1/8',
        'bolt_circle_diameter': 514.4,
        'weight_kg': 82
    },
    '16': {
        'nps': '16',
        'flange_od': 647.7,
        'flange_thickness': 57.2,
        'rf_diameter': 469.9,
        'hub_base_diameter': 482.6,
        'hub_end_diameter': 406.4,
        'hub_length': 146.1,
        'bolt_holes': 20,
        'bolt_hole_diameter': 35.1,
        'bolt_size': '1-1/4',
        'bolt_circle_diameter': 571.8,
        'weight_kg': 113
    },
    '18': {
        'nps': '18',
        'flange_od': 711.2,
        'flange_thickness': 60.5,
        'rf_diameter': 533.4,
        'hub_base_diameter': 533.4,
        'hub_end_diameter': 457.2,
        'hub_length': 158.8,
        'bolt_holes': 24,
        'bolt_hole_diameter': 35.1,
        'bolt_size': '1-1/4',
        'bolt_circle_diameter': 628.7,
        'weight_kg': 145
    },
    '20': {
        'nps': '20',
        'flange_od': 774.7,
        'flange_thickness': 63.5,
        'rf_diameter': 584.2,
        'hub_base_diameter': 587.2,
        'hub_end_diameter': 508,
        'hub_length': 162.1,
        'bolt_holes': 24,
        'bolt_hole_diameter': 35.1,
        'bolt_size': '1-1/4',
        'bolt_circle_diameter': 685.8,
        'weight_kg': 181
    },
    '24': {
        'nps': '24',
        'flange_od': 914.4,
        'flange_thickness': 69.9,
        'rf_diameter': 692.2,
        'hub_base_diameter': 701.5,
        'hub_end_diameter': 609.6,
        'hub_length': 168.1,
        'bolt_holes': 24,
        'bolt_hole_diameter': 41.1,
        'bolt_size': '38.1',
        'bolt_circle_diameter': 812.8,
        'weight_kg': 263
    },
}

# Class 400 RF Weld Neck Flanges  
# Note: Some dimensions not provided in this specification
CLASS_400_RF_WN = {
    '1/2': {'nps': '1/2', 'flange_od': 95, 'flange_thickness': 14.3, 'hub_length': 59, 'bolt_holes': 4, 'bolt_hole_diameter': 16, 'bolt_circle_diameter': 66.7},
    '3/4': {'nps': '3/4', 'flange_od': 115, 'flange_thickness': 15.9, 'hub_length': 64, 'bolt_holes': 4, 'bolt_hole_diameter': 20, 'bolt_circle_diameter': 82.6},
    '1': {'nps': '1', 'flange_od': 125, 'flange_thickness': 17.5, 'hub_length': 69, 'bolt_holes': 4, 'bolt_hole_diameter': 20, 'bolt_circle_diameter': 88.9},
    '1-1/4': {'nps': '1-1/4', 'flange_od': 135, 'flange_thickness': 20.7, 'hub_length': 74, 'bolt_holes': 4, 'bolt_hole_diameter': 20, 'bolt_circle_diameter': 98.4},
    '1-1/2': {'nps': '1-1/2', 'flange_od': 155, 'flange_thickness': 22.3, 'hub_length': 77, 'bolt_holes': 4, 'bolt_hole_diameter': 22, 'bolt_circle_diameter': 114.3},
    '2': {'nps': '2', 'flange_od': 165, 'flange_thickness': 25.4, 'hub_length': 80, 'bolt_holes': 8, 'bolt_hole_diameter': 20, 'bolt_circle_diameter': 127},
    '2-1/2': {'nps': '2-1/2', 'flange_od': 190, 'flange_thickness': 28.6, 'hub_length': 86, 'bolt_holes': 8, 'bolt_hole_diameter': 22, 'bolt_circle_diameter': 149.2},
    '3': {'nps': '3', 'flange_od': 210, 'flange_thickness': 31.8, 'hub_length': 90, 'bolt_holes': 8, 'bolt_hole_diameter': 22, 'bolt_circle_diameter': 168.3},
    '3-1/2': {'nps': '3-1/2', 'flange_od': 230, 'flange_thickness': 35, 'hub_length': 93, 'bolt_holes': 8, 'bolt_hole_diameter': 26, 'bolt_circle_diameter': 184.2},
    '4': {'nps': '4', 'flange_od': 255, 'flange_thickness': 35, 'hub_length': 96, 'bolt_holes': 8, 'bolt_hole_diameter': 26, 'bolt_circle_diameter': 200},
    '5': {'nps': '5', 'flange_od': 280, 'flange_thickness': 38.1, 'hub_length': 109, 'bolt_holes': 8, 'bolt_hole_diameter': 26, 'bolt_circle_diameter': 235},
    '6': {'nps': '6', 'flange_od': 320, 'flange_thickness': 41.3, 'hub_length': 115, 'bolt_holes': 12, 'bolt_hole_diameter': 30, 'bolt_circle_diameter': 269.9},
    '8': {'nps': '8', 'flange_od': 380, 'flange_thickness': 47.7, 'hub_length': 124, 'bolt_holes': 12, 'bolt_hole_diameter': 30, 'bolt_circle_diameter': 330},
    '10': {'nps': '10', 'flange_od': 445, 'flange_thickness': 54, 'hub_length': 131, 'bolt_holes': 16, 'bolt_hole_diameter': 32, 'bolt_circle_diameter': 387.5},
    '12': {'nps': '12', 'flange_od': 520, 'flange_thickness': 57.2, 'hub_length': 144, 'bolt_holes': 16, 'bolt_hole_diameter': 35, 'bolt_circle_diameter': 450.8},
    '14': {'nps': '14', 'flange_od': 585, 'flange_thickness': 60.4, 'hub_length': 156, 'bolt_holes': 20, 'bolt_hole_diameter': 35, 'bolt_circle_diameter': 514.4},
    '16': {'nps': '16', 'flange_od': 650, 'flange_thickness': 63.5, 'hub_length': 159, 'bolt_holes': 20, 'bolt_hole_diameter': 38, 'bolt_circle_diameter': 571.5},
    '18': {'nps': '18', 'flange_od': 710, 'flange_thickness': 66.7, 'hub_length': 172, 'bolt_holes': 24, 'bolt_hole_diameter': 38, 'bolt_circle_diameter': 628.6},
    '20': {'nps': '20', 'flange_od': 775, 'flange_thickness': 69.9, 'hub_length': 175, 'bolt_holes': 24, 'bolt_hole_diameter': 42, 'bolt_circle_diameter': 685.8},
    '24': {'nps': '24', 'flange_od': 915, 'flange_thickness': 76.2, 'hub_length': 182, 'bolt_holes': 24, 'bolt_hole_diameter': 48, 'bolt_circle_diameter': 812.8},
}

# Class 600 RF Weld Neck Flanges
CLASS_600_RF_WN = {
    '1/2': {'nps': '1/2', 'flange_od': 95.3, 'flange_thickness': 14.2, 'rf_diameter': 35.1, 'hub_base_diameter': 38.1, 'hub_end_diameter': 21.3, 'hub_length': 52.3, 'bolt_holes': 4, 'bolt_hole_diameter': 15.7, 'bolt_size': '1/2', 'bolt_circle_diameter': 66.5, 'weight_kg': 1},
    '3/4': {'nps': '3/4', 'flange_od': 117.3, 'flange_thickness': 15.7, 'rf_diameter': 42.9, 'hub_base_diameter': 47.8, 'hub_end_diameter': 26.7, 'hub_length': 57.2, 'bolt_holes': 4, 'bolt_hole_diameter': 19.1, 'bolt_size': '5/8', 'bolt_circle_diameter': 82.6, 'weight_kg': 2},
    '1': {'nps': '1', 'flange_od': 124, 'flange_thickness': 17.5, 'rf_diameter': 50.8, 'hub_base_diameter': 53.8, 'hub_end_diameter': 33.5, 'hub_length': 62, 'bolt_holes': 4, 'bolt_hole_diameter': 19.1, 'bolt_size': '5/8', 'bolt_circle_diameter': 88.9, 'weight_kg': 2},
    '1-1/4': {'nps': '1-1/4', 'flange_od': 133.4, 'flange_thickness': 20.6, 'rf_diameter': 63.5, 'hub_base_diameter': 63.5, 'hub_end_diameter': 42.2, 'hub_length': 66.5, 'bolt_holes': 4, 'bolt_hole_diameter': 19.1, 'bolt_size': '5/8', 'bolt_circle_diameter': 98.6, 'weight_kg': 3},
    '1-1/2': {'nps': '1-1/2', 'flange_od': 155.4, 'flange_thickness': 22.4, 'rf_diameter': 73.2, 'hub_base_diameter': 69.9, 'hub_end_diameter': 48.3, 'hub_length': 69.9, 'bolt_holes': 4, 'bolt_hole_diameter': 22.4, 'bolt_size': '3/4', 'bolt_circle_diameter': 114.3, 'weight_kg': 4},
    '2': {'nps': '2', 'flange_od': 165.1, 'flange_thickness': 25.4, 'rf_diameter': 91.9, 'hub_base_diameter': 84.1, 'hub_end_diameter': 60.5, 'hub_length': 73.2, 'bolt_holes': 8, 'bolt_hole_diameter': 19.1, 'bolt_size': '5/8', 'bolt_circle_diameter': 127, 'weight_kg': 5},
    '2-1/2': {'nps': '2-1/2', 'flange_od': 190.5, 'flange_thickness': 28.4, 'rf_diameter': 104.6, 'hub_base_diameter': 100.1, 'hub_end_diameter': 73.2, 'hub_length': 79.2, 'bolt_holes': 8, 'bolt_hole_diameter': 22.4, 'bolt_size': '3/4', 'bolt_circle_diameter': 149.4, 'weight_kg': 8},
    '3': {'nps': '3', 'flange_od': 209.6, 'flange_thickness': 31.8, 'rf_diameter': 127, 'hub_base_diameter': 117.3, 'hub_end_diameter': 88.9, 'hub_length': 82.6, 'bolt_holes': 8, 'bolt_hole_diameter': 22.4, 'bolt_size': '3/4', 'bolt_circle_diameter': 168.1, 'weight_kg': 10},
    '3-1/2': {'nps': '3-1/2', 'flange_od': 228.6, 'flange_thickness': 35.1, 'rf_diameter': 139.7, 'hub_base_diameter': 133.4, 'hub_end_diameter': 101.6, 'hub_length': 85.9, 'bolt_holes': 8, 'bolt_hole_diameter': 25.4, 'bolt_size': '7/8', 'bolt_circle_diameter': 184.2, 'weight_kg': 12},
    '4': {'nps': '4', 'flange_od': 273.1, 'flange_thickness': 38.1, 'rf_diameter': 157.2, 'hub_base_diameter': 152.4, 'hub_end_diameter': 114.3, 'hub_length': 101.6, 'bolt_holes': 8, 'bolt_hole_diameter': 25.4, 'bolt_size': '7/8', 'bolt_circle_diameter': 215.9, 'weight_kg': 19},
    '5': {'nps': '5', 'flange_od': 330.2, 'flange_thickness': 44.5, 'rf_diameter': 185.7, 'hub_base_diameter': 189, 'hub_end_diameter': 141.2, 'hub_length': 114.3, 'bolt_holes': 8, 'bolt_hole_diameter': 28.4, 'bolt_size': '1', 'bolt_circle_diameter': 266.7, 'weight_kg': 31},
    '6': {'nps': '6', 'flange_od': 355.6, 'flange_thickness': 47.8, 'rf_diameter': 215.9, 'hub_base_diameter': 222.3, 'hub_end_diameter': 168.4, 'hub_length': 117.3, 'bolt_holes': 12, 'bolt_hole_diameter': 28.4, 'bolt_size': '1', 'bolt_circle_diameter': 292.1, 'weight_kg': 37},
    '8': {'nps': '8', 'flange_od': 419.1, 'flange_thickness': 55.6, 'rf_diameter': 269.7, 'hub_base_diameter': 273.1, 'hub_end_diameter': 219.2, 'hub_length': 133.4, 'bolt_holes': 12, 'bolt_hole_diameter': 31.8, 'bolt_size': '1-1/8', 'bolt_circle_diameter': 349.3, 'weight_kg': 54},
    '10': {'nps': '10', 'flange_od': 508, 'flange_thickness': 63.5, 'rf_diameter': 323.9, 'hub_base_diameter': 342.9, 'hub_end_diameter': 273.1, 'hub_length': 152.4, 'bolt_holes': 16, 'bolt_hole_diameter': 35.1, 'bolt_size': '1-1/4', 'bolt_circle_diameter': 431.8, 'weight_kg': 86},
    '12': {'nps': '12', 'flange_od': 558.8, 'flange_thickness': 66.5, 'rf_diameter': 381, 'hub_base_diameter': 400.1, 'hub_end_diameter': 323.9, 'hub_length': 155.4, 'bolt_holes': 20, 'bolt_hole_diameter': 35.1, 'bolt_size': '1-1/4', 'bolt_circle_diameter': 489, 'weight_kg': 102},
    '14': {'nps': '14', 'flange_od': 603.3, 'flange_thickness': 69.9, 'rf_diameter': 412.8, 'hub_base_diameter': 431.8, 'hub_end_diameter': 355.6, 'hub_length': 165.1, 'bolt_holes': 20, 'bolt_hole_diameter': 38.1, 'bolt_size': '1-3/8', 'bolt_circle_diameter': 527.1, 'weight_kg': 127},
    '16': {'nps': '16', 'flange_od': 685.8, 'flange_thickness': 76.2, 'rf_diameter': 469.9, 'hub_base_diameter': 495.3, 'hub_end_diameter': 406.4, 'hub_length': 177.8, 'bolt_holes': 20, 'bolt_hole_diameter': 41.1, 'bolt_size': '1-1/2', 'bolt_circle_diameter': 603.3, 'weight_kg': 177},
    '18': {'nps': '18', 'flange_od': 743, 'flange_thickness': 82.6, 'rf_diameter': 533.4, 'hub_base_diameter': 546.1, 'hub_end_diameter': 457.2, 'hub_length': 184.2, 'bolt_holes': 20, 'bolt_hole_diameter': 44.5, 'bolt_size': '1-5/8', 'bolt_circle_diameter': 654.1, 'weight_kg': 215},
    '20': {'nps': '20', 'flange_od': 812.8, 'flange_thickness': 88.9, 'rf_diameter': 584.2, 'hub_base_diameter': 609.6, 'hub_end_diameter': 508, 'hub_length': 190.5, 'bolt_holes': 24, 'bolt_hole_diameter': 44.5, 'bolt_size': '1-5/8', 'bolt_circle_diameter': 723.9, 'weight_kg': 268},
    '24': {'nps': '24', 'flange_od': 939.8, 'flange_thickness': 101.6, 'rf_diameter': 692.2, 'hub_base_diameter': 717.6, 'hub_end_diameter': 609.6, 'hub_length': 203.2, 'bolt_holes': 24, 'bolt_hole_diameter': 50.8, 'bolt_size': '1-7/8', 'bolt_circle_diameter': 838.2, 'weight_kg': 376},
}

# Class 900 RF Weld Neck Flanges
CLASS_900_RF_WN = {
    '1/2': {'nps': '1/2', 'flange_od': 120.7, 'flange_thickness': 22.4, 'rf_diameter': 35.1, 'hub_base_diameter': 38.1, 'hub_end_diameter': 21.3, 'hub_length': 60.5, 'bolt_holes': 4, 'bolt_hole_diameter': 22.4, 'bolt_size': '3/4', 'bolt_circle_diameter': 82.6, 'weight_kg': 2},
    '3/4': {'nps': '3/4', 'flange_od': 130, 'flange_thickness': 25.4, 'rf_diameter': 42.9, 'hub_base_diameter': 44.5, 'hub_end_diameter': 26.7, 'hub_length': 69.9, 'bolt_holes': 4, 'bolt_hole_diameter': 22.4, 'bolt_size': '3/4', 'bolt_circle_diameter': 88.9, 'weight_kg': 3},
    '1': {'nps': '1', 'flange_od': 149.4, 'flange_thickness': 28.4, 'rf_diameter': 50.8, 'hub_base_diameter': 52.3, 'hub_end_diameter': 33.5, 'hub_length': 73.2, 'bolt_holes': 4, 'bolt_hole_diameter': 25.4, 'bolt_size': '7/8', 'bolt_circle_diameter': 101.6, 'weight_kg': 4},
    '1-1/4': {'nps': '1-1/4', 'flange_od': 158.8, 'flange_thickness': 28.4, 'rf_diameter': 63.5, 'hub_base_diameter': 63.5, 'hub_end_diameter': 42.2, 'hub_length': 73.2, 'bolt_holes': 4, 'bolt_hole_diameter': 25.4, 'bolt_size': '7/8', 'bolt_circle_diameter': 111.3, 'weight_kg': 5},
    '1-1/2': {'nps': '1-1/2', 'flange_od': 177.8, 'flange_thickness': 31.8, 'rf_diameter': 73.2, 'hub_base_diameter': 69.9, 'hub_end_diameter': 48.3, 'hub_length': 82.6, 'bolt_holes': 4, 'bolt_hole_diameter': 28.4, 'bolt_size': '1', 'bolt_circle_diameter': 124, 'weight_kg': 6},
    '2': {'nps': '2', 'flange_od': 215.9, 'flange_thickness': 38.1, 'rf_diameter': 91.9, 'hub_base_diameter': 104.6, 'hub_end_diameter': 60.5, 'hub_length': 101.6, 'bolt_holes': 8, 'bolt_hole_diameter': 25.4, 'bolt_size': '7/8', 'bolt_circle_diameter': 165.1, 'weight_kg': 11},
    '2-1/2': {'nps': '2-1/2', 'flange_od': 244.3, 'flange_thickness': 41.1, 'rf_diameter': 104.6, 'hub_base_diameter': 124, 'hub_end_diameter': 73.2, 'hub_length': 104.6, 'bolt_holes': 8, 'bolt_hole_diameter': 28.4, 'bolt_size': '1', 'bolt_circle_diameter': 190.5, 'weight_kg': 16},
    '3': {'nps': '3', 'flange_od': 241.3, 'flange_thickness': 38.1, 'rf_diameter': 127, 'hub_base_diameter': 127, 'hub_end_diameter': 88.9, 'hub_length': 101.6, 'bolt_holes': 8, 'bolt_hole_diameter': 25.4, 'bolt_size': '7/8', 'bolt_circle_diameter': 190.5, 'weight_kg': 14},
    '4': {'nps': '4', 'flange_od': 292.1, 'flange_thickness': 44.5, 'rf_diameter': 157.2, 'hub_base_diameter': 158.8, 'hub_end_diameter': 114.3, 'hub_length': 114.3, 'bolt_holes': 8, 'bolt_hole_diameter': 31.8, 'bolt_size': '1-1/8', 'bolt_circle_diameter': 235, 'weight_kg': 24},
    '5': {'nps': '5', 'flange_od': 349.3, 'flange_thickness': 50.8, 'rf_diameter': 185.7, 'hub_base_diameter': 190.5, 'hub_end_diameter': 141.2, 'hub_length': 127, 'bolt_holes': 8, 'bolt_hole_diameter': 35.1, 'bolt_size': '1-1/4', 'bolt_circle_diameter': 279.4, 'weight_kg': 39},
    '6': {'nps': '6', 'flange_od': 381, 'flange_thickness': 55.6, 'rf_diameter': 215.9, 'hub_base_diameter': 235, 'hub_end_diameter': 168.4, 'hub_length': 139.7, 'bolt_holes': 12, 'bolt_hole_diameter': 31.8, 'bolt_size': '1-1/8', 'bolt_circle_diameter': 317.5, 'weight_kg': 50},
    '8': {'nps': '8', 'flange_od': 469.9, 'flange_thickness': 63.5, 'rf_diameter': 269.7, 'hub_base_diameter': 298.5, 'hub_end_diameter': 219.2, 'hub_length': 162.1, 'bolt_holes': 12, 'bolt_hole_diameter': 38.1, 'bolt_size': '1-3/8', 'bolt_circle_diameter': 393.7, 'weight_kg': 79},
    '10': {'nps': '10', 'flange_od': 546.1, 'flange_thickness': 69.9, 'rf_diameter': 323.9, 'hub_base_diameter': 368.3, 'hub_end_diameter': 273.1, 'hub_length': 184.2, 'bolt_holes': 16, 'bolt_hole_diameter': 38.1, 'bolt_size': '1-3/8', 'bolt_circle_diameter': 469.9, 'weight_kg': 118},
    '12': {'nps': '12', 'flange_od': 609.6, 'flange_thickness': 79.2, 'rf_diameter': 381, 'hub_base_diameter': 419.1, 'hub_end_diameter': 323.9, 'hub_length': 200.2, 'bolt_holes': 20, 'bolt_hole_diameter': 38.1, 'bolt_size': '1-3/8', 'bolt_circle_diameter': 533.4, 'weight_kg': 147},
    '14': {'nps': '14', 'flange_od': 641.4, 'flange_thickness': 85.9, 'rf_diameter': 412.8, 'hub_base_diameter': 450.9, 'hub_end_diameter': 355.6, 'hub_length': 212.9, 'bolt_holes': 20, 'bolt_hole_diameter': 41.1, 'bolt_size': '1-1/2', 'bolt_circle_diameter': 558.8, 'weight_kg': 181},
    '16': {'nps': '16', 'flange_od': 704.9, 'flange_thickness': 88.9, 'rf_diameter': 469.9, 'hub_base_diameter': 508, 'hub_end_diameter': 406.4, 'hub_length': 215.9, 'bolt_holes': 20, 'bolt_hole_diameter': 44.5, 'bolt_size': '1-5/8', 'bolt_circle_diameter': 616, 'weight_kg': 225},
    '18': {'nps': '18', 'flange_od': 787.4, 'flange_thickness': 101.6, 'rf_diameter': 533.4, 'hub_base_diameter': 565.2, 'hub_end_diameter': 457.2, 'hub_length': 228.6, 'bolt_holes': 20, 'bolt_hole_diameter': 50.8, 'bolt_size': '1-7/8', 'bolt_circle_diameter': 685.8, 'weight_kg': 308},
    '20': {'nps': '20', 'flange_od': 857.3, 'flange_thickness': 108, 'rf_diameter': 584.2, 'hub_base_diameter': 622.3, 'hub_end_diameter': 508, 'hub_length': 247.7, 'bolt_holes': 20, 'bolt_hole_diameter': 53.8, 'bolt_size': '2', 'bolt_circle_diameter': 749.3, 'weight_kg': 376},
    '24': {'nps': '24', 'flange_od': 1041.4, 'flange_thickness': 139.7, 'rf_diameter': 692.2, 'hub_base_diameter': 749.3, 'hub_end_diameter': 609.6, 'hub_length': 292.1, 'bolt_holes': 20, 'bolt_hole_diameter': 66.5, 'bolt_size': '2-1/2', 'bolt_circle_diameter': 901.7, 'weight_kg': 680},
}

# Class 1500 RF Weld Neck Flanges
CLASS_1500_RF_WN = {
    '1/2': {'nps': '1/2', 'flange_od': 120.7, 'flange_thickness': 22.4, 'rf_diameter': 35.1, 'hub_base_diameter': 38.1, 'hub_end_diameter': 21.3, 'hub_length': 60.5, 'bolt_holes': 4, 'bolt_hole_diameter': 22.4, 'bolt_size': '3/4', 'bolt_circle_diameter': 82.6, 'weight_kg': 2},
    '3/4': {'nps': '3/4', 'flange_od': 130, 'flange_thickness': 25.4, 'rf_diameter': 42.9, 'hub_base_diameter': 44.5, 'hub_end_diameter': 26.7, 'hub_length': 69.9, 'bolt_holes': 4, 'bolt_hole_diameter': 22.4, 'bolt_size': '3/4', 'bolt_circle_diameter': 88.9, 'weight_kg': 3},
    '1': {'nps': '1', 'flange_od': 149.4, 'flange_thickness': 28.4, 'rf_diameter': 50.8, 'hub_base_diameter': 52.3, 'hub_end_diameter': 33.5, 'hub_length': 73.2, 'bolt_holes': 4, 'bolt_hole_diameter': 25.4, 'bolt_size': '7/8', 'bolt_circle_diameter': 101.6, 'weight_kg': 4},
    '1-1/4': {'nps': '1-1/4', 'flange_od': 158.8, 'flange_thickness': 28.4, 'rf_diameter': 63.5, 'hub_base_diameter': 63.5, 'hub_end_diameter': 42.2, 'hub_length': 73.2, 'bolt_holes': 4, 'bolt_hole_diameter': 25.4, 'bolt_size': '7/8', 'bolt_circle_diameter': 111.3, 'weight_kg': 5},
    '1-1/2': {'nps': '1-1/2', 'flange_od': 177.8, 'flange_thickness': 31.8, 'rf_diameter': 73.2, 'hub_base_diameter': 69.9, 'hub_end_diameter': 48.3, 'hub_length': 82.6, 'bolt_holes': 4, 'bolt_hole_diameter': 28.4, 'bolt_size': '1', 'bolt_circle_diameter': 124, 'weight_kg': 6},
    '2': {'nps': '2', 'flange_od': 215.9, 'flange_thickness': 38.1, 'rf_diameter': 91.9, 'hub_base_diameter': 104.6, 'hub_end_diameter': 60.5, 'hub_length': 101.6, 'bolt_holes': 8, 'bolt_hole_diameter': 25.4, 'bolt_size': '7/8', 'bolt_circle_diameter': 165.1, 'weight_kg': 11},
    '2-1/2': {'nps': '2-1/2', 'flange_od': 244.3, 'flange_thickness': 41.1, 'rf_diameter': 104.6, 'hub_base_diameter': 124, 'hub_end_diameter': 73.2, 'hub_length': 104.6, 'bolt_holes': 8, 'bolt_hole_diameter': 28.4, 'bolt_size': '1', 'bolt_circle_diameter': 190.5, 'weight_kg': 16},
    '3': {'nps': '3', 'flange_od': 266.7, 'flange_thickness': 47.8, 'rf_diameter': 127, 'hub_base_diameter': 133.4, 'hub_end_diameter': 88.9, 'hub_length': 117.3, 'bolt_holes': 8, 'bolt_hole_diameter': 31.8, 'bolt_size': '1-1/8', 'bolt_circle_diameter': 203.2, 'weight_kg': 22},
    '4': {'nps': '4', 'flange_od': 311.2, 'flange_thickness': 53.8, 'rf_diameter': 157.2, 'hub_base_diameter': 162.1, 'hub_end_diameter': 114.3, 'hub_length': 124, 'bolt_holes': 8, 'bolt_hole_diameter': 35.1, 'bolt_size': '1-1/4', 'bolt_circle_diameter': 241.3, 'weight_kg': 33},
    '5': {'nps': '5', 'flange_od': 374.7, 'flange_thickness': 73.2, 'rf_diameter': 185.7, 'hub_base_diameter': 196.9, 'hub_end_diameter': 141.2, 'hub_length': 155.4, 'bolt_holes': 8, 'bolt_hole_diameter': 41.1, 'bolt_size': '1-1/2', 'bolt_circle_diameter': 292.1, 'weight_kg': 59},
    '6': {'nps': '6', 'flange_od': 393.7, 'flange_thickness': 82.6, 'rf_diameter': 215.9, 'hub_base_diameter': 228.6, 'hub_end_diameter': 168.4, 'hub_length': 171.5, 'bolt_holes': 12, 'bolt_hole_diameter': 38.1, 'bolt_size': '1-3/8', 'bolt_circle_diameter': 317.5, 'weight_kg': 75},
    '8': {'nps': '8', 'flange_od': 482.6, 'flange_thickness': 91.9, 'rf_diameter': 269.7, 'hub_base_diameter': 292.1, 'hub_end_diameter': 219.2, 'hub_length': 212.9, 'bolt_holes': 12, 'bolt_hole_diameter': 44.5, 'bolt_size': '1-5/8', 'bolt_circle_diameter': 393.7, 'weight_kg': 125},
    '10': {'nps': '10', 'flange_od': 584.2, 'flange_thickness': 108, 'rf_diameter': 323.9, 'hub_base_diameter': 368.3, 'hub_end_diameter': 273.1, 'hub_length': 254, 'bolt_holes': 12, 'bolt_hole_diameter': 50.8, 'bolt_size': '1-7/8', 'bolt_circle_diameter': 482.6, 'weight_kg': 206},
    '12': {'nps': '12', 'flange_od': 673.1, 'flange_thickness': 124, 'rf_diameter': 381, 'hub_base_diameter': 450.9, 'hub_end_diameter': 323.9, 'hub_length': 282.4, 'bolt_holes': 16, 'bolt_hole_diameter': 53.8, 'bolt_size': '2', 'bolt_circle_diameter': 571.5, 'weight_kg': 313},
    '14': {'nps': '14', 'flange_od': 749.3, 'flange_thickness': 133.4, 'rf_diameter': 412.8, 'hub_base_diameter': 495.3, 'hub_end_diameter': 355.6, 'hub_length': 298.5, 'bolt_holes': 16, 'bolt_hole_diameter': 60.5, 'bolt_size': '2-1/4', 'bolt_circle_diameter': 635, 'weight_kg': 426},
    '16': {'nps': '16', 'flange_od': 825.5, 'flange_thickness': 146.1, 'rf_diameter': 469.9, 'hub_base_diameter': 552.5, 'hub_end_diameter': 406.4, 'hub_length': 311.2, 'bolt_holes': 16, 'bolt_hole_diameter': 66.5, 'bolt_size': '2-1/2', 'bolt_circle_diameter': 704.9, 'weight_kg': 567},
    '18': {'nps': '18', 'flange_od': 914.4, 'flange_thickness': 162.1, 'rf_diameter': 533.4, 'hub_base_diameter': 569.9, 'hub_end_diameter': 457.2, 'hub_length': 327.2, 'bolt_holes': 16, 'bolt_hole_diameter': 73.2, 'bolt_size': '2-3/4', 'bolt_circle_diameter': 774.7, 'weight_kg': 737},
    '20': {'nps': '20', 'flange_od': 984.3, 'flange_thickness': 177.8, 'rf_diameter': 584.2, 'hub_base_diameter': 641.4, 'hub_end_diameter': 508, 'hub_length': 355.6, 'bolt_holes': 16, 'bolt_hole_diameter': 79.2, 'bolt_size': '3', 'bolt_circle_diameter': 831.9, 'weight_kg': 930},
    '24': {'nps': '24', 'flange_od': 1168.4, 'flange_thickness': 203.2, 'rf_diameter': 692.2, 'hub_base_diameter': 762, 'hub_end_diameter': 609.6, 'hub_length': 406.4, 'bolt_holes': 16, 'bolt_hole_diameter': 91.9, 'bolt_size': '3-1/2', 'bolt_circle_diameter': 990.6, 'weight_kg': 1508},
}

# Class 2500 RF Weld Neck Flanges
CLASS_2500_RF_WN = {
    '1/2': {'nps': '1/2', 'flange_od': 133.4, 'flange_thickness': 30.2, 'rf_diameter': 35.1, 'hub_base_diameter': 42.9, 'hub_end_diameter': 21.3, 'hub_length': 73.2, 'bolt_holes': 4, 'bolt_hole_diameter': 22.4, 'bolt_size': '3/4', 'bolt_circle_diameter': 88.9, 'weight_kg': 3},
    '3/4': {'nps': '3/4', 'flange_od': 139.7, 'flange_thickness': 31.8, 'rf_diameter': 42.9, 'hub_base_diameter': 50.8, 'hub_end_diameter': 26.7, 'hub_length': 79.2, 'bolt_holes': 4, 'bolt_hole_diameter': 22.4, 'bolt_size': '3/4', 'bolt_circle_diameter': 95.3, 'weight_kg': 4},
    '1': {'nps': '1', 'flange_od': 158.8, 'flange_thickness': 35.1, 'rf_diameter': 50.8, 'hub_base_diameter': 57.2, 'hub_end_diameter': 33.5, 'hub_length': 88.9, 'bolt_holes': 4, 'bolt_hole_diameter': 25.4, 'bolt_size': '7/8', 'bolt_circle_diameter': 108, 'weight_kg': 5},
    '1-1/4': {'nps': '1-1/4', 'flange_od': 184.2, 'flange_thickness': 38.1, 'rf_diameter': 63.5, 'hub_base_diameter': 73.2, 'hub_end_diameter': 42.2, 'hub_length': 95.3, 'bolt_holes': 4, 'bolt_hole_diameter': 28.4, 'bolt_size': '1', 'bolt_circle_diameter': 130, 'weight_kg': 8},
    '1-1/2': {'nps': '1-1/2', 'flange_od': 203.2, 'flange_thickness': 44.5, 'rf_diameter': 73.2, 'hub_base_diameter': 79.2, 'hub_end_diameter': 48.3, 'hub_length': 111.3, 'bolt_holes': 4, 'bolt_hole_diameter': 31.8, 'bolt_size': '1-1/8', 'bolt_circle_diameter': 146.1, 'weight_kg': 11},
    '2': {'nps': '2', 'flange_od': 235, 'flange_thickness': 50.8, 'rf_diameter': 91.9, 'hub_base_diameter': 95.3, 'hub_end_diameter': 60.5, 'hub_length': 127, 'bolt_holes': 8, 'bolt_hole_diameter': 28.4, 'bolt_size': '1', 'bolt_circle_diameter': 171.5, 'weight_kg': 19},
    '2-1/2': {'nps': '2-1/2', 'flange_od': 266.7, 'flange_thickness': 57.2, 'rf_diameter': 104.6, 'hub_base_diameter': 114.3, 'hub_end_diameter': 73.2, 'hub_length': 142.7, 'bolt_holes': 8, 'bolt_hole_diameter': 31.8, 'bolt_size': '1-1/8', 'bolt_circle_diameter': 196.9, 'weight_kg': 24},
    '3': {'nps': '3', 'flange_od': 304.8, 'flange_thickness': 66.5, 'rf_diameter': 127, 'hub_base_diameter': 133.4, 'hub_end_diameter': 88.9, 'hub_length': 168.1, 'bolt_holes': 8, 'bolt_hole_diameter': 35.1, 'bolt_size': '1-1/4', 'bolt_circle_diameter': 228.6, 'weight_kg': 43},
    '4': {'nps': '4', 'flange_od': 355.6, 'flange_thickness': 76.2, 'rf_diameter': 157.2, 'hub_base_diameter': 165.1, 'hub_end_diameter': 114.3, 'hub_length': 190.5, 'bolt_holes': 8, 'bolt_hole_diameter': 41.1, 'bolt_size': '1-1/2', 'bolt_circle_diameter': 273.1, 'weight_kg': 66},
    '5': {'nps': '5', 'flange_od': 419.1, 'flange_thickness': 91.9, 'rf_diameter': 185.7, 'hub_base_diameter': 203.2, 'hub_end_diameter': 141.2, 'hub_length': 228.6, 'bolt_holes': 8, 'bolt_hole_diameter': 47.8, 'bolt_size': '1-3/4', 'bolt_circle_diameter': 323.9, 'weight_kg': 111},
    '6': {'nps': '6', 'flange_od': 482.6, 'flange_thickness': 108, 'rf_diameter': 215.9, 'hub_base_diameter': 235, 'hub_end_diameter': 168.4, 'hub_length': 273.1, 'bolt_holes': 8, 'bolt_hole_diameter': 53.8, 'bolt_size': '2', 'bolt_circle_diameter': 368.3, 'weight_kg': 172},
    '8': {'nps': '8', 'flange_od': 552.5, 'flange_thickness': 127, 'rf_diameter': 269.7, 'hub_base_diameter': 304.8, 'hub_end_diameter': 219.2, 'hub_length': 317.5, 'bolt_holes': 12, 'bolt_hole_diameter': 53.8, 'bolt_size': '2', 'bolt_circle_diameter': 438.2, 'weight_kg': 263},
    '10': {'nps': '10', 'flange_od': 673.1, 'flange_thickness': 165.1, 'rf_diameter': 323.9, 'hub_base_diameter': 374.7, 'hub_end_diameter': 273.1, 'hub_length': 419.1, 'bolt_holes': 12, 'bolt_hole_diameter': 66.5, 'bolt_size': '2-1/2', 'bolt_circle_diameter': 539.8, 'weight_kg': 488},
    '12': {'nps': '12', 'flange_od': 762, 'flange_thickness': 184.2, 'rf_diameter': 381, 'hub_base_diameter': 441.5, 'hub_end_diameter': 323.9, 'hub_length': 463.6, 'bolt_holes': 12, 'bolt_hole_diameter': 73.2, 'bolt_size': '2-3/4', 'bolt_circle_diameter': 619.3, 'weight_kg': 692},
}

# ASME B16.47 Series B RF Weld Neck Flanges (Large Diameter 26"-60")
B1647_SERIES_B_RF_WN = {
    '26': {'nps': '26', 'flange_od': 785.9, 'flange_thickness': 41.1, 'hub_length': 88.9, 'hub_base_diameter': 684.3, 'hub_end_diameter': 661.9, 'rf_diameter': 771.2, 'bolt_circle_diameter': 744.5, 'bolt_holes': 36, 'bolt_hole_diameter': 22.4, 'bolt_size': '19.1', 'fillet_radius': 9.7, 'weight_kg': 63},
    '28': {'nps': '28', 'flange_od': 836.7, 'flange_thickness': 44.5, 'hub_length': 95.3, 'hub_base_diameter': 735.1, 'hub_end_diameter': 712.7, 'rf_diameter': 762, 'bolt_circle_diameter': 795.3, 'bolt_holes': 40, 'bolt_hole_diameter': 22.4, 'bolt_size': '19.1', 'fillet_radius': 9.7, 'weight_kg': 72},
    '30': {'nps': '30', 'flange_od': 887.5, 'flange_thickness': 44.5, 'hub_length': 100.1, 'hub_base_diameter': 787.4, 'hub_end_diameter': 763.5, 'rf_diameter': 812.8, 'bolt_circle_diameter': 846.1, 'bolt_holes': 44, 'bolt_hole_diameter': 22.4, 'bolt_size': '19.1', 'fillet_radius': 9.7, 'weight_kg': 79},
    '32': {'nps': '32', 'flange_od': 941.3, 'flange_thickness': 46, 'hub_length': 108, 'hub_base_diameter': 839.7, 'hub_end_diameter': 814.3, 'rf_diameter': 863.6, 'bolt_circle_diameter': 900.2, 'bolt_holes': 48, 'bolt_hole_diameter': 22.4, 'bolt_size': '19.1', 'fillet_radius': 9.7, 'weight_kg': 91},
    '34': {'nps': '34', 'flange_od': 1004.8, 'flange_thickness': 49.3, 'hub_length': 110.2, 'hub_base_diameter': 892, 'hub_end_diameter': 865.1, 'rf_diameter': 920.8, 'bolt_circle_diameter': 957.3, 'bolt_holes': 40, 'bolt_hole_diameter': 25.4, 'bolt_size': '22.2', 'fillet_radius': 9.7, 'weight_kg': 109},
    '36': {'nps': '36', 'flange_od': 1057.1, 'flange_thickness': 52.3, 'hub_length': 117.3, 'hub_base_diameter': 944.6, 'hub_end_diameter': 915.9, 'rf_diameter': 971.6, 'bolt_circle_diameter': 1009.7, 'bolt_holes': 44, 'bolt_hole_diameter': 25.4, 'bolt_size': '22.2', 'fillet_radius': 9.7, 'weight_kg': 124},
    '38': {'nps': '38', 'flange_od': 1124, 'flange_thickness': 53.8, 'hub_length': 124, 'hub_base_diameter': 996.95, 'hub_end_diameter': 968.2, 'rf_diameter': 1022.4, 'bolt_circle_diameter': 1069.8, 'bolt_holes': 40, 'bolt_hole_diameter': 28.4, 'bolt_size': '25.7', 'fillet_radius': 9.7, 'weight_kg': 146},
    '40': {'nps': '40', 'flange_od': 1174.8, 'flange_thickness': 55.6, 'hub_length': 128.5, 'hub_base_diameter': 1049.3, 'hub_end_diameter': 1019, 'rf_diameter': 1079.5, 'bolt_circle_diameter': 1120.6, 'bolt_holes': 44, 'bolt_hole_diameter': 28.4, 'bolt_size': '25.4', 'fillet_radius': 9.7, 'weight_kg': 159},
    '42': {'nps': '42', 'flange_od': 1225.6, 'flange_thickness': 58.7, 'hub_length': 133.4, 'hub_base_diameter': 1101.9, 'hub_end_diameter': 1069.8, 'rf_diameter': 1130.3, 'bolt_circle_diameter': 1171.4, 'bolt_holes': 48, 'bolt_hole_diameter': 28.4, 'bolt_size': '25.4', 'fillet_radius': 11.2, 'weight_kg': 175},
    '44': {'nps': '44', 'flange_od': 1276.4, 'flange_thickness': 60.5, 'hub_length': 136.7, 'hub_base_diameter': 1152.7, 'hub_end_diameter': 1120.6, 'rf_diameter': 1181.1, 'bolt_circle_diameter': 1222.2, 'bolt_holes': 52, 'bolt_hole_diameter': 28.4, 'bolt_size': '25.4', 'fillet_radius': 11.2, 'weight_kg': 187},
    '46': {'nps': '46', 'flange_od': 1341.4, 'flange_thickness': 62, 'hub_length': 144.5, 'hub_base_diameter': 1205, 'hub_end_diameter': 1171.4, 'rf_diameter': 1234.9, 'bolt_circle_diameter': 1284.2, 'bolt_holes': 40, 'bolt_hole_diameter': 31.8, 'bolt_size': '28.6', 'fillet_radius': 11.2, 'weight_kg': 220},
    '48': {'nps': '48', 'flange_od': 1392.2, 'flange_thickness': 65, 'hub_length': 149.4, 'hub_base_diameter': 1257.3, 'hub_end_diameter': 1222.2, 'rf_diameter': 1289.1, 'bolt_circle_diameter': 1335, 'bolt_holes': 44, 'bolt_hole_diameter': 31.8, 'bolt_size': '28.6', 'fillet_radius': 11.2, 'weight_kg': 239},
    '50': {'nps': '50', 'flange_od': 1443, 'flange_thickness': 68.3, 'hub_length': 153.9, 'hub_base_diameter': 1308.1, 'hub_end_diameter': 1273, 'rf_diameter': 1339.9, 'bolt_circle_diameter': 1385.8, 'bolt_holes': 48, 'bolt_hole_diameter': 31.8, 'bolt_size': '28.6', 'fillet_radius': 11.2, 'weight_kg': 258},
    '52': {'nps': '52', 'flange_od': 1493.8, 'flange_thickness': 69.9, 'hub_length': 157.2, 'hub_base_diameter': 1360.4, 'hub_end_diameter': 1323.8, 'rf_diameter': 1390.7, 'bolt_circle_diameter': 1436.6, 'bolt_holes': 52, 'bolt_hole_diameter': 31.8, 'bolt_size': '28.6', 'fillet_radius': 11.2, 'weight_kg': 274},
    '54': {'nps': '54', 'flange_od': 1549.4, 'flange_thickness': 71.4, 'hub_length': 162.1, 'hub_base_diameter': 1412.7, 'hub_end_diameter': 1374.6, 'rf_diameter': 1441.5, 'bolt_circle_diameter': 1492.3, 'bolt_holes': 56, 'bolt_hole_diameter': 31.8, 'bolt_size': '28.6', 'fillet_radius': 11.2, 'weight_kg': 299},
    '56': {'nps': '56', 'flange_od': 1600.2, 'flange_thickness': 73.2, 'hub_length': 166.6, 'hub_base_diameter': 1465.3, 'hub_end_diameter': 1425.4, 'rf_diameter': 1492.3, 'bolt_circle_diameter': 1543.1, 'bolt_holes': 60, 'bolt_hole_diameter': 31.8, 'bolt_size': '28.6', 'fillet_radius': 14.2, 'weight_kg': 318},
    '58': {'nps': '58', 'flange_od': 1674.9, 'flange_thickness': 74.7, 'hub_length': 174.8, 'hub_base_diameter': 1516.1, 'hub_end_diameter': 1476.2, 'rf_diameter': 1543.1, 'bolt_circle_diameter': 1611.4, 'bolt_holes': 48, 'bolt_hole_diameter': 35.1, 'bolt_size': '31.8', 'fillet_radius': 14.2, 'weight_kg': 377},
    '60': {'nps': '60', 'flange_od': 1725.7, 'flange_thickness': 76.2, 'hub_length': 179.3, 'hub_base_diameter': 1570, 'hub_end_diameter': 1527, 'rf_diameter': 1600.2, 'bolt_circle_diameter': 1662.2, 'bolt_holes': 52, 'bolt_hole_diameter': 35.1, 'bolt_size': '31.8', 'fillet_radius': 14.2, 'weight_kg': 401},
}

# ASME B16.47 Series B RF Class 300 Weld Neck Flanges (Large Diameter 26"-60")
B1647_SERIES_B_CLASS300_RF_WN = {
    '26': {'nps': '26', 'flange_od': 899.6, 'flange_thickness': 88.9, 'hub_length': 144.5, 'hub_base_diameter': 701.5, 'hub_end_diameter': 665.2, 'rf_diameter': 936.6, 'bolt_circle_diameter': 803.1, 'bolt_holes': 32, 'bolt_hole_diameter': 35.1, 'bolt_size': '31.8', 'fillet_radius': 14.2, 'weight_kg': 185},
    '28': {'nps': '28', 'flange_od': 920.8, 'flange_thickness': 88.9, 'hub_length': 149.4, 'hub_base_diameter': 755.7, 'hub_end_diameter': 716, 'rf_diameter': 787.4, 'bolt_circle_diameter': 857.3, 'bolt_holes': 36, 'bolt_hole_diameter': 35.1, 'bolt_size': '31.8', 'fillet_radius': 14.2, 'weight_kg': 202},
    '30': {'nps': '30', 'flange_od': 990.6, 'flange_thickness': 93.7, 'hub_length': 158, 'hub_base_diameter': 812.8, 'hub_end_diameter': 768.4, 'rf_diameter': 844.6, 'bolt_circle_diameter': 920.8, 'bolt_holes': 36, 'bolt_hole_diameter': 38.1, 'bolt_size': '34.9', 'fillet_radius': 14.2, 'weight_kg': 246},
    '32': {'nps': '32', 'flange_od': 1054.1, 'flange_thickness': 103.1, 'hub_length': 168.1, 'hub_base_diameter': 863.6, 'hub_end_diameter': 819.2, 'rf_diameter': 901.7, 'bolt_circle_diameter': 977.9, 'bolt_holes': 32, 'bolt_hole_diameter': 41.1, 'bolt_size': '38.1', 'fillet_radius': 15.7, 'weight_kg': 302},
    '34': {'nps': '34', 'flange_od': 1107.9, 'flange_thickness': 103.1, 'hub_length': 173, 'hub_base_diameter': 917.4, 'hub_end_diameter': 870, 'rf_diameter': 952.6, 'bolt_circle_diameter': 1031.7, 'bolt_holes': 36, 'bolt_hole_diameter': 41.1, 'bolt_size': '38.1', 'fillet_radius': 15.7, 'weight_kg': 324},
    '36': {'nps': '36', 'flange_od': 1171.4, 'flange_thickness': 103.1, 'hub_length': 180.8, 'hub_base_diameter': 965.2, 'hub_end_diameter': 920.8, 'rf_diameter': 1009.7, 'bolt_circle_diameter': 1089.7, 'bolt_holes': 32, 'bolt_hole_diameter': 44.5, 'bolt_size': '41.3', 'fillet_radius': 15.7, 'weight_kg': 363},
    '38': {'nps': '38', 'flange_od': 1222.2, 'flange_thickness': 111.3, 'hub_length': 192, 'hub_base_diameter': 1016, 'hub_end_diameter': 971.6, 'rf_diameter': 1066.5, 'bolt_circle_diameter': 1140, 'bolt_holes': 36, 'bolt_hole_diameter': 44.5, 'bolt_size': '41.3', 'fillet_radius': 15.7, 'weight_kg': 407},
    '40': {'nps': '40', 'flange_od': 1273, 'flange_thickness': 115.8, 'hub_length': 198.4, 'hub_base_diameter': 1066.8, 'hub_end_diameter': 1022.4, 'rf_diameter': 1114.6, 'bolt_circle_diameter': 1190.8, 'bolt_holes': 40, 'bolt_hole_diameter': 44.5, 'bolt_size': '41.3', 'fillet_radius': 15.7, 'weight_kg': 440},
    '42': {'nps': '42', 'flange_od': 1333.5, 'flange_thickness': 119.1, 'hub_length': 204.7, 'hub_base_diameter': 1117.6, 'hub_end_diameter': 1074.7, 'rf_diameter': 1168.4, 'bolt_circle_diameter': 1244.6, 'bolt_holes': 36, 'bolt_hole_diameter': 47.8, 'bolt_size': '44.5', 'fillet_radius': 15.7, 'weight_kg': 489},
    '44': {'nps': '44', 'flange_od': 1384.3, 'flange_thickness': 127, 'hub_length': 214.4, 'hub_base_diameter': 1173.2, 'hub_end_diameter': 1125.2, 'rf_diameter': 1219.2, 'bolt_circle_diameter': 1295.4, 'bolt_holes': 40, 'bolt_hole_diameter': 47.8, 'bolt_size': '44.5', 'fillet_radius': 15.7, 'weight_kg': 541},
    '46': {'nps': '46', 'flange_od': 1460.5, 'flange_thickness': 128.5, 'hub_length': 222.3, 'hub_base_diameter': 1228.9, 'hub_end_diameter': 1176.3, 'rf_diameter': 1270, 'bolt_circle_diameter': 1365.3, 'bolt_holes': 36, 'bolt_hole_diameter': 50.8, 'bolt_size': '47.6', 'fillet_radius': 15.7, 'weight_kg': 637},
    '48': {'nps': '48', 'flange_od': 1511.3, 'flange_thickness': 128.5, 'hub_length': 223.8, 'hub_base_diameter': 1277.9, 'hub_end_diameter': 1227.1, 'rf_diameter': 1327.2, 'bolt_circle_diameter': 1416.1, 'bolt_holes': 40, 'bolt_hole_diameter': 50.8, 'bolt_size': '47.6', 'fillet_radius': 15.7, 'weight_kg': 656},
    '50': {'nps': '50', 'flange_od': 1562.1, 'flange_thickness': 138.2, 'hub_length': 235, 'hub_base_diameter': 1330.5, 'hub_end_diameter': 1277.9, 'rf_diameter': 1378, 'bolt_circle_diameter': 1466.9, 'bolt_holes': 44, 'bolt_hole_diameter': 50.8, 'bolt_size': '47.6', 'fillet_radius': 15.7, 'weight_kg': 724},
    '52': {'nps': '52', 'flange_od': 1612.9, 'flange_thickness': 142.7, 'hub_length': 242.8, 'hub_base_diameter': 1382.8, 'hub_end_diameter': 1328.7, 'rf_diameter': 1428.8, 'bolt_circle_diameter': 1517.7, 'bolt_holes': 48, 'bolt_hole_diameter': 50.8, 'bolt_size': '47.6', 'fillet_radius': 15.7, 'weight_kg': 772},
    '54': {'nps': '54', 'flange_od': 1673.4, 'flange_thickness': 136.7, 'hub_length': 239.8, 'hub_base_diameter': 1435.1, 'hub_end_diameter': 1379.5, 'rf_diameter': 1479.6, 'bolt_circle_diameter': 1577.8, 'bolt_holes': 48, 'bolt_hole_diameter': 50.8, 'bolt_size': '47.6', 'fillet_radius': 15.7, 'weight_kg': 803},
    '56': {'nps': '56', 'flange_od': 1765.3, 'flange_thickness': 153.9, 'hub_length': 268.2, 'hub_base_diameter': 1493.8, 'hub_end_diameter': 1430.3, 'rf_diameter': 1536.7, 'bolt_circle_diameter': 1651, 'bolt_holes': 36, 'bolt_hole_diameter': 60.5, 'bolt_size': '57.2', 'fillet_radius': 17.5, 'weight_kg': 1075},
    '58': {'nps': '58', 'flange_od': 1827.3, 'flange_thickness': 153.9, 'hub_length': 274.6, 'hub_base_diameter': 1547.9, 'hub_end_diameter': 1481.1, 'rf_diameter': 1593.9, 'bolt_circle_diameter': 1713, 'bolt_holes': 40, 'bolt_hole_diameter': 60.5, 'bolt_size': '57.2', 'fillet_radius': 17.5, 'weight_kg': 1132},
    '60': {'nps': '60', 'flange_od': 1878, 'flange_thickness': 150.9, 'hub_length': 271.5, 'hub_base_diameter': 1598.7, 'hub_end_diameter': 1531.9, 'rf_diameter': 1651, 'bolt_circle_diameter': 1763.8, 'bolt_holes': 40, 'bolt_hole_diameter': 60.5, 'bolt_size': '57.2', 'fillet_radius': 17.5, 'weight_kg': 1168},
}

# ASME B16.47 Series B RF Class 600 Weld Neck Flanges (Large Diameter 26"-60")
B1647_SERIES_B_CLASS600_RF_WN = {
    '26': {'nps': '26', 'flange_od': 889, 'flange_thickness': 111.3, 'hub_length': 180.8, 'hub_base_diameter': 698.5, 'hub_end_diameter': 660.4, 'rf_diameter': 726.9, 'bolt_circle_diameter': 806.5, 'bolt_holes': 28, 'bolt_hole_diameter': 44.5, 'bolt_size': '41.3', 'fillet_radius': 12.7, 'weight_kg': 259},
    '28': {'nps': '28', 'flange_od': 952.5, 'flange_thickness': 115.8, 'hub_length': 190.5, 'hub_base_diameter': 752.3, 'hub_end_diameter': 711.2, 'rf_diameter': 784.4, 'bolt_circle_diameter': 863.6, 'bolt_holes': 28, 'bolt_hole_diameter': 47.8, 'bolt_size': '44.5', 'fillet_radius': 12.7, 'weight_kg': 303},
    '30': {'nps': '30', 'flange_od': 1022.5, 'flange_thickness': 125.5, 'hub_length': 204.7, 'hub_base_diameter': 806.5, 'hub_end_diameter': 762, 'rf_diameter': 841.2, 'bolt_circle_diameter': 927.1, 'bolt_holes': 28, 'bolt_hole_diameter': 50.8, 'bolt_size': '47.6', 'fillet_radius': 12.7, 'weight_kg': 376},
    '32': {'nps': '32', 'flange_od': 1085.9, 'flange_thickness': 130, 'hub_length': 215.9, 'hub_base_diameter': 860.6, 'hub_end_diameter': 812.8, 'rf_diameter': 895.4, 'bolt_circle_diameter': 984.3, 'bolt_holes': 28, 'bolt_hole_diameter': 53.8, 'bolt_size': '50.8', 'fillet_radius': 12.7, 'weight_kg': 435},
    '34': {'nps': '34', 'flange_od': 1212.9, 'flange_thickness': 146.3, 'hub_length': 242.8, 'hub_base_diameter': 968.2, 'hub_end_diameter': 914.4, 'rf_diameter': 1009.7, 'bolt_circle_diameter': 1104.9, 'bolt_holes': 24, 'bolt_hole_diameter': 60.5, 'bolt_size': '57.2', 'fillet_radius': 14.2, 'weight_kg': 548},
    '36': {'nps': '36', 'flange_od': 1212.9, 'flange_thickness': 146.3, 'hub_length': 242.8, 'hub_base_diameter': 968.2, 'hub_end_diameter': 914.4, 'rf_diameter': 1009.7, 'bolt_circle_diameter': 1104.9, 'bolt_holes': 28, 'bolt_hole_diameter': 60.5, 'bolt_size': '57.2', 'fillet_radius': 14.2, 'weight_kg': 590},
    '38': {'nps': '38', 'flange_od': 1270, 'flange_thickness': 152.4, 'hub_length': 254, 'hub_base_diameter': 1022.4, 'hub_end_diameter': 965.2, 'rf_diameter': 1054.1, 'bolt_circle_diameter': 1162.1, 'bolt_holes': 28, 'bolt_hole_diameter': 60.5, 'bolt_size': '57.2', 'fillet_radius': 14.2, 'weight_kg': 667},
    '40': {'nps': '40', 'flange_od': 1320, 'flange_thickness': 158.8, 'hub_length': 263.7, 'hub_base_diameter': 1073.2, 'hub_end_diameter': 1016, 'rf_diameter': 1111.3, 'bolt_circle_diameter': 1212.9, 'bolt_holes': 32, 'bolt_hole_diameter': 60.5, 'bolt_size': '57.2', 'fillet_radius': 14.2, 'weight_kg': 717},
    '42': {'nps': '42', 'flange_od': 1403.4, 'flange_thickness': 168.1, 'hub_length': 279.4, 'hub_base_diameter': 1127.3, 'hub_end_diameter': 1066.8, 'rf_diameter': 1168.4, 'bolt_circle_diameter': 1282.7, 'bolt_holes': 28, 'bolt_hole_diameter': 66.5, 'bolt_size': '63.5', 'fillet_radius': 14.2, 'weight_kg': 886},
    '44': {'nps': '44', 'flange_od': 1454.2, 'flange_thickness': 173, 'hub_length': 289.1, 'hub_base_diameter': 1181.1, 'hub_end_diameter': 1117.6, 'rf_diameter': 1225.6, 'bolt_circle_diameter': 1333.5, 'bolt_holes': 32, 'bolt_hole_diameter': 66.5, 'bolt_size': '63.5', 'fillet_radius': 14.2, 'weight_kg': 940},
    '46': {'nps': '46', 'flange_od': 1511.3, 'flange_thickness': 179.3, 'hub_length': 300, 'hub_base_diameter': 1234.9, 'hub_end_diameter': 1168.4, 'rf_diameter': 1276.4, 'bolt_circle_diameter': 1390.7, 'bolt_holes': 32, 'bolt_hole_diameter': 66.5, 'bolt_size': '63.5', 'fillet_radius': 14.2, 'weight_kg': 1044},
    '48': {'nps': '48', 'flange_od': 1593.9, 'flange_thickness': 189, 'hub_length': 316, 'hub_base_diameter': 1289.1, 'hub_end_diameter': 1219.2, 'rf_diameter': 1333.5, 'bolt_circle_diameter': 1460.5, 'bolt_holes': 32, 'bolt_hole_diameter': 73.12, 'bolt_size': '69.9', 'fillet_radius': 14.2, 'weight_kg': 1236},
    '50': {'nps': '50', 'flange_od': 1670.1, 'flange_thickness': 196.9, 'hub_length': 328.7, 'hub_base_diameter': 1343.2, 'hub_end_diameter': 1270, 'rf_diameter': 1384.3, 'bolt_circle_diameter': 1524, 'bolt_holes': 28, 'bolt_hole_diameter': 79.2, 'bolt_size': '76.2', 'fillet_radius': 14.2, 'weight_kg': 1442},
    '52': {'nps': '52', 'flange_od': 1720.9, 'flange_thickness': 203.2, 'hub_length': 336.6, 'hub_base_diameter': 1394, 'hub_end_diameter': 1320.8, 'rf_diameter': 1435.1, 'bolt_circle_diameter': 1574.8, 'bolt_holes': 32, 'bolt_hole_diameter': 79.2, 'bolt_size': '76.2', 'fillet_radius': 14.2, 'weight_kg': 1514},
    '54': {'nps': '54', 'flange_od': 1778, 'flange_thickness': 209.6, 'hub_length': 349.3, 'hub_base_diameter': 1449.8, 'hub_end_diameter': 1371.6, 'rf_diameter': 1492.3, 'bolt_circle_diameter': 1632, 'bolt_holes': 32, 'bolt_hole_diameter': 79.2, 'bolt_size': '76.2', 'fillet_radius': 14.2, 'weight_kg': 1659},
    '56': {'nps': '56', 'flange_od': 1854.2, 'flange_thickness': 217.4, 'hub_length': 362, 'hub_base_diameter': 1501.6, 'hub_end_diameter': 1422.4, 'rf_diameter': 1543.1, 'bolt_circle_diameter': 1695.5, 'bolt_holes': 32, 'bolt_hole_diameter': 85.9, 'bolt_size': '82.6', 'fillet_radius': 15.7, 'weight_kg': 1869},
    '58': {'nps': '58', 'flange_od': 1905, 'flange_thickness': 222.3, 'hub_length': 369.8, 'hub_base_diameter': 1552.4, 'hub_end_diameter': 1473.2, 'rf_diameter': 1600.2, 'bolt_circle_diameter': 1746.3, 'bolt_holes': 32, 'bolt_hole_diameter': 85.9, 'bolt_size': '82.6', 'fillet_radius': 15.7, 'weight_kg': 1981},
    '60': {'nps': '60', 'flange_od': 1993.9, 'flange_thickness': 233.4, 'hub_length': 388.9, 'hub_base_diameter': 1609.9, 'hub_end_diameter': 1524, 'rf_diameter': 1657.4, 'bolt_circle_diameter': 1822.5, 'bolt_holes': 28, 'bolt_hole_diameter': 91.9, 'bolt_size': '88.9', 'fillet_radius': 17.5, 'weight_kg': 2382},
}

# ASME B16.47 Series B RF Class 900 Weld Neck Flanges (Large Diameter 26"-48")
B1647_SERIES_B_CLASS900_RF_WN = {
    '26': {'nps': '26', 'flange_od': 1022.4, 'flange_thickness': 134.9, 'hub_length': 258.8, 'hub_base_diameter': 743, 'hub_end_diameter': 660.4, 'rf_diameter': 962, 'bolt_circle_diameter': 901.7, 'bolt_holes': 20, 'bolt_hole_diameter': 66.5, 'bolt_size': '63.5', 'fillet_radius': 11.2, 'weight_kg': 538},
    '28': {'nps': '28', 'flange_od': 1104.9, 'flange_thickness': 147.6, 'hub_length': 276.4, 'hub_base_diameter': 797.1, 'hub_end_diameter': 711.2, 'rf_diameter': 819.2, 'bolt_circle_diameter': 971.6, 'bolt_holes': 20, 'bolt_hole_diameter': 73.2, 'bolt_size': '69.9', 'fillet_radius': 12.7, 'weight_kg': 675},
    '30': {'nps': '30', 'flange_od': 1181.1, 'flange_thickness': 155.4, 'hub_length': 289.1, 'hub_base_diameter': 850.9, 'hub_end_diameter': 762, 'rf_diameter': 876.3, 'bolt_circle_diameter': 1035.1, 'bolt_holes': 20, 'bolt_hole_diameter': 79.2, 'bolt_size': '76.2', 'fillet_radius': 12.7, 'weight_kg': 798},
    '32': {'nps': '32', 'flange_od': 1238.3, 'flange_thickness': 160.3, 'hub_length': 303.3, 'hub_base_diameter': 908.1, 'hub_end_diameter': 812.8, 'rf_diameter': 927.1, 'bolt_circle_diameter': 1092.2, 'bolt_holes': 20, 'bolt_hole_diameter': 79.2, 'bolt_size': '76.2', 'fillet_radius': 12.7, 'weight_kg': 898},
    '34': {'nps': '34', 'flange_od': 1314.5, 'flange_thickness': 171.5, 'hub_length': 319, 'hub_base_diameter': 962.2, 'hub_end_diameter': 863.6, 'rf_diameter': 990.6, 'bolt_circle_diameter': 1155.7, 'bolt_holes': 20, 'bolt_hole_diameter': 85.9, 'bolt_size': '82.6', 'fillet_radius': 14.2, 'weight_kg': 1063},
    '36': {'nps': '36', 'flange_od': 1346.2, 'flange_thickness': 173, 'hub_length': 325.4, 'hub_base_diameter': 1016, 'hub_end_diameter': 914.4, 'rf_diameter': 1028.7, 'bolt_circle_diameter': 1200.2, 'bolt_holes': 24, 'bolt_hole_diameter': 79.2, 'bolt_size': '76.2', 'fillet_radius': 14.2, 'weight_kg': 1078},
    '38': {'nps': '38', 'flange_od': 1460.5, 'flange_thickness': 190.5, 'hub_length': 352.6, 'hub_base_diameter': 1073.2, 'hub_end_diameter': 965.2, 'rf_diameter': 1098.6, 'bolt_circle_diameter': 1289.1, 'bolt_holes': 20, 'bolt_hole_diameter': 91.9, 'bolt_size': '88.9', 'fillet_radius': 19.1, 'weight_kg': 1445},
    '40': {'nps': '40', 'flange_od': 1511.3, 'flange_thickness': 196.9, 'hub_length': 363.5, 'hub_base_diameter': 1127.3, 'hub_end_diameter': 1016, 'rf_diameter': 1162.1, 'bolt_circle_diameter': 1339.9, 'bolt_holes': 24, 'bolt_hole_diameter': 91.9, 'bolt_size': '88.9', 'fillet_radius': 20.6, 'weight_kg': 1529},
    '42': {'nps': '42', 'flange_od': 1562.1, 'flange_thickness': 206.2, 'hub_length': 371.3, 'hub_base_diameter': 1176.3, 'hub_end_diameter': 1066.8, 'rf_diameter': 1212.9, 'bolt_circle_diameter': 1390.7, 'bolt_holes': 24, 'bolt_hole_diameter': 91.9, 'bolt_size': '88.9', 'fillet_radius': 20.6, 'weight_kg': 1666},
    '44': {'nps': '44', 'flange_od': 1648, 'flange_thickness': 214.4, 'hub_length': 390.7, 'hub_base_diameter': 1234.9, 'hub_end_diameter': 1117.6, 'rf_diameter': 1270, 'bolt_circle_diameter': 1463.5, 'bolt_holes': 24, 'bolt_hole_diameter': 98.6, 'bolt_size': '95.3', 'fillet_radius': 22.4, 'weight_kg': 1939},
    '46': {'nps': '46', 'flange_od': 1733.6, 'flange_thickness': 225.6, 'hub_length': 411, 'hub_base_diameter': 1292.4, 'hub_end_diameter': 1168.4, 'rf_diameter': 1333.5, 'bolt_circle_diameter': 1536.7, 'bolt_holes': 24, 'bolt_hole_diameter': 104.6, 'bolt_size': '101.6', 'fillet_radius': 22.4, 'weight_kg': 2265},
    '48': {'nps': '48', 'flange_od': 1784.4, 'flange_thickness': 233.4, 'hub_length': 419.1, 'hub_base_diameter': 1343.2, 'hub_end_diameter': 1219.2, 'rf_diameter': 1384.3, 'bolt_circle_diameter': 1587.5, 'bolt_holes': 24, 'bolt_hole_diameter': 104.6, 'bolt_size': '101.6', 'fillet_radius': 23.9, 'weight_kg': 2433},
}

# ASME B16.47 Series A RF Weld Neck Flanges (Large Diameter 26"-60")
B1647_SERIES_A_RF_WN = {
    '26': {'nps': '26', 'flange_od': 870, 'flange_thickness': 68.3, 'hub_length': 120.7, 'hub_base_diameter': 676.1, 'hub_end_diameter': 660.4, 'rf_diameter': 749.3, 'bolt_circle_diameter': 806.5, 'bolt_holes': 24, 'bolt_hole_diameter': 35.1, 'bolt_size': '31.8', 'fillet_radius': 9.7, 'weight_kg': 150},
    '28': {'nps': '28', 'flange_od': 927.1, 'flange_thickness': 71.4, 'hub_length': 125.5, 'hub_base_diameter': 726.9, 'hub_end_diameter': 711.2, 'rf_diameter': 800.1, 'bolt_circle_diameter': 863.6, 'bolt_holes': 28, 'bolt_hole_diameter': 35.1, 'bolt_size': '31.8', 'fillet_radius': 11.2, 'weight_kg': 171},
    '30': {'nps': '30', 'flange_od': 984.3, 'flange_thickness': 74.7, 'hub_length': 136.7, 'hub_base_diameter': 781.1, 'hub_end_diameter': 762, 'rf_diameter': 857.3, 'bolt_circle_diameter': 914.4, 'bolt_holes': 28, 'bolt_hole_diameter': 35.1, 'bolt_size': '31.8', 'fillet_radius': 11.2, 'weight_kg': 200},
    '32': {'nps': '32', 'flange_od': 1060.5, 'flange_thickness': 81, 'hub_length': 144.5, 'hub_base_diameter': 831.9, 'hub_end_diameter': 812.8, 'rf_diameter': 914.4, 'bolt_circle_diameter': 977.9, 'bolt_holes': 28, 'bolt_hole_diameter': 41.1, 'bolt_size': '38.1', 'fillet_radius': 11.2, 'weight_kg': 250},
    '34': {'nps': '34', 'flange_od': 1111.3, 'flange_thickness': 82.6, 'hub_length': 149.4, 'hub_base_diameter': 882.7, 'hub_end_diameter': 863.6, 'rf_diameter': 965.2, 'bolt_circle_diameter': 1028.7, 'bolt_holes': 32, 'bolt_hole_diameter': 41.1, 'bolt_size': '38.1', 'fillet_radius': 12.7, 'weight_kg': 267},
    '36': {'nps': '36', 'flange_od': 1168.4, 'flange_thickness': 90.4, 'hub_length': 157.2, 'hub_base_diameter': 933.5, 'hub_end_diameter': 914.4, 'rf_diameter': 1022.4, 'bolt_circle_diameter': 1085.9, 'bolt_holes': 32, 'bolt_hole_diameter': 41.1, 'bolt_size': '38.1', 'fillet_radius': 12.7, 'weight_kg': 316},
    '38': {'nps': '38', 'flange_od': 1238.3, 'flange_thickness': 87.4, 'hub_length': 157.2, 'hub_base_diameter': 990.6, 'hub_end_diameter': 965.2, 'rf_diameter': 1073.2, 'bolt_circle_diameter': 1149.4, 'bolt_holes': 32, 'bolt_hole_diameter': 41.1, 'bolt_size': '38.1', 'fillet_radius': 12.7, 'weight_kg': 352},
    '40': {'nps': '40', 'flange_od': 1289, 'flange_thickness': 90.4, 'hub_length': 163.6, 'hub_base_diameter': 1041.4, 'hub_end_diameter': 1016, 'rf_diameter': 1124, 'bolt_circle_diameter': 1200.2, 'bolt_holes': 36, 'bolt_hole_diameter': 41.1, 'bolt_size': '38.1', 'fillet_radius': 12.7, 'weight_kg': 379},
    '42': {'nps': '42', 'flange_od': 1346.2, 'flange_thickness': 96.8, 'hub_length': 171.5, 'hub_base_diameter': 1092.2, 'hub_end_diameter': 1066.8, 'rf_diameter': 1193.8, 'bolt_circle_diameter': 1257.3, 'bolt_holes': 36, 'bolt_hole_diameter': 41.1, 'bolt_size': '38.1', 'fillet_radius': 12.7, 'weight_kg': 435},
    '44': {'nps': '44', 'flange_od': 1403.4, 'flange_thickness': 101.6, 'hub_length': 177.8, 'hub_base_diameter': 1143, 'hub_end_diameter': 1117.6, 'rf_diameter': 1244.6, 'bolt_circle_diameter': 1314.5, 'bolt_holes': 40, 'bolt_hole_diameter': 41.1, 'bolt_size': '38.1', 'fillet_radius': 12.7, 'weight_kg': 484},
    '46': {'nps': '46', 'flange_od': 1454.2, 'flange_thickness': 103.1, 'hub_length': 185.7, 'hub_base_diameter': 1196.8, 'hub_end_diameter': 1168.4, 'rf_diameter': 1295.4, 'bolt_circle_diameter': 1365.3, 'bolt_holes': 40, 'bolt_hole_diameter': 41.1, 'bolt_size': '38.1', 'fillet_radius': 12.7, 'weight_kg': 518},
    '48': {'nps': '48', 'flange_od': 1511.3, 'flange_thickness': 108, 'hub_length': 192, 'hub_base_diameter': 1247.6, 'hub_end_diameter': 1219.2, 'rf_diameter': 1358.9, 'bolt_circle_diameter': 1422.4, 'bolt_holes': 44, 'bolt_hole_diameter': 41.1, 'bolt_size': '38.1', 'fillet_radius': 12.7, 'weight_kg': 572},
    '50': {'nps': '50', 'flange_od': 1568.5, 'flange_thickness': 111.3, 'hub_length': 203.2, 'hub_base_diameter': 1301.8, 'hub_end_diameter': 1270, 'rf_diameter': 1409.7, 'bolt_circle_diameter': 1479.6, 'bolt_holes': 44, 'bolt_hole_diameter': 47.8, 'bolt_size': '44.5', 'fillet_radius': 12.7, 'weight_kg': 616},
    '52': {'nps': '52', 'flange_od': 1625.6, 'flange_thickness': 115.8, 'hub_length': 209.6, 'hub_base_diameter': 1352.6, 'hub_end_diameter': 1320.8, 'rf_diameter': 1460.5, 'bolt_circle_diameter': 1530.4, 'bolt_holes': 44, 'bolt_hole_diameter': 47.8, 'bolt_size': '44.5', 'fillet_radius': 12.7, 'weight_kg': 681},
    '54': {'nps': '54', 'flange_od': 1682.8, 'flange_thickness': 120.7, 'hub_length': 215.9, 'hub_base_diameter': 1403.4, 'hub_end_diameter': 1371.6, 'rf_diameter': 1511.3, 'bolt_circle_diameter': 1593.9, 'bolt_holes': 44, 'bolt_hole_diameter': 47.8, 'bolt_size': '44.5', 'fillet_radius': 12.7, 'weight_kg': 751},
    '56': {'nps': '56', 'flange_od': 1746.3, 'flange_thickness': 124, 'hub_length': 228.6, 'hub_base_diameter': 1457.5, 'hub_end_diameter': 1422.4, 'rf_diameter': 1574.8, 'bolt_circle_diameter': 1651, 'bolt_holes': 48, 'bolt_hole_diameter': 47.8, 'bolt_size': '44.5', 'fillet_radius': 12.7, 'weight_kg': 835},
    '58': {'nps': '58', 'flange_od': 1803.4, 'flange_thickness': 128.5, 'hub_length': 235, 'hub_base_diameter': 1508.3, 'hub_end_diameter': 1473.2, 'rf_diameter': 1625.6, 'bolt_circle_diameter': 1708.2, 'bolt_holes': 48, 'bolt_hole_diameter': 47.8, 'bolt_size': '44.5', 'fillet_radius': 12.7, 'weight_kg': 914},
    '60': {'nps': '60', 'flange_od': 1854.2, 'flange_thickness': 131.8, 'hub_length': 239.8, 'hub_base_diameter': 1559.1, 'hub_end_diameter': 1524, 'rf_diameter': 1676.4, 'bolt_circle_diameter': 1759, 'bolt_holes': 52, 'bolt_hole_diameter': 47.8, 'bolt_size': '44.5', 'fillet_radius': 12.7, 'weight_kg': 961},
}

# ASME B16.47 Series A RF Class 300 Weld Neck Flanges (Large Diameter 26"-60")
B1647_SERIES_A_CLASS300_RF_WN = {
    '26': {'nps': '26', 'flange_od': 971.6, 'flange_thickness': 79.2, 'hub_length': 184.2, 'hub_base_diameter': 720.9, 'hub_end_diameter': 660.4, 'rf_diameter': 749.3, 'bolt_circle_diameter': 876.3, 'bolt_holes': 28, 'bolt_hole_diameter': 44.5, 'bolt_size': '41.4', 'fillet_radius': 9.7, 'weight_kg': 283},
    '28': {'nps': '28', 'flange_od': 1035.1, 'flange_thickness': 85.9, 'hub_length': 196.9, 'hub_base_diameter': 774.7, 'hub_end_diameter': 711.2, 'rf_diameter': 800.1, 'bolt_circle_diameter': 939.8, 'bolt_holes': 28, 'bolt_hole_diameter': 44.5, 'bolt_size': '41.4', 'fillet_radius': 11.2, 'weight_kg': 343},
    '30': {'nps': '30', 'flange_od': 1092.2, 'flange_thickness': 91.9, 'hub_length': 209.6, 'hub_base_diameter': 827, 'hub_end_diameter': 762, 'rf_diameter': 857.3, 'bolt_circle_diameter': 997, 'bolt_holes': 28, 'bolt_hole_diameter': 47.8, 'bolt_size': '44.5', 'fillet_radius': 11.2, 'weight_kg': 395},
    '32': {'nps': '32', 'flange_od': 1149.4, 'flange_thickness': 98.6, 'hub_length': 222.3, 'hub_base_diameter': 881.1, 'hub_end_diameter': 812.8, 'rf_diameter': 914.4, 'bolt_circle_diameter': 1054.1, 'bolt_holes': 28, 'bolt_hole_diameter': 50.8, 'bolt_size': '47.8', 'fillet_radius': 11.2, 'weight_kg': 455},
    '34': {'nps': '34', 'flange_od': 1206.5, 'flange_thickness': 101.6, 'hub_length': 231.6, 'hub_base_diameter': 936.8, 'hub_end_diameter': 863.6, 'rf_diameter': 965.2, 'bolt_circle_diameter': 1104.9, 'bolt_holes': 28, 'bolt_hole_diameter': 50.8, 'bolt_size': '47.8', 'fillet_radius': 12.7, 'weight_kg': 511},
    '36': {'nps': '36', 'flange_od': 1270, 'flange_thickness': 104.6, 'hub_length': 241.3, 'hub_base_diameter': 990.6, 'hub_end_diameter': 914.4, 'rf_diameter': 1022.4, 'bolt_circle_diameter': 1168.4, 'bolt_holes': 32, 'bolt_hole_diameter': 53.8, 'bolt_size': '50.8', 'fillet_radius': 12.7, 'weight_kg': 568},
    '38': {'nps': '38', 'flange_od': 1168.4, 'flange_thickness': 108, 'hub_length': 180.8, 'hub_base_diameter': 993.6, 'hub_end_diameter': 965.2, 'rf_diameter': 1028.7, 'bolt_circle_diameter': 1092.2, 'bolt_holes': 32, 'bolt_hole_diameter': 41.1, 'bolt_size': '38.1', 'fillet_radius': 12.7, 'weight_kg': 318},
    '40': {'nps': '40', 'flange_od': 1238.3, 'flange_thickness': 114.3, 'hub_length': 193.5, 'hub_base_diameter': 1054.6, 'hub_end_diameter': 1016, 'rf_diameter': 1085.9, 'bolt_circle_diameter': 1155.7, 'bolt_holes': 32, 'bolt_hole_diameter': 44.5, 'bolt_size': '41.4', 'fillet_radius': 12.7, 'weight_kg': 348},
    '42': {'nps': '42', 'flange_od': 1289.1, 'flange_thickness': 119.1, 'hub_length': 200.2, 'hub_base_diameter': 1098.6, 'hub_end_diameter': 1066.8, 'rf_diameter': 1136.7, 'bolt_circle_diameter': 1206.5, 'bolt_holes': 32, 'bolt_hole_diameter': 44.5, 'bolt_size': '41.4', 'fillet_radius': 12.7, 'weight_kg': 420},
    '44': {'nps': '44', 'flange_od': 1352.6, 'flange_thickness': 124, 'hub_length': 206.2, 'hub_base_diameter': 1149.4, 'hub_end_diameter': 1117.6, 'rf_diameter': 1193.8, 'bolt_circle_diameter': 1263.7, 'bolt_holes': 32, 'bolt_hole_diameter': 47.8, 'bolt_size': '44.5', 'fillet_radius': 12.7, 'weight_kg': 476},
    '46': {'nps': '46', 'flange_od': 1416.1, 'flange_thickness': 128.5, 'hub_length': 215.9, 'hub_base_diameter': 1203.5, 'hub_end_diameter': 1168.4, 'rf_diameter': 1244.6, 'bolt_circle_diameter': 1320.8, 'bolt_holes': 28, 'bolt_hole_diameter': 50.8, 'bolt_size': '47.8', 'fillet_radius': 12.7, 'weight_kg': 549},
    '48': {'nps': '48', 'flange_od': 1466.9, 'flange_thickness': 108, 'hub_length': 192, 'hub_base_diameter': 1247.6, 'hub_end_diameter': 1219.2, 'rf_diameter': 1358.9, 'bolt_circle_diameter': 1422.4, 'bolt_holes': 32, 'bolt_hole_diameter': 41.1, 'bolt_size': '38.1', 'fillet_radius': 12.7, 'weight_kg': 587},
    '50': {'nps': '50', 'flange_od': 1530.4, 'flange_thickness': 139.7, 'hub_length': 231.6, 'hub_base_diameter': 1305.1, 'hub_end_diameter': 1270, 'rf_diameter': 1358.9, 'bolt_circle_diameter': 1428.8, 'bolt_holes': 32, 'bolt_hole_diameter': 53.8, 'bolt_size': '50.8', 'fillet_radius': 12.7, 'weight_kg': 664},
    '52': {'nps': '52', 'flange_od': 1581.2, 'flange_thickness': 144.5, 'hub_length': 238.3, 'hub_base_diameter': 1355.9, 'hub_end_diameter': 1320.8, 'rf_diameter': 1409.7, 'bolt_circle_diameter': 1479.6, 'bolt_holes': 32, 'bolt_hole_diameter': 53.8, 'bolt_size': '50.8', 'fillet_radius': 12.7, 'weight_kg': 715},
    '54': {'nps': '54', 'flange_od': 1657.4, 'flange_thickness': 152.4, 'hub_length': 252.5, 'hub_base_diameter': 1409.7, 'hub_end_diameter': 1371.6, 'rf_diameter': 1466.9, 'bolt_circle_diameter': 1549.4, 'bolt_holes': 28, 'bolt_hole_diameter': 60.5, 'bolt_size': '57.2', 'fillet_radius': 12.7, 'weight_kg': 857},
    '56': {'nps': '56', 'flange_od': 1708.2, 'flange_thickness': 153.9, 'hub_length': 260.4, 'hub_base_diameter': 1463.5, 'hub_end_diameter': 1422.4, 'rf_diameter': 1517.7, 'bolt_circle_diameter': 1600.2, 'bolt_holes': 28, 'bolt_hole_diameter': 60.5, 'bolt_size': '57.2', 'fillet_radius': 12.7, 'weight_kg': 905},
    '58': {'nps': '58', 'flange_od': 1759, 'flange_thickness': 158.8, 'hub_length': 266.7, 'hub_base_diameter': 1514.3, 'hub_end_diameter': 1473.2, 'rf_diameter': 1574.8, 'bolt_circle_diameter': 1651, 'bolt_holes': 32, 'bolt_hole_diameter': 60.5, 'bolt_size': '57.2', 'fillet_radius': 12.7, 'weight_kg': 952},
    '60': {'nps': '60', 'flange_od': 1809.8, 'flange_thickness': 163.6, 'hub_length': 273.1, 'hub_base_diameter': 1565.1, 'hub_end_diameter': 1524, 'rf_diameter': 1625.6, 'bolt_circle_diameter': 1701.8, 'bolt_holes': 32, 'bolt_hole_diameter': 60.5, 'bolt_size': '57.2', 'fillet_radius': 12.7, 'weight_kg': 1015},
}

# ASME B16.47 Series A RF Class 600 Weld Neck Flanges (Large Diameter 26"-60")
B1647_SERIES_A_CLASS600_RF_WN = {
    '26': {'nps': '26', 'flange_od': 1016, 'flange_thickness': 108, 'hub_length': 222.3, 'hub_base_diameter': 747.8, 'hub_end_diameter': 660.4, 'rf_diameter': 749.3, 'bolt_circle_diameter': 914.4, 'bolt_holes': 28, 'bolt_hole_diameter': 50.8, 'bolt_size': '47.6', 'fillet_radius': 12.7, 'weight_kg': 444},
    '28': {'nps': '28', 'flange_od': 1073.2, 'flange_thickness': 111.3, 'hub_length': 235, 'hub_base_diameter': 803.1, 'hub_end_diameter': 711.2, 'rf_diameter': 800.1, 'bolt_circle_diameter': 965.2, 'bolt_holes': 28, 'bolt_hole_diameter': 53.8, 'bolt_size': '50.8', 'fillet_radius': 12.7, 'weight_kg': 499},
    '30': {'nps': '30', 'flange_od': 1130.3, 'flange_thickness': 114.3, 'hub_length': 247.7, 'hub_base_diameter': 862.1, 'hub_end_diameter': 762, 'rf_diameter': 857.3, 'bolt_circle_diameter': 1022.4, 'bolt_holes': 28, 'bolt_hole_diameter': 53.8, 'bolt_size': '50.8', 'fillet_radius': 12.7, 'weight_kg': 567},
    '32': {'nps': '32', 'flange_od': 1193.8, 'flange_thickness': 117.3, 'hub_length': 260.4, 'hub_base_diameter': 917.4, 'hub_end_diameter': 812.8, 'rf_diameter': 914.4, 'bolt_circle_diameter': 1079.5, 'bolt_holes': 28, 'bolt_hole_diameter': 60.5, 'bolt_size': '57.2', 'fillet_radius': 12.7, 'weight_kg': 633},
    '34': {'nps': '34', 'flange_od': 1244.6, 'flange_thickness': 120.7, 'hub_length': 269.7, 'hub_base_diameter': 973.1, 'hub_end_diameter': 863.6, 'rf_diameter': 965.2, 'bolt_circle_diameter': 1130.3, 'bolt_holes': 28, 'bolt_hole_diameter': 60.5, 'bolt_size': '57.2', 'fillet_radius': 14.2, 'weight_kg': 695},
    '36': {'nps': '36', 'flange_od': 1314.5, 'flange_thickness': 124, 'hub_length': 282.4, 'hub_base_diameter': 1031.7, 'hub_end_diameter': 914.4, 'rf_diameter': 1022.4, 'bolt_circle_diameter': 1193.8, 'bolt_holes': 28, 'bolt_hole_diameter': 60.5, 'bolt_size': '57.2', 'fillet_radius': 14.2, 'weight_kg': 789},
    '38': {'nps': '38', 'flange_od': 1270, 'flange_thickness': 152.4, 'hub_length': 254, 'hub_base_diameter': 1022.4, 'hub_end_diameter': 965.2, 'rf_diameter': 1054.1, 'bolt_circle_diameter': 1162.1, 'bolt_holes': 28, 'bolt_hole_diameter': 60.5, 'bolt_size': '57.2', 'fillet_radius': 14.2, 'weight_kg': 667},
    '40': {'nps': '40', 'flange_od': 1320.8, 'flange_thickness': 158.8, 'hub_length': 263.7, 'hub_base_diameter': 1073.2, 'hub_end_diameter': 1016, 'rf_diameter': 1111.3, 'bolt_circle_diameter': 1212.9, 'bolt_holes': 32, 'bolt_hole_diameter': 60.5, 'bolt_size': '57.2', 'fillet_radius': 14.2, 'weight_kg': 717},
    '42': {'nps': '42', 'flange_od': 1403.4, 'flange_thickness': 168.1, 'hub_length': 279.4, 'hub_base_diameter': 1127.3, 'hub_end_diameter': 1066.8, 'rf_diameter': 1168.4, 'bolt_circle_diameter': 1282.7, 'bolt_holes': 28, 'bolt_hole_diameter': 66.5, 'bolt_size': '63.5', 'fillet_radius': 14.2, 'weight_kg': 886},
    '44': {'nps': '44', 'flange_od': 1454, 'flange_thickness': 173, 'hub_length': 289.1, 'hub_base_diameter': 1181.1, 'hub_end_diameter': 1117.6, 'rf_diameter': 1225.6, 'bolt_circle_diameter': 1333.5, 'bolt_holes': 32, 'bolt_hole_diameter': 66.5, 'bolt_size': '63.5', 'fillet_radius': 14.2, 'weight_kg': 940},
    '46': {'nps': '46', 'flange_od': 1511.2, 'flange_thickness': 179.3, 'hub_length': 300, 'hub_base_diameter': 1234.9, 'hub_end_diameter': 1168.4, 'rf_diameter': 1276.4, 'bolt_circle_diameter': 1390.7, 'bolt_holes': 32, 'bolt_hole_diameter': 66.5, 'bolt_size': '63.5', 'fillet_radius': 14.2, 'weight_kg': 1044},
    '48': {'nps': '48', 'flange_od': 1593.9, 'flange_thickness': 189, 'hub_length': 316, 'hub_base_diameter': 1289.1, 'hub_end_diameter': 1219.2, 'rf_diameter': 1333.5, 'bolt_circle_diameter': 1460.5, 'bolt_holes': 32, 'bolt_hole_diameter': 73.12, 'bolt_size': '69.9', 'fillet_radius': 14.2, 'weight_kg': 1236},
    '50': {'nps': '50', 'flange_od': 1670.1, 'flange_thickness': 196.9, 'hub_length': 328.7, 'hub_base_diameter': 1343.2, 'hub_end_diameter': 1270, 'rf_diameter': 1384.3, 'bolt_circle_diameter': 1524, 'bolt_holes': 28, 'bolt_hole_diameter': 79.2, 'bolt_size': '76.2', 'fillet_radius': 14.2, 'weight_kg': 1442},
    '52': {'nps': '52', 'flange_od': 1720.9, 'flange_thickness': 203.2, 'hub_length': 336.6, 'hub_base_diameter': 1394, 'hub_end_diameter': 1320.8, 'rf_diameter': 1435.1, 'bolt_circle_diameter': 1574.8, 'bolt_holes': 32, 'bolt_hole_diameter': 79.2, 'bolt_size': '76.2', 'fillet_radius': 14.2, 'weight_kg': 1514},
    '54': {'nps': '54', 'flange_od': 1778, 'flange_thickness': 209.6, 'hub_length': 349.3, 'hub_base_diameter': 1447.8, 'hub_end_diameter': 1371.6, 'rf_diameter': 1492.3, 'bolt_circle_diameter': 1632, 'bolt_holes': 32, 'bolt_hole_diameter': 79.2, 'bolt_size': '76.2', 'fillet_radius': 14.2, 'weight_kg': 1659},
    '56': {'nps': '56', 'flange_od': 1854.2, 'flange_thickness': 217.4, 'hub_length': 362, 'hub_base_diameter': 1501.6, 'hub_end_diameter': 1422.4, 'rf_diameter': 1543.1, 'bolt_circle_diameter': 1695.5, 'bolt_holes': 32, 'bolt_hole_diameter': 85.9, 'bolt_size': '82.6', 'fillet_radius': 15.7, 'weight_kg': 1869},
    '58': {'nps': '58', 'flange_od': 1905, 'flange_thickness': 222.3, 'hub_length': 369.8, 'hub_base_diameter': 1552.4, 'hub_end_diameter': 1473.2, 'rf_diameter': 1600.2, 'bolt_circle_diameter': 1746.3, 'bolt_holes': 32, 'bolt_hole_diameter': 85.9, 'bolt_size': '82.6', 'fillet_radius': 15.7, 'weight_kg': 1981},
    '60': {'nps': '60', 'flange_od': 1993.9, 'flange_thickness': 233.4, 'hub_length': 388.9, 'hub_base_diameter': 1609.9, 'hub_end_diameter': 1524, 'rf_diameter': 1657.4, 'bolt_circle_diameter': 1822.5, 'bolt_holes': 28, 'bolt_hole_diameter': 91.9, 'bolt_size': '88.9', 'fillet_radius': 17.5, 'weight_kg': 2382},
}

# ASME B16.47 Series A RF Class 900 Weld Neck Flanges (Large Diameter 26"-48")
B1647_SERIES_A_CLASS900_RF_WN = {
    '26': {'nps': '26', 'flange_od': 1085.9, 'flange_thickness': 139.7, 'hub_length': 258.8, 'hub_base_diameter': 774.7, 'hub_end_diameter': 660.4, 'rf_diameter': 749.3, 'bolt_circle_diameter': 952.5, 'bolt_holes': 20, 'bolt_hole_diameter': 73.2, 'bolt_size': '69.9', 'fillet_radius': 11.2, 'weight_kg': 686},
    '28': {'nps': '28', 'flange_od': 1168.4, 'flange_thickness': 142.7, 'hub_length': 298.5, 'hub_base_diameter': 831.9, 'hub_end_diameter': 711.2, 'rf_diameter': 800.1, 'bolt_circle_diameter': 1022.4, 'bolt_holes': 20, 'bolt_hole_diameter': 79.2, 'bolt_size': '76.2', 'fillet_radius': 12.7, 'weight_kg': 808},
    '30': {'nps': '30', 'flange_od': 1231.9, 'flange_thickness': 149.4, 'hub_length': 311.2, 'hub_base_diameter': 889, 'hub_end_diameter': 762, 'rf_diameter': 857.3, 'bolt_circle_diameter': 1085.9, 'bolt_holes': 20, 'bolt_hole_diameter': 79.2, 'bolt_size': '76.2', 'fillet_radius': 12.7, 'weight_kg': 933},
    '32': {'nps': '32', 'flange_od': 1314.5, 'flange_thickness': 158.8, 'hub_length': 330.2, 'hub_base_diameter': 946.2, 'hub_end_diameter': 812.8, 'rf_diameter': 914.4, 'bolt_circle_diameter': 1155.7, 'bolt_holes': 20, 'bolt_hole_diameter': 85.9, 'bolt_size': '82.6', 'fillet_radius': 12.7, 'weight_kg': 1116},
    '34': {'nps': '34', 'flange_od': 1397, 'flange_thickness': 165.1, 'hub_length': 349.3, 'hub_base_diameter': 1006.3, 'hub_end_diameter': 863.6, 'rf_diameter': 965.2, 'bolt_circle_diameter': 1225.6, 'bolt_holes': 20, 'bolt_hole_diameter': 91.9, 'bolt_size': '88.9', 'fillet_radius': 14.2, 'weight_kg': 1310},
    '36': {'nps': '36', 'flange_od': 1460.5, 'flange_thickness': 171.5, 'hub_length': 362, 'hub_base_diameter': 1063.8, 'hub_end_diameter': 914.4, 'rf_diameter': 1022.4, 'bolt_circle_diameter': 1289.1, 'bolt_holes': 20, 'bolt_hole_diameter': 91.9, 'bolt_size': '88.9', 'fillet_radius': 14.2, 'weight_kg': 1479},
    '38': {'nps': '38', 'flange_od': 1460.5, 'flange_thickness': 190.5, 'hub_length': 352.6, 'hub_base_diameter': 1073.2, 'hub_end_diameter': 965.2, 'rf_diameter': 1098.6, 'bolt_circle_diameter': 1289.1, 'bolt_holes': 20, 'bolt_hole_diameter': 91.9, 'bolt_size': '88.9', 'fillet_radius': 19.1, 'weight_kg': 1445},
    '40': {'nps': '40', 'flange_od': 1511.3, 'flange_thickness': 196.9, 'hub_length': 363.5, 'hub_base_diameter': 1127.3, 'hub_end_diameter': 1016, 'rf_diameter': 1162.1, 'bolt_circle_diameter': 1339.9, 'bolt_holes': 24, 'bolt_hole_diameter': 91.9, 'bolt_size': '88.9', 'fillet_radius': 20.6, 'weight_kg': 1529},
    '42': {'nps': '42', 'flange_od': 1562.1, 'flange_thickness': 206.2, 'hub_length': 371.3, 'hub_base_diameter': 1176.3, 'hub_end_diameter': 1066.8, 'rf_diameter': 1212.9, 'bolt_circle_diameter': 1390.7, 'bolt_holes': 24, 'bolt_hole_diameter': 91.9, 'bolt_size': '88.9', 'fillet_radius': 20.6, 'weight_kg': 1666},
    '44': {'nps': '44', 'flange_od': 1648, 'flange_thickness': 214.4, 'hub_length': 390.7, 'hub_base_diameter': 1234.9, 'hub_end_diameter': 1117.6, 'rf_diameter': 1270, 'bolt_circle_diameter': 1463.5, 'bolt_holes': 24, 'bolt_hole_diameter': 98.6, 'bolt_size': '95.3', 'fillet_radius': 22.4, 'weight_kg': 1939},
    '46': {'nps': '46', 'flange_od': 1733.6, 'flange_thickness': 225.6, 'hub_length': 411, 'hub_base_diameter': 1292.4, 'hub_end_diameter': 1168.4, 'rf_diameter': 1333.5, 'bolt_circle_diameter': 1536.7, 'bolt_holes': 24, 'bolt_hole_diameter': 104.6, 'bolt_size': '101.6', 'fillet_radius': 22.4, 'weight_kg': 2265},
    '48': {'nps': '48', 'flange_od': 1784.4, 'flange_thickness': 233.4, 'hub_length': 419.1, 'hub_base_diameter': 1343.2, 'hub_end_diameter': 1219.2, 'rf_diameter': 1384.3, 'bolt_circle_diameter': 1587.5, 'bolt_holes': 24, 'bolt_hole_diameter': 104.6, 'bolt_size': '101.6', 'fillet_radius': 23.9, 'weight_kg': 2433},
}


# ============================================================================
# ASME B16.5 BLIND FLANGE DATA
# ============================================================================

CLASS_150_RF_BLIND = {
    '1/2': {'flange_od': 88.9, 'thickness': 11.2, 'rf_diameter': 35.1, 
            'bolt_circle_diameter': 60.5, 'bolt_holes': 4, 'bolt_hole_diameter': 15.7, 'weight_kg': 0.5},
    '3/4': {'flange_od': 98.6, 'thickness': 12.7, 'rf_diameter': 42.9,
            'bolt_circle_diameter': 69.9, 'bolt_holes': 4, 'bolt_hole_diameter': 15.7, 'weight_kg': 1},
    '1': {'flange_od': 108, 'thickness': 14.2, 'rf_diameter': 50.8,
          'bolt_circle_diameter': 79.2, 'bolt_holes': 4, 'bolt_hole_diameter': 15.7, 'weight_kg': 1},
    '1-1/4': {'flange_od': 117.3, 'thickness': 15.7, 'rf_diameter': 63.5,
              'bolt_circle_diameter': 88.9, 'bolt_holes': 4, 'bolt_hole_diameter': 15.7, 'weight_kg': 1},
    '1-1/2': {'flange_od': 127, 'thickness': 17.5, 'rf_diameter': 73.2,
              'bolt_circle_diameter': 98.6, 'bolt_holes': 4, 'bolt_hole_diameter': 15.7, 'weight_kg': 2},
    '2': {'flange_od': 152.4, 'thickness': 19.1, 'rf_diameter': 91.9,
          'bolt_circle_diameter': 120.7, 'bolt_holes': 4, 'bolt_hole_diameter': 19.1, 'weight_kg': 2},
    '2-1/2': {'flange_od': 177.8, 'thickness': 22.4, 'rf_diameter': 104.6,
              'bolt_circle_diameter': 139.7, 'bolt_holes': 4, 'bolt_hole_diameter': 19.1, 'weight_kg': 3},
    '3': {'flange_od': 190.5, 'thickness': 23.9, 'rf_diameter': 127,
          'bolt_circle_diameter': 152.4, 'bolt_holes': 4, 'bolt_hole_diameter': 19.1, 'weight_kg': 4},
    '3-1/2': {'flange_od': 215.9, 'thickness': 23.9, 'rf_diameter': 139.7,
              'bolt_circle_diameter': 177.8, 'bolt_holes': 8, 'bolt_hole_diameter': 19.1, 'weight_kg': 6},
    '4': {'flange_od': 228.6, 'thickness': 23.9, 'rf_diameter': 157.2,
          'bolt_circle_diameter': 190.5, 'bolt_holes': 8, 'bolt_hole_diameter': 19.1, 'weight_kg': 8},
    '5': {'flange_od': 254, 'thickness': 23.9, 'rf_diameter': 185.7,
          'bolt_circle_diameter': 215.9, 'bolt_holes': 8, 'bolt_hole_diameter': 22.4, 'weight_kg': 9},
    '6': {'flange_od': 279.4, 'thickness': 25.4, 'rf_diameter': 215.9,
          'bolt_circle_diameter': 241.3, 'bolt_holes': 8, 'bolt_hole_diameter': 22.4, 'weight_kg': 12},
    '8': {'flange_od': 342.9, 'thickness': 28.4, 'rf_diameter': 269.7,
          'bolt_circle_diameter': 298.5, 'bolt_holes': 8, 'bolt_hole_diameter': 22.4, 'weight_kg': 20},
    '10': {'flange_od': 406.4, 'thickness': 30.2, 'rf_diameter': 323.9,
           'bolt_circle_diameter': 362, 'bolt_holes': 12, 'bolt_hole_diameter': 25.4, 'weight_kg': 32},
    '12': {'flange_od': 482.6, 'thickness': 31.8, 'rf_diameter': 381,
           'bolt_circle_diameter': 431.8, 'bolt_holes': 12, 'bolt_hole_diameter': 25.4, 'weight_kg': 50},
    '14': {'flange_od': 533.4, 'thickness': 35.1, 'rf_diameter': 412.8,
           'bolt_circle_diameter': 476.3, 'bolt_holes': 12, 'bolt_hole_diameter': 28.4, 'weight_kg': 64},
    '16': {'flange_od': 596.9, 'thickness': 36.6, 'rf_diameter': 469.9,
           'bolt_circle_diameter': 539.8, 'bolt_holes': 16, 'bolt_hole_diameter': 28.4, 'weight_kg': 82},
    '18': {'flange_od': 635, 'thickness': 39.6, 'rf_diameter': 533.4,
           'bolt_circle_diameter': 577.9, 'bolt_holes': 16, 'bolt_hole_diameter': 31.8, 'weight_kg': 100},
    '20': {'flange_od': 698.5, 'thickness': 42.9, 'rf_diameter': 584.2,
           'bolt_circle_diameter': 635, 'bolt_holes': 20, 'bolt_hole_diameter': 31.8, 'weight_kg': 129},
    '24': {'flange_od': 812.8, 'thickness': 47.8, 'rf_diameter': 692.2,
           'bolt_circle_diameter': 749.3, 'bolt_holes': 20, 'bolt_hole_diameter': 35.1, 'weight_kg': 195},
}

CLASS_600_RF_BLIND = {
    '1/2': {'flange_od': 95.3, 'thickness': 14.2, 'rf_diameter': 35.1, 
            'bolt_circle_diameter': 66.5, 'bolt_holes': 4, 'bolt_hole_diameter': 15.7, 'weight_kg': 1},
    '3/4': {'flange_od': 117.3, 'thickness': 15.7, 'rf_diameter': 42.9,
            'bolt_circle_diameter': 82.6, 'bolt_holes': 4, 'bolt_hole_diameter': 19.1, 'weight_kg': 1},
    '1': {'flange_od': 124, 'thickness': 17.5, 'rf_diameter': 50.8,
          'bolt_circle_diameter': 88.9, 'bolt_holes': 4, 'bolt_hole_diameter': 19.1, 'weight_kg': 2},
    '1-1/4': {'flange_od': 133.4, 'thickness': 20.6, 'rf_diameter': 63.5,
              'bolt_circle_diameter': 98.6, 'bolt_holes': 4, 'bolt_hole_diameter': 19.1, 'weight_kg': 2},
    '1-1/2': {'flange_od': 155.4, 'thickness': 22.4, 'rf_diameter': 73.2,
              'bolt_circle_diameter': 114.3, 'bolt_holes': 4, 'bolt_hole_diameter': 22.4, 'weight_kg': 4},
    '2': {'flange_od': 165.1, 'thickness': 25.4, 'rf_diameter': 91.9,
          'bolt_circle_diameter': 127, 'bolt_holes': 8, 'bolt_hole_diameter': 19.1, 'weight_kg': 5},
    '2-1/2': {'flange_od': 190.5, 'thickness': 28.4, 'rf_diameter': 104.6,
              'bolt_circle_diameter': 149.4, 'bolt_holes': 8, 'bolt_hole_diameter': 22.4, 'weight_kg': 7},
    '3': {'flange_od': 209.6, 'thickness': 31.8, 'rf_diameter': 127,
          'bolt_circle_diameter': 168.1, 'bolt_holes': 8, 'bolt_hole_diameter': 22.4, 'weight_kg': 9},
    '3-1/2': {'flange_od': 228.6, 'thickness': 35.1, 'rf_diameter': 139.7,
              'bolt_circle_diameter': 184.2, 'bolt_holes': 8, 'bolt_hole_diameter': 25.4, 'weight_kg': 13},
    '4': {'flange_od': 273.1, 'thickness': 38.1, 'rf_diameter': 157.2,
          'bolt_circle_diameter': 215.9, 'bolt_holes': 8, 'bolt_hole_diameter': 25.4, 'weight_kg': 19},
    '5': {'flange_od': 330.2, 'thickness': 44.5, 'rf_diameter': 185.7,
          'bolt_circle_diameter': 266.7, 'bolt_holes': 8, 'bolt_hole_diameter': 28.4, 'weight_kg': 31},
    '6': {'flange_od': 355.6, 'thickness': 47.8, 'rf_diameter': 215.9,
          'bolt_circle_diameter': 292.1, 'bolt_holes': 12, 'bolt_hole_diameter': 28.4, 'weight_kg': 39},
    '8': {'flange_od': 419.1, 'thickness': 55.6, 'rf_diameter': 269.7,
          'bolt_circle_diameter': 349.3, 'bolt_holes': 12, 'bolt_hole_diameter': 31.8, 'weight_kg': 64},
    '10': {'flange_od': 508, 'thickness': 63.5, 'rf_diameter': 323.9,
           'bolt_circle_diameter': 431.8, 'bolt_holes': 16, 'bolt_hole_diameter': 35.1, 'weight_kg': 104},
    '12': {'flange_od': 558.8, 'thickness': 66.5, 'rf_diameter': 381,
           'bolt_circle_diameter': 489, 'bolt_holes': 20, 'bolt_hole_diameter': 35.1, 'weight_kg': 134},
    '14': {'flange_od': 603.3, 'thickness': 69.9, 'rf_diameter': 412.8,
           'bolt_circle_diameter': 527.1, 'bolt_holes': 20, 'bolt_hole_diameter': 38.1, 'weight_kg': 161},
    '16': {'flange_od': 685.8, 'thickness': 76.2, 'rf_diameter': 469.9,
           'bolt_circle_diameter': 603.3, 'bolt_holes': 20, 'bolt_hole_diameter': 41.1, 'weight_kg': 225},
    '18': {'flange_od': 743, 'thickness': 82.6, 'rf_diameter': 533.4,
           'bolt_circle_diameter': 654.1, 'bolt_holes': 20, 'bolt_hole_diameter': 44.5, 'weight_kg': 286},
    '20': {'flange_od': 812.8, 'thickness': 88.9, 'rf_diameter': 584.2,
           'bolt_circle_diameter': 723.9, 'bolt_holes': 24, 'bolt_hole_diameter': 44.5, 'weight_kg': 367},
    '24': {'flange_od': 939.8, 'thickness': 101.6, 'rf_diameter': 692.2,
           'bolt_circle_diameter': 838.2, 'bolt_holes': 24, 'bolt_hole_diameter': 50.8, 'weight_kg': 567},
}

CLASS_900_RF_BLIND = {
    '1/2': {'flange_od': 120.7, 'thickness': 22.4, 'rf_diameter': 35.1, 
            'bolt_circle_diameter': 82.6, 'bolt_holes': 4, 'bolt_hole_diameter': 22.4, 'weight_kg': 2},
    '3/4': {'flange_od': 130, 'thickness': 25.4, 'rf_diameter': 42.9,
            'bolt_circle_diameter': 88.9, 'bolt_holes': 4, 'bolt_hole_diameter': 22.4, 'weight_kg': 3},
    '1': {'flange_od': 149.4, 'thickness': 28.4, 'rf_diameter': 50.8,
          'bolt_circle_diameter': 101.6, 'bolt_holes': 4, 'bolt_hole_diameter': 25.4, 'weight_kg': 4},
    '1-1/4': {'flange_od': 158.8, 'thickness': 28.4, 'rf_diameter': 63.5,
              'bolt_circle_diameter': 111.3, 'bolt_holes': 4, 'bolt_hole_diameter': 25.4, 'weight_kg': 4},
    '1-1/2': {'flange_od': 177.8, 'thickness': 31.8, 'rf_diameter': 73.2,
              'bolt_circle_diameter': 124, 'bolt_holes': 4, 'bolt_hole_diameter': 28.4, 'weight_kg': 6},
    '2': {'flange_od': 215.9, 'thickness': 38.1, 'rf_diameter': 91.9,
          'bolt_circle_diameter': 165.1, 'bolt_holes': 8, 'bolt_hole_diameter': 25.4, 'weight_kg': 11},
    '2-1/2': {'flange_od': 244.3, 'thickness': 41.1, 'rf_diameter': 104.6,
              'bolt_circle_diameter': 190.5, 'bolt_holes': 8, 'bolt_hole_diameter': 28.4, 'weight_kg': 16},
    '3': {'flange_od': 241.3, 'thickness': 38.1, 'rf_diameter': 127,
          'bolt_circle_diameter': 190.5, 'bolt_holes': 8, 'bolt_hole_diameter': 25.4, 'weight_kg': 13},
    '4': {'flange_od': 292.1, 'thickness': 44.5, 'rf_diameter': 157.2,
          'bolt_circle_diameter': 235, 'bolt_holes': 8, 'bolt_hole_diameter': 31.8, 'weight_kg': 24},
    '5': {'flange_od': 349.3, 'thickness': 50.8, 'rf_diameter': 185.7,
          'bolt_circle_diameter': 279.4, 'bolt_holes': 8, 'bolt_hole_diameter': 35.1, 'weight_kg': 39},
    '6': {'flange_od': 381, 'thickness': 55.6, 'rf_diameter': 215.9,
          'bolt_circle_diameter': 317.5, 'bolt_holes': 12, 'bolt_hole_diameter': 31.8, 'weight_kg': 52},
    '8': {'flange_od': 469.9, 'thickness': 63.5, 'rf_diameter': 269.7,
          'bolt_circle_diameter': 393.7, 'bolt_holes': 12, 'bolt_hole_diameter': 38.1, 'weight_kg': 91},
    '10': {'flange_od': 546.1, 'thickness': 69.9, 'rf_diameter': 323.9,
           'bolt_circle_diameter': 469.9, 'bolt_holes': 16, 'bolt_hole_diameter': 38.1, 'weight_kg': 132},
    '12': {'flange_od': 609.6, 'thickness': 79.2, 'rf_diameter': 381,
           'bolt_circle_diameter': 533.4, 'bolt_holes': 20, 'bolt_hole_diameter': 38.1, 'weight_kg': 188},
    '14': {'flange_od': 641.4, 'thickness': 85.9, 'rf_diameter': 412.8,
           'bolt_circle_diameter': 558.8, 'bolt_holes': 20, 'bolt_hole_diameter': 41.1, 'weight_kg': 236},
    '16': {'flange_od': 704.9, 'thickness': 88.9, 'rf_diameter': 469.9,
           'bolt_circle_diameter': 616, 'bolt_holes': 20, 'bolt_hole_diameter': 44.5, 'weight_kg': 272},
    '18': {'flange_od': 787.4, 'thickness': 101.6, 'rf_diameter': 533.4,
           'bolt_circle_diameter': 685.8, 'bolt_holes': 20, 'bolt_hole_diameter': 50.8, 'weight_kg': 386},
    '20': {'flange_od': 857.3, 'thickness': 108, 'rf_diameter': 584.2,
           'bolt_circle_diameter': 749.3, 'bolt_holes': 20, 'bolt_hole_diameter': 53.8, 'weight_kg': 488},
    '24': {'flange_od': 1041.4, 'thickness': 139.7, 'rf_diameter': 692.2,
           'bolt_circle_diameter': 901.7, 'bolt_holes': 20, 'bolt_hole_diameter': 66.5, 'weight_kg': 919},
}

CLASS_1500_RF_BLIND = {
    '1/2': {'flange_od': 120.7, 'thickness': 22.4, 'rf_diameter': 35.1, 
            'bolt_circle_diameter': 82.6, 'bolt_holes': 4, 'bolt_hole_diameter': 22.4, 'weight_kg': 2},
    '3/4': {'flange_od': 130, 'thickness': 25.4, 'rf_diameter': 42.9,
            'bolt_circle_diameter': 88.9, 'bolt_holes': 4, 'bolt_hole_diameter': 22.4, 'weight_kg': 3},
    '1': {'flange_od': 149.4, 'thickness': 28.4, 'rf_diameter': 50.8,
          'bolt_circle_diameter': 101.6, 'bolt_holes': 4, 'bolt_hole_diameter': 25.4, 'weight_kg': 4},
    '1-1/4': {'flange_od': 158.8, 'thickness': 28.4, 'rf_diameter': 63.5,
              'bolt_circle_diameter': 111.3, 'bolt_holes': 4, 'bolt_hole_diameter': 25.4, 'weight_kg': 4},
    '1-1/2': {'flange_od': 177.8, 'thickness': 31.8, 'rf_diameter': 73.2,
              'bolt_circle_diameter': 124, 'bolt_holes': 4, 'bolt_hole_diameter': 28.4, 'weight_kg': 6},
    '2': {'flange_od': 215.9, 'thickness': 38.1, 'rf_diameter': 91.9,
          'bolt_circle_diameter': 165.1, 'bolt_holes': 8, 'bolt_hole_diameter': 25.4, 'weight_kg': 11},
    '2-1/2': {'flange_od': 244.3, 'thickness': 41.1, 'rf_diameter': 104.6,
              'bolt_circle_diameter': 190.5, 'bolt_holes': 8, 'bolt_hole_diameter': 28.4, 'weight_kg': 16},
    '3': {'flange_od': 266.7, 'thickness': 47.8, 'rf_diameter': 127,
          'bolt_circle_diameter': 203.2, 'bolt_holes': 8, 'bolt_hole_diameter': 31.8, 'weight_kg': 22},
    '4': {'flange_od': 311.2, 'thickness': 53.8, 'rf_diameter': 157.2,
          'bolt_circle_diameter': 241.3, 'bolt_holes': 8, 'bolt_hole_diameter': 35.1, 'weight_kg': 33},
    '5': {'flange_od': 374.7, 'thickness': 73.2, 'rf_diameter': 185.7,
          'bolt_circle_diameter': 292.1, 'bolt_holes': 8, 'bolt_hole_diameter': 41.1, 'weight_kg': 64},
    '6': {'flange_od': 393.7, 'thickness': 82.6, 'rf_diameter': 215.9,
          'bolt_circle_diameter': 317.5, 'bolt_holes': 12, 'bolt_hole_diameter': 38.1, 'weight_kg': 73},
    '8': {'flange_od': 482.6, 'thickness': 91.9, 'rf_diameter': 269.7,
          'bolt_circle_diameter': 393.7, 'bolt_holes': 12, 'bolt_hole_diameter': 44.5, 'weight_kg': 136},
    '10': {'flange_od': 584.2, 'thickness': 108, 'rf_diameter': 323.9,
           'bolt_circle_diameter': 482.6, 'bolt_holes': 12, 'bolt_hole_diameter': 50.8, 'weight_kg': 231},
    '12': {'flange_od': 673.1, 'thickness': 124, 'rf_diameter': 381,
           'bolt_circle_diameter': 571.5, 'bolt_holes': 16, 'bolt_hole_diameter': 53.8, 'weight_kg': 313},
    '14': {'flange_od': 749.3, 'thickness': 133.4, 'rf_diameter': 412.8,
           'bolt_circle_diameter': 635, 'bolt_holes': 16, 'bolt_hole_diameter': 60.5, 'weight_kg': 442},
    '16': {'flange_od': 825.5, 'thickness': 146.1, 'rf_diameter': 469.9,
           'bolt_circle_diameter': 704.9, 'bolt_holes': 16, 'bolt_hole_diameter': 66.5, 'weight_kg': 590},
    '18': {'flange_od': 914.4, 'thickness': 162.1, 'rf_diameter': 533.4,
           'bolt_circle_diameter': 774.7, 'bolt_holes': 16, 'bolt_hole_diameter': 73.2, 'weight_kg': 794},
    '20': {'flange_od': 984.3, 'thickness': 177.8, 'rf_diameter': 584.2,
           'bolt_circle_diameter': 831.9, 'bolt_holes': 16, 'bolt_hole_diameter': 79.2, 'weight_kg': 1009},
    '24': {'flange_od': 1168.4, 'thickness': 203.2, 'rf_diameter': 692.2,
           'bolt_circle_diameter': 990.6, 'bolt_holes': 16, 'bolt_hole_diameter': 91.9, 'weight_kg': 1644},
}

CLASS_2500_RF_BLIND = {
    '1/2': {'flange_od': 133.4, 'thickness': 30.2, 'rf_diameter': 35.1, 
            'bolt_circle_diameter': 88.9, 'bolt_holes': 4, 'bolt_hole_diameter': 22.4, 'weight_kg': 3},
    '3/4': {'flange_od': 139.7, 'thickness': 31.8, 'rf_diameter': 42.9,
            'bolt_circle_diameter': 95.3, 'bolt_holes': 4, 'bolt_hole_diameter': 22.4, 'weight_kg': 4},
    '1': {'flange_od': 158.8, 'thickness': 35.1, 'rf_diameter': 50.8,
          'bolt_circle_diameter': 108, 'bolt_holes': 4, 'bolt_hole_diameter': 25.4, 'weight_kg': 5},
    '1-1/4': {'flange_od': 184.2, 'thickness': 38.1, 'rf_diameter': 63.5,
              'bolt_circle_diameter': 130, 'bolt_holes': 4, 'bolt_hole_diameter': 28.4, 'weight_kg': 8},
    '1-1/2': {'flange_od': 203.2, 'thickness': 44.5, 'rf_diameter': 73.2,
              'bolt_circle_diameter': 146.1, 'bolt_holes': 4, 'bolt_hole_diameter': 31.8, 'weight_kg': 10},
    '2': {'flange_od': 235, 'thickness': 50.8, 'rf_diameter': 91.9,
          'bolt_circle_diameter': 171.5, 'bolt_holes': 8, 'bolt_hole_diameter': 28.4, 'weight_kg': 18},
    '2-1/2': {'flange_od': 266.7, 'thickness': 57.2, 'rf_diameter': 104.6,
              'bolt_circle_diameter': 196.9, 'bolt_holes': 8, 'bolt_hole_diameter': 31.8, 'weight_kg': 25},
    '3': {'flange_od': 304.8, 'thickness': 66.5, 'rf_diameter': 127,
          'bolt_circle_diameter': 228.6, 'bolt_holes': 8, 'bolt_hole_diameter': 35.1, 'weight_kg': 39},
    '4': {'flange_od': 355.6, 'thickness': 76.2, 'rf_diameter': 157.2,
          'bolt_circle_diameter': 273.1, 'bolt_holes': 8, 'bolt_hole_diameter': 41.1, 'weight_kg': 61},
    '5': {'flange_od': 419.1, 'thickness': 91.9, 'rf_diameter': 185.7,
          'bolt_circle_diameter': 323.9, 'bolt_holes': 8, 'bolt_hole_diameter': 47.8, 'weight_kg': 102},
    '6': {'flange_od': 482.6, 'thickness': 108, 'rf_diameter': 215.9,
          'bolt_circle_diameter': 368.3, 'bolt_holes': 8, 'bolt_hole_diameter': 53.8, 'weight_kg': 156},
    '8': {'flange_od': 552.5, 'thickness': 127, 'rf_diameter': 269.7,
          'bolt_circle_diameter': 438.2, 'bolt_holes': 12, 'bolt_hole_diameter': 53.8, 'weight_kg': 240},
    '10': {'flange_od': 673.1, 'thickness': 165.1, 'rf_diameter': 323.9,
           'bolt_circle_diameter': 539.8, 'bolt_holes': 12, 'bolt_hole_diameter': 66.5, 'weight_kg': 465},
    '12': {'flange_od': 762, 'thickness': 184.2, 'rf_diameter': 381,
           'bolt_circle_diameter': 619.3, 'bolt_holes': 12, 'bolt_hole_diameter': 73.2, 'weight_kg': 590},
}

# ============================================================================
# ASME B16.47 SERIES A BLIND FLANGE DATA
# ============================================================================

B1647_SERIES_A_CLASS150_RF_BLIND = {
    '26': {'flange_od': 870, 'thickness': 68.3, 'rf_diameter': 749.3,
           'bolt_circle_diameter': 806.5, 'bolt_holes': 24, 'bolt_hole_diameter': 35.1, 'weight_kg': 306},
    '36': {'flange_od': 1168.4, 'thickness': 90.4, 'rf_diameter': 1022.4,
           'bolt_circle_diameter': 1085.9, 'bolt_holes': 32, 'bolt_hole_diameter': 41.1, 'weight_kg': 733},
    '48': {'flange_od': 1511.3, 'thickness': 108, 'rf_diameter': 1358.9,
           'bolt_circle_diameter': 1422.4, 'bolt_holes': 44, 'bolt_hole_diameter': 41.1, 'weight_kg': 1476},
    '60': {'flange_od': 1854.2, 'thickness': 131.8, 'rf_diameter': 1676.4,
           'bolt_circle_diameter': 1759, 'bolt_holes': 52, 'bolt_hole_diameter': 47.8, 'weight_kg': 2710},
}

B1647_SERIES_A_CLASS300_RF_BLIND = {
    '26': {'flange_od': 971.6, 'thickness': 84.1, 'rf_diameter': 749.3,
           'bolt_circle_diameter': 876.3, 'bolt_holes': 28, 'bolt_hole_diameter': 44.5, 'weight_kg': 460},
    '36': {'flange_od': 1270, 'thickness': 111.3, 'rf_diameter': 1022.4,
           'bolt_circle_diameter': 1168.4, 'bolt_holes': 32, 'bolt_hole_diameter': 53.8, 'weight_kg': 1044},
    '48': {'flange_od': 1466.9, 'thickness': 108, 'rf_diameter': 1358.9,
           'bolt_circle_diameter': 1422.4, 'bolt_holes': 32, 'bolt_hole_diameter': 41.1, 'weight_kg': 1707},
    '60': {'flange_od': 1809.8, 'thickness': 163.6, 'rf_diameter': 1625.6,
           'bolt_circle_diameter': 1701.8, 'bolt_holes': 32, 'bolt_hole_diameter': 60.5, 'weight_kg': 3198},
}

B1647_SERIES_A_CLASS600_RF_BLIND = {
    '26': {'flange_od': 1016, 'thickness': 125.5, 'rf_diameter': 749.3,
           'bolt_circle_diameter': 914.4, 'bolt_holes': 28, 'bolt_hole_diameter': 50.8, 'weight_kg': 768},
    '36': {'flange_od': 1314.5, 'thickness': 167.1, 'rf_diameter': 1022.4,
           'bolt_circle_diameter': 1193.8, 'bolt_holes': 28, 'bolt_hole_diameter': 60.5, 'weight_kg': 1652},
    '48': {'flange_od': 1593.9, 'thickness': 195.3, 'rf_diameter': 1333.5,
           'bolt_circle_diameter': 1460.5, 'bolt_holes': 32, 'bolt_hole_diameter': 73.12, 'weight_kg': 2939},
    '60': {'flange_od': 1993.9, 'thickness': 242.8, 'rf_diameter': 1657.4,
           'bolt_circle_diameter': 1822.5, 'bolt_holes': 28, 'bolt_hole_diameter': 91.9, 'weight_kg': 5737},
}

B1647_SERIES_A_CLASS900_RF_BLIND = {
    '26': {'flange_od': 1085.9, 'thickness': 160.3, 'rf_diameter': 749.3,
           'bolt_circle_diameter': 952.5, 'bolt_holes': 20, 'bolt_hole_diameter': 73.2, 'weight_kg': 1087},
    '36': {'flange_od': 1460.5, 'thickness': 214.4, 'rf_diameter': 1022.4,
           'bolt_circle_diameter': 1289.1, 'bolt_holes': 20, 'bolt_hole_diameter': 91.9, 'weight_kg': 2651},
    '44': {'flange_od': 1648, 'thickness': 242.8, 'rf_diameter': 1270,
           'bolt_circle_diameter': 1463.5, 'bolt_holes': 24, 'bolt_hole_diameter': 98.6, 'weight_kg': 3801},
    '48': {'flange_od': 1784.4, 'thickness': 263.7, 'rf_diameter': 1384.3,
           'bolt_circle_diameter': 1587.5, 'bolt_holes': 24, 'bolt_hole_diameter': 104.6, 'weight_kg': 4850},
}

# ============================================================================
# ASME B16.47 SERIES B BLIND FLANGE DATA
# ============================================================================

B1647_SERIES_B_CLASS150_RF_BLIND = {
    '26': {'flange_od': 785.9, 'thickness': 44.5, 'rf_diameter': 771.2,
           'bolt_circle_diameter': 744.5, 'bolt_holes': 36, 'bolt_hole_diameter': 22.4, 'weight_kg': 164},
    '36': {'flange_od': 1057.1, 'thickness': 58.7, 'rf_diameter': 971.6,
           'bolt_circle_diameter': 1009.7, 'bolt_holes': 44, 'bolt_hole_diameter': 25.4, 'weight_kg': 395},
    '48': {'flange_od': 1392.2, 'thickness': 77.7, 'rf_diameter': 1289.1,
           'bolt_circle_diameter': 1335, 'bolt_holes': 44, 'bolt_hole_diameter': 31.8, 'weight_kg': 911},
    '60': {'flange_od': 1725.7, 'thickness': 96.8, 'rf_diameter': 1600.2,
           'bolt_circle_diameter': 1662.2, 'bolt_holes': 52, 'bolt_hole_diameter': 35.1, 'weight_kg': 1746},
}

B1647_SERIES_B_CLASS300_RF_BLIND = {
    '26': {'flange_od': 901.7, 'thickness': 88.9, 'rf_diameter': 936.6,
           'bolt_circle_diameter': 803.1, 'bolt_holes': 32, 'bolt_hole_diameter': 35.1, 'weight_kg': 390},
    '28': {'flange_od': 920.8, 'thickness': 88.9, 'rf_diameter': 787.4,
           'bolt_circle_diameter': 857.3, 'bolt_holes': 36, 'bolt_hole_diameter': 35.1, 'weight_kg': 441},
    '36': {'flange_od': 1171.4, 'thickness': 103.1, 'rf_diameter': 1009.7,
           'bolt_circle_diameter': 1089.7, 'bolt_holes': 32, 'bolt_hole_diameter': 44.5, 'weight_kg': 843},
    '48': {'flange_od': 1511.3, 'thickness': 134.9, 'rf_diameter': 1327.2,
           'bolt_circle_diameter': 1416.1, 'bolt_holes': 40, 'bolt_hole_diameter': 50.8, 'weight_kg': 1819},
    '60': {'flange_od': 1878, 'thickness': 166.6, 'rf_diameter': 1651,
           'bolt_circle_diameter': 1763.8, 'bolt_holes': 40, 'bolt_hole_diameter': 60.5, 'weight_kg': 3486},
}

B1647_SERIES_B_CLASS600_RF_BLIND = {
    '26': {'flange_od': 889, 'thickness': 111.3, 'rf_diameter': 726.9,
           'bolt_circle_diameter': 806.5, 'bolt_holes': 28, 'bolt_hole_diameter': 44.5, 'weight_kg': 527},
    '34': {'flange_od': 1212.9, 'thickness': 150.9, 'rf_diameter': 1009.7,
           'bolt_circle_diameter': 1104.9, 'bolt_holes': 24, 'bolt_hole_diameter': 60.5, 'weight_kg': 1165},
    '36': {'flange_od': 1212.9, 'thickness': 150.9, 'rf_diameter': 1009.7,
           'bolt_circle_diameter': 1104.9, 'bolt_holes': 28, 'bolt_hole_diameter': 60.5, 'weight_kg': 1320},
    '48': {'flange_od': 1593.9, 'thickness': 195.3, 'rf_diameter': 1333.5,
           'bolt_circle_diameter': 1460.5, 'bolt_holes': 32, 'bolt_hole_diameter': 73.12, 'weight_kg': 2939},
    '60': {'flange_od': 1993.9, 'thickness': 242.8, 'rf_diameter': 1657.4,
           'bolt_circle_diameter': 1822.5, 'bolt_holes': 28, 'bolt_hole_diameter': 91.9, 'weight_kg': 5737},
}

B1647_SERIES_B_CLASS900_RF_BLIND = {
    '26': {'flange_od': 1022.4, 'thickness': 153.9, 'rf_diameter': 962,
           'bolt_circle_diameter': 901.7, 'bolt_holes': 20, 'bolt_hole_diameter': 66.5, 'weight_kg': 935},
    '36': {'flange_od': 1346.2, 'thickness': 201.7, 'rf_diameter': 1028.7,
           'bolt_circle_diameter': 1200.2, 'bolt_holes': 24, 'bolt_hole_diameter': 79.2, 'weight_kg': 2001},
    '44': {'flange_od': 1648, 'thickness': 242.8, 'rf_diameter': 1270,
           'bolt_circle_diameter': 1463.5, 'bolt_holes': 24, 'bolt_hole_diameter': 98.6, 'weight_kg': 3801},
    '48': {'flange_od': 1784.4, 'thickness': 263.7, 'rf_diameter': 1384.3,
           'bolt_circle_diameter': 1587.5, 'bolt_holes': 24, 'bolt_hole_diameter': 104.6, 'weight_kg': 4850},
}


def get_flange_info(nps, pressure_class='150', flange_type='RF-WN', series='B16.5'):
    """
    Look up flange properties by NPS, pressure class, and series
    
    Args:
        nps: Nominal Pipe Size (e.g., '2', '4', '1-1/2', '26', '60')
        pressure_class: ASME pressure class ('150', '300', '600', '900', '1500', '2500')
        flange_type: Flange type ('RF-WN' for Raised Face Weld Neck, 'RF-BLIND' for Blind)
        series: Flange standard series: 'B16.5' (NPS 1/2-24), 'B16.47-A' (NPS 26-60), 'B16.47-B' (NPS 26-60)
    
    Returns:
        Dictionary with flange dimensions or None if not found
    """
    if series == 'B16.5':
        if flange_type == 'RF-BLIND':
            class_map = {
                '150': CLASS_150_RF_BLIND,
                '600': CLASS_600_RF_BLIND,
                '900': CLASS_900_RF_BLIND,
                '1500': CLASS_1500_RF_BLIND,
                '2500': CLASS_2500_RF_BLIND,
            }
        else:  # RF-WN
            class_map = {
                '150': CLASS_150_RF_WN,
                '300': CLASS_300_RF_WN,
                '400': CLASS_400_RF_WN,
                '600': CLASS_600_RF_WN,
                '900': CLASS_900_RF_WN,
                '1500': CLASS_1500_RF_WN,
                '2500': CLASS_2500_RF_WN,
            }
    elif series == 'B16.47-A':
        if flange_type == 'RF-BLIND':
            class_map = {
                '150': B1647_SERIES_A_CLASS150_RF_BLIND,
                '300': B1647_SERIES_A_CLASS300_RF_BLIND,
                '600': B1647_SERIES_A_CLASS600_RF_BLIND,
                '900': B1647_SERIES_A_CLASS900_RF_BLIND,
            }
        else:  # RF-WN
            class_map = {
                '150': B1647_SERIES_A_RF_WN,
                '300': B1647_SERIES_A_CLASS300_RF_WN,
                '600': B1647_SERIES_A_CLASS600_RF_WN,
                '900': B1647_SERIES_A_CLASS900_RF_WN,
            }
    elif series == 'B16.47-B':
        if flange_type == 'RF-BLIND':
            class_map = {
                '150': B1647_SERIES_B_CLASS150_RF_BLIND,
                '300': B1647_SERIES_B_CLASS300_RF_BLIND,
                '600': B1647_SERIES_B_CLASS600_RF_BLIND,
                '900': B1647_SERIES_B_CLASS900_RF_BLIND,
            }
        else:  # RF-WN
            class_map = {
                '150': B1647_SERIES_B_RF_WN,
                '300': B1647_SERIES_B_CLASS300_RF_WN,
                '600': B1647_SERIES_B_CLASS600_RF_WN,
                '900': B1647_SERIES_B_CLASS900_RF_WN,
            }
    else:
        return None
    
    flange_db = class_map.get(pressure_class)
    if not flange_db:
        return None
    
    return flange_db.get(nps)


def list_available_sizes(pressure_class='150', series='B16.5'):
    """
    List all available NPS sizes for a given pressure class and series
    
    Args:
        pressure_class: ASME pressure class ('150', '300', '600', '900', '1500', '2500')
        series: Flange standard series: 'B16.5' (NPS 1/2-24), 'B16.47-A' (NPS 26-60), 'B16.47-B' (NPS 26-60)
    
    Returns:
        Sorted list of available NPS sizes
    """
    if series == 'B16.5':
        class_map = {
            '150': CLASS_150_RF_WN,
            '300': CLASS_300_RF_WN,
            '400': CLASS_400_RF_WN,
            '600': CLASS_600_RF_WN,
            '900': CLASS_900_RF_WN,
            '1500': CLASS_1500_RF_WN,
            '2500': CLASS_2500_RF_WN,
        }
    elif series == 'B16.47-A':
        class_map = {
            '150': B1647_SERIES_A_RF_WN,
            '300': B1647_SERIES_A_CLASS300_RF_WN,
            '600': B1647_SERIES_A_CLASS600_RF_WN,
            '900': B1647_SERIES_A_CLASS900_RF_WN,
        }
    elif series == 'B16.47-B':
        class_map = {
            '150': B1647_SERIES_B_RF_WN,
            '300': B1647_SERIES_B_CLASS300_RF_WN,
            '600': B1647_SERIES_B_CLASS600_RF_WN,
            '900': B1647_SERIES_B_CLASS900_RF_WN,
        }
    else:
        return []
    
    flange_db = class_map.get(pressure_class)
    if not flange_db:
        return []
    
    def nps_to_float(nps):
        """Convert NPS string to float for sorting"""
        if '/' in nps:
            # Handle fractions like '1/2', '3/4', '1-1/2', '2-1/2'
            if '-' in nps:
                # e.g., '1-1/2' -> whole part '1' + fraction '1/2'
                parts = nps.split('-')
                whole = float(parts[0])
                frac_parts = parts[1].split('/')
                return whole + float(frac_parts[0]) / float(frac_parts[1])
            else:
                # e.g., '1/2' -> just fraction
                frac_parts = nps.split('/')
                return float(frac_parts[0]) / float(frac_parts[1])
        else:
            return float(nps)
    
    return sorted(flange_db.keys(), key=nps_to_float)
    
    return sorted(flange_db.keys(), key=lambda x: float(x.replace('-', '.')) if '-' in x else float(x.split()[0]))


if __name__ == "__main__":
    # Test lookups
    print("ASME B16.5 RF Weld Neck Flange Database")
    print("=" * 50)
    
    # Test Class 150
    test_sizes = ['1/2', '2', '6', '12']
    for size in test_sizes:
        flange = get_flange_info(size, '150')
        if flange:
            print(f"\nClass 150 NPS {size}:")
            print(f"  Flange OD: {flange['flange_od']} mm")
            print(f"  Thickness: {flange['flange_thickness']} mm")
            print(f"  Bolt Holes: {flange['bolt_holes']} x {flange['bolt_hole_diameter']} mm")
            print(f"  Weight: {flange['weight_kg']} kg")
    
    # Test Class 300
    print(f"\n\nClass 300 NPS 4:")
    flange = get_flange_info('4', '300')
    if flange:
        print(f"  Flange OD: {flange['flange_od']} mm")
        print(f"  RF Diameter: {flange['rf_diameter']} mm")
        print(f"  Hub Length: {flange['hub_length']} mm")
    
    # List available sizes
    print(f"\n\nAvailable Class 150 sizes: {len(list_available_sizes('150'))}")
    print(f"Available Class 300 sizes: {len(list_available_sizes('300'))}")
