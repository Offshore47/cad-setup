#!/bin/bash
# ============================================================
# Equation Paradise CAD Generator Setup (macOS & Linux)
# Version 1.3.0
# ============================================================

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Functions for colored output
print_status() { echo -e "${BLUE}[*]${NC} $1"; }
print_success() { echo -e "${GREEN}[✓]${NC} $1"; }
print_warning() { echo -e "${YELLOW}[!]${NC} $1"; }
print_error() { echo -e "${RED}[✗]${NC} $1"; }

echo ""
echo -e "${CYAN}============================================================${NC}"
echo -e "${CYAN}  Equation Paradise CAD Generator Setup${NC}"
echo -e "${CYAN}  Version 1.3.0${NC}"
echo -e "${CYAN}============================================================${NC}"
echo ""

# ============================================================
# Detect OS and Architecture
# ============================================================
print_status "Detecting system..."

OS="$(uname -s)"
ARCH="$(uname -m)"

case "$OS" in
    Linux*)
        PLATFORM="Linux"
        MINICONDA_OS="Linux"
        SHORTCUT_DIR="$HOME/.local/share/applications"
        ICON_DIR="$HOME/.local/share/icons"
        ;;
    Darwin*)
        PLATFORM="macOS"
        MINICONDA_OS="MacOSX"
        SHORTCUT_DIR="$HOME/Applications"
        ICON_DIR="$HOME/.local/share/icons"
        ;;
    *)
        print_error "Unsupported operating system: $OS"
        exit 1
        ;;
esac

case "$ARCH" in
    x86_64|amd64)
        MINICONDA_ARCH="x86_64"
        ;;
    arm64|aarch64)
        MINICONDA_ARCH="arm64"
        ;;
    *)
        print_error "Unsupported architecture: $ARCH"
        exit 1
        ;;
esac

print_success "Detected: $PLATFORM ($ARCH)"

# ============================================================
# Configuration
# ============================================================
INSTALL_DIR="$HOME/EquationParadise"
SCRIPTS_DIR="$INSTALL_DIR/scripts"
OUTPUT_DIR="$INSTALL_DIR/CAD_Output"
MINICONDA_DIR="$INSTALL_DIR/miniconda"
ENV_NAME="pyocc"

MINICONDA_URL="https://repo.anaconda.com/miniconda/Miniconda3-latest-${MINICONDA_OS}-${MINICONDA_ARCH}.sh"
MINICONDA_INSTALLER="/tmp/miniconda_installer.sh"

# ============================================================
# Step 1: Create Directories
# ============================================================
print_status "Creating directories..."

mkdir -p "$INSTALL_DIR"
mkdir -p "$SCRIPTS_DIR"
mkdir -p "$OUTPUT_DIR"
mkdir -p "$SHORTCUT_DIR"
mkdir -p "$ICON_DIR"

print_success "Directories created at $INSTALL_DIR"

# ============================================================
# Step 2: Download and Install Miniconda
# ============================================================
if [ -d "$MINICONDA_DIR" ]; then
    print_warning "Miniconda already installed, skipping..."
else
    print_status "Downloading Miniconda..."
    
    if command -v curl &> /dev/null; then
        curl -fsSL "$MINICONDA_URL" -o "$MINICONDA_INSTALLER"
    elif command -v wget &> /dev/null; then
        wget -q "$MINICONDA_URL" -O "$MINICONDA_INSTALLER"
    else
        print_error "Neither curl nor wget found. Please install one of them."
        exit 1
    fi
    
    print_success "Miniconda downloaded"
    
    print_status "Installing Miniconda (this may take a few minutes)..."
    bash "$MINICONDA_INSTALLER" -b -p "$MINICONDA_DIR"
    rm -f "$MINICONDA_INSTALLER"
    
    print_success "Miniconda installed"
fi

# ============================================================
# Step 3: Create Conda Environment with PythonOCC
# ============================================================
CONDA_EXE="$MINICONDA_DIR/bin/conda"

# Check if environment exists
if "$CONDA_EXE" env list | grep -q "^$ENV_NAME "; then
    print_warning "Environment '$ENV_NAME' already exists, skipping creation..."
else
    print_status "Creating conda environment '$ENV_NAME' with Python 3.11..."
    "$CONDA_EXE" create -n "$ENV_NAME" python=3.11 -y -q
    print_success "Environment created"
