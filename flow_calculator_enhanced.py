"""
Enhanced Flow Calculator for Pipe Sizing
Includes proper fluid properties, friction factors, compressibility, and engineering calculations

Fluid Properties Source Data:
- Engineering Toolbox (www.engineeringtoolbox.com)
- API Technical Data Book - Petroleum Refining
- NIST Chemistry WebBook
- ASME Steam Tables
- Perry's Chemical Engineers' Handbook
"""
import math

class FluidProperties:
    """
    Comprehensive fluid property database with temperature-dependent properties
    
    API Gravity Equation: API = 141.5 / SG - 131.5
    Inverted: SG = 141.5 / (API + 131.5)
    
    Density from SG: ρ (lb/ft³) = SG × 62.4
    """
    
    # ==========================================================================
    # FLUIDS DATABASE
    # Properties at 60°F (15.6°C) unless otherwise noted
    # density: lb/ft³, viscosity: centipoise (cP), compressible: bool
    # ==========================================================================
    
    FLUIDS = {
        # ======================================================================
        # WATER
        # ======================================================================
        'Fresh Water': {
            'density': 62.4,           # lb/ft³ at 60°F
            'viscosity': 1.12,         # cP at 60°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'description': 'Pure water at atmospheric pressure'
        },
        'Salt Water': {
            'density': 64.0,           # lb/ft³ at 60°F (3.5% salinity seawater)
            'viscosity': 1.20,         # cP at 60°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'salinity_percent': 3.5,
            'description': 'Seawater at 3.5% salinity'
        },
        'Produced Water': {
            'density': 65.0,           # lb/ft³ (high TDS oilfield water)
            'viscosity': 1.25,         # cP at 60°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'description': 'Oilfield produced water with high TDS'
        },
        
        # ======================================================================
        # CRUDE OILS (by API Gravity)
        # ======================================================================
        'Light Crude Oil (API 40)': {
            'density': 51.5,           # SG = 0.825
            'viscosity': 4.0,          # cP at 60°F
            'api_gravity': 40,
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'description': 'Light crude, West Texas Intermediate type'
        },
        'Medium Crude Oil (API 30)': {
            'density': 54.7,           # SG = 0.876
            'viscosity': 15.0,         # cP at 60°F
            'api_gravity': 30,
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'description': 'Medium crude, Arabian Light type'
        },
        'Heavy Crude Oil (API 20)': {
            'density': 57.7,           # SG = 0.934
            'viscosity': 100.0,        # cP at 60°F
            'api_gravity': 20,
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'description': 'Heavy crude, high viscosity'
        },
        'Extra Heavy Crude (API 10)': {
            'density': 62.4,           # SG = 1.0
            'viscosity': 1000.0,       # cP at 60°F
            'api_gravity': 10,
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'description': 'Bitumen/tar sand type, may require heating'
        },
        
        # ======================================================================
        # REFINED PETROLEUM PRODUCTS
        # ======================================================================
        'Gasoline': {
            'density': 46.5,           # SG = 0.745, API 58
            'viscosity': 0.6,          # cP at 60°F
            'api_gravity': 58,
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'flash_point_f': -45,
            'description': 'Motor gasoline'
        },
        'Diesel Fuel (#2)': {
            'density': 52.9,           # SG = 0.848, API 35
            'viscosity': 2.5,          # cP at 60°F
            'api_gravity': 35,
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'flash_point_f': 125,
            'description': 'ASTM #2 Diesel fuel'
        },
        'Jet Fuel (Jet-A)': {
            'density': 50.6,           # SG = 0.811
            'viscosity': 1.4,          # cP at 60°F
            'api_gravity': 43,
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'flash_point_f': 100,
            'description': 'Commercial aviation fuel'
        },
        'Kerosene': {
            'density': 51.2,           # SG = 0.820
            'viscosity': 1.8,          # cP at 60°F
            'api_gravity': 41,
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'flash_point_f': 100,
            'description': 'Heating kerosene / #1 fuel oil'
        },
        'Fuel Oil #2 (Heating Oil)': {
            'density': 53.7,           # SG = 0.860
            'viscosity': 3.0,          # cP at 60°F
            'api_gravity': 33,
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'flash_point_f': 130,
            'description': 'Home heating oil / light diesel'
        },
        'Fuel Oil #4': {
            'density': 56.2,           # SG = 0.900
            'viscosity': 15.0,         # cP at 60°F
            'api_gravity': 25,
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'description': 'Commercial / industrial heating'
        },
        'Fuel Oil #6 (Bunker C)': {
            'density': 59.9,           # SG = 0.960
            'viscosity': 300.0,        # cP at 60°F (varies widely 150-500)
            'api_gravity': 15,
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'pour_point_f': 65,
            'description': 'Residual fuel oil, requires heating'
        },
        'Bunker Fuel (IFO 380)': {
            'density': 60.6,           # SG = 0.970
            'viscosity': 380.0,        # cP at 122°F (50°C)
            'api_gravity': 14,
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'pour_point_f': 80,
            'description': 'Marine intermediate fuel oil 380 cSt'
        },
        
        # ======================================================================
        # LPG / NGL (Liquefied Petroleum Gas / Natural Gas Liquids)
        # ======================================================================
        'Propane (Liquid)': {
            'density': 31.2,           # SG = 0.50 at 60°F under pressure
            'viscosity': 0.11,         # cP at 60°F
            'api_gravity': 148,
            'compressible': False,     # Liquid phase
            'specific_heat_ratio': 1.13,
            'vapor_pressure_psi': 124, # at 60°F
            'boiling_point_f': -44,
            'description': 'Liquefied propane (C3H8)'
        },
        'Butane (Liquid)': {
            'density': 36.2,           # SG = 0.58 at 60°F
            'viscosity': 0.18,         # cP at 60°F
            'api_gravity': 111,
            'compressible': False,
            'specific_heat_ratio': 1.09,
            'vapor_pressure_psi': 31,  # at 60°F
            'boiling_point_f': 31,
            'description': 'Liquefied butane (C4H10)'
        },
        'LPG (Propane/Butane Mix)': {
            'density': 33.7,           # SG = 0.54 (70/30 mix)
            'viscosity': 0.14,         # cP at 60°F
            'compressible': False,
            'specific_heat_ratio': 1.11,
            'vapor_pressure_psi': 100, # at 60°F (varies with mix)
            'description': 'LPG 70% propane / 30% butane mix'
        },
        'NGL (Natural Gas Liquids)': {
            'density': 39.9,           # SG = 0.64 (typical Y-grade)
            'viscosity': 0.25,         # cP at 60°F
            'compressible': False,
            'specific_heat_ratio': 1.1,
            'description': 'Y-grade NGL (ethane through pentane mix)'
        },
        
        # ======================================================================
        # LNG (Liquefied Natural Gas) - Cryogenic
        # ======================================================================
        'LNG (Liquefied Natural Gas)': {
            'density': 26.5,           # SG = 0.425 at -260°F
            'viscosity': 0.12,         # cP at -260°F
            'compressible': False,     # Liquid phase
            'specific_heat_ratio': 1.31,
            'boiling_point_f': -260,
            'storage_temp_f': -260,
            'description': 'Cryogenic LNG (primarily methane)'
        },
        
        # ======================================================================
        # GASES
        # ======================================================================
        'Natural Gas': {
            'density': 0.0458,         # lb/ft³ at 60°F, 14.7 psia (SG=0.65)
            'viscosity': 0.011,        # cP
            'compressible': True,
            'specific_heat_ratio': 1.31,
            'gas_constant': 96.3,      # ft-lbf/(lbm-°R)
            'specific_gravity_gas': 0.65,
            'description': 'Natural gas (methane rich)'
        },
        'Compressed Air': {
            'density': 0.0765,         # lb/ft³ at 60°F, 14.7 psia
            'viscosity': 0.018,        # cP
            'compressible': True,
            'specific_heat_ratio': 1.4,
            'description': 'Dry air at standard conditions'
        },
        'Nitrogen': {
            'density': 0.0743,         # lb/ft³ at 60°F, 14.7 psia
            'viscosity': 0.018,        # cP
            'compressible': True,
            'specific_heat_ratio': 1.4,
            'description': 'Industrial nitrogen gas'
        },
        'Oxygen': {
            'density': 0.0846,         # lb/ft³ at 60°F, 14.7 psia
            'viscosity': 0.020,        # cP
            'compressible': True,
            'specific_heat_ratio': 1.4,
            'description': 'Industrial oxygen gas'
        },
        'Carbon Dioxide': {
            'density': 0.117,          # lb/ft³ at 60°F, 14.7 psia
            'viscosity': 0.015,        # cP
            'compressible': True,
            'specific_heat_ratio': 1.29,
            'description': 'Carbon dioxide gas'
        },
        'Hydrogen': {
            'density': 0.00533,        # lb/ft³ at 60°F, 14.7 psia
            'viscosity': 0.009,        # cP
            'compressible': True,
            'specific_heat_ratio': 1.41,
            'description': 'Hydrogen gas'
        },
        
        # ======================================================================
        # STEAM
        # ======================================================================
        'Steam (Saturated @ 100 psig)': {
            'density': 0.231,          # lb/ft³ at 338°F
            'viscosity': 0.014,        # cP
            'compressible': True,
            'specific_heat_ratio': 1.33,
            'temperature_f': 338,
            'description': 'Saturated steam at 100 psig'
        },
        'Steam (Saturated @ 150 psig)': {
            'density': 0.334,          # lb/ft³ at 366°F
            'viscosity': 0.015,        # cP
            'compressible': True,
            'specific_heat_ratio': 1.32,
            'temperature_f': 366,
            'description': 'Saturated steam at 150 psig'
        },
        'Steam (Saturated @ 300 psig)': {
            'density': 0.62,           # lb/ft³ at 422°F
            'viscosity': 0.017,        # cP
            'compressible': True,
            'specific_heat_ratio': 1.30,
            'temperature_f': 422,
            'description': 'Saturated steam at 300 psig'
        },
        'Steam (Superheated @ 600 psig)': {
            'density': 1.12,           # lb/ft³ at 750°F, 600 psig
            'viscosity': 0.021,        # cP at 750°F
            'compressible': True,
            'specific_heat_ratio': 1.28,
            'temperature_f': 750,
            'pressure_psig': 600,
            'saturation_temp_f': 489,
            'superheat_f': 261,
            'description': 'Superheated steam at 600 psig, 750°F (261°F superheat)'
        },
        'Steam (Superheated @ 1200 psig)': {
            'density': 1.85,           # lb/ft³ at 950°F, 1200 psig
            'viscosity': 0.026,        # cP at 950°F
            'compressible': True,
            'specific_heat_ratio': 1.26,
            'temperature_f': 950,
            'pressure_psig': 1200,
            'saturation_temp_f': 567,
            'superheat_f': 383,
            'description': 'Superheated steam at 1200 psig, 950°F (383°F superheat)'
        },
        'Steam (Low Pressure)': {
            'density': 0.0372,         # lb/ft³ at 212°F, 14.7 psia
            'viscosity': 0.013,        # cP
            'compressible': True,
            'specific_heat_ratio': 1.33,
            'temperature_f': 212,
            'description': 'Atmospheric pressure saturated steam'
        },
        
        # ======================================================================
        # SPECIALTY / INDUSTRIAL FLUIDS
        # ======================================================================
        'Glycol (50% Ethylene)': {
            'density': 67.4,           # lb/ft³ at 60°F
            'viscosity': 4.8,          # cP at 60°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'freeze_point_f': -34,
            'description': '50% ethylene glycol antifreeze'
        },
        'Glycol (TEG)': {
            'density': 69.9,           # lb/ft³ at 60°F
            'viscosity': 37.3,         # cP at 60°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'description': 'Triethylene glycol for gas dehydration'
        },
        'Methanol': {
            'density': 49.4,           # lb/ft³ at 60°F
            'viscosity': 0.59,         # cP at 60°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'flash_point_f': 52,
            'description': 'Methyl alcohol (hydrate inhibitor)'
        },
        'Ammonia (Liquid)': {
            'density': 38.5,           # lb/ft³ at 60°F under pressure
            'viscosity': 0.14,         # cP at 60°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'vapor_pressure_psi': 128, # at 60°F
            'description': 'Anhydrous ammonia liquid'
        },
        'Sulfuric Acid (98%)': {
            'density': 114.2,          # lb/ft³ at 60°F
            'viscosity': 24.0,         # cP at 60°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'description': 'Concentrated sulfuric acid - CORROSIVE'
        },
        'Caustic Soda (50%)': {
            'density': 93.5,           # lb/ft³ at 60°F
            'viscosity': 40.0,         # cP at 60°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'description': '50% sodium hydroxide solution - CORROSIVE'
        },
        'Nitric Acid (70%)': {
            'density': 89.2,           # lb/ft³ (1430 kg/m³)
            'viscosity': 1.8,          # cP at 68°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'description': 'Nitric acid 70% concentration - CORROSIVE'
        },
        'Hydrochloric Acid (37%)': {
            'density': 74.3,           # lb/ft³ (1190 kg/m³)
            'viscosity': 1.9,          # cP at 68°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'description': 'Hydrochloric acid 37% (muriatic) - CORROSIVE'
        },
        
        # ======================================================================
        # SOLVENTS & PETROCHEMICALS
        # ======================================================================
        'Acetone': {
            'density': 49.0,           # lb/ft³ (785 kg/m³ at 25°C)
            'viscosity': 0.32,         # cP at 68°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'flash_point_f': -4,
            'description': 'Acetone solvent'
        },
        'Benzene': {
            'density': 54.5,           # lb/ft³ (874 kg/m³ at 25°C)
            'viscosity': 0.60,         # cP at 68°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'flash_point_f': 12,
            'description': 'Benzene - petrochemical feedstock'
        },
        'Toluene': {
            'density': 54.1,           # lb/ft³ (867 kg/m³ at 20°C)
            'viscosity': 0.56,         # cP at 68°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'flash_point_f': 40,
            'description': 'Toluene solvent'
        },
        'Xylene (Mixed)': {
            'density': 54.1,           # lb/ft³ (867 kg/m³)
            'viscosity': 0.62,         # cP at 68°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'flash_point_f': 77,
            'description': 'Mixed xylenes solvent'
        },
        'Hexane': {
            'density': 40.9,           # lb/ft³ (655 kg/m³ at 25°C)
            'viscosity': 0.31,         # cP at 68°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'flash_point_f': -7,
            'description': 'n-Hexane solvent'
        },
        'Heptane': {
            'density': 42.4,           # lb/ft³ (680 kg/m³ at 25°C)
            'viscosity': 0.39,         # cP at 68°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'flash_point_f': 25,
            'description': 'n-Heptane solvent'
        },
        'Ethanol (Anhydrous)': {
            'density': 49.3,           # lb/ft³ (790 kg/m³ at 20°C)
            'viscosity': 1.10,         # cP at 68°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'flash_point_f': 55,
            'description': 'Ethyl alcohol 100%'
        },
        'Isopropyl Alcohol': {
            'density': 49.0,           # lb/ft³ (785 kg/m³ at 20°C)
            'viscosity': 2.0,          # cP at 68°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'flash_point_f': 53,
            'description': 'Isopropanol (IPA)'
        },
        'Carbon Tetrachloride': {
            'density': 98.9,           # lb/ft³ (1584 kg/m³ at 25°C)
            'viscosity': 0.97,         # cP at 68°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'description': 'Carbon tetrachloride (legacy solvent)'
        },
        'Chloroform': {
            'density': 91.5,           # lb/ft³ (1465 kg/m³ at 25°C)
            'viscosity': 0.54,         # cP at 68°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'description': 'Chloroform solvent'
        },
        'Ethyl Acetate': {
            'density': 56.2,           # lb/ft³ (901 kg/m³ at 20°C)
            'viscosity': 0.45,         # cP at 68°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'flash_point_f': 24,
            'description': 'Ethyl acetate solvent'
        },
        'Turpentine': {
            'density': 53.7,           # lb/ft³ (860 kg/m³ at 25°C)
            'viscosity': 1.49,         # cP at 68°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'flash_point_f': 95,
            'description': 'Turpentine oil'
        },
        'Naphtha': {
            'density': 41.5,           # lb/ft³ (665 kg/m³ at 15°C)
            'viscosity': 0.50,         # cP at 68°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'flash_point_f': -40,
            'description': 'Petroleum naphtha'
        },
        
        # ======================================================================
        # CRYOGENIC FLUIDS
        # ======================================================================
        'Liquid Oxygen (LOX)': {
            'density': 71.1,           # lb/ft³ (1140 kg/m³ at -183°C)
            'viscosity': 0.19,         # cP at boiling point
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'boiling_point_f': -297,
            'storage_temp_f': -297,
            'description': 'Cryogenic liquid oxygen'
        },
        'Liquid Nitrogen (LIN)': {
            'density': 50.4,           # lb/ft³ (807 kg/m³ at -196°C)
            'viscosity': 0.16,         # cP at boiling point
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'boiling_point_f': -320,
            'storage_temp_f': -320,
            'description': 'Cryogenic liquid nitrogen'
        },
        'Liquid Argon (LAR)': {
            'density': 87.0,           # lb/ft³ (1394 kg/m³ at -186°C)
            'viscosity': 0.27,         # cP at boiling point
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'boiling_point_f': -303,
            'storage_temp_f': -303,
            'description': 'Cryogenic liquid argon'
        },
        'Ethane (Liquid)': {
            'density': 35.6,           # lb/ft³ (570 kg/m³ at -89°C)
            'viscosity': 0.12,         # cP
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'boiling_point_f': -128,
            'description': 'Liquefied ethane (C2)'
        },
        
        # ======================================================================
        # VEGETABLE / BIO-OILS
        # ======================================================================
        'Soybean Oil': {
            'density': 57.4,           # lb/ft³ (920 kg/m³ at 20°C)
            'viscosity': 50.0,         # cP at 68°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'flash_point_f': 540,
            'description': 'Soybean vegetable oil'
        },
        'Corn Oil': {
            'density': 57.4,           # lb/ft³ (919 kg/m³ at 20°C)
            'viscosity': 52.0,         # cP at 68°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'flash_point_f': 490,
            'description': 'Corn vegetable oil'
        },
        'Olive Oil': {
            'density': 56.8,           # lb/ft³ (911 kg/m³ at 20°C)
            'viscosity': 84.0,         # cP at 68°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'flash_point_f': 437,
            'description': 'Olive oil'
        },
        'Castor Oil': {
            'density': 59.4,           # lb/ft³ (952 kg/m³ at 25°C)
            'viscosity': 650.0,        # cP at 68°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'description': 'Castor oil (very high viscosity)'
        },
        'Biodiesel (B100)': {
            'density': 54.9,           # lb/ft³ (880 kg/m³)
            'viscosity': 4.5,          # cP at 104°F (40°C)
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'flash_point_f': 266,
            'description': 'Biodiesel B100 (FAME)'
        },
        
        # ======================================================================
        # REFRIGERANTS
        # ======================================================================
        'R-11 (CFC)': {
            'density': 92.1,           # lb/ft³ (1476 kg/m³ at 25°C)
            'viscosity': 0.42,         # cP
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'boiling_point_f': 75,
            'description': 'Trichlorofluoromethane (legacy refrigerant)'
        },
        'R-12 (CFC)': {
            'density': 81.8,           # lb/ft³ (1311 kg/m³ at 25°C)
            'viscosity': 0.20,         # cP
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'boiling_point_f': -22,
            'description': 'Dichlorodifluoromethane (legacy refrigerant)'
        },
        'R-22 (HCFC)': {
            'density': 74.5,           # lb/ft³ (1194 kg/m³ at 25°C)
            'viscosity': 0.21,         # cP
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'boiling_point_f': -41,
            'description': 'Chlorodifluoromethane (phaseout refrigerant)'
        },
        'R-134a (HFC)': {
            'density': 75.7,           # lb/ft³ (1212 kg/m³ at 25°C)
            'viscosity': 0.20,         # cP
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'boiling_point_f': -15,
            'description': 'Tetrafluoroethane (common refrigerant)'
        },
        
        # ======================================================================
        # MISCELLANEOUS INDUSTRIAL
        # ======================================================================
        'Glycerol (Glycerin)': {
            'density': 78.7,           # lb/ft³ (1261 kg/m³ at 25°C)
            'viscosity': 1412.0,       # cP at 68°F (very viscous!)
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'description': 'Pure glycerol - very high viscosity'
        },
        'Ethylene Glycol (100%)': {
            'density': 68.5,           # lb/ft³ (1097 kg/m³ at 25°C)
            'viscosity': 16.1,         # cP at 68°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'freeze_point_f': 9,
            'description': 'Pure ethylene glycol'
        },
        'Propylene Glycol': {
            'density': 64.6,           # lb/ft³ (1036 kg/m³ at 25°C)
            'viscosity': 42.0,         # cP at 68°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'freeze_point_f': -76,
            'description': 'Propylene glycol (food-grade antifreeze)'
        },
        'Hydraulic Oil (ISO 32)': {
            'density': 53.7,           # lb/ft³ (860 kg/m³)
            'viscosity': 32.0,         # cP at 104°F (by definition ISO 32)
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'description': 'Hydraulic fluid ISO VG 32'
        },
        'Hydraulic Oil (ISO 46)': {
            'density': 54.3,           # lb/ft³ (870 kg/m³)
            'viscosity': 46.0,         # cP at 104°F (by definition ISO 46)
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'description': 'Hydraulic fluid ISO VG 46'
        },
        'Hydraulic Oil (ISO 68)': {
            'density': 54.9,           # lb/ft³ (880 kg/m³)
            'viscosity': 68.0,         # cP at 104°F (by definition ISO 68)
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'description': 'Hydraulic fluid ISO VG 68'
        },
        'Transformer Oil': {
            'density': 54.9,           # lb/ft³ (880 kg/m³ at 20°C)
            'viscosity': 10.0,         # cP at 68°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'flash_point_f': 295,
            'description': 'Electrical transformer oil'
        },
        'Lubricating Oil (SAE 10W-30)': {
            'density': 54.9,           # lb/ft³ (880 kg/m³)
            'viscosity': 80.0,         # cP at 104°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'description': 'Motor oil SAE 10W-30'
        },
        'Creosote': {
            'density': 66.6,           # lb/ft³ (1067 kg/m³ at 15°C)
            'viscosity': 12.0,         # cP at 68°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'description': 'Creosote wood preservative'
        },
        'Tar': {
            'density': 74.9,           # lb/ft³ (1200 kg/m³ at 20°C)
            'viscosity': 10000.0,      # cP - extremely viscous
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'description': 'Coal tar - extremely viscous'
        },
        'Brine (Saturated NaCl)': {
            'density': 76.8,           # lb/ft³ (1230 kg/m³ at 15°C)
            'viscosity': 1.8,          # cP at 68°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'freeze_point_f': -6,
            'description': 'Saturated salt brine'
        },
        'Milk': {
            'density': 64.3,           # lb/ft³ (1030 kg/m³ at 15°C)
            'viscosity': 2.0,          # cP at 68°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'description': 'Whole milk'
        },
        'Beer': {
            'density': 63.0,           # lb/ft³ (1010 kg/m³ at 10°C)
            'viscosity': 1.8,          # cP at 50°F
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'description': 'Beer (varies by type)'
        }
    }
    
    # ==========================================================================
    # WATER VISCOSITY TABLE (Temperature vs Viscosity)
    # Temperature (°F) : Viscosity (cP)
    # ==========================================================================
    WATER_VISCOSITY_TABLE = {
        32:  1.79,
        40:  1.55,
        50:  1.31,
        60:  1.12,
        70:  0.98,
        80:  0.86,
        90:  0.76,
        100: 0.68,
        120: 0.56,
        140: 0.47,
        160: 0.40,
        180: 0.35,
        200: 0.31,
        212: 0.28
    }
    
    # ==========================================================================
    # PIPE MATERIAL ROUGHNESS (inches)
    # Source: Crane Technical Paper 410, Cameron Hydraulic Data
    # ==========================================================================
    PIPE_ROUGHNESS = {
        # Material: (roughness_inches, description)
        'Commercial Steel': (0.0018, 'New commercial steel/wrought iron'),
        'Carbon Steel (New)': (0.0018, 'New carbon steel pipe'),
        'Carbon Steel (Corroded)': (0.010, 'Moderately corroded carbon steel'),
        'Carbon Steel (Severe Corrosion)': (0.030, 'Severely corroded/tuberculated'),
        'Stainless Steel': (0.00059, 'New stainless steel'),
        'Stainless Steel (Pickled)': (0.00004, 'Pickled/polished stainless'),
        'Cast Iron (New)': (0.0102, 'New cast iron'),
        'Cast Iron (Old)': (0.040, 'Old/corroded cast iron'),
        'Ductile Iron': (0.0102, 'Ductile iron, cement lined'),
        'Ductile Iron (Unlined)': (0.010, 'Ductile iron, unlined'),
        'Galvanized Steel': (0.006, 'Galvanized steel pipe'),
        'Copper': (0.00006, 'Drawn copper tubing'),
        'Brass': (0.00006, 'Drawn brass tubing'),
        'PVC': (0.00006, 'PVC plastic pipe'),
        'CPVC': (0.00006, 'CPVC plastic pipe'),
        'HDPE': (0.00006, 'High density polyethylene'),
        'FRP/GRP': (0.0002, 'Fiberglass reinforced plastic'),
        'Concrete (Smooth)': (0.012, 'Smooth concrete'),
        'Concrete (Rough)': (0.060, 'Rough concrete'),
        'Concrete (Very Rough)': (0.120, 'Very rough concrete'),
        'Riveted Steel': (0.036, 'Riveted steel'),
        'Wood Stave': (0.007, 'Wood stave pipe'),
        'Glass': (0.00001, 'Glass tubing'),
        'Rubber Lined': (0.00004, 'Rubber lined pipe'),
        'Epoxy Lined': (0.00004, 'Epoxy/plastic lined steel'),
    }
    
    # ==========================================================================
    # PIPE MATERIAL GRADES - Allowable Stress & Temperature Limits
    # Source: ASME B31.3, ASME Section II Part D
    # Allowable stress values in psi at various temperatures
    # ==========================================================================
    PIPE_MATERIAL_GRADES = {
        # ======================================================================
        # CARBON STEEL
        # ======================================================================
        'A106 Gr B (Carbon Steel)': {
            'category': 'Carbon Steel',
            'spec': 'ASTM A106 Grade B',
            'description': 'Seamless carbon steel pipe for high-temp service',
            'min_temp_f': -20,
            'max_temp_f': 800,
            'allowable_stress': {  # Temperature (°F): Allowable stress (psi)
                100: 20000, 200: 20000, 300: 20000, 400: 20000,
                500: 18900, 600: 17300, 700: 14400, 800: 10800
            },
            'yield_strength': 35000,
            'tensile_strength': 60000,
            'density_lb_ft3': 490,
            'corrosion_allowance': 0.0625,  # inches (typical 1/16")
        },
        'A53 Gr B (Carbon Steel)': {
            'category': 'Carbon Steel',
            'spec': 'ASTM A53 Grade B',
            'description': 'Welded/seamless carbon steel pipe',
            'min_temp_f': -20,
            'max_temp_f': 700,
            'allowable_stress': {
                100: 20000, 200: 20000, 300: 20000, 400: 20000,
                500: 18900, 600: 17300, 700: 14400
            },
            'yield_strength': 35000,
            'tensile_strength': 60000,
            'density_lb_ft3': 490,
            'corrosion_allowance': 0.0625,
        },
        'API 5L Gr B (Carbon Steel)': {
            'category': 'Carbon Steel',
            'spec': 'API 5L Grade B',
            'description': 'Line pipe for oil/gas transmission',
            'min_temp_f': -20,
            'max_temp_f': 450,
            'allowable_stress': {
                100: 21700, 200: 21700, 300: 21700, 400: 21700, 450: 21700
            },
            'yield_strength': 35000,
            'tensile_strength': 60000,
            'density_lb_ft3': 490,
            'corrosion_allowance': 0.0625,
        },
        'API 5L X52 (Carbon Steel)': {
            'category': 'Carbon Steel',
            'spec': 'API 5L Grade X52',
            'description': 'High-strength line pipe',
            'min_temp_f': -20,
            'max_temp_f': 450,
            'allowable_stress': {
                100: 26000, 200: 26000, 300: 26000, 400: 26000, 450: 26000
            },
            'yield_strength': 52000,
            'tensile_strength': 66000,
            'density_lb_ft3': 490,
            'corrosion_allowance': 0.0625,
        },
        'API 5L X65 (Carbon Steel)': {
            'category': 'Carbon Steel',
            'spec': 'API 5L Grade X65',
            'description': 'High-strength line pipe for high pressure',
            'min_temp_f': -20,
            'max_temp_f': 450,
            'allowable_stress': {
                100: 32500, 200: 32500, 300: 32500, 400: 32500, 450: 32500
            },
            'yield_strength': 65000,
            'tensile_strength': 77000,
            'density_lb_ft3': 490,
            'corrosion_allowance': 0.0625,
        },
        'A333 Gr 6 (Low Temp Carbon)': {
            'category': 'Carbon Steel',
            'spec': 'ASTM A333 Grade 6',
            'description': 'Low-temperature carbon steel',
            'min_temp_f': -50,
            'max_temp_f': 650,
            'allowable_stress': {
                -50: 20000, 100: 20000, 200: 20000, 300: 20000,
                400: 20000, 500: 18900, 600: 17300, 650: 15800
            },
            'yield_strength': 35000,
            'tensile_strength': 60000,
            'density_lb_ft3': 490,
            'corrosion_allowance': 0.0625,
        },
        # ======================================================================
        # STAINLESS STEEL - AUSTENITIC
        # ======================================================================
        '304/304L (Stainless)': {
            'category': 'Stainless Steel',
            'spec': 'ASTM A312 TP304/304L',
            'description': '18Cr-8Ni austenitic stainless',
            'min_temp_f': -425,
            'max_temp_f': 1500,
            'allowable_stress': {
                -425: 16700, 100: 16700, 200: 16700, 300: 15400,
                400: 14300, 500: 13500, 600: 12900, 700: 12500,
                800: 12200, 900: 11700, 1000: 9300, 1100: 6600,
                1200: 4500, 1300: 3000, 1400: 2000, 1500: 1400
            },
            'yield_strength': 25000,
            'tensile_strength': 70000,
            'density_lb_ft3': 501,
            'corrosion_allowance': 0.0,  # Generally no CA for stainless
        },
        '316/316L (Stainless)': {
            'category': 'Stainless Steel',
            'spec': 'ASTM A312 TP316/316L',
            'description': '16Cr-12Ni-2Mo austenitic stainless',
            'min_temp_f': -425,
            'max_temp_f': 1500,
            'allowable_stress': {
                -425: 16700, 100: 16700, 200: 16700, 300: 14800,
                400: 13800, 500: 13100, 600: 12700, 700: 12400,
                800: 12100, 900: 11700, 1000: 9600, 1100: 6900,
                1200: 4600, 1300: 3100, 1400: 2100, 1500: 1500
            },
            'yield_strength': 25000,
            'tensile_strength': 70000,
            'density_lb_ft3': 501,
            'corrosion_allowance': 0.0,
        },
        '321 (Stainless)': {
            'category': 'Stainless Steel',
            'spec': 'ASTM A312 TP321',
            'description': 'Ti-stabilized austenitic stainless',
            'min_temp_f': -425,
            'max_temp_f': 1500,
            'allowable_stress': {
                -425: 16700, 100: 16700, 200: 16700, 300: 16100,
                400: 15400, 500: 15000, 600: 14700, 700: 14500,
                800: 14300, 900: 13600, 1000: 10700, 1100: 6900,
                1200: 4500, 1300: 3000, 1400: 2000, 1500: 1400
            },
            'yield_strength': 30000,
            'tensile_strength': 75000,
            'density_lb_ft3': 501,
            'corrosion_allowance': 0.0,
        },
        '347 (Stainless)': {
            'category': 'Stainless Steel',
            'spec': 'ASTM A312 TP347',
            'description': 'Nb-stabilized austenitic stainless',
            'min_temp_f': -425,
            'max_temp_f': 1500,
            'allowable_stress': {
                -425: 16700, 100: 16700, 200: 16700, 300: 16100,
                400: 15400, 500: 15000, 600: 14700, 700: 14500,
                800: 14300, 900: 13600, 1000: 10700, 1100: 6900,
                1200: 4500, 1300: 3000, 1400: 2000, 1500: 1400
            },
            'yield_strength': 30000,
            'tensile_strength': 75000,
            'density_lb_ft3': 501,
            'corrosion_allowance': 0.0,
        },
        # ======================================================================
        # DUPLEX STAINLESS STEEL
        # ======================================================================
        '2205 Duplex (22Cr)': {
            'category': 'Duplex',
            'spec': 'ASTM A790 UNS S31803',
            'description': '22Cr-5Ni-3Mo duplex stainless',
            'min_temp_f': -60,
            'max_temp_f': 600,
            'allowable_stress': {
                -60: 25000, 100: 25000, 200: 25000, 300: 25000,
                400: 23800, 500: 22600, 600: 21500
            },
            'yield_strength': 65000,
            'tensile_strength': 90000,
            'density_lb_ft3': 489,
            'corrosion_allowance': 0.0,
        },
        '2507 Super Duplex (25Cr)': {
            'category': 'Super Duplex',
            'spec': 'ASTM A790 UNS S32750',
            'description': '25Cr-7Ni-4Mo super duplex stainless',
            'min_temp_f': -60,
            'max_temp_f': 550,
            'allowable_stress': {
                -60: 36700, 100: 36700, 200: 36700, 300: 34400,
                400: 32200, 500: 30500, 550: 29500
            },
            'yield_strength': 80000,
            'tensile_strength': 116000,
            'density_lb_ft3': 489,
            'corrosion_allowance': 0.0,
        },
        '255 Super Duplex (25Cr Ferralium)': {
            'category': 'Super Duplex',
            'spec': 'ASTM A790 UNS S32550',
            'description': '25Cr-5Ni-3Mo-2Cu super duplex',
            'min_temp_f': -60,
            'max_temp_f': 550,
            'allowable_stress': {
                -60: 33300, 100: 33300, 200: 33300, 300: 31500,
                400: 29900, 500: 28400, 550: 27700
            },
            'yield_strength': 80000,
            'tensile_strength': 110000,
            'density_lb_ft3': 490,
            'corrosion_allowance': 0.0,
        },
        # ======================================================================
        # TITANIUM
        # ======================================================================
        'Titanium Gr 2': {
            'category': 'Titanium',
            'spec': 'ASTM B861 Grade 2',
            'description': 'Commercially pure titanium',
            'min_temp_f': -75,
            'max_temp_f': 600,
            'allowable_stress': {
                -75: 16700, 100: 16700, 200: 14700, 300: 12500,
                400: 10400, 500: 8500, 600: 6800
            },
            'yield_strength': 40000,
            'tensile_strength': 50000,
            'density_lb_ft3': 282,
            'corrosion_allowance': 0.0,
        },
        'Titanium Gr 5 (6Al-4V)': {
            'category': 'Titanium',
            'spec': 'ASTM B861 Grade 5',
            'description': 'Ti-6Al-4V alloy',
            'min_temp_f': -75,
            'max_temp_f': 600,
            'allowable_stress': {
                -75: 40000, 100: 40000, 200: 36700, 300: 33000,
                400: 29700, 500: 26700, 600: 23000
            },
            'yield_strength': 120000,
            'tensile_strength': 130000,
            'density_lb_ft3': 282,
            'corrosion_allowance': 0.0,
        },
        'Titanium Gr 12': {
            'category': 'Titanium',
            'spec': 'ASTM B861 Grade 12',
            'description': 'Ti-0.3Mo-0.8Ni corrosion resistant',
            'min_temp_f': -75,
            'max_temp_f': 600,
            'allowable_stress': {
                -75: 23300, 100: 23300, 200: 21100, 300: 18100,
                400: 15200, 500: 12700, 600: 10500
            },
            'yield_strength': 70000,
            'tensile_strength': 70000,
            'density_lb_ft3': 282,
            'corrosion_allowance': 0.0,
        },
        # ======================================================================
        # NICKEL ALLOYS
        # ======================================================================
        'Alloy 625 (Inconel)': {
            'category': 'Nickel Alloy',
            'spec': 'ASTM B444 UNS N06625',
            'description': 'Ni-Cr-Mo-Nb alloy, high corrosion resistance',
            'min_temp_f': -325,
            'max_temp_f': 1200,
            'allowable_stress': {
                -325: 33300, 100: 33300, 200: 33300, 300: 32900,
                400: 32300, 500: 31800, 600: 31400, 700: 30900,
                800: 30500, 900: 29400, 1000: 25700, 1100: 18800, 1200: 13000
            },
            'yield_strength': 60000,
            'tensile_strength': 120000,
            'density_lb_ft3': 536,
            'corrosion_allowance': 0.0,
        },
        'Alloy 825 (Incoloy)': {
            'category': 'Nickel Alloy',
            'spec': 'ASTM B423 UNS N08825',
            'description': 'Ni-Fe-Cr-Mo-Cu alloy',
            'min_temp_f': -325,
            'max_temp_f': 1000,
            'allowable_stress': {
                -325: 23300, 100: 23300, 200: 23300, 300: 22400,
                400: 21600, 500: 20900, 600: 20400, 700: 20000,
                800: 19600, 900: 18900, 1000: 16700
            },
            'yield_strength': 35000,
            'tensile_strength': 85000,
            'density_lb_ft3': 516,
            'corrosion_allowance': 0.0,
        },
        'Alloy C276 (Hastelloy)': {
            'category': 'Nickel Alloy',
            'spec': 'ASTM B622 UNS N10276',
            'description': 'Ni-Mo-Cr alloy, excellent chemical resistance',
            'min_temp_f': -325,
            'max_temp_f': 1250,
            'allowable_stress': {
                -325: 28300, 100: 28300, 200: 28300, 300: 27700,
                400: 27100, 500: 26700, 600: 26400, 700: 26200,
                800: 25600, 900: 24700, 1000: 22100, 1100: 16800, 1200: 12100
            },
            'yield_strength': 41000,
            'tensile_strength': 100000,
            'density_lb_ft3': 559,
            'corrosion_allowance': 0.0,
        },
        # ======================================================================
        # COPPER ALLOYS
        # ======================================================================
        '90-10 Cu-Ni': {
            'category': 'Copper-Nickel',
            'spec': 'ASTM B466 UNS C70600',
            'description': '90% Cu - 10% Ni, seawater service',
            'min_temp_f': -325,
            'max_temp_f': 600,
            'allowable_stress': {
                -325: 10000, 100: 10000, 200: 10000, 300: 10000,
                400: 10000, 500: 9400, 600: 7800
            },
            'yield_strength': 15000,
            'tensile_strength': 40000,
            'density_lb_ft3': 558,
            'corrosion_allowance': 0.0,
        },
        '70-30 Cu-Ni': {
            'category': 'Copper-Nickel',
            'spec': 'ASTM B466 UNS C71500',
            'description': '70% Cu - 30% Ni, seawater/marine',
            'min_temp_f': -325,
            'max_temp_f': 600,
            'allowable_stress': {
                -325: 12500, 100: 12500, 200: 12500, 300: 12500,
                400: 12200, 500: 11500, 600: 9700
            },
            'yield_strength': 18000,
            'tensile_strength': 50000,
            'density_lb_ft3': 556,
            'corrosion_allowance': 0.0,
        },
    }
    
    @staticmethod
    def get_material_grades_by_category():
        """Return pipe material grades organized by category for UI dropdowns"""
        categories = {}
        for name, data in FluidProperties.PIPE_MATERIAL_GRADES.items():
            cat = data['category']
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(name)
        return categories
    
    @staticmethod
    def get_material_grade_list():
        """Return flat list of all material grades"""
        return sorted(FluidProperties.PIPE_MATERIAL_GRADES.keys())
    
    @staticmethod
    def get_material_properties(material_grade, temperature_f=100):
        """Get material properties including interpolated allowable stress at temperature"""
        if material_grade not in FluidProperties.PIPE_MATERIAL_GRADES:
            # Return defaults for unknown material
            return {
                'allowable_stress': 20000,
                'min_temp_f': -20,
                'max_temp_f': 800,
                'corrosion_allowance': 0.0625,
                'category': 'Unknown'
            }
        
        mat = FluidProperties.PIPE_MATERIAL_GRADES[material_grade]
        stress_table = mat['allowable_stress']
        
        # Interpolate allowable stress at temperature
        temps = sorted(stress_table.keys())
        
        if temperature_f <= temps[0]:
            allowable = stress_table[temps[0]]
        elif temperature_f >= temps[-1]:
            allowable = stress_table[temps[-1]]
        else:
            # Linear interpolation
            for i in range(len(temps) - 1):
                if temps[i] <= temperature_f <= temps[i+1]:
                    t1, t2 = temps[i], temps[i+1]
                    s1, s2 = stress_table[t1], stress_table[t2]
                    allowable = s1 + (s2 - s1) * (temperature_f - t1) / (t2 - t1)
                    break
        
        return {
            'allowable_stress': allowable,
            'min_temp_f': mat['min_temp_f'],
            'max_temp_f': mat['max_temp_f'],
            'corrosion_allowance': mat.get('corrosion_allowance', 0),
            'yield_strength': mat.get('yield_strength', 35000),
            'tensile_strength': mat.get('tensile_strength', 60000),
            'category': mat['category'],
            'spec': mat.get('spec', ''),
            'description': mat.get('description', '')
        }
    
    @staticmethod
    def calculate_allowable_pressure(od_inches, wall_thickness, material_grade, temperature_f=100, weld_efficiency=1.0):
        """
        Calculate allowable internal pressure per ASME B31.3
        
        P = (2 * S * E * t) / (D - 2 * Y * t)
        
        Where:
            P = allowable pressure (psi)
            S = allowable stress at temperature (psi)
            E = weld joint efficiency (0.6 to 1.0)
            t = wall thickness minus corrosion allowance (inches)
            D = outside diameter (inches)
            Y = temperature coefficient (0.4 for ductile materials < 900°F)
        """
        mat_props = FluidProperties.get_material_properties(material_grade, temperature_f)
        S = mat_props['allowable_stress']
        CA = mat_props['corrosion_allowance']
        
        # Effective wall thickness after corrosion allowance
        t_eff = wall_thickness - CA
        if t_eff <= 0:
            return 0
        
        # Y factor (temperature coefficient)
        Y = 0.4  # For ductile materials below 900°F
        if temperature_f > 900:
            Y = 0.5
        
        E = weld_efficiency
        D = od_inches
        
        # ASME B31.3 pressure formula
        P = (2 * S * E * t_eff) / (D - 2 * Y * t_eff)
        
        return max(0, P)
    
    # ==========================================================================
    # FITTING K-FACTORS (Resistance Coefficients)
    # Source: Crane Technical Paper 410
    # K = f × (L/D) equivalent, or direct K values
    # Head loss: h = K × (v²/2g)
    # ==========================================================================
    FITTING_K_FACTORS = {
        # Elbows
        '90° Elbow (LR)': 0.30,           # Long radius (R/D = 1.5)
        '90° Elbow (SR)': 0.60,           # Short radius (R/D = 1.0)
        '90° Elbow (Threaded)': 1.50,     # Threaded/screwed
        '90° Elbow (Mitered-1)': 1.10,    # Single miter
        '90° Elbow (Mitered-2)': 0.40,    # 2 welds, 45° each
        '90° Elbow (Mitered-3)': 0.30,    # 3 welds, 30° each
        '45° Elbow (LR)': 0.20,           # Long radius
        '45° Elbow (Threaded)': 0.40,     # Threaded/screwed
        '45° Elbow (Mitered)': 0.30,      # Mitered
        '180° Return Bend (LR)': 0.40,    # Long radius
        '180° Return Bend (SR)': 0.60,    # Short radius
        
        # Tees
        'Tee (Flow Through Run)': 0.20,   # Straight through
        'Tee (Flow Through Branch)': 1.00, # 90° to branch
        'Tee (Flow Into Run)': 0.40,      # Combining flow, run
        'Tee (Flow Into Branch)': 1.00,   # Combining flow, from branch
        
        # Reducers
        'Reducer (Concentric)': 0.10,     # Gradual reduction
        'Reducer (Eccentric)': 0.15,      # Eccentric reduction
        'Sudden Contraction': 0.50,       # Abrupt reduction
        'Sudden Expansion': 1.00,         # Abrupt expansion (based on v1)
        'Gradual Expansion (15°)': 0.15,  # 15° included angle
        'Gradual Expansion (30°)': 0.40,  # 30° included angle
        
        # Valves - Fully Open
        'Gate Valve (Full Open)': 0.17,
        'Gate Valve (3/4 Open)': 0.90,
        'Gate Valve (1/2 Open)': 4.50,
        'Gate Valve (1/4 Open)': 24.0,
        'Globe Valve (Full Open)': 6.00,
        'Globe Valve (1/2 Open)': 9.50,
        'Ball Valve (Full Open)': 0.05,
        'Ball Valve (1/3 Closed)': 5.50,
        'Ball Valve (2/3 Closed)': 200.0,
        'Butterfly Valve (Full Open)': 0.25,
        'Butterfly Valve (30° Open)': 1.50,
        'Butterfly Valve (60° Open)': 10.0,
        'Plug Valve (Full Open)': 0.40,
        'Plug Valve (3-Way, Thru)': 0.50,
        'Plug Valve (3-Way, Branch)': 0.90,
        'Diaphragm Valve (Full Open)': 2.30,
        'Check Valve (Swing)': 2.00,
        'Check Valve (Lift)': 10.0,
        'Check Valve (Ball)': 4.00,
        'Check Valve (Tilting Disc)': 1.50,
        'Foot Valve (Poppet)': 8.00,
        'Foot Valve (Hinged)': 3.00,
        
        # Entrances and Exits
        'Pipe Entrance (Sharp)': 0.50,
        'Pipe Entrance (Rounded)': 0.04,
        'Pipe Entrance (Projecting)': 1.00,  # Borda entrance
        'Pipe Entrance (Bellmouth)': 0.03,
        'Pipe Exit (Sharp)': 1.00,           # Into tank/atmosphere
        'Pipe Exit (Submerged)': 1.00,       # Into tank below surface
        
        # Strainers and Filters
        'Y-Strainer (Clean)': 2.00,
        'Y-Strainer (Dirty)': 8.00,
        'Basket Strainer (Clean)': 1.50,
        'Basket Strainer (Dirty)': 6.00,
        
        # Miscellaneous
        'Coupling': 0.04,
        'Union': 0.04,
        'Flange (Welded)': 0.02,
    }
    
    # ==========================================================================
    # EQUIVALENT LENGTH (L/D) RATIOS
    # Alternative to K-factors, multiply by pipe diameter for equivalent length
    # Source: Crane Technical Paper 410, Table A-29
    # ==========================================================================
    FITTING_LD_RATIOS = {
        # Elbows
        '90° Elbow (LR)': 16,             # Long radius
        '90° Elbow (SR)': 30,             # Short radius  
        '90° Elbow (Threaded)': 57,       # Threaded
        '45° Elbow (LR)': 10,             # Long radius
        '45° Elbow (Threaded)': 16,       # Threaded
        
        # Tees
        'Tee (Flow Through Run)': 10,
        'Tee (Flow Through Branch)': 60,
        
        # Valves
        'Gate Valve (Full Open)': 8,
        'Globe Valve (Full Open)': 340,
        'Ball Valve (Full Open)': 3,
        'Butterfly Valve (Full Open)': 20,
        'Check Valve (Swing)': 100,
        'Check Valve (Lift)': 600,
    }
    
    # ==========================================================================
    # CRUDE OIL VISCOSITY TABLE (API Gravity vs Viscosity at different temps)
    # From API Technical Data Book
    # ==========================================================================
    CRUDE_OIL_VISCOSITY_TABLE = {
        # API Gravity: {Temperature (°F): Viscosity (cP)}
        10: {60: 1000, 100: 300, 150: 80, 200: 30},
        15: {60: 300, 100: 100, 150: 35, 200: 15},
        20: {60: 100, 100: 40, 150: 15, 200: 7},
        25: {60: 40, 100: 18, 150: 8, 200: 4},
        30: {60: 15, 100: 8, 150: 4, 200: 2.5},
        35: {60: 7, 100: 4, 150: 2.5, 200: 1.8},
        40: {60: 4, 100: 2.5, 150: 1.8, 200: 1.3},
        45: {60: 2.5, 100: 1.8, 150: 1.3, 200: 1.0},
        50: {60: 1.5, 100: 1.2, 150: 1.0, 200: 0.8}
    }
    
    @staticmethod
    def api_to_specific_gravity(api_gravity):
        """
        Convert API gravity to specific gravity
        
        Formula: SG = 141.5 / (API + 131.5)
        
        Source: API Technical Data Book, Equation 5973 in EquationParadise DB
        """
        return 141.5 / (api_gravity + 131.5)
    
    @staticmethod
    def specific_gravity_to_api(sg):
        """
        Convert specific gravity to API gravity
        
        Formula: API = 141.5 / SG - 131.5
        """
        return (141.5 / sg) - 131.5
    
    @staticmethod
    def sg_to_density_lb_ft3(sg):
        """Convert specific gravity to density in lb/ft³"""
        return sg * 62.4
    
    @staticmethod
    def get_water_viscosity(temperature_f):
        """
        Get water viscosity at specified temperature using interpolation
        
        Args:
            temperature_f: Temperature in Fahrenheit
            
        Returns:
            Viscosity in centipoise (cP)
        """
        table = FluidProperties.WATER_VISCOSITY_TABLE
        temps = sorted(table.keys())
        
        # Clamp to table range
        if temperature_f <= temps[0]:
            return table[temps[0]]
        if temperature_f >= temps[-1]:
            return table[temps[-1]]
        
        # Linear interpolation
        for i in range(len(temps) - 1):
            if temps[i] <= temperature_f <= temps[i + 1]:
                t1, t2 = temps[i], temps[i + 1]
                v1, v2 = table[t1], table[t2]
                return v1 + (v2 - v1) * (temperature_f - t1) / (t2 - t1)
        
        return 1.0  # Default
    
    @staticmethod
    def get_crude_oil_viscosity(api_gravity, temperature_f):
        """
        Get crude oil viscosity at specified API gravity and temperature
        Uses bilinear interpolation from the viscosity table
        
        Args:
            api_gravity: API gravity (10-50 typical range)
            temperature_f: Temperature in Fahrenheit
            
        Returns:
            Viscosity in centipoise (cP)
        """
        table = FluidProperties.CRUDE_OIL_VISCOSITY_TABLE
        api_values = sorted(table.keys())
        
        # Clamp API gravity to table range
        api_gravity = max(min(api_gravity, api_values[-1]), api_values[0])
        
        # Find bracketing API values
        api_low = api_values[0]
        api_high = api_values[-1]
        for i in range(len(api_values) - 1):
            if api_values[i] <= api_gravity <= api_values[i + 1]:
                api_low = api_values[i]
                api_high = api_values[i + 1]
                break
        
        # Get temperature-viscosity data for bracketing API values
        temps_low = table[api_low]
        temps_high = table[api_high]
        
        # Interpolate viscosity at low API
        visc_low = FluidProperties._interpolate_temp_viscosity(temps_low, temperature_f)
        # Interpolate viscosity at high API
        visc_high = FluidProperties._interpolate_temp_viscosity(temps_high, temperature_f)
        
        # Interpolate between API values (log scale for viscosity)
        if api_high == api_low:
            return visc_low
        
        api_fraction = (api_gravity - api_low) / (api_high - api_low)
        # Use logarithmic interpolation for viscosity
        log_visc = math.log(visc_low) + api_fraction * (math.log(visc_high) - math.log(visc_low))
        
        return math.exp(log_visc)
    
    @staticmethod
    def _interpolate_temp_viscosity(temp_visc_dict, temperature_f):
        """Helper to interpolate viscosity from temperature-viscosity dict"""
        temps = sorted(temp_visc_dict.keys())
        
        if temperature_f <= temps[0]:
            return temp_visc_dict[temps[0]]
        if temperature_f >= temps[-1]:
            return temp_visc_dict[temps[-1]]
        
        for i in range(len(temps) - 1):
            if temps[i] <= temperature_f <= temps[i + 1]:
                t1, t2 = temps[i], temps[i + 1]
                v1, v2 = temp_visc_dict[t1], temp_visc_dict[t2]
                # Logarithmic interpolation for viscosity
                log_v = math.log(v1) + (math.log(v2) - math.log(v1)) * (temperature_f - t1) / (t2 - t1)
                return math.exp(log_v)
        
        return 10.0  # Default
    
    @staticmethod
    def get_pipe_roughness(material):
        """
        Get pipe roughness for a given material
        
        Args:
            material: Pipe material name from PIPE_ROUGHNESS dict
            
        Returns:
            tuple: (roughness_inches, description)
        """
        return FluidProperties.PIPE_ROUGHNESS.get(
            material, 
            FluidProperties.PIPE_ROUGHNESS['Commercial Steel']
        )
    
    @staticmethod
    def get_pipe_material_list():
        """Return list of available pipe materials for dropdown menus"""
        return sorted(FluidProperties.PIPE_ROUGHNESS.keys())
    
    @staticmethod
    def get_fitting_k_factor(fitting_name):
        """
        Get K-factor (resistance coefficient) for a fitting
        
        K is used in: h_loss = K × (v²/2g)
        
        Args:
            fitting_name: Name of fitting from FITTING_K_FACTORS dict
            
        Returns:
            float: K-factor value
        """
        return FluidProperties.FITTING_K_FACTORS.get(fitting_name, 0.0)
    
    @staticmethod
    def get_fitting_ld_ratio(fitting_name):
        """
        Get L/D equivalent length ratio for a fitting
        
        Equivalent length = (L/D) × pipe_diameter
        
        Args:
            fitting_name: Name of fitting from FITTING_LD_RATIOS dict
            
        Returns:
            float: L/D ratio value
        """
        return FluidProperties.FITTING_LD_RATIOS.get(fitting_name, 0.0)
    
    @staticmethod
    def get_fitting_list():
        """Return list of available fittings for dropdown menus"""
        return sorted(FluidProperties.FITTING_K_FACTORS.keys())
    
    @staticmethod
    def get_fittings_by_category():
        """Return fittings organized by category for UI"""
        return {
            'Elbows': [
                '90° Elbow (LR)',
                '90° Elbow (SR)',
                '90° Elbow (Threaded)',
                '90° Elbow (Mitered-1)',
                '90° Elbow (Mitered-2)',
                '90° Elbow (Mitered-3)',
                '45° Elbow (LR)',
                '45° Elbow (Threaded)',
                '45° Elbow (Mitered)',
                '180° Return Bend (LR)',
                '180° Return Bend (SR)'
            ],
            'Tees': [
                'Tee (Flow Through Run)',
                'Tee (Flow Through Branch)',
                'Tee (Flow Into Run)',
                'Tee (Flow Into Branch)'
            ],
            'Reducers': [
                'Reducer (Concentric)',
                'Reducer (Eccentric)',
                'Sudden Contraction',
                'Sudden Expansion',
                'Gradual Expansion (15°)',
                'Gradual Expansion (30°)'
            ],
            'Gate Valves': [
                'Gate Valve (Full Open)',
                'Gate Valve (3/4 Open)',
                'Gate Valve (1/2 Open)',
                'Gate Valve (1/4 Open)'
            ],
            'Globe Valves': [
                'Globe Valve (Full Open)',
                'Globe Valve (1/2 Open)'
            ],
            'Ball Valves': [
                'Ball Valve (Full Open)',
                'Ball Valve (1/3 Closed)',
                'Ball Valve (2/3 Closed)'
            ],
            'Butterfly Valves': [
                'Butterfly Valve (Full Open)',
                'Butterfly Valve (30° Open)',
                'Butterfly Valve (60° Open)'
            ],
            'Plug Valves': [
                'Plug Valve (Full Open)',
                'Plug Valve (3-Way, Thru)',
                'Plug Valve (3-Way, Branch)'
            ],
            'Check Valves': [
                'Check Valve (Swing)',
                'Check Valve (Lift)',
                'Check Valve (Ball)',
                'Check Valve (Tilting Disc)',
                'Foot Valve (Poppet)',
                'Foot Valve (Hinged)'
            ],
            'Other Valves': [
                'Diaphragm Valve (Full Open)'
            ],
            'Entrances': [
                'Pipe Entrance (Sharp)',
                'Pipe Entrance (Rounded)',
                'Pipe Entrance (Projecting)',
                'Pipe Entrance (Bellmouth)'
            ],
            'Exits': [
                'Pipe Exit (Sharp)',
                'Pipe Exit (Submerged)'
            ],
            'Strainers': [
                'Y-Strainer (Clean)',
                'Y-Strainer (Dirty)',
                'Basket Strainer (Clean)',
                'Basket Strainer (Dirty)'
            ],
            'Miscellaneous': [
                'Coupling',
                'Union',
                'Flange (Welded)'
            ]
        }
    
    @staticmethod
    def calculate_fitting_head_loss(k_factor, velocity_ft_s):
        """
        Calculate head loss through a fitting using K-factor method
        
        Formula: h = K × (v²/2g)
        
        Args:
            k_factor: Resistance coefficient (K)
            velocity_ft_s: Flow velocity in ft/s
            
        Returns:
            float: Head loss in feet of fluid
        """
        g = 32.174  # ft/s²
        return k_factor * (velocity_ft_s ** 2) / (2 * g)
    
    @staticmethod
    def calculate_fitting_pressure_drop(k_factor, velocity_ft_s, density_lb_ft3):
        """
        Calculate pressure drop through a fitting
        
        Formula: ΔP = K × (ρ × v²) / (2 × 144)
        
        Args:
            k_factor: Resistance coefficient (K)
            velocity_ft_s: Flow velocity in ft/s
            density_lb_ft3: Fluid density in lb/ft³
            
        Returns:
            float: Pressure drop in psi
        """
        return k_factor * density_lb_ft3 * (velocity_ft_s ** 2) / (2 * 32.174 * 144)
    
    @staticmethod
    def get_custom_crude_oil_properties(api_gravity, temperature_f=60):
        """
        Get properties for a crude oil with custom API gravity
        
        Args:
            api_gravity: API gravity value (10-50 typical)
            temperature_f: Temperature in Fahrenheit
            
        Returns:
            dict with density, viscosity, and other properties
        """
        sg = FluidProperties.api_to_specific_gravity(api_gravity)
        density = FluidProperties.sg_to_density_lb_ft3(sg)
        viscosity = FluidProperties.get_crude_oil_viscosity(api_gravity, temperature_f)
        
        return {
            'density': density,
            'viscosity': viscosity,
            'api_gravity': api_gravity,
            'specific_gravity': sg,
            'compressible': False,
            'specific_heat_ratio': 1.0,
            'temperature_f': temperature_f
        }
    
    @staticmethod
    def get_properties(fluid_name, temperature_f=60, pressure_psi=14.7):
        """
        Get fluid properties with temperature/pressure corrections
        
        Args:
            fluid_name: Name of fluid from FLUIDS dictionary
            temperature_f: Temperature in Fahrenheit (default 60°F)
            pressure_psi: Pressure in psia (default 14.7 psia)
            
        Returns:
            dict with corrected fluid properties
        """
        props = FluidProperties.FLUIDS.get(fluid_name, FluidProperties.FLUIDS['Fresh Water']).copy()
        base_density = props['density']  # Store base density at 60°F
        
        # Temperature correction for water
        if 'Water' in fluid_name:
            props['viscosity'] = FluidProperties.get_water_viscosity(temperature_f)
            # Adjust viscosity for salt water (slightly higher)
            if 'Salt' in fluid_name or 'Produced' in fluid_name:
                props['viscosity'] *= 1.07  # Salt water ~7% higher viscosity
            # Density correction (water expands with temperature)
            props['density'] = base_density * (1 - 0.0002 * (temperature_f - 60))
        
        # Temperature correction for crude oils
        elif 'Crude' in fluid_name and 'api_gravity' in props:
            api = props['api_gravity']
            props['viscosity'] = FluidProperties.get_crude_oil_viscosity(api, temperature_f)
            # Density correction for thermal expansion
            props['density'] *= (1 - 0.00045 * (temperature_f - 60))
        
        # Temperature correction for other petroleum products
        elif props.get('api_gravity'):
            # Use simplified temperature correction
            temp_factor = math.exp(-0.025 * (temperature_f - 60))
            props['viscosity'] *= temp_factor
            props['density'] *= (1 - 0.00045 * (temperature_f - 60))
        
        # Temperature correction for glycols
        elif 'Glycol' in fluid_name:
            temp_factor = math.exp(-0.03 * (temperature_f - 60))
            props['viscosity'] *= temp_factor
        
        # Pressure correction for gas density (ideal gas law)
        if props['compressible']:
            # ρ2 = ρ1 × (P2/P1) × (T1/T2)
            temp_r = temperature_f + 459.67  # Convert to Rankine
            base_temp_r = 519.67  # 60°F in Rankine
            props['density'] *= (pressure_psi / 14.7) * (base_temp_r / temp_r)
            
            # Gas viscosity increases slightly with temperature
            temp_factor = (temp_r / base_temp_r) ** 0.7
            props['viscosity'] *= temp_factor
        
        return props
    
    @staticmethod
    def get_fluid_list():
        """Return list of available fluid names for dropdown menus"""
        return sorted(FluidProperties.FLUIDS.keys())
    
    @staticmethod
    def get_fluids_by_category():
        """Return fluids organized by category for UI"""
        return {
            'Water': [
                'Fresh Water',
                'Salt Water',
                'Produced Water',
                'Brine (Saturated NaCl)'
            ],
            'Crude Oil': [
                'Light Crude Oil (API 40)',
                'Medium Crude Oil (API 30)',
                'Heavy Crude Oil (API 20)',
                'Extra Heavy Crude (API 10)'
            ],
            'Refined Products': [
                'Gasoline',
                'Jet Fuel (Jet-A)',
                'Kerosene',
                'Diesel Fuel (#2)',
                'Fuel Oil #2 (Heating Oil)',
                'Fuel Oil #4',
                'Fuel Oil #6 (Bunker C)',
                'Bunker Fuel (IFO 380)',
                'Naphtha',
                'Biodiesel (B100)'
            ],
            'LPG/NGL': [
                'Propane (Liquid)',
                'Butane (Liquid)',
                'LPG (Propane/Butane Mix)',
                'NGL (Natural Gas Liquids)',
                'Ethane (Liquid)',
                'LNG (Liquefied Natural Gas)'
            ],
            'Gases': [
                'Natural Gas',
                'Compressed Air',
                'Nitrogen',
                'Oxygen',
                'Carbon Dioxide',
                'Hydrogen'
            ],
            'Steam': [
                'Steam (Low Pressure)',
                'Steam (Saturated @ 100 psig)',
                'Steam (Saturated @ 150 psig)',
                'Steam (Saturated @ 300 psig)',
                'Steam (Superheated @ 600 psig)',
                'Steam (Superheated @ 1200 psig)'
            ],
            'Cryogenic': [
                'LNG (Liquefied Natural Gas)',
                'Liquid Oxygen (LOX)',
                'Liquid Nitrogen (LIN)',
                'Liquid Argon (LAR)',
                'Ethane (Liquid)'
            ],
            'Solvents': [
                'Acetone',
                'Benzene',
                'Toluene',
                'Xylene (Mixed)',
                'Hexane',
                'Heptane',
                'Ethanol (Anhydrous)',
                'Isopropyl Alcohol',
                'Methanol',
                'Ethyl Acetate',
                'Turpentine',
                'Naphtha'
            ],
            'Glycols & Antifreeze': [
                'Glycol (50% Ethylene)',
                'Ethylene Glycol (100%)',
                'Propylene Glycol',
                'Glycol (TEG)',
                'Glycerol (Glycerin)'
            ],
            'Acids & Caustics': [
                'Sulfuric Acid (98%)',
                'Nitric Acid (70%)',
                'Hydrochloric Acid (37%)',
                'Caustic Soda (50%)',
                'Ammonia (Liquid)'
            ],
            'Hydraulic & Lube Oils': [
                'Hydraulic Oil (ISO 32)',
                'Hydraulic Oil (ISO 46)',
                'Hydraulic Oil (ISO 68)',
                'Transformer Oil',
                'Lubricating Oil (SAE 10W-30)'
            ],
            'Vegetable Oils': [
                'Soybean Oil',
                'Corn Oil',
                'Olive Oil',
                'Castor Oil'
            ],
            'Refrigerants': [
                'R-134a (HFC)',
                'R-22 (HCFC)',
                'R-12 (CFC)',
                'R-11 (CFC)'
            ],
            'Food & Beverage': [
                'Milk',
                'Beer',
                'Fresh Water'
            ],
            'Specialty': [
                'Carbon Tetrachloride',
                'Chloroform',
                'Creosote',
                'Tar'
            ]
        }


