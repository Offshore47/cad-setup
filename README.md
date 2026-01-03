# Equation Paradise CAD Setup

One-click installer for the Equation Paradise CAD generator engine. Generate professional STEP files for oil & gas and structural components directly on your Windows desktop.

## 🚀 Quick Start

1. **Download** the latest release: [EquationParadise_CAD_Setup.exe](../../releases/latest/download/EquationParadise_CAD_Setup.exe)
2. **Run** the installer (takes ~5 minutes)
3. **Generate** parts at [equationparadise.com/cad](https://equationparadise.com/cad.html)

## 📦 What's Included

The installer sets up:
- **Python Environment** - Miniconda with pythonocc-core 7.9.0
- **CAD Generators** - Scripts for creating STEP files
- **Output Folder** - `%USERPROFILE%\EquationParadise\CAD`

## 🔧 Available Libraries

| Library | Status | Components |
|---------|--------|------------|
| **API 6A/6BX Flanges** | ✅ Ready | Weld Neck, Blind (2K-20K) |
| **ASME B16 Piping** | 🔜 Coming | Pipe, Elbows, Tees, Reducers |
| **AISC Steel Shapes** | 🔜 Coming | W, HSS, Channels, Angles |

## 🛢️ API 6BX Flange Specifications

Generated flanges conform to **API Specification 6A** (21st Edition):
- BX ring groove geometry with 23° tapered walls
- Weld neck flanges with standard bore and hub dimensions
- Blind flanges with E1/J4 back pockets (large sizes)
- Pressure classes: 2K, 3K, 5K, 10K, 15K, 20K
- Sizes: 4-1/16" through 30"

## 💻 System Requirements

- Windows 10 or 11 (64-bit)
- 1 GB free disk space
- Internet connection (for initial setup)
- No admin rights required

## 🔒 Security

- Downloads Python from official [Anaconda](https://www.anaconda.com/) servers
- Downloads pythonocc from [conda-forge](https://conda-forge.org/)
- Installs to user folder only (no system changes)
- No telemetry or data collection

## 📄 Output Format

All generated parts are saved as **STEP files** (ISO 10303-21), compatible with:
- FreeCAD
- SolidWorks
- Inventor
- Fusion 360
- Onshape
- Any CAD software supporting STEP import

## 🔗 Links

- [Equation Paradise](https://equationparadise.com)
- [CAD Library](https://equationparadise.com/cad.html)
- [Help & Documentation](https://equationparadise.com/help.html)

## 📝 Changelog

### v1.1.0 (January 2026)
- Fixeds Bugs for certain errors when generating flanges or Blinds of certain Sizes
- API 6A/6BX Weld Neck and Blind flanges
- 24 flange configurations (6 pressure classes × 4 sizes)

---

*Powered by [PythonOCC](https://github.com/tpaviot/pythonocc-core) and [Open CASCADE Technology](https://www.opencascade.com/)*
