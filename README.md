# Equation Paradise

**The Complete Engineering Toolkit** — CAD generators, engineering calculators, material databases, and reference tables for STEM students and professionals.

🌐 **Website:** [equationparadise.com](https://equationparadise.com)

---

## 🚀 Quick Start — CAD Generator

### Windows
1. Download: [EquationParadise_CAD_Setup.exe](../../releases/latest/download/EquationParadise_CAD_Setup.exe)
2. Run the installer (~5 minutes)
3. Launch from desktop shortcut

### macOS
1. Download: [EquationParadise_CAD_Setup_macOS.sh](../../releases/latest/download/EquationParadise_CAD_Setup_macOS.sh)
2. Run in Terminal:
   ```bash
   chmod +x ~/Downloads/EquationParadise_CAD_Setup_macOS.sh
   ~/Downloads/EquationParadise_CAD_Setup_macOS.sh
   ```

### Linux
1. Download: [EquationParadise_CAD_Setup_Linux.sh](../../releases/latest/download/EquationParadise_CAD_Setup_Linux.sh)
2. Run in Terminal:
   ```bash
   chmod +x ~/Downloads/EquationParadise_CAD_Setup_Linux.sh
   ~/Downloads/EquationParadise_CAD_Setup_Linux.sh
   ```

---

## 📦 What's Included

### CAD Generator (Desktop App)
Generate industry-standard **STEP files** for:

| Category | Components |
|----------|------------|
| **Flanges** | API 6A/6BX (2K-20K), ASME B16.5 (150-2500), ASME B16.47 Series A & B (26"-60") |
| **Flange Types** | Weld Neck, Blind, Slip-On, Socket Weld, Threaded, Lap Joint, RTJ |
| **Fasteners** | Heavy Hex Nuts (H/2H with washer face), Stud Bolts (B16.5, API 6B, API 6BX) |
| **Gaskets** | Full Face, Flat Ring, Spiral Wound, Ring Joint Type R & RX |
| **Piping** | Pipe, 90°/45° Elbows, 180° Returns, Tees (Equal/Reducing), Reducers (Con/Ecc), Crosses |
| **Pressure Vessels** | Hemispherical, Elliptical, Torispherical, and Flat heads |
| **Steel Shapes** | AISC W-Beams, HSS Round, HSS Rectangular, Channels, Angles (2,301 shapes) |
| **Lumber** | Dimensional (2x4 through 12x12), Engineered (LVL, Glulam, PSL, TJI) |
| **Steel Framing** | Cold-Formed Steel studs, tracks, joists |
| **Rebar** | Standard reinforcement bars #3 through #18 |
| **Sheet Steel** | Various gauges and sizes |

**Tools:**
- **Assembly Package Generator** — Complete flange assemblies (flange + gasket + studs + nuts) in one click
- **Flow Calculator** — Pipe flow calculations with friction factors

### Web Platform (equationparadise.com)

| Feature | Description |
|---------|-------------|
| **36 Engineering Calculators** | Beam analysis, pipe flow, pressure drop, unit conversions, and more |
| **Material Properties** | Steel, aluminum, stainless, copper, plastics — yield strength, modulus, density |
| **Pipe Schedules** | Complete NPS tables with ID, OD, wall thickness, weights |
| **Steel Shape Tables** | AISC W-Beams, HSS, Channels, Angles — all properties |
| **Lumber Tables** | Dimensional lumber sizes, engineered wood specs |
| **Concrete & Rebar** | Rebar sizes, concrete mix data, reinforcement tables |
| **Fastener Data** | Bolt dimensions, torque specs, thread pitches |

---

## 💻 System Requirements

| Platform | Requirements |
|----------|--------------|
| **Windows** | Windows 10/11 (64-bit) |
| **macOS** | macOS 10.15+ (Intel or Apple Silicon) |
| **Linux** | Any distro with bash (Ubuntu, Debian, Fedora, Arch, etc.) |
| **All** | 1 GB disk space, Internet for setup, Equation Paradise subscription |

---

## 📄 Output Format

All CAD files are saved as **STEP files** (ISO 10303-21), compatible with:
- FreeCAD, SolidWorks, Inventor, Fusion 360, Onshape, CATIA, NX, Creo
- Any CAD software supporting STEP import

---

## 🗺️ Roadmap

| Planned | Components |
|---------|------------|
| **Specialty Flanges** | Spectacle Blinds, Paddle Blinds, Bleed Rings, Orifice Flanges |
| **Branch Connections** | Weldolets, Sockolets, Threadolets, Latrolets, Elbolets |
| **Reinforcing Pads** | Repads for branch connections per ASME B31.3 |

| Not Planned | Reason |
|-------------|--------|
| **Valves** | Manufacturer-specific dimensions; generic placeholders available for layout |

---

## 💰 Pricing

Early adopter pricing (locked in as long as you stay subscribed):

| Tier | Monthly | Annual |
|------|---------|--------|
| First 1,000 users | $3/mo | $30/yr |
| 1,001 - 2,000 | $4/mo | $40/yr |
| 2,001 - 3,000 | $5/mo | $50/yr |
| 3,001+ | $6/mo | $60/yr |

*If your subscription lapses, you'll rejoin at the current tier price.*

---

## 📝 Changelog

### v1.3.0 (January 2026)

**🌐 Cross-Platform Support**
- NEW: macOS installer (Intel & Apple Silicon)
- NEW: Linux installer (all major distros)
- Desktop shortcuts with custom icon

**🔩 Flanges**
- NEW: ASME B16.5 — Weld Neck, Blind, Slip-On, Socket Weld, Threaded, Lap Joint (Class 150-2500)
- NEW: ASME B16.47 Series A — Large diameter 26"-60" (Class 150-900)
- NEW: ASME B16.47 Series B — Large diameter 26"-60" (Class 150-900)
- IMPROVED: API 6A/6BX generation stability

**🔧 Fasteners**
- NEW: Heavy Hex Nuts — Standard and 2H types with integral washer face (78 configurations)
- NEW: Stud Bolts — ASME B16.5, API 6B, API 6BX (273 configurations)

**⭕ Gaskets**
- NEW: Full Face gaskets
- NEW: Flat Ring gaskets
- NEW: Spiral Wound gaskets with inner/outer rings (651 configurations)
- NEW: Ring Joint Type R — Octagonal and oval profiles
- NEW: Ring Joint Type RX — With pressure balance holes (135 configurations)

**🔌 Piping**
- NEW: Pipe with beveled ends (all schedules)
- NEW: 90° Elbows — Short and Long radius
- NEW: 45° Elbows — Long radius
- NEW: 180° Returns — Short and Long radius
- NEW: Tees — Equal and Reducing
- NEW: Reducers — Concentric and Eccentric
- NEW: Crosses — Equal

**🛢️ Pressure Vessels**
- NEW: Hemispherical heads
- NEW: Elliptical heads (ASME 2:1)
- NEW: Torispherical heads (ASME F&D)
- NEW: Flat heads with corner radius

**🏗️ Structural**
- NEW: AISC Steel Shapes — W-Beams, HSS Round, HSS Rectangular, Channels, Angles (2,301 shapes)
- NEW: Dimensional Lumber — 2x4 through 12x12
- NEW: Engineered Lumber — LVL, Glulam, PSL, TJI
- NEW: Cold-Formed Steel Framing — Studs, Tracks, Joists
- NEW: Rebar — #3 through #18
- NEW: Sheet Steel — Various gauges

**🛠️ Tools**
- NEW: Assembly Package Generator — Complete flange assemblies in one click
- NEW: Flow Calculator — Integrated pipe flow calculations

**Total: 5,000+ component configurations**

---

### v1.1.0 (January 2026)
- Fixed bugs for certain flange and blind sizes
- Improved API 6A/6BX generator stability

### v1.0.0 (January 2026)
- Initial release
- API 6A/6BX Weld Neck and Blind flanges

---

## 🔒 Security

- Python downloaded from official [Anaconda](https://www.anaconda.com/) servers
- PythonOCC from [conda-forge](https://conda-forge.org/)
- Installs to user folder only (no system changes)
- No telemetry or data collection

---

## 📄 License

**Software:** MIT License

**Generated CAD Files:** You may use generated STEP files freely in your projects, designs, and products. You may NOT sell or redistribute the generated files as standalone assets.

---

## 🔗 Links

- **Website:** [equationparadise.com](https://equationparadise.com)
- **CAD Generator:** [equationparadise.com/cad](https://equationparadise.com/cad.html)
- **Workspace:** [equationparadise.com/workspace](https://equationparadise.com/workspace.html)
- **Help:** [equationparadise.com/help](https://equationparadise.com/help.html)

---

*Powered by [PythonOCC](https://github.com/tpaviot/pythonocc-core) and [Open CASCADE Technology](https://www.opencascade.com/)*