class PipeData:
    """Pipe dimension database for standard schedules"""
    
    PIPE_DIMENSIONS = {
        # NPS: {Schedule: (OD, ID, Wall_Thickness)}
        '1/2': {
            '5': (0.840, 0.710, 0.065),
            '10': (0.840, 0.674, 0.083),
            '40': (0.840, 0.622, 0.109),
            '80': (0.840, 0.546, 0.147),
            '160': (0.840, 0.466, 0.187),
            'STD': (0.840, 0.622, 0.109),
            'XS': (0.840, 0.546, 0.147),
            'XXS': (0.840, 0.252, 0.294)
        },
        '3/4': {
            '5': (1.050, 0.920, 0.065),
            '10': (1.050, 0.884, 0.083),
            '40': (1.050, 0.824, 0.113),
            '80': (1.050, 0.742, 0.154),
            '160': (1.050, 0.612, 0.219),
            'STD': (1.050, 0.824, 0.113),
            'XS': (1.050, 0.742, 0.154),
            'XXS': (1.050, 0.434, 0.308)
        },
        '1': {
            '5': (1.315, 1.185, 0.065),
            '10': (1.315, 1.097, 0.109),
            '40': (1.315, 1.049, 0.133),
            '80': (1.315, 0.957, 0.179),
            '160': (1.315, 0.815, 0.250),
            'STD': (1.315, 1.049, 0.133),
            'XS': (1.315, 0.957, 0.179),
            'XXS': (1.315, 0.599, 0.358)
        },
        '1-1/4': {
            '5': (1.660, 1.530, 0.065),
            '10': (1.660, 1.442, 0.109),
            '40': (1.660, 1.380, 0.140),
            '80': (1.660, 1.278, 0.191),
            '160': (1.660, 1.160, 0.250),
            'STD': (1.660, 1.380, 0.140),
            'XS': (1.660, 1.278, 0.191),
            'XXS': (1.660, 0.896, 0.382)
        },
        '1-1/2': {
            '5': (1.900, 1.770, 0.065),
            '10': (1.900, 1.682, 0.109),
            '40': (1.900, 1.610, 0.145),
            '80': (1.900, 1.500, 0.200),
            '160': (1.900, 1.338, 0.281),
            'STD': (1.900, 1.610, 0.145),
            'XS': (1.900, 1.500, 0.200),
            'XXS': (1.900, 1.100, 0.400)
        },
        '2': {
            '5': (2.375, 2.245, 0.065),
            '10': (2.375, 2.157, 0.109),
            '40': (2.375, 2.067, 0.154),
            '80': (2.375, 1.939, 0.218),
            '160': (2.375, 1.689, 0.343),
            'STD': (2.375, 2.067, 0.154),
            'XS': (2.375, 1.939, 0.218),
            'XXS': (2.375, 1.503, 0.436)
        },
        '2-1/2': {
            '5': (2.875, 2.709, 0.083),
            '10': (2.875, 2.635, 0.120),
            '40': (2.875, 2.469, 0.203),
            '80': (2.875, 2.323, 0.276),
            '160': (2.875, 2.125, 0.375),
            'STD': (2.875, 2.469, 0.203),
            'XS': (2.875, 2.323, 0.276),
            'XXS': (2.875, 1.771, 0.552)
        },
        '3': {
            '5': (3.500, 3.334, 0.083),
            '10': (3.500, 3.260, 0.120),
            '40': (3.500, 3.068, 0.216),
            '80': (3.500, 2.900, 0.300),
            '160': (3.500, 2.624, 0.438),
            'STD': (3.500, 3.068, 0.216),
            'XS': (3.500, 2.900, 0.300),
            'XXS': (3.500, 2.300, 0.600)
        },
        '4': {
            '5': (4.500, 4.334, 0.083),
            '10': (4.500, 4.260, 0.120),
            '40': (4.500, 4.026, 0.237),
            '80': (4.500, 3.826, 0.337),
            '120': (4.500, 3.624, 0.438),
            '160': (4.500, 3.438, 0.531),
            'STD': (4.500, 4.026, 0.237),
            'XS': (4.500, 3.826, 0.337),
            'XXS': (4.500, 3.152, 0.674)
        },
        '6': {
            '5': (6.625, 6.407, 0.109),
            '10': (6.625, 6.357, 0.134),
            '40': (6.625, 6.065, 0.280),
            '80': (6.625, 5.761, 0.432),
            '120': (6.625, 5.501, 0.562),
            '160': (6.625, 5.187, 0.719),
            'STD': (6.625, 6.065, 0.280),
            'XS': (6.625, 5.761, 0.432),
            'XXS': (6.625, 4.897, 0.864)
        },
        '8': {
            '5': (8.625, 8.407, 0.109),
            '10': (8.625, 8.329, 0.148),
            '20': (8.625, 8.125, 0.250),
            '30': (8.625, 7.981, 0.322),
            '40': (8.625, 7.981, 0.322),
            '60': (8.625, 7.813, 0.406),
            '80': (8.625, 7.625, 0.500),
            '100': (8.625, 7.437, 0.594),
            '120': (8.625, 7.187, 0.719),
            '140': (8.625, 7.001, 0.812),
            '160': (8.625, 7.001, 0.812),
            'STD': (8.625, 7.981, 0.322),
            'XS': (8.625, 7.625, 0.500),
            'XXS': (8.625, 6.875, 0.875)
        },
        '10': {
            '5': (10.750, 10.482, 0.134),
            '10': (10.750, 10.420, 0.165),
            '20': (10.750, 10.250, 0.250),
            '30': (10.750, 10.136, 0.307),
            '40': (10.750, 10.020, 0.365),
            '60': (10.750, 9.750, 0.500),
            '80': (10.750, 9.562, 0.594),
            '100': (10.750, 9.312, 0.719),
            '120': (10.750, 9.062, 0.844),
            '140': (10.750, 8.750, 1.000),
            '160': (10.750, 8.750, 1.000),
            'STD': (10.750, 10.020, 0.365),
            'XS': (10.750, 9.562, 0.594),
            'XXS': (10.750, 8.500, 1.125)
        },
        '12': {
            '5': (12.750, 12.438, 0.156),
            '10': (12.750, 12.390, 0.180),
            '20': (12.750, 12.250, 0.250),
            '30': (12.750, 12.090, 0.330),
            '40': (12.750, 11.938, 0.406),
            'STD': (12.750, 11.938, 0.406),
            '60': (12.750, 11.626, 0.562),
            '80': (12.750, 11.374, 0.688),
            'XS': (12.750, 11.374, 0.688),
            '100': (12.750, 11.062, 0.844),
            '120': (12.750, 10.750, 1.000),
            '140': (12.750, 10.500, 1.125),
            '160': (12.750, 10.750, 1.000),
            'XXS': (12.750, 10.126, 1.312)
        }
    }
    
    @staticmethod
    def get_pipe_id(nps, schedule):
        """Get pipe inside diameter in inches"""
        if nps in PipeData.PIPE_DIMENSIONS:
            if schedule in PipeData.PIPE_DIMENSIONS[nps]:
                return PipeData.PIPE_DIMENSIONS[nps][schedule][1]
        return 0
    
    @staticmethod
    def get_pipe_dimensions(nps, schedule):
        """Get full pipe dimensions (OD, ID, wall thickness)"""
        if nps in PipeData.PIPE_DIMENSIONS:
            if schedule in PipeData.PIPE_DIMENSIONS[nps]:
                return PipeData.PIPE_DIMENSIONS[nps][schedule]
        return (0, 0, 0)


