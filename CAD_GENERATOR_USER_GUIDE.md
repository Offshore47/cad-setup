# Equation Paradise CAD Generator v1.3.0
## Complete User Guide

---

# Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
   - [System Requirements](#system-requirements)
   - [Installation](#installation)
   - [First Launch & Authentication](#first-launch--authentication)
3. [User Interface Overview](#user-interface-overview)
   - [Main Window Layout](#main-window-layout)
   - [Navigation Tabs](#navigation-tabs)
   - [Status Bar](#status-bar)
4. [Package Generator Mode](#package-generator-mode)
   - [What is Package Mode?](#what-is-package-mode)
   - [Creating Complete Flange Assemblies](#creating-complete-flange-assemblies)
   - [Output Structure](#output-structure)
5. [One-off Part Generator Mode](#one-off-part-generator-mode)
   - [Flanges](#flanges)
   - [Gaskets](#gaskets)
   - [Fasteners (Studs & Nuts)](#fasteners-studs--nuts)
   - [Pipe Fittings](#pipe-fittings)
   - [Pressure Vessels](#pressure-vessels)
   - [Steel Shapes](#steel-shapes)
   - [Lumber](#lumber)
   - [Rebar](#rebar)
6. [Flow Calculator Tab](#flow-calculator-tab)
   - [Fluid Properties Database](#fluid-properties-database)
   - [Pipe Sizing Calculations](#pipe-sizing-calculations)
   - [Bypass Mode](#bypass-mode)
   - [Fittings Estimator](#fittings-estimator)
7. [Supported Standards](#supported-standards)
   - [API Standards](#api-standards)
   - [ASME Standards](#asme-standards)
   - [AISC Standards](#aisc-standards)
8. [Output Files](#output-files)
   - [STEP File Format](#step-file-format)
   - [File Naming Conventions](#file-naming-conventions)
   - [Folder Structure](#folder-structure)
9. [Troubleshooting](#troubleshooting)
10. [Technical Reference](#technical-reference)
11. [Keyboard Shortcuts](#keyboard-shortcuts)
12. [FAQ](#faq)
13. [Support & Contact](#support--contact)

---

# Introduction

The Equation Paradise CAD Generator is a professional-grade parametric CAD file generator designed for engineers, designers, and fabricators working in the oil & gas, petrochemical, structural steel, and construction industries.

## Key Features

- **1,200+ Component Configurations** - Generate STEP files for flanges, fittings, fasteners, vessels, steel shapes, and more
- **Industry Standard Compliance** - API 6A, API 6BX, ASME B16.5, ASME B16.47, AISC, and other recognized standards
- **Package Generator** - Create complete flange assemblies with matching gaskets, studs, and nuts in one operation
- **Flow Calculator** - Built-in pipe sizing calculator with pressure drop calculations
- **Offline Generation** - All CAD files are generated locally on your computer
- **Universal STEP Format** - Compatible with all major CAD software (SolidWorks, Inventor, FreeCAD, Fusion 360, etc.)

## What's New in v1.3.0

- Cross-platform support (Windows, macOS, Linux)
- Pressure Vessel generator with multiple head types
- Steel shapes (W-beams, HSS, Channels, Angles)
- Dimensional and engineered lumber
- Rebar generator
- Enhanced Flow Calculator with 50+ fluid types
- Fittings pressure drop estimator
- Improved bypass mode with selectable flange class

---

# Getting Started

## System Requirements

### Windows
- Windows 10 or 11 (64-bit)
- 4 GB RAM minimum (8 GB recommended)
- 2 GB free disk space
- Internet connection for authentication

### macOS
- macOS 10.14 (Mojave) or later
- Apple Silicon (M1/M2/M3) or Intel
- 4 GB RAM minimum
- 2 GB free disk space

### Linux
- Ubuntu 20.04+, Debian 11+, Fedora 35+, or equivalent
- 4 GB RAM minimum
- 2 GB free disk space

## Installation

### Windows Installation

1. Download `EquationParadise_CAD_Setup_v1.3.0.exe` from [equationparadise.com/cad-downloads](https://equationparadise.com/cad-downloads.html)
2. Run the installer (no admin rights required)
3. The installer will:
   - Install Miniconda (if not present)
   - Create the `pyocc` Python environment
   - Install PythonOCC-Core from conda-forge
   - Copy generator scripts to `%USERPROFILE%\EquationParadise\scripts`
   - Create a desktop shortcut
4. Installation takes approximately 5-10 minutes depending on your internet speed

**Note:** Windows may show a SmartScreen warning because we don't use Microsoft code signing. Click "More info" then "Run anyway" to proceed.

### macOS Installation

1. Download `EquationParadise_CAD_Setup_macOS.sh`
2. Open Terminal and run:
   ```bash
   chmod +x ~/Downloads/EquationParadise_CAD_Setup_macOS.sh
   ~/Downloads/EquationParadise_CAD_Setup_macOS.sh
   ```
3. Follow the on-screen prompts
4. A desktop shortcut will be created

### Linux Installation

1. Download `EquationParadise_CAD_Setup_Linux.sh`
2. Open Terminal and run:
   ```bash
   chmod +x ~/Downloads/EquationParadise_CAD_Setup_Linux.sh
   ~/Downloads/EquationParadise_CAD_Setup_Linux.sh
   ```

## First Launch & Authentication

When you first launch the CAD Generator:

1. **Sign In Required** - You'll see the authentication window
2. Enter your **Equation Paradise account email and password**
3. Click **Sign In**

### Authentication Requirements

- Active Equation Paradise subscription required
- Your subscription status is verified with our servers
- Token is cached locally for 15-minute offline use
- Admin accounts have unlimited access

### Creating an Account

If you don't have an account:
1. Click **"Sign up at equationparadise.com"** in the login window
2. Create your account and select a subscription plan
3. Return to the CAD Generator and sign in

### Subscription Plans

| Plan | Price | Features |
|------|-------|----------|
| Grandfathered | $3/month | Early adopters - all features |
| Standard | $6/month | Full access to all generators |
| Student | $3/month | Academic discount with .edu email |

---

# User Interface Overview

## Main Window Layout

```
+--------------------------------------------------------------+
|  Equation Paradise CAD Generator v1.3.0                      |
+--------------------------------------------------------------+
|  [Package Generator] [One-off Part Generator] [Flow Calc]   |
+--------------------------------------------------------------+
|                                                              |
|                    Tab Content Area                          |
|                                                              |
+--------------------------------------------------------------+
|  [Help]  [Settings]                            [Status Bar]  |
+--------------------------------------------------------------+
```

## Navigation Tabs

### Package Generator Tab
Generate complete flange assemblies including:
- Two flanges (Weld Neck, Blind, or combination)
- Matching gasket
- Full stud bolt set
- Heavy hex nut set

### One-off Part Generator Tab
Generate individual components:
- Flanges (6 types across multiple standards)
- Gaskets (Full Face, Spiral Wound, Ring Joint)
- Studs and Nuts
- Pipe Fittings (Elbows, Tees, Reducers, etc.)
- Pressure Vessels
- Steel Shapes
- Lumber
- Rebar

### Flow Calculator Tab
- Select fluid type from 50+ options
- Input flow rate and conditions
- Calculate optimal pipe size
- Generate matched components

## Status Bar

Located at the bottom of the window:
- Shows current operation status
- Displays success/error messages
- Shows file paths when generating

---

# Package Generator Mode

## What is Package Mode?

Package Generator creates a **complete flange connection assembly** in a single operation. This is ideal for:
- Bill of Materials (BOM) creation
- Assembly drawings
- Procurement packages
- 3D model imports

## Creating Complete Flange Assemblies

### Step 1: Select Standard
Choose from:
- **API 6A/6BX** - Oil & gas wellhead/tree flanges (2K-20K PSI)
- **ASME B16.5** - Standard pipe flanges (Class 150-2500)
- **ASME B16.47 Series A** - Large diameter (MSS SP-44)
- **ASME B16.47 Series B** - Large diameter (API 605)

### Step 2: Select Size
- API: 4-1/16" to 30"
- ASME B16.5: 1/2" to 24"
- ASME B16.47: 26" to 60"

### Step 3: Select Pressure Class
| Standard | Available Classes |
|----------|------------------|
| API 6A/6BX | 2000, 3000, 5000, 10000, 15000, 20000 PSI |
| ASME B16.5 | 150, 300, 600, 900, 1500, 2500 |
| ASME B16.47 | 75, 150, 300, 400, 600, 900 |

### Step 4: Select Flange Types
- **Flange A** (Top/Left): Weld Neck, Blind, Slip-On, Socket Weld, Threaded, Lap Joint
- **Flange B** (Bottom/Right): Same options

Common combinations:
- Weld Neck + Weld Neck (pipe-to-pipe)
- Weld Neck + Blind (end cap)
- Weld Neck + Slip-On (lower cost option)

### Step 5: Select Facing
- **RF** (Raised Face) - Standard, serrated finish
- **RTJ** (Ring Type Joint) - Metal-to-metal seal for high pressure

### Step 6: Select Components
Check which components to include:
- [x] Flanges (always included)
- [x] Gasket
- [x] Studs
- [x] Nuts

### Step 7: Generate
Click **"Generate Package"** to create all files.

## Output Structure

```
FlowCalc_4in_Sch80_Class600_RF_20260112_143052/
    Flanges/
        WN_4in_Class600_RF_connA.step
        WN_4in_Class600_RF_connB.step
    Gaskets/
        Gasket_4in_Class600_conn01.step
    Fasteners/
        StudSet_4in_Class600_conn01.step
        NutSet_4in_Class600_conn01.step
    README.txt
```

---

# One-off Part Generator Mode

## Flanges

### Supported Flange Types

| Type | Description | Standards |
|------|-------------|-----------|
| **Weld Neck (WN)** | Full penetration butt weld, tapered hub | All |
| **Blind (BL)** | Solid disc for end closure | All |
| **Slip-On (SO)** | Slides over pipe, fillet welded | B16.5, B16.47 |
| **Socket Weld (SW)** | Pipe inserts into socket, fillet welded | B16.5 (4" and smaller) |
| **Threaded (TH)** | NPT threaded bore | B16.5 (4" and smaller) |
| **Lap Joint (LJ)** | Used with stub end, rotatable | B16.5 |

### API 6A/6BX Flanges

API flanges are used in wellhead and Christmas tree applications:

- **Type 6A** - Standard wellhead flanges
- **Type 6BX** - High-pressure flanges with BX ring groove

**BX Ring Groove Geometry:**
- 23 degree tapered walls
- Precise groove depth per API spec
- Type R and RX ring compatibility

**Sizes:** 4-1/16", 7-1/16", 9", 11", 13-5/8", 16-3/4", 21-1/4", 26-3/4", 30"

**Pressure Ratings:** 2,000 / 3,000 / 5,000 / 10,000 / 15,000 / 20,000 PSI

### ASME B16.5 Flanges

Standard pipe flanges for process piping:

**Sizes:** 1/2" through 24" NPS

**Pressure Classes:** 150, 300, 600, 900, 1500, 2500

**Temperature Ratings:** Based on material group (-20F to 1000F+)

### ASME B16.47 Flanges

Large diameter flanges:

**Series A (MSS SP-44):** Optimized for weight/strength
**Series B (API 605):** Heavier, more conservative design

**Sizes:** 26" through 60" NPS

## Gaskets

### Gasket Types

| Type | Description | Application |
|------|-------------|-------------|
| **Full Face** | Covers entire flange face including bolt holes | Class 150 flat face |
| **Flat Ring** | Covers raised face only | RF flanges, all classes |
| **Spiral Wound** | Metal/filler spiral with inner ring | High temperature, high pressure |
| **Ring Joint (R)** | Solid metal oval/octagonal | RTJ flanges |
| **Ring Joint (RX)** | Pressure-energized metal ring | High pressure RTJ |
| **Ring Joint (BX)** | API 6BX applications | API 6BX flanges |

### Gasket Parameters

- **NPS Size** - Nominal Pipe Size
- **Pressure Class** - Must match flange class
- **Material** - Graphite, PTFE, Spiral Wound, Metal

## Fasteners (Studs & Nuts)

### Stud Bolts

Generated per ASME B16.5 and API specifications:

- **Diameter** - Based on flange size and class
- **Length** - Calculated for proper engagement
- **Thread** - 8 UN series (coarse thread)
- **Quantity** - Per flange bolt pattern

### Heavy Hex Nuts

- **ASME B18.2.2** - Heavy hex dimensions
- **Quantity** - 2 per stud (one each end)
- **Across Flats** - Standard heavy hex sizing

## Pipe Fittings

### Available Fittings

| Fitting | Variations |
|---------|------------|
| **90 Degree Elbow** | Long radius, Short radius |
| **45 Degree Elbow** | Standard |
| **180 Degree Return** | Long radius |
| **Tee** | Equal, Reducing |
| **Reducer** | Concentric, Eccentric |
| **Cross** | Equal, Reducing |
| **Pipe** | Beveled ends, various schedules |

### Parameters

- **NPS Size** - 1/2" through 48"
- **Schedule** - 5, 10, 20, 30, STD, 40, 60, XS, 80, 100, 120, 140, 160, XXS
- **Material Spec** - A106 Gr B, A312 TP304, A312 TP316, etc.

## Pressure Vessels

### Vessel Configuration

Generate cylindrical pressure vessels with:

- **Shell Diameter** - ID or OD specification
- **Shell Length** - Tangent to tangent
- **Shell Thickness** - Based on design pressure
- **Head Types:**
  - Hemispherical (2:1 elliptical)
  - Elliptical (2:1 standard)
  - Torispherical (ASME F&D)
  - Flat

### Design Parameters

- **Design Pressure** - MAWP (PSI)
- **Design Temperature** - Degrees F
- **Material** - SA-516 Gr 70, SA-240 TP304, etc.
- **Corrosion Allowance** - Inches

## Steel Shapes

### AISC Shapes Database

| Shape | Description |
|-------|-------------|
| **W-Beams** | Wide flange beams (W4x13 through W44x335) |
| **HSS Round** | Hollow structural sections (HSS2.375x0.154 through HSS20x0.500) |
| **HSS Rectangular** | Rectangular tubes (HSS2x2x0.125 through HSS20x12x0.625) |
| **Channels** | C and MC shapes |
| **Angles** | Equal and unequal leg |

### Parameters

- **Shape Designation** - AISC naming convention
- **Length** - Specify member length
- **Material** - A992, A500 Gr B/C, A36

## Lumber

### Dimensional Lumber

Standard softwood lumber dimensions:
- **2x4** through **2x12**
- **4x4** through **4x12**
- **6x6** through **6x12**

**Actual vs Nominal:**
| Nominal | Actual |
|---------|--------|
| 2x4 | 1.5" x 3.5" |
| 2x6 | 1.5" x 5.5" |
| 2x8 | 1.5" x 7.25" |
| 4x4 | 3.5" x 3.5" |

### Engineered Lumber

- **LVL (Laminated Veneer Lumber)** - 1-3/4" x various depths
- **Glulam** - Glued laminated timber beams
- **PSL (Parallel Strand Lumber)** - High-strength beams
- **TJI (I-Joists)** - Engineered floor joists

## Rebar

### Reinforcing Bar Sizes

| Bar Size | Diameter | Area |
|----------|----------|------|
| #3 | 0.375" | 0.11 sq in |
| #4 | 0.500" | 0.20 sq in |
| #5 | 0.625" | 0.31 sq in |
| #6 | 0.750" | 0.44 sq in |
| #7 | 0.875" | 0.60 sq in |
| #8 | 1.000" | 0.79 sq in |
| #9 | 1.128" | 1.00 sq in |
| #10 | 1.270" | 1.27 sq in |
| #11 | 1.410" | 1.56 sq in |
| #14 | 1.693" | 2.25 sq in |
| #18 | 2.257" | 4.00 sq in |

---

# Flow Calculator Tab

## Overview

The Flow Calculator helps you:
1. Select the correct pipe size for your flow conditions
2. Verify velocity is within acceptable limits
3. Calculate pressure drop per 100 feet
4. Generate matched components

## Fluid Properties Database

### Included Fluids (50+ types)

**Water:**
- Fresh Water
- Salt Water (Seawater)
- Produced Water

**Crude Oils:**
- Light Crude (API 40)
- Medium Crude (API 30)
- Heavy Crude (API 20)
- Extra Heavy (API 10)

**Refined Products:**
- Gasoline
- Diesel
- Jet Fuel
- Kerosene

**Gases:**
- Natural Gas
- Air
- Nitrogen
- CO2
- Steam

**Chemicals:**
- Methanol
- Ethanol
- Ammonia
- Sulfuric Acid
- Caustic Soda

**Custom:**
- Enter custom density and viscosity

## Pipe Sizing Calculations

### Input Parameters

1. **Flow Rate** - GPM, BPD, SCFM, MMSCFD
2. **Fluid Type** - Select from database
3. **Temperature** - Operating temperature (F)
4. **Pressure** - Operating pressure (PSI)
5. **Max Velocity** - Design velocity limit (ft/s)

### Output

- **Recommended Pipe Size** - NPS with schedule
- **Actual Velocity** - At selected size
- **Pressure Drop** - PSI per 100 ft
- **Reynolds Number** - Flow regime indicator
- **Flange Class** - Required for operating conditions

### Velocity Guidelines

| Service | Recommended Velocity |
|---------|---------------------|
| Water (suction) | 2-4 ft/s |
| Water (discharge) | 4-10 ft/s |
| Oil | 3-6 ft/s |
| Gas | 30-60 ft/s |
| Steam (saturated) | 80-120 ft/s |
| Steam (superheated) | 150-200 ft/s |

## Bypass Mode

Use Bypass Mode when:
- You already know the pipe size you need
- You want to skip flow calculations
- You're generating for an existing design

### How to Use Bypass Mode

1. Check **"BYPASS MODE - Skip calculations, just generate"**
2. Select **NPS** from dropdown
3. Select **Schedule** from dropdown
4. Click **"Generate Selected Size"**
5. Proceed to component selection and generation

### Flange Class Selection in Bypass Mode

After clicking Generate:
1. The **Flange Class** dropdown becomes active
2. Select the required pressure class (150-2500)
3. A warning will display if class is inadequate for entered pressure
4. Flange type options update based on selected class

## Fittings Estimator

Quickly estimate additional pressure drop from fittings:

1. Enter quantities of each fitting type:
   - 90 Degree Elbows (Long Radius)
   - 90 Degree Elbows (Short Radius)
   - 45 Degree Elbows
   - Tees (Flow Through)
   - Tees (Branch Flow)
   - Gate Valves
   - Globe Valves
   - Check Valves
   - Ball Valves

2. Enter total pipe length (feet)

3. View calculated:
   - Total equivalent length
   - Total pressure drop

---

# Supported Standards

## API Standards

### API Specification 6A (21st Edition)
- Wellhead and Christmas tree equipment
- Flanges, connectors, and valves
- Pressure ratings: 2K, 3K, 5K, 10K, 15K, 20K
- Ring groove geometry (R, RX, BX)

### API Specification 6BX
- High-pressure wellhead flanges
- BX ring groove with 23 degree taper
- Enhanced fatigue resistance

## ASME Standards

### ASME B16.5 - Pipe Flanges and Flanged Fittings
- NPS 1/2 through 24
- Classes 150, 300, 600, 900, 1500, 2500
- Material groups for temperature ratings
- Bolt patterns and dimensions

### ASME B16.47 - Large Diameter Steel Flanges
- NPS 26 through 60
- Series A (MSS SP-44) and Series B (API 605)
- Classes 75, 150, 300, 400, 600, 900

### ASME B16.9 - Factory-Made Wrought Buttwelding Fittings
- Elbows, tees, reducers, caps
- Dimensional standards

### ASME B16.11 - Forged Fittings, Socket-Welding and Threaded
- Socket weld and threaded connections
- Class 2000, 3000, 6000, 9000

### ASME B18.2.2 - Nuts for General Applications
- Heavy hex nut dimensions
- Thread specifications

### ASME B1.1 - Unified Inch Screw Threads
- UN/UNC/UNF thread series
- Thread dimensions and tolerances

## AISC Standards

### AISC Steel Construction Manual (15th Edition)
- W-shapes (Wide Flange)
- HSS (Hollow Structural Sections)
- Channels (C, MC)
- Angles (L)
- Plates

---

# Output Files

## STEP File Format

All generated parts are saved as **STEP** files (ISO 10303-21):

- **Full Name:** Standard for the Exchange of Product Data
- **Extension:** .step or .stp
- **Standard:** ISO 10303-21
- **Version:** AP214 (Automotive Design) or AP203 (Configuration Controlled 3D Design)

### Compatibility

STEP files can be imported into:
- SolidWorks
- Autodesk Inventor
- Autodesk Fusion 360
- PTC Creo
- Siemens NX
- CATIA
- FreeCAD
- Onshape
- Rhino
- Blender (with add-on)

## File Naming Conventions

### Flanges
```
[Type]_[Size]_[Class]_[Facing].step
WN_4-1-16in_10000psi_RTJ.step
BLIND_6in_Class600_RF.step
```

### Gaskets
```
Gasket_[Type]_[Size]_[Class].step
Gasket_SpiralWound_4in_Class600.step
Gasket_RingJoint_BX156_10000psi.step
```

### Studs
```
Stud_[Diameter]x[Length]_[Thread].step
Stud_0.875x6.5_8UN.step
```

### Fittings
```
[Type]_[Size]_[Schedule]_[Spec].step
Elbow90LR_4in_Sch80_A106B.step
TeeEqual_6in_Sch40_A312-316.step
```

## Folder Structure

### Default Output Location

**Windows:** C:\Users\[Username]\EquationParadise\CAD\

**macOS/Linux:** ~/EquationParadise/CAD/

### Package Output Structure

```
[PackageName]_[Date]_[Time]/
    Flanges/
        [Flange files]
    Gaskets/
        [Gasket files]
    Fasteners/
        [Stud files]
        [Nut files]
    Fittings/
        [Fitting files]
    Valves/
        [Valve files]
    README.txt
```

---

# Troubleshooting

## Common Issues

### "Module not found" Error

**Problem:** Python cannot find a required module.

**Solution:**
1. Reinstall by running the installer again
2. The installer will repair missing files

### "Cannot connect to authentication server"

**Problem:** Network connectivity or server issue.

**Solutions:**
1. Check your internet connection
2. Try again in a few minutes
3. Check if equationparadise.com is accessible

### "Subscription expired"

**Problem:** Your subscription has lapsed.

**Solution:**
1. Visit equationparadise.com
2. Log into your account
3. Renew your subscription
4. Return to CAD Generator and sign in again

### Desktop Shortcut Doesn't Work

**Problem:** Clicking the shortcut does nothing.

**Solutions:**
1. Run the PowerShell installer again:
   ```
   cd C:\ParadiseSuite\scripts
   powershell -ExecutionPolicy Bypass -File install_pythonocc.ps1
   ```
2. Check if all script files exist in %USERPROFILE%\EquationParadise\scripts\

### STEP File Won't Open in CAD Software

**Problem:** Generated file cannot be imported.

**Solutions:**
1. Verify file is complete (check file size > 0 KB)
2. Try opening in FreeCAD (free, good STEP support)
3. Check for error messages in the status bar

### Slow Generation

**Problem:** Parts take a long time to generate.

**Notes:**
- First generation is always slower (JIT compilation)
- Large assemblies take longer
- Complex geometry (spiral wound gaskets) takes longer
- Normal time: 2-10 seconds per part

## Getting Help

If you encounter issues not covered here:

1. Email: support@equationparadise.com
2. Include:
   - Your operating system
   - CAD Generator version (shown in title bar)
   - Error message (if any)
   - What you were trying to do

---

# Technical Reference

## Dimensional Data Sources

All dimensions are sourced from official standards:

| Standard | Source |
|----------|--------|
| API 6A | API Spec 6A, 21st Edition |
| ASME B16.5 | ASME B16.5-2020 |
| ASME B16.47 | ASME B16.47-2020 |
| AISC Shapes | AISC Steel Construction Manual, 15th Edition |
| Pipe Schedules | ASME B36.10M / B36.19M |

## Coordinate System

All generated parts use:
- **Origin:** Center of part (flanges centered on bore axis)
- **Z-Axis:** Vertical (flange face normal)
- **Units:** Inches (internal), STEP file contains unit data

## Material Properties (Reference)

| Material | Density (lb/in3) | E (ksi) |
|----------|------------------|---------|
| Carbon Steel | 0.284 | 29,000 |
| 304 Stainless | 0.289 | 28,000 |
| 316 Stainless | 0.289 | 28,000 |
| Aluminum 6061 | 0.098 | 10,000 |

---

# Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Ctrl+G | Generate current selection |
| Ctrl+O | Open output folder |
| Ctrl+L | View generation log |
| F1 | Open this help guide |
| Escape | Cancel current operation |

---

# FAQ

## General Questions

**Q: Do I need CAD software to use the generator?**
A: You need CAD software to VIEW the generated files, but not to generate them. Free options include FreeCAD and Onshape.

**Q: Can I use generated parts commercially?**
A: Yes! Generated parts can be used in your projects, designs, and commercial work. See the LICENSE file for full terms.

**Q: Are the dimensions accurate?**
A: Yes, all dimensions are taken directly from official standards (API, ASME, AISC).

**Q: How often are new parts added?**
A: We release updates approximately monthly with new component types and sizes.

## Technical Questions

**Q: Why does the first generation take longer?**
A: PythonOCC uses Just-In-Time (JIT) compilation. The first run compiles OpenCASCADE kernels.

**Q: Can I generate parts offline?**
A: Yes, but you must authenticate online at least once every 15 minutes. After that, generation is fully offline.

**Q: What Python version is required?**
A: Python 3.11 is installed automatically with Miniconda.

**Q: Can I modify the generator scripts?**
A: The scripts are editable Python files. Advanced users can customize them, but we don't provide support for modified versions.

## Subscription Questions

**Q: What happens if my subscription expires?**
A: The CAD Generator will require you to renew before generating new parts. Previously generated files remain yours.

**Q: Can I cancel anytime?**
A: Yes, subscriptions can be canceled at any time from your account page.

**Q: Is there a free trial?**
A: Contact support@equationparadise.com for trial access.

---

# Support & Contact

## Contact Information

- **Email:** support@equationparadise.com
- **Website:** equationparadise.com
- **GitHub:** github.com/Offshore47/cad-setup

## Reporting Bugs

When reporting a bug, please include:
1. CAD Generator version (v1.3.0)
2. Operating system (Windows 11, macOS Sonoma, etc.)
3. Steps to reproduce the issue
4. Error message (if any)
5. Screenshot (if applicable)

## Feature Requests

We welcome suggestions! Email support@equationparadise.com with:
- Description of the feature
- Use case (why you need it)
- Any relevant standards or references

---

# Appendix A: Complete Size Tables

## API 6A/6BX Flange Sizes

| Size | OD (in) | ID (in) | Bolt Circle | # Bolts |
|------|---------|---------|-------------|---------|
| 4-1/16" | 11.00 | 4.062 | 8.50 | 8 |
| 7-1/16" | 15.50 | 7.062 | 12.50 | 12 |
| 9" | 18.50 | 9.000 | 15.00 | 12 |
| 11" | 22.50 | 11.000 | 18.50 | 12 |
| 13-5/8" | 27.00 | 13.625 | 22.50 | 16 |
| 16-3/4" | 31.00 | 16.750 | 26.50 | 16 |
| 21-1/4" | 37.00 | 21.250 | 32.00 | 20 |
| 26-3/4" | 45.00 | 26.750 | 40.00 | 24 |

## ASME B16.5 Flange Sizes

| NPS | Class 150 OD | Class 300 OD | Class 600 OD |
|-----|--------------|--------------|--------------|
| 1/2" | 3.50 | 3.75 | 3.75 |
| 1" | 4.25 | 4.88 | 4.88 |
| 2" | 6.00 | 6.50 | 6.50 |
| 4" | 9.00 | 10.00 | 10.75 |
| 6" | 11.00 | 12.50 | 14.00 |
| 8" | 13.50 | 15.00 | 16.50 |
| 10" | 16.00 | 17.50 | 20.00 |
| 12" | 19.00 | 20.50 | 22.00 |

## ASME B16.5 Stud Bolt Quantities

| NPS | Class 150 | Class 300 | Class 600 | Class 900 | Class 1500 | Class 2500 |
|-----|-----------|-----------|-----------|-----------|------------|------------|
| 1/2" | 4 | 4 | 4 | 4 | 4 | 4 |
| 1" | 4 | 4 | 4 | 4 | 4 | 4 |
| 2" | 4 | 8 | 8 | 8 | 8 | 8 |
| 4" | 8 | 8 | 8 | 8 | 8 | 8 |
| 6" | 8 | 12 | 12 | 12 | 12 | 12 |
| 8" | 8 | 12 | 12 | 12 | 12 | 12 |
| 10" | 12 | 16 | 16 | 16 | 12 | 12 |
| 12" | 12 | 16 | 20 | 20 | 12 | 12 |

## Pipe Schedule Wall Thickness (inches)

| NPS | Sch 40 | Sch 80 | Sch 160 | XXS |
|-----|--------|--------|---------|-----|
| 1" | 0.133 | 0.179 | 0.250 | 0.358 |
| 2" | 0.154 | 0.218 | 0.344 | 0.436 |
| 4" | 0.237 | 0.337 | 0.531 | 0.674 |
| 6" | 0.280 | 0.432 | 0.719 | 0.864 |
| 8" | 0.322 | 0.500 | 0.906 | 0.875 |
| 10" | 0.365 | 0.500 | 1.125 | 1.000 |
| 12" | 0.375 | 0.500 | 1.312 | 1.000 |

---

**Document Version:** 1.3.0
**Last Updated:** January 2026
**Copyright 2026 Equation Paradise. All rights reserved.**