fi

# Install PythonOCC
print_status "Installing PythonOCC-Core (this may take several minutes)..."
"$CONDA_EXE" install -n "$ENV_NAME" -c conda-forge pythonocc-core requests pillow -y -q
print_success "PythonOCC-Core installed"

# ============================================================
# Step 4: Download Generator Scripts from GitHub
# ============================================================
print_status "Downloading generator scripts from GitHub..."

GITHUB_RAW="https://raw.githubusercontent.com/Offshore47/cad-setup/main"

SCRIPTS_TO_DOWNLOAD=(
    "cad_generator_gui_v1.3.0.py"
    "cad_auth.py"
    "cad_updater.py"
    "flange_data.py"
    "heavy_hex_nut_data.py"
    "asme_b165_stud_data.py"
    "api_6b_stud_data.py"
    "api_6bx_stud_data.py"
    "gasket_data.py"
    "generate_all_flanges_test.py"
    "generate_api_flange_v5.py"
    "generate_api_flange.py"
    "generate_beveled_pipe.py"
    "generate_cross.py"
    "generate_elbow.py"
    "generate_reducer.py"
    "generate_tee.py"
    "generate_hex_nut.py"
    "generate_stud.py"
    "generate_gasket.py"
    "generate_ring_joint.py"
    "generate_180_return.py"
    "generate_pressure_vessel.py"
    "generate_steel_shapes.py"
    "generate_dimensional_lumber.py"
    "generate_lvl.py"
    "generate_glulam.py"
    "generate_psl.py"
    "generate_tji.py"
    "generate_cfs_framing.py"
    "generate_rebar.py"
    "generate_sheet_steel.py"
    "generate_slip_on_flange.py"
    "generate_socket_weld_flange.py"
    "generate_threaded_flange.py"
    "generate_lap_joint_flange.py"
    "generate_pipe.py"
    "flow_calculator_enhanced.py"
    "CAD_GENERATOR_USER_GUIDE.md"
    "cadgen.png"
)

download_file() {
    local filename="$1"
    local url="$GITHUB_RAW/$filename"
    local dest="$SCRIPTS_DIR/$filename"
    
    if command -v curl &> /dev/null; then
        curl -fsSL "$url" -o "$dest" 2>/dev/null
    elif command -v wget &> /dev/null; then
        wget -q "$url" -O "$dest" 2>/dev/null
    fi
    
    if [ -f "$dest" ]; then
        print_success "Downloaded $filename"
        return 0
    else
        print_warning "Could not download $filename"
        return 1
    fi
}

for script in "${SCRIPTS_TO_DOWNLOAD[@]}"; do
    download_file "$script"
done

# ============================================================
# Step 5: Verify Installation
# ============================================================
print_status "Verifying PythonOCC installation..."

PYTHON_EXE="$MINICONDA_DIR/envs/$ENV_NAME/bin/python"

if "$PYTHON_EXE" -c "from OCC.Core.gp import gp_Pnt; print('OK')" 2>/dev/null | grep -q "OK"; then
    print_success "PythonOCC is working correctly!"
else
    print_error "PythonOCC verification failed"
    exit 1
fi

# ============================================================
# Step 6: Create Desktop Shortcut / Application Launcher
# ============================================================
print_status "Creating application launcher..."

GUI_SCRIPT="$SCRIPTS_DIR/cad_generator_gui_v1.3.0.py"
ICON_PATH="$SCRIPTS_DIR/cadgen.png"

if [ "$PLATFORM" = "Linux" ]; then
    # Linux: Create .desktop file
    DESKTOP_FILE="$SHORTCUT_DIR/equationparadise-cad.desktop"
    
    cat > "$DESKTOP_FILE" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=EquationParadise CAD Generator
Comment=Generate STEP files for flanges, fittings, and fasteners
Exec=$PYTHON_EXE "$GUI_SCRIPT"
Icon=$ICON_PATH
Terminal=false
Categories=Engineering;Graphics;Science;
StartupNotify=true
EOF
    
    chmod +x "$DESKTOP_FILE"
    
    # Also copy to desktop if it exists
    if [ -d "$HOME/Desktop" ]; then
        cp "$DESKTOP_FILE" "$HOME/Desktop/"
        chmod +x "$HOME/Desktop/equationparadise-cad.desktop"
        # Mark as trusted on GNOME
        if command -v gio &> /dev/null; then
            gio set "$HOME/Desktop/equationparadise-cad.desktop" metadata::trusted true 2>/dev/null || true
        fi
    fi
    
    # Update desktop database
    if command -v update-desktop-database &> /dev/null; then
        update-desktop-database "$SHORTCUT_DIR" 2>/dev/null || true
    fi
    
    print_success "Desktop launcher created"
    