class FlowCalculator:
    """Enhanced flow calculator with proper engineering physics"""
    
    @staticmethod
    def calculate_reynolds_number(flow_gpm, id_inches, density_lb_ft3, viscosity_cp):
        """Calculate Reynolds number"""
        # Re = (ρ × V × D) / μ
        # Re = (3160 × Q × ρ) / (D × μ) for US units
        reynolds = (3160 * flow_gpm * density_lb_ft3) / (id_inches * viscosity_cp)
        return reynolds
    
    @staticmethod
    def calculate_friction_factor(reynolds, roughness=0.00015):
        """
        Calculate Darcy-Weisbach friction factor
        Uses Swamee-Jain equation for turbulent flow
        Uses 64/Re for laminar flow
        """
        if reynolds < 2300:
            # Laminar flow
            return 64.0 / reynolds
        elif reynolds < 4000:
            # Transitional - interpolate
            f_lam = 64.0 / reynolds
            f_turb = FlowCalculator._swamee_jain_friction(reynolds, roughness, 1.0)
            transition_factor = (reynolds - 2300) / 1700
            return f_lam + transition_factor * (f_turb - f_lam)
        else:
            # Turbulent flow - Swamee-Jain
            return FlowCalculator._swamee_jain_friction(reynolds, roughness, 1.0)
    
    @staticmethod
    def _swamee_jain_friction(reynolds, roughness, diameter):
        """Swamee-Jain equation for turbulent friction factor"""
        # f = 0.25 / [log10(ε/(3.7D) + 5.74/Re^0.9)]²
        relative_roughness = roughness / diameter
        term1 = relative_roughness / 3.7
        term2 = 5.74 / (reynolds ** 0.9)
        f = 0.25 / ((math.log10(term1 + term2)) ** 2)
        return f
    
    @staticmethod
    def calculate_pressure_drop(flow_gpm, id_inches, length_ft, density_lb_ft3, viscosity_cp, 
                                 roughness=0.0018, pipe_material=None):
        """
        Calculate pressure drop using Darcy-Weisbach equation
        
        Args:
            flow_gpm: Flow rate in gallons per minute
            id_inches: Pipe inside diameter in inches
            length_ft: Pipe length in feet
            density_lb_ft3: Fluid density in lb/ft³
            viscosity_cp: Fluid viscosity in centipoise
            roughness: Pipe roughness in inches (default 0.0018 for commercial steel)
            pipe_material: Optional pipe material name to look up roughness
            
        Returns:
            float: Pressure drop in psi
        """
        # If pipe material specified, look up roughness
        if pipe_material and pipe_material in FluidProperties.PIPE_ROUGHNESS:
            roughness = FluidProperties.PIPE_ROUGHNESS[pipe_material][0]
        
        # Calculate velocity (ft/s)
        velocity = (0.408 * flow_gpm) / (id_inches ** 2)
        
        # Calculate Reynolds number
        reynolds = FlowCalculator.calculate_reynolds_number(flow_gpm, id_inches, density_lb_ft3, viscosity_cp)
        
        # Calculate friction factor
        friction_factor = FlowCalculator.calculate_friction_factor(reynolds, roughness / (id_inches / 12))
        
        # Darcy-Weisbach: ΔP = f × (L/D) × (ρ × V²/2)
        # In US units: ΔP (psi) = f × (L/D) × (ρ × V²) / (2 × 32.2 × 144)
        diameter_ft = id_inches / 12
        pressure_drop = (friction_factor * (length_ft / diameter_ft) * density_lb_ft3 * (velocity ** 2)) / (2 * 32.2 * 144)
        
        return pressure_drop
    
    @staticmethod
    def calculate_total_pressure_drop(flow_gpm, id_inches, length_ft, density_lb_ft3, viscosity_cp,
                                       fittings=None, pipe_material='Commercial Steel'):
        """
        Calculate total pressure drop including pipe and fittings
        
        Args:
            flow_gpm: Flow rate in gallons per minute
            id_inches: Pipe inside diameter in inches
            length_ft: Pipe length in feet
            density_lb_ft3: Fluid density in lb/ft³
            viscosity_cp: Fluid viscosity in centipoise
            fittings: List of tuples [(fitting_name, quantity), ...]
            pipe_material: Pipe material name for roughness lookup
            
        Returns:
            dict: Breakdown of pressure drops
        """
        # Get pipe roughness
        roughness = FluidProperties.PIPE_ROUGHNESS.get(
            pipe_material, 
            FluidProperties.PIPE_ROUGHNESS['Commercial Steel']
        )[0]
        
        # Calculate velocity
        velocity = (0.408 * flow_gpm) / (id_inches ** 2)
        
        # Pipe pressure drop
        pipe_dp = FlowCalculator.calculate_pressure_drop(
            flow_gpm, id_inches, length_ft, density_lb_ft3, viscosity_cp, roughness
        )
        
        # Fitting pressure drops
        fitting_dp = 0.0
        fitting_details = []
        
        if fittings:
            for fitting_name, qty in fittings:
                k = FluidProperties.get_fitting_k_factor(fitting_name)
                if k > 0:
                    dp = FluidProperties.calculate_fitting_pressure_drop(k, velocity, density_lb_ft3)
                    total_dp = dp * qty
                    fitting_dp += total_dp
                    fitting_details.append({
                        'fitting': fitting_name,
                        'quantity': qty,
                        'k_factor': k,
                        'dp_each': dp,
                        'dp_total': total_dp
                    })
        
        return {
            'pipe_dp_psi': pipe_dp,
            'fitting_dp_psi': fitting_dp,
            'total_dp_psi': pipe_dp + fitting_dp,
            'velocity_fps': velocity,
            'pipe_material': pipe_material,
            'roughness_in': roughness,
            'fitting_details': fitting_details
        }
    
    @staticmethod
    def calculate_velocity(flow_gpm, id_inches):
        """Calculate flow velocity in ft/s"""
        # V (ft/s) = (0.408 × Q) / D²
        velocity = (0.408 * flow_gpm) / (id_inches ** 2)
        return velocity
    
    @staticmethod
    def get_flow_regime(reynolds):
        """Determine flow regime from Reynolds number"""
        if reynolds < 2300:
            return "Laminar"
        elif reynolds < 4000:
            return "Transitional"
        else:
            return "Turbulent"
    
    @staticmethod
    def calculate_erosional_velocity(density_lb_ft3, c_factor=100):
        """
        Calculate erosional velocity limit for gas/liquid systems
        Ve = C / √ρ where C is empirical constant (100-200)
        """
        if density_lb_ft3 > 0:
            return c_factor / math.sqrt(density_lb_ft3)
        return 999
    
    @staticmethod
    def get_max_velocity_for_fluid(fluid_name, density_lb_ft3=None):
        """
        Get industry-standard maximum velocity limits for different fluids
        Based on API RP 14E, ASME B31.3, and industry practice
        
        Returns: (max_velocity_ft_s, reason)
        """
        # Industry standard maximum velocities (ft/s)
        # Based on service type and erosion/corrosion considerations
        
        # Check for specific fluid matches first
        velocity_limits = {
            # Water services
            'Fresh Water': (10.0, "ASME B31.3 noise/vibration limit"),
            'Salt Water': (8.0, "Corrosion rate limit for seawater"),
            'Produced Water': (6.0, "High TDS erosion/corrosion limit"),
            
            # Crude oils by weight
            'Light Crude Oil (API 40)': (10.0, "Light crude piping practice"),
            'Medium Crude Oil (API 30)': (8.0, "Medium crude erosion limit"),
            'Heavy Crude Oil (API 20)': (6.0, "Heavy crude viscosity limit"),
            'Extra Heavy Crude (API 10)': (4.0, "Bitumen - typically heated"),
            
            # Refined products
            'Gasoline': (15.0, "Low viscosity petroleum"),
            'Jet Fuel (Jet-A)': (12.0, "Aviation fuel piping"),
            'Kerosene': (12.0, "Light distillate"),
            'Diesel Fuel (#2)': (10.0, "Light petroleum product"),
            'Fuel Oil #2 (Heating Oil)': (10.0, "Light fuel oil"),
            'Fuel Oil #4': (8.0, "Medium fuel oil"),
            'Fuel Oil #6 (Bunker C)': (5.0, "Residual fuel - heated"),
            'Bunker Fuel (IFO 380)': (4.0, "Marine fuel - heated"),
            
            # LPG / NGL
            'Propane (Liquid)': (12.0, "Low viscosity LPG"),
            'Butane (Liquid)': (12.0, "Low viscosity LPG"),
            'LPG (Propane/Butane Mix)': (12.0, "LPG service"),
            'NGL (Natural Gas Liquids)': (10.0, "NGL pipeline practice"),
            'LNG (Liquefied Natural Gas)': (8.0, "Cryogenic service limit"),
            
            # Gases
            'Natural Gas': (60.0, "API RP 14E erosional"),
            'Compressed Air': (80.0, "Industrial air systems"),
            'Nitrogen': (80.0, "Industrial gas systems"),
            'Oxygen': (60.0, "Reduced for fire safety"),
            'Carbon Dioxide': (60.0, "CO2 pipeline practice"),
            'Hydrogen': (80.0, "High velocity gas"),
            
            # Steam
            'Steam (Low Pressure)': (200.0, "Low pressure saturated"),
            'Steam (Saturated @ 100 psig)': (150.0, "Medium pressure steam"),
            'Steam (Saturated @ 150 psig)': (120.0, "Industrial steam"),
            'Steam (Saturated @ 300 psig)': (100.0, "High pressure steam"),
            'Steam (Superheated @ 600 psig)': (80.0, "High pressure superheated"),
            'Steam (Superheated @ 1200 psig)': (60.0, "Very high pressure superheated"),
            
            # Industrial fluids
            'Glycol (50% Ethylene)': (8.0, "Glycol service"),
            'Glycol (TEG)': (6.0, "Viscous glycol"),
            'Ethylene Glycol (100%)': (8.0, "Glycol service"),
            'Propylene Glycol': (8.0, "Glycol service"),
            'Glycerol (Glycerin)': (3.0, "Very high viscosity"),
            'Methanol': (12.0, "Low viscosity solvent"),
            'Ammonia (Liquid)': (8.0, "Anhydrous ammonia"),
            'Sulfuric Acid (98%)': (4.0, "Corrosive service"),
            'Nitric Acid (70%)': (4.0, "Corrosive service"),
            'Hydrochloric Acid (37%)': (4.0, "Corrosive service"),
            'Caustic Soda (50%)': (4.0, "Corrosive service"),
            
            # Solvents
            'Acetone': (15.0, "Low viscosity solvent"),
            'Benzene': (12.0, "Aromatic hydrocarbon"),
            'Toluene': (12.0, "Aromatic hydrocarbon"),
            'Xylene (Mixed)': (12.0, "Aromatic hydrocarbon"),
            'Hexane': (15.0, "Low viscosity solvent"),
            'Heptane': (15.0, "Low viscosity solvent"),
            'Ethanol (Anhydrous)': (12.0, "Alcohol"),
            'Isopropyl Alcohol': (10.0, "Alcohol"),
            'Ethyl Acetate': (12.0, "Ester solvent"),
            'Turpentine': (10.0, "Natural solvent"),
            'Naphtha': (15.0, "Light hydrocarbon"),
            'Carbon Tetrachloride': (8.0, "Chlorinated solvent"),
            'Chloroform': (10.0, "Chlorinated solvent"),
            
            # Cryogenic
            'Liquid Oxygen (LOX)': (8.0, "Cryogenic service"),
            'Liquid Nitrogen (LIN)': (10.0, "Cryogenic service"),
            'Liquid Argon (LAR)': (8.0, "Cryogenic service"),
            'Ethane (Liquid)': (10.0, "NGL cryogenic"),
            
            # Oils
            'Hydraulic Oil (ISO 32)': (8.0, "Hydraulic system"),
            'Hydraulic Oil (ISO 46)': (8.0, "Hydraulic system"),
            'Hydraulic Oil (ISO 68)': (6.0, "Viscous hydraulic"),
            'Transformer Oil': (6.0, "Electrical insulating oil"),
            'Lubricating Oil (SAE 10W-30)': (6.0, "Motor oil"),
            'Soybean Oil': (4.0, "Vegetable oil"),
            'Corn Oil': (4.0, "Vegetable oil"),
            'Olive Oil': (4.0, "Vegetable oil"),
            'Castor Oil': (2.0, "Very high viscosity oil"),
            'Biodiesel (B100)': (10.0, "Biodiesel"),
            
            # Refrigerants
            'R-134a (HFC)': (10.0, "Refrigerant liquid"),
            'R-22 (HCFC)': (10.0, "Refrigerant liquid"),
            'R-12 (CFC)': (10.0, "Refrigerant liquid"),
            'R-11 (CFC)': (10.0, "Refrigerant liquid"),
            
            # Food & beverage
            'Milk': (8.0, "Dairy product"),
            'Beer': (8.0, "Beverage"),
            
            # Specialty
            'Brine (Saturated NaCl)': (6.0, "Corrosive brine"),
            'Creosote': (6.0, "Wood preservative"),
            'Tar': (2.0, "Extremely viscous"),
        }
        
        # Check for exact match first
        if fluid_name in velocity_limits:
            limit = velocity_limits[fluid_name]
        else:
            # Try to match by category keywords
            if 'Water' in fluid_name:
                limit = (10.0, "Water service default")
            elif 'Crude' in fluid_name:
                limit = (8.0, "Crude oil default")
            elif 'Steam' in fluid_name:
                limit = (150.0, "Steam service default")
            elif 'Fuel Oil' in fluid_name or 'Bunker' in fluid_name:
                limit = (6.0, "Heavy fuel default")
            elif 'Gas' in fluid_name and density_lb_ft3 and density_lb_ft3 < 1.0:
                limit = (60.0, "Gas service default")
            else:
                limit = (10.0, "Default liquid limit")
        
        # For gases, also check erosional velocity (API RP 14E)
        if density_lb_ft3 and density_lb_ft3 < 0.5:  # Likely a gas
            erosional_vel = FlowCalculator.calculate_erosional_velocity(density_lb_ft3)
            if erosional_vel < limit[0]:
                return (erosional_vel, f"API RP 14E erosional limit Ve=C/√ρ")
        
        return limit
    
    @staticmethod
    def calculate_max_flow_rate(id_inches, max_velocity_ft_s):
        """
        Calculate maximum flow rate for given pipe size and velocity limit
        
        Q (GPM) = V × A / 0.408 where A = π × D²/4
        Simplified: Q = V × D² / 0.408
        
        Args:
            id_inches: Pipe inside diameter (inches)
            max_velocity_ft_s: Maximum allowable velocity (ft/s)
        
        Returns:
            float: Maximum flow rate in GPM
        """
        max_flow_gpm = (max_velocity_ft_s * id_inches ** 2) / 0.408
        return max_flow_gpm
    
    @staticmethod
    def calculate_min_pipe_size(flow_gpm, max_velocity_ft_s):
        """
        Calculate minimum pipe ID for given flow rate and max velocity
        
        D = √(0.408 × Q / V)
        
        Args:
            flow_gpm: Flow rate in GPM
            max_velocity_ft_s: Maximum allowable velocity (ft/s)
        
        Returns:
            float: Minimum pipe inside diameter (inches)
        """
        min_id = math.sqrt((0.408 * flow_gpm) / max_velocity_ft_s)
        return min_id
    
    @staticmethod
    def get_schedule_pressure_rating(schedule, nps, material='A106B', temp_f=100):
        """
        Get pressure rating for pipe schedule using Barlow's Formula
        
        Barlow's Formula: P = (2 × S × t) / D
        
        Where:
            P = Internal pressure (psi)
            S = Allowable stress (psi)
            t = Wall thickness (inches)
            D = Outside diameter (inches)
        
        Args:
            schedule: Pipe schedule ('20', '40', '80', etc.)
            nps: Nominal pipe size (inches)
            material: Pipe material (default 'A106B')
            temp_f: Temperature in Fahrenheit (default 100°F)
        
        Returns:
            int: Pressure rating in psi
        """
        # Allowable stress for A106 Grade B carbon steel (ASME B31.3)
        allowable_stress_table = {
            100: 20000,   # psi at 100°F
            200: 20000,
            300: 20000,
            400: 19100,
            500: 17900,
            600: 15700,
            650: 14200
        }
        
        # Find closest temperature
        temps = sorted(allowable_stress_table.keys())
        closest_temp = min(temps, key=lambda x: abs(x - temp_f))
        S = allowable_stress_table[closest_temp]
        
        # Get pipe dimensions
        od, id_val, wall = PipeData.get_pipe_dimensions(nps, schedule)
        if od == 0:
            return 0
        
        # Barlow's Formula: P = (2 × S × t) / D
        pressure_rating = (2 * S * wall) / od
        
        return int(pressure_rating)


def convert_flow_to_gpm(value, unit):
    """Convert various flow units to GPM"""
    conversions = {
        "GPM": 1.0,
        "GPH": 1/60,
        "BBL/D": 0.0292,
        "CFM": 7.481,
        "L/min": 0.264,
        "L/s": 15.85,
        "m³/hr": 4.403
    }
    return value * conversions.get(unit, 1.0)


def convert_pressure_to_psi(value, unit):
    """Convert pressure to PSI"""
    conversions = {
        "PSI": 1.0,
        "bar": 14.504,
        "kPa": 0.145,
        "MPa": 145.0
    }
    return value * conversions.get(unit, 1.0)