elif [ "$PLATFORM" = "macOS" ]; then
    # macOS: Create .app bundle
    APP_DIR="$SHORTCUT_DIR/EquationParadise CAD Generator.app"
    CONTENTS_DIR="$APP_DIR/Contents"
    MACOS_DIR="$CONTENTS_DIR/MacOS"
    RESOURCES_DIR="$CONTENTS_DIR/Resources"
    
    mkdir -p "$MACOS_DIR"
    mkdir -p "$RESOURCES_DIR"
    
    # Create launcher script
    cat > "$MACOS_DIR/launch.sh" << EOF
#!/bin/bash
"$PYTHON_EXE" "$GUI_SCRIPT"
EOF
    chmod +x "$MACOS_DIR/launch.sh"
    
    # Create Info.plist
    cat > "$CONTENTS_DIR/Info.plist" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleExecutable</key>
    <string>launch.sh</string>
    <key>CFBundleIconFile</key>
    <string>cadgen.icns</string>
    <key>CFBundleIdentifier</key>
    <string>com.equationparadise.cadgenerator</string>
    <key>CFBundleName</key>
    <string>EquationParadise CAD Generator</string>
    <key>CFBundleVersion</key>
    <string>1.3.0</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
</dict>
</plist>
EOF
    
    # Copy icon (convert if needed, or use PNG as fallback)
    if [ -f "$ICON_PATH" ]; then
        cp "$ICON_PATH" "$RESOURCES_DIR/cadgen.png"
    fi
    
    # Also create alias on Desktop
    if [ -d "$HOME/Desktop" ]; then
        ln -sf "$APP_DIR" "$HOME/Desktop/EquationParadise CAD Generator"
    fi
    
    print_success "macOS application bundle created"
fi

# ============================================================
# Create command-line launcher
# ============================================================
print_status "Creating command-line launcher..."

LAUNCHER_SCRIPT="$INSTALL_DIR/cadgen"
cat > "$LAUNCHER_SCRIPT" << EOF
#!/bin/bash
# EquationParadise CAD Generator launcher
"$PYTHON_EXE" "$GUI_SCRIPT" "\$@"
EOF
chmod +x "$LAUNCHER_SCRIPT"

# Add to PATH suggestion
print_success "Command-line launcher created at $LAUNCHER_SCRIPT"

# ============================================================
# Complete!
# ============================================================
echo ""
echo -e "${GREEN}============================================================${NC}"
echo -e "${GREEN}  Equation Paradise CAD Setup Complete!${NC}"
echo -e "${GREEN}============================================================${NC}"
echo ""
echo -e "  Python environment: ${CYAN}$MINICONDA_DIR/envs/$ENV_NAME${NC}"
echo -e "  CAD output folder:  ${CYAN}$OUTPUT_DIR${NC}"
echo -e "  Generator scripts:  ${CYAN}$SCRIPTS_DIR${NC}"
echo ""

if [ "$PLATFORM" = "Linux" ]; then
    echo -e "  ${YELLOW}To launch:${NC}"
    echo -e "    • Click 'EquationParadise CAD Generator' in your applications menu"
    echo -e "    • Or double-click the desktop icon"
    echo -e "    • Or run: ${CYAN}$LAUNCHER_SCRIPT${NC}"
elif [ "$PLATFORM" = "macOS" ]; then
    echo -e "  ${YELLOW}To launch:${NC}"
    echo -e "    • Open 'EquationParadise CAD Generator' from ~/Applications"
    echo -e "    • Or double-click the desktop alias"
    echo -e "    • Or run: ${CYAN}$LAUNCHER_SCRIPT${NC}"
fi

echo ""
echo -e "  ${YELLOW}Optional:${NC} Add to PATH for easy command-line access:"
echo -e "    echo 'export PATH=\"\$HOME/EquationParadise:\$PATH\"' >> ~/.bashrc"
echo ""

exit 0
