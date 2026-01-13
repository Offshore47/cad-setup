# ============================================================
# Equation Paradise - CAD Parts Generator v1.3.2
# Multi-component generator with authentication
# Added: 180° Returns, Pressure Vessels, Valve Placeholders
# ============================================================

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
import sys
import threading
import time
import json
import requests
from datetime import datetime, timedelta
from pathlib import Path

# Import authentication module
from cad_auth import require_authentication, AuthManager

# Import enhanced flow calculator
from flow_calculator_enhanced import (
    FluidProperties, PipeData, FlowCalculator,
    convert_flow_to_gpm, convert_pressure_to_psi
)

# Version and Update Checking
VERSION = "v1.3.0"
UPDATE_CHECK_URL = "https://equationparadise.com/api/cad/version"
LATEST_VERSION = VERSION
UPDATE_AVAILABLE = False

# Config file for storing library path
CONFIG_FILE = Path.home() / ".equationparadise" / "cad_config.json"

# Build lookups for ALL flanges (API 6BX + ASME B16.5)
FLANGE_STANDARDS = {}  # standard -> {size -> [pressures]}
ALL_FLANGE_SIZES = set()

# GitHub raw URL for downloading updates
GITHUB_RAW_URL = "https://raw.githubusercontent.com/Offshore47/cad-setup/main"

# List of all scripts that should be kept up to date
UPDATABLE_SCRIPTS = [
    "cad_generator_gui_v1.3.0.py",
    "cad_auth.py",
    "cad_updater.py",
    "flange_data.py",
    "heavy_hex_nut_data.py",
    "asme_b165_stud_data.py",
    "api_6b_stud_data.py",
    "api_6bx_stud_data.py",
    "gasket_data.py",
    "generate_all_flanges_test.py",
    "generate_api_flange_v5.py",
    "generate_api_flange.py",
    "generate_beveled_pipe.py",
    "generate_cross.py",
    "generate_elbow.py",
    "generate_reducer.py",
    "generate_tee.py",
    "generate_hex_nut.py",
    "generate_stud.py",
    "generate_gasket.py",
    "generate_ring_joint.py",
    "generate_180_return.py",
    "generate_pressure_vessel.py",
    "generate_steel_shapes.py",
    "generate_dimensional_lumber.py",
    "generate_lvl.py",
    "generate_glulam.py",
    "generate_psl.py",
    "generate_tji.py",
    "generate_cfs_framing.py",
    "generate_rebar.py",
    "generate_sheet_steel.py",
    "generate_slip_on_flange.py",
    "generate_socket_weld_flange.py",
    "generate_threaded_flange.py",
    "generate_lap_joint_flange.py",
    "generate_pipe.py",
    "flow_calculator_enhanced.py",
    "CAD_GENERATOR_USER_GUIDE.md"
]

def silent_auto_update():
    """
    Silently check for updates and automatically download/install them.
    Runs on startup before the GUI loads.
    Returns True if app was updated and needs restart, False otherwise.
    """
    global LATEST_VERSION, UPDATE_AVAILABLE
    
    scripts_dir = os.path.dirname(os.path.abspath(__file__))
    
    try:
        # Check for updates from API
        response = requests.get(UPDATE_CHECK_URL, timeout=5)
        if response.status_code != 200:
            print(f"Update check failed: HTTP {response.status_code}")
            return False
        
        data = response.json()
        LATEST_VERSION = data.get('version', VERSION)
        download_url = data.get('download_url', GITHUB_RAW_URL)
        scripts_list = data.get('scripts', UPDATABLE_SCRIPTS)
        
        # Compare versions (strip 'v' prefix for comparison)
        local_ver = VERSION.lstrip('v').split('.')
        remote_ver = LATEST_VERSION.lstrip('v').split('.')
        
        # Convert to integers for proper comparison
        try:
            local_nums = [int(x) for x in local_ver]
            remote_nums = [int(x) for x in remote_ver]
        except ValueError:
            # If version parsing fails, skip update
            return False
        
        # Check if remote is newer
        needs_update = False
        for i in range(max(len(local_nums), len(remote_nums))):
            local_n = local_nums[i] if i < len(local_nums) else 0
            remote_n = remote_nums[i] if i < len(remote_nums) else 0
            if remote_n > local_n:
                needs_update = True
                break
            elif remote_n < local_n:
                break
        
        if not needs_update:
            print(f"CAD Generator is up to date (v{VERSION})")
            return False
        
        UPDATE_AVAILABLE = True
        print(f"Updating CAD Generator: {VERSION} -> {LATEST_VERSION}")
        
        # Download and update each script
        updated_count = 0
        failed_count = 0
        
        for script_name in scripts_list:
            try:
                script_url = f"{download_url}/{script_name}"
                script_path = os.path.join(scripts_dir, script_name)
                
                # Download the file
                resp = requests.get(script_url, timeout=30)
                if resp.status_code == 200:
                    # Write to a temp file first, then rename (atomic operation)
                    temp_path = script_path + ".tmp"
                    with open(temp_path, 'wb') as f:
                        f.write(resp.content)
                    
                    # Replace the original file
                    if os.path.exists(script_path):
                        os.remove(script_path)
                    os.rename(temp_path, script_path)
                    
                    updated_count += 1
                    print(f"  Updated: {script_name}")
                else:
                    print(f"  Skipped (not found): {script_name}")
            except Exception as e:
                failed_count += 1
                print(f"  Failed: {script_name} - {e}")
        
        print(f"Update complete: {updated_count} files updated, {failed_count} failed")
        
        # If we updated the main GUI script, we need to restart
        if "cad_generator_gui" in str(scripts_list) and updated_count > 0:
            return True
        
        return False
        
    except requests.exceptions.RequestException as e:
        print(f"Update check failed (network): {e}")
        return False
    except Exception as e:
        print(f"Update check failed: {e}")
        return False

def check_for_updates():
    """Legacy function - now calls silent_auto_update"""
    return silent_auto_update()

def build_complete_flange_lookup():
    """Build lookup table for ALL flanges: API 6BX and ASME B16.5."""
    global FLANGE_STANDARDS, ALL_FLANGE_SIZES
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    if script_dir not in sys.path:
        sys.path.insert(0, script_dir)
    
    try:
        # API 6BX flanges
        import generate_all_flanges_test as api_gen
        api_sizes = {}
        for pressure, sizes_dict in api_gen.ALL_PRESSURE_CLASSES.items():
            for size in sizes_dict.keys():
                if size not in api_sizes:
                    api_sizes[size] = []
                api_sizes[size].append(pressure)
                ALL_FLANGE_SIZES.add(size)
        
        # Sort API pressure classes
        pressure_order = ["2K", "3K", "5K", "10K", "15K", "20K"]
        for size in api_sizes:
            api_sizes[size] = sorted(api_sizes[size], 
                                     key=lambda x: pressure_order.index(x) if x in pressure_order else 99)
        
        FLANGE_STANDARDS['API_6BX'] = api_sizes
        
        # ASME B16.5 flanges
        import flange_data as asme_data
        asme_classes = {
            '150': asme_data.CLASS_150_RF_WN,
            '300': asme_data.CLASS_300_RF_WN,
            '400': asme_data.CLASS_400_RF_WN,
            '600': asme_data.CLASS_600_RF_WN,
            '900': asme_data.CLASS_900_RF_WN,
            '1500': asme_data.CLASS_1500_RF_WN,
            '2500': asme_data.CLASS_2500_RF_WN,
        }
        
        asme_sizes = {}
        for pressure_class, sizes_dict in asme_classes.items():
            for size in sizes_dict.keys():
                if size not in asme_sizes:
                    asme_sizes[size] = []
                asme_sizes[size].append(pressure_class)
                ALL_FLANGE_SIZES.add(size)
        
        # Sort ASME pressure classes
        class_order = ['150', '300', '400', '600', '900', '1500', '2500']
        for size in asme_sizes:
            asme_sizes[size] = sorted(asme_sizes[size],
                                     key=lambda x: class_order.index(x) if x in class_order else 99)
        
        FLANGE_STANDARDS['ASME_B16_5'] = asme_sizes
        
        # ASME B16.47 Series A flanges (26"-60")
        b1647a_classes = {
            '150': asme_data.B1647_SERIES_A_RF_WN,
            '300': asme_data.B1647_SERIES_A_CLASS300_RF_WN,
            '600': asme_data.B1647_SERIES_A_CLASS600_RF_WN,
            '900': asme_data.B1647_SERIES_A_CLASS900_RF_WN,
        }
        
        b1647a_sizes = {}
        for pressure_class, sizes_dict in b1647a_classes.items():
            for size in sizes_dict.keys():
                if size not in b1647a_sizes:
                    b1647a_sizes[size] = []
                b1647a_sizes[size].append(pressure_class)
                ALL_FLANGE_SIZES.add(size)
        
        # Sort pressure classes
        for size in b1647a_sizes:
            b1647a_sizes[size] = sorted(b1647a_sizes[size],
                                        key=lambda x: class_order.index(x) if x in class_order else 99)
        
        FLANGE_STANDARDS['ASME_B16_47A'] = b1647a_sizes
        
        # ASME B16.47 Series B flanges (26"-60")
        b1647b_classes = {
            '150': asme_data.B1647_SERIES_B_RF_WN,
            '300': asme_data.B1647_SERIES_B_CLASS300_RF_WN,
            '600': asme_data.B1647_SERIES_B_CLASS600_RF_WN,
            '900': asme_data.B1647_SERIES_B_CLASS900_RF_WN,
        }
        
        b1647b_sizes = {}
        for pressure_class, sizes_dict in b1647b_classes.items():
            for size in sizes_dict.keys():
                if size not in b1647b_sizes:
                    b1647b_sizes[size] = []
                b1647b_sizes[size].append(pressure_class)
                ALL_FLANGE_SIZES.add(size)
        
        # Sort pressure classes
        for size in b1647b_sizes:
            b1647b_sizes[size] = sorted(b1647b_sizes[size],
                                        key=lambda x: class_order.index(x) if x in class_order else 99)
        
        FLANGE_STANDARDS['ASME_B16_47B'] = b1647b_sizes
        
    except Exception as e:
        print(f"Error loading flange data: {e}")
        FLANGE_STANDARDS = {'API_6BX': {}, 'ASME_B16_5': {}, 'ASME_B16_47A': {}, 'ASME_B16_47B': {}}


class CADGeneratorApp:
    def __init__(self, root, auth_manager):
        self.root = root
        self.auth_manager = auth_manager
        self.root.title(f"Equation Paradise - CAD Generator {VERSION}")
        self.root.geometry("500x750")
        self.root.minsize(500, 650)  # Minimum size to ensure all controls are visible
        # Window is resizable and draggable across monitors by default
        
        # Start background validation thread
        self.validation_thread = threading.Thread(target=self._background_validation, daemon=True)
        self.validation_thread.start()
        
        # Dark theme colors
        self.bg_dark = "#1a1a22"
        self.bg_card = "#2a2a35"
        self.text_primary = "#f8fafc"
        self.text_secondary = "#94a3b8"
        self.text_muted = "#64748b"
        self.accent = "#10b981"
        
        self.root.configure(bg=self.bg_dark)
        
        # Make window open maximized (full screen)
        self.root.state('zoomed')
        
        # Check for updates in background
        threading.Thread(target=check_for_updates, daemon=True).start()
        
        # Load or prompt for library location
        self.library_path = self._get_library_path()
        self._create_folder_structure()
        
        self._create_ui()
        
        # Show update notification after UI loads
        self.root.after(2000, self._show_update_notification)
        
    def _get_library_path(self):
        """Load library path from config or prompt user to select"""
        # Try to load from config
        if CONFIG_FILE.exists():
            try:
                with open(CONFIG_FILE, 'r') as f:
                    config = json.load(f)
                    library_path = config.get('library_path')
                    if library_path and os.path.exists(library_path):
                        return Path(library_path)  # Return as Path object
            except Exception as e:
                print(f"Error loading config: {e}")
        
        # No config or invalid path - prompt user
        return Path(self._prompt_library_location())  # Return as Path object
    
    def _prompt_library_location(self):
        """Show dialog to select library location"""
        # Create a temporary window for the dialog
        dialog = tk.Toplevel(self.root)
        dialog.title("Select CAD Library Location")
        dialog.geometry("500x300")
        dialog.configure(bg=self.bg_dark)
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Center the dialog
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (500 // 2)
        y = (dialog.winfo_screenheight() // 2) - (300 // 2)
        dialog.geometry(f"500x300+{x}+{y}")
        
        # Content
        tk.Label(
            dialog,
            text="📁 Choose Library Location",
            font=("Segoe UI", 16, "bold"),
            bg=self.bg_dark,
            fg=self.text_primary
        ).pack(pady=(30, 10))
        
        tk.Label(
            dialog,
            text="Select where you want to store your CAD parts library.\nA folder structure will be created automatically.",
            font=("Segoe UI", 10),
            bg=self.bg_dark,
            fg=self.text_secondary,
            justify="center"
        ).pack(pady=10)
        
        # Path display
        path_var = tk.StringVar(value=str(Path.home() / "Documents" / "EquationParadise_CAD_Library"))
        
        # Label for path
        tk.Label(
            dialog,
            text="Selected Location:",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", padx=40, pady=(10, 0))
        
        path_frame = tk.Frame(dialog, bg=self.bg_card)
        path_frame.pack(pady=(5, 20), padx=30, fill="x")
        
        # Browse button first (pack right)
        tk.Button(
            path_frame,
            text="Browse...",
            font=("Segoe UI", 9, "bold"),
            bg=self.accent,
            fg="white",
            activebackground="#059669",
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=5,
            command=lambda: self._browse_for_folder(path_var)
        ).pack(side="right", padx=(10, 0))
        
        # Path entry (pack left, fill remaining space)
        path_entry = tk.Entry(
            path_frame,
            textvariable=path_var,
            font=("Segoe UI", 9),
            bg=self.bg_dark,
            fg=self.text_primary,
            insertbackground=self.text_primary,
            relief="flat",
            width=50
        )
        path_entry.pack(side="left", fill="x", expand=True, padx=(0, 10), ipady=8)
        
        # Confirm button
        selected_path = [None]  # Use list to capture in closure
        
        def confirm():
            selected_path[0] = path_var.get()
            dialog.destroy()
        
        tk.Button(
            dialog,
            text="✓ Confirm Location",
            font=("Segoe UI", 11, "bold"),
            bg=self.accent,
            fg="white",
            activebackground="#059669",
            relief="flat",
            cursor="hand2",
            padx=30,
            pady=10,
            command=confirm
        ).pack(pady=20)
        
        # Wait for dialog to close
        self.root.wait_window(dialog)
        
        library_path = selected_path[0] or str(Path.home() / "Documents" / "EquationParadise_CAD_Library")
        
        # Save to config
        self._save_library_path(library_path)
        
        return library_path
    
    def _browse_for_folder(self, path_var):
        """Browse for folder and update path variable"""
        folder = filedialog.askdirectory(
            title="Select CAD Library Location",
            initialdir=str(Path.home() / "Documents")
        )
        if folder:
            # Add library name if user just selected parent folder
            lib_path = Path(folder)
            if not lib_path.name.startswith("EquationParadise"):
                lib_path = lib_path / "EquationParadise_CAD_Library"
            path_var.set(str(lib_path))
    
    def _save_library_path(self, path):
        """Save library path to config file"""
        try:
            CONFIG_FILE.parent.mkdir(exist_ok=True)
            with open(CONFIG_FILE, 'w') as f:
                json.dump({'library_path': path}, f)
        except Exception as e:
            print(f"Error saving config: {e}")
    
    def _create_folder_structure(self):
        """Create hierarchical folder structure for CAD library"""
        # Define folder structure
        structure = {
            'Flanges': {
                'API_6BX': ['2K_PSI', '3K_PSI', '5K_PSI', '10K_PSI', '15K_PSI', '20K_PSI'],
                'ASME_B16_5': ['Class_150', 'Class_300', 'Class_600', 'Class_900', 'Class_1500', 'Class_2500']
            },
            'Fasteners': {
                'Hex_Nuts': ['Standard', 'Heavy_Hex'],
                'Studs': ['B16_5', 'API_6B', 'API_6BX']
            },
            'Gaskets': {
                'Full_Face': [],
                'Flat_Ring': [],
                'Spiral_Wound': [],
                'Ring_Joint': ['Type_R', 'Type_RX']
            },
            'Piping': {
                'Elbows_90': [],
                'Elbows_45': [],
                'Returns_180': [],
                'Tees': ['Equal', 'Reducing'],
                'Reducers': ['Concentric', 'Eccentric'],
                'Crosses': [],
                'Pipe': []
            },
            'Pressure_Vessels': {
                'Hemispherical': [],
                'Elliptical': [],
                'Torispherical': [],
                'Flat': []
            },
            'Steel': {
                'W_Beams': [],
                'HSS_Round': [],
                'HSS_Rectangular': [],
                'Channels': [],
                'Angles': []
            },
            'Lumber': {
                'Dimensional': [],
                'Engineered': []
            },
            'Rebar': []
        }
        
        # Create folders
        for category, subcategories in structure.items():
            category_path = Path(self.library_path) / category
            category_path.mkdir(parents=True, exist_ok=True)
            
            if isinstance(subcategories, dict):
                for subcat, sub_subcats in subcategories.items():
                    subcat_path = category_path / subcat
                    subcat_path.mkdir(exist_ok=True)
                    
                    if isinstance(sub_subcats, list):
                        for sub_subcat in sub_subcats:
                            sub_subcat_path = subcat_path / sub_subcat
                            sub_subcat_path.mkdir(exist_ok=True)
    
    def _get_output_path(self, component_type, subtype=None, sub_subtype=None):
        """Get the appropriate output path for a component"""
        base_path = Path(self.library_path) / component_type
        
        if subtype:
            base_path = base_path / subtype
        
        if sub_subtype:
            base_path = base_path / sub_subtype
        
        # Ensure path exists
        base_path.mkdir(parents=True, exist_ok=True)
        
        return str(base_path)
    
    def _background_validation(self):
        """Background thread that checks subscription status periodically"""
        while True:
            time.sleep(300)  # Check every 5 minutes
            
            # Skip checks for admin users
            if self.auth_manager.is_admin():
                continue
            
            if self.auth_manager.needs_recheck():
                try:
                    valid = self.auth_manager.validate_token()
                    if not valid:
                        # Schedule UI update in main thread
                        self.root.after(0, self._show_subscription_expired)
                except Exception as e:
                    print(f"Background validation error: {e}")
    
    def _show_subscription_expired(self):
        """Show error message when subscription expires mid-session"""
        messagebox.showerror(
            "Subscription Expired",
            "Your subscription has expired. Please visit equationparadise.com/pricing to renew and continue generating parts."
        )
        self.root.quit()
    
    def _show_help(self):
        """Show comprehensive help window"""
        help_window = tk.Toplevel(self.root)
        help_window.title("CAD Generator - User Guide")
        help_window.geometry("900x700")
        help_window.configure(bg=self.bg_dark)
        
        # Make it modal
        help_window.transient(self.root)
        help_window.grab_set()
        
        # Header
        header = tk.Frame(help_window, bg=self.bg_card, height=60)
        header.pack(fill="x", padx=0, pady=0)
        header.pack_propagate(False)
        
        tk.Label(
            header,
            text="📖 User Guide & Help",
            font=("Segoe UI", 16, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(side="left", padx=20, pady=15)
        
        close_btn = tk.Button(
            header,
            text="✕",
            font=("Segoe UI", 14, "bold"),
            bg=self.bg_card,
            fg=self.text_secondary,
            activebackground="#3a3a45",
            activeforeground=self.text_primary,
            relief="flat",
            cursor="hand2",
            padx=15,
            command=help_window.destroy
        )
        close_btn.pack(side="right", padx=10)
        
        # Tabbed interface
        tab_frame = tk.Frame(help_window, bg=self.bg_dark)
        tab_frame.pack(fill="x", padx=20, pady=(10, 0))
        
        # Tab buttons
        self.active_tab = "overview"
        tabs = [
            ("📋 Overview", "overview"),
            ("📁 Files", "files"),
            ("🔧 Components", "components"),
            ("🖥️ Import Guides", "import"),
            ("❓ Troubleshooting", "troubleshooting")
        ]
        
        tab_buttons = {}
        for label, tab_id in tabs:
            btn = tk.Button(
                tab_frame,
                text=label,
                font=("Segoe UI", 9, "bold"),
                bg=self.bg_card if tab_id == "overview" else self.bg_dark,
                fg=self.text_primary,
                activebackground=self.bg_card,
                activeforeground=self.text_primary,
                relief="flat",
                cursor="hand2",
                padx=15,
                pady=8,
                command=lambda t=tab_id: self._switch_help_tab(t, tab_buttons, content_text)
            )
            btn.pack(side="left", padx=2)
            tab_buttons[tab_id] = btn
        
        # Content area with scrollbar
        content_frame = tk.Frame(help_window, bg=self.bg_dark)
        content_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        scrollbar = tk.Scrollbar(content_frame)
        scrollbar.pack(side="right", fill="y")
        
        content_text = tk.Text(
            content_frame,
            wrap="word",
            bg=self.bg_card,
            fg=self.text_primary,
            font=("Segoe UI", 10),
            padx=20,
            pady=15,
            yscrollcommand=scrollbar.set,
            relief="flat",
            state="normal"
        )
        content_text.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=content_text.yview)
        
        # Configure text tags for formatting
        content_text.tag_configure("heading1", font=("Segoe UI", 14, "bold"), foreground=self.accent, spacing1=10, spacing3=5)
        content_text.tag_configure("heading2", font=("Segoe UI", 12, "bold"), foreground=self.text_primary, spacing1=8, spacing3=3)
        content_text.tag_configure("bullet", lmargin1=20, lmargin2=40)
        content_text.tag_configure("code", font=("Consolas", 9), foreground="#a0a0ff", background="#2a2a35")
        content_text.tag_configure("emphasis", font=("Segoe UI", 10, "bold"), foreground=self.accent)
        
        # Load initial content
        self._load_help_content("overview", content_text)
        
        # Footer with buttons
        footer = tk.Frame(help_window, bg=self.bg_dark)
        footer.pack(fill="x", padx=20, pady=(0, 15))
        
        open_folder_btn = tk.Button(
            footer,
            text="📁 Open Library Folder",
            font=("Segoe UI", 10, "bold"),
            bg=self.accent,
            fg="white",
            activebackground="#059669",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=8,
            command=lambda: os.startfile(self.library_path)
        )
        open_folder_btn.pack(side="left", padx=5)
        
        readme_btn = tk.Button(
            footer,
            text="📄 Full Guide (README)",
            font=("Segoe UI", 10),
            bg=self.bg_card,
            fg=self.text_primary,
            activebackground="#3a3a45",
            activeforeground=self.text_primary,
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=8,
            command=self._open_full_readme
        )
        readme_btn.pack(side="left", padx=5)
    
    def _switch_help_tab(self, tab_id, tab_buttons, content_text):
        """Switch between help tabs"""
        self.active_tab = tab_id
        
        # Update button styles
        for tid, btn in tab_buttons.items():
            if tid == tab_id:
                btn.configure(bg=self.bg_card)
            else:
                btn.configure(bg=self.bg_dark)
        
        # Load new content
        self._load_help_content(tab_id, content_text)
    
    def _load_help_content(self, tab_id, text_widget):
        """Load content for specific help tab"""
        text_widget.config(state="normal")
        text_widget.delete("1.0", "end")
        
        if tab_id == "overview":
            text_widget.insert("end", "🎯 What is the CAD Generator?\n", "heading1")
            text_widget.insert("end", "\nThe Equation Paradise CAD Generator creates industry-standard STEP files for piping components, fasteners, gaskets, and structural elements. All files are generated locally on your computer with precise dimensions based on industry standards (ASME B16.5, API 6A/6BX, AISC, etc.).\n\n")
            
            text_widget.insert("end", "What Are STEP Files?\n", "heading2")
            text_widget.insert("end", "\nSTEP files (.step or .stp) are universal 3D CAD files that work with ALL major CAD systems:\n\n")
            text_widget.insert("end", "✅ SolidWorks, AutoCAD, Fusion 360, Inventor\n", "bullet")
            text_widget.insert("end", "✅ CATIA, NX, Creo, Rhino\n", "bullet")
            text_widget.insert("end", "✅ FreeCAD, Onshape, SketchUp\n", "bullet")
            text_widget.insert("end", "✅ Blender, 3ds Max (for visualization)\n\n", "bullet")
            
            text_widget.insert("end", "Benefits:\n", "heading2")
            text_widget.insert("end", "• Universal compatibility across all CAD platforms\n", "bullet")
            text_widget.insert("end", "• Preserves exact geometry and dimensions\n", "bullet")
            text_widget.insert("end", "• Includes accurate 3D solid models\n", "bullet")
            text_widget.insert("end", "• Can be edited, assembled, and analyzed\n\n", "bullet")
            
            text_widget.insert("end", "🚀 Getting Started\n", "heading1")
            text_widget.insert("end", "\n1. ", "emphasis")
            text_widget.insert("end", "Select Component Type: ", "emphasis")
            text_widget.insert("end", "Choose from dropdown (Flanges, Fasteners, Gaskets, etc.)\n\n")
            text_widget.insert("end", "2. ", "emphasis")
            text_widget.insert("end", "Configure Options: ", "emphasis")
            text_widget.insert("end", "Select size, pressure class, material grade\n\n")
            text_widget.insert("end", "3. ", "emphasis")
            text_widget.insert("end", "Click Generate: ", "emphasis")
            text_widget.insert("end", "Creates STEP file in seconds\n\n")
            text_widget.insert("end", "4. ", "emphasis")
            text_widget.insert("end", "File Opens: ", "emphasis")
            text_widget.insert("end", "Your file explorer opens to the generated file\n\n")
            
            text_widget.insert("end", "💡 Quick Tips\n", "heading1")
            text_widget.insert("end", "\n• Library location: ", "")
            text_widget.insert("end", f"{self.library_path}", "code")
            text_widget.insert("end", "\n• Files organized by type (Flanges, Fasteners, etc.)\n")
            text_widget.insert("end", "• Internet connection required (subscription validation)\n")
            text_widget.insert("end", "• All dimensions in millimeters (mm)\n")
            text_widget.insert("end", "• Files are never deleted - they persist between sessions\n")
            text_widget.insert("end", "• Click the 📁 button below to open library folder anytime\n")
        
        elif tab_id == "files":
            text_widget.insert("end", "📁 File Organization\n", "heading1")
            text_widget.insert("end", "\nAll generated files are saved to:\n\n")
            text_widget.insert("end", f"{self.library_path}\n\n", "code")
            
            text_widget.insert("end", "File Naming Convention\n", "heading2")
            text_widget.insert("end", "\nFiles are automatically named with descriptive identifiers:\n\n")
            
            text_widget.insert("end", "Flanges:\n", "emphasis")
            text_widget.insert("end", "API-6BX-10K-4-1-16-WN.step\n", "code")
            text_widget.insert("end", "  └─ Type (WN=Weld Neck)\n")
            text_widget.insert("end", "  └─ Size (4-1/16 inches)\n")
            text_widget.insert("end", "  └─ Pressure Class (10K PSI)\n")
            text_widget.insert("end", "  └─ Standard (API 6BX)\n\n")
            
            text_widget.insert("end", "Fasteners:\n", "emphasis")
            text_widget.insert("end", "HexNut-Standard-1-2.step\n", "code")
            text_widget.insert("end", "Stud-B165-2-Class150-80mm-0.625in.step\n\n", "code")
            
            text_widget.insert("end", "Gaskets:\n", "emphasis")
            text_widget.insert("end", "Gasket-FullFace-NPS2-Class150-3.2mm.step\n\n", "code")
            
            text_widget.insert("end", "File Properties\n", "heading2")
            text_widget.insert("end", "\n• ", "emphasis")
            text_widget.insert("end", "Units: ", "emphasis")
            text_widget.insert("end", "Millimeters (mm)\n")
            text_widget.insert("end", "• ", "emphasis")
            text_widget.insert("end", "Origin: ", "emphasis")
            text_widget.insert("end", "Centered on part centerline\n")
            text_widget.insert("end", "• ", "emphasis")
            text_widget.insert("end", "Solid Body: ", "emphasis")
            text_widget.insert("end", "Closed, manifold geometry (ready for analysis)\n")
            text_widget.insert("end", "• ", "emphasis")
            text_widget.insert("end", "Precision: ", "emphasis")
            text_widget.insert("end", "±0.01mm (meets industry tolerances)\n")
        
        elif tab_id == "components":
            text_widget.insert("end", "🔧 Available Components\n", "heading1")
            text_widget.insert("end", "\nCurrent Library: 1,200+ Configurations\n", "heading2")
            
            text_widget.insert("end", "\n1. Flanges (API 6A/6BX & ASME B16.5)\n", "emphasis")
            text_widget.insert("end", "   • Types: Weld Neck, Blind\n")
            text_widget.insert("end", "   • Sizes: 1/2\" to 12\" (fractional supported)\n")
            text_widget.insert("end", "   • Pressure: 2K, 3K, 5K, 10K, 15K, 20K PSI\n")
            text_widget.insert("end", "   • Count: ~135 configurations\n\n")
            
            text_widget.insert("end", "2. Fasteners\n", "emphasis")
            text_widget.insert("end", "   Hex Nuts: Standard & Heavy Hex (2H)\n", "emphasis")
            text_widget.insert("end", "   • Sizes: 1/4\" to 4\"\n")
            text_widget.insert("end", "   • Standards: ASME B18.2.2\n")
            text_widget.insert("end", "   • Count: 78 configurations\n\n")
            
            text_widget.insert("end", "   Studs: B16.5, API 6B, API 6BX\n", "emphasis")
            text_widget.insert("end", "   • Sizes: 1/2\" to 12\"\n")
            text_widget.insert("end", "   • Lengths: 40mm to 300mm\n")
            text_widget.insert("end", "   • Count: 273 configurations\n\n")
            
            text_widget.insert("end", "3. Gaskets\n", "emphasis")
            text_widget.insert("end", "   • Full Face (covers entire flange)\n")
            text_widget.insert("end", "   • Flat Ring (inside bolt circle)\n")
            text_widget.insert("end", "   • Spiral Wound (high-temp/pressure)\n")
            text_widget.insert("end", "   • Ring Joint (Type R, RX)\n")
            text_widget.insert("end", "   • Sizes: 1/2\" to 24\"\n")
            text_widget.insert("end", "   • Pressure: 150# to 2500#\n")
            text_widget.insert("end", "   • Count: 651 configurations\n\n")
            
            text_widget.insert("end", "4. Piping Components\n", "emphasis")
            text_widget.insert("end", "   • Elbows: 90° and 45°\n")
            text_widget.insert("end", "   • 180° Returns: LR and SR\n")
            text_widget.insert("end", "   • Tees: Equal and Reducing\n")
            text_widget.insert("end", "   • Reducers: Concentric/Eccentric\n")
            text_widget.insert("end", "   • Crosses, Pipes (beveled ends)\n")
            text_widget.insert("end", "   • Sizes: 1/2\" to 24\" NPS\n")
            text_widget.insert("end", "   • Schedules: 10-160\n\n")
            
            text_widget.insert("end", "5. Pressure Vessels\n", "emphasis")
            text_widget.insert("end", "   • Hemispherical heads (half sphere)\n")
            text_widget.insert("end", "   • Elliptical heads (2:1 ASME)\n")
            text_widget.insert("end", "   • Torispherical heads (F&D)\n")
            text_widget.insert("end", "   • Flat heads\n")
            text_widget.insert("end", "   • Custom ID, wall, length\n\n")
            
            text_widget.insert("end", "Coming Soon:\n", "heading2")
            text_widget.insert("end", "   • Steel Shapes (W-Beams, HSS) - 2,301 shapes\n")
            text_widget.insert("end", "   • Dimensional Lumber (2x4, 2x6, etc.) - 50+ sizes\n")
            text_widget.insert("end", "   • Rebar (#3 through #11) - 27 configurations\n\n")
            
            text_widget.insert("end", "Total When Complete: 23,000+ parts\n", "emphasis")
        
        elif tab_id == "import":
            text_widget.insert("end", "🖥️ CAD System Import Guides\n", "heading1")
            
            cad_systems = [
                ("SolidWorks", "File → Open → Select STEP → Open\n• Change file type to 'STEP (*.step, *.stp)'\n• Check 'Try to form solid'\n• Or just drag-and-drop!"),
                ("AutoCAD", "Insert tab → Import → Select STEP\n• Type 'IMPORT' command\n• Choose STEP file\n• Import as 3D solid"),
                ("Fusion 360", "File → Open → Upload\n• Select .step file\n• Units: Millimeter\n• Auto-imports to browser tree"),
                ("Inventor", "File → Open → STEP Files\n• Import as composite feature\n• Units: Millimeters\n• Appears in feature tree"),
                ("FreeCAD", "File → Open → Select file\n• Free and open-source!\n• Auto-imports, switch to Part workbench\n• Works on Windows, Mac, Linux"),
                ("Onshape", "Cloud-based CAD\n• Click + icon → Import\n• Upload .step file\n• Auto-imports to parts list"),
                ("CATIA", "File → Open → STEP\n• Mode: Automatic\n• Units: Millimeter\n• Create 3D geometry"),
                ("Rhino 3D", "File → Import → STEP\n• Join surfaces into polysurfaces\n• Great for rendering/visualization")
            ]
            
            for system, instructions in cad_systems:
                text_widget.insert("end", f"\n{system}\n", "heading2")
                text_widget.insert("end", f"{instructions}\n\n")
            
            text_widget.insert("end", "\n💡 General Tips\n", "heading2")
            text_widget.insert("end", "• All files are in millimeters (1 inch = 25.4mm)\n")
            text_widget.insert("end", "• STEP files import as 'dumb' solids (no feature history)\n")
            text_widget.insert("end", "• Use direct modeling tools to edit geometry\n")
            text_widget.insert("end", "• Most CAD systems support STEP natively\n")
            text_widget.insert("end", "• If one system fails, try FreeCAD (it's free!)\n")
        
        elif tab_id == "troubleshooting":
            text_widget.insert("end", "❓ Troubleshooting\n", "heading1")
            
            text_widget.insert("end", "\nFile Won't Import\n", "heading2")
            text_widget.insert("end", "• Verify file extension is .step or .stp\n")
            text_widget.insert("end", "• Try opening in different CAD software (FreeCAD is free)\n")
            text_widget.insert("end", "• Re-generate the file in case of corruption\n")
            text_widget.insert("end", "• Check file size (should be 5-50KB typically)\n\n")
            
            text_widget.insert("end", "Wrong Units After Import\n", "heading2")
            text_widget.insert("end", "• All files are in millimeters\n", "emphasis")
            text_widget.insert("end", "• Check: Edit → Properties → Units in your CAD\n")
            text_widget.insert("end", "• Convert if needed: 1 inch = 25.4 mm\n\n")
            
            text_widget.insert("end", "Can't Find Generated Files\n", "heading2")
            text_widget.insert("end", f"• Library location: {self.library_path}\n", "code")
            text_widget.insert("end", "• Files organized in subfolders by type\n")
            text_widget.insert("end", "• Click '📁 Open Library Folder' button below\n")
            text_widget.insert("end", "• Search Windows Explorer for '*.step'\n\n")
            
            text_widget.insert("end", "Part Looks Wrong in CAD\n", "heading2")
            text_widget.insert("end", "• Check orientation (Z-up for flanges, X-along for pipes)\n")
            text_widget.insert("end", "• Verify scale (should be 1:1)\n")
            text_widget.insert("end", "• Try different import settings\n")
            text_widget.insert("end", "• Some viewers show wireframe - switch to shaded\n\n")
            
            text_widget.insert("end", "Can't Edit Imported Geometry\n", "heading2")
            text_widget.insert("end", "• STEP files import as 'dumb' solids (no history)\n")
            text_widget.insert("end", "• Use direct modeling tools (Push/Pull, Fillet, etc.)\n")
            text_widget.insert("end", "• Create new sketch on face and extrude/cut\n\n")
            
            text_widget.insert("end", "Generator Asks for Login Again\n", "heading2")
            text_widget.insert("end", "• Token expires after 7 days (security)\n")
            text_widget.insert("end", "• Subscription must be active\n")
            text_widget.insert("end", "• Check internet connection\n")
            text_widget.insert("end", "• Contact: staff@equationparadise.com\n\n")
            
            text_widget.insert("end", "📧 Need More Help?\n", "heading1")
            text_widget.insert("end", "\nEmail: staff@equationparadise.com\n")
            text_widget.insert("end", "Website: https://equationparadise.com\n")
            text_widget.insert("end", "Documentation: https://equationparadise.com/docs\n")
        
        text_widget.config(state="disabled")
    
    def _open_full_readme(self):
        """Open the full README file"""
        readme_path = os.path.join(os.path.dirname(__file__), "CAD_GENERATOR_USER_GUIDE.md")
        if os.path.exists(readme_path):
            os.startfile(readme_path)
        else:
            messagebox.showinfo("README Not Found", f"Full guide not found at:\n{readme_path}")
    
    def _create_ui(self):
        # Header
        header_frame = tk.Frame(self.root, bg=self.bg_dark)
        header_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        # Title on left, help button on right
        title_container = tk.Frame(header_frame, bg=self.bg_dark)
        title_container.pack(fill="x")
        
        # Left side - title
        title_left = tk.Frame(title_container, bg=self.bg_dark)
        title_left.pack(side="left", fill="x", expand=True)
        
        title_label = tk.Label(
            title_left,
            text="⚡ Equation Paradise",
            font=("Segoe UI", 18, "bold"),
            bg=self.bg_dark,
            fg=self.text_primary
        )
        title_label.pack(anchor="w")
        
        subtitle_label = tk.Label(
            title_left,
            text=f"CAD Parts Generator {VERSION}",
            font=("Segoe UI", 10),
            bg=self.bg_dark,
            fg=self.text_secondary
        )
        subtitle_label.pack(anchor="w")
        
        # Right side - help button
        help_btn = tk.Button(
            title_container,
            text="ℹ️ Help",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary,
            activebackground="#3a3a45",
            activeforeground=self.text_primary,
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=5,
            command=self._show_help
        )
        help_btn.pack(side="right", padx=5)
        
        # Main scrollable card with canvas
        card = tk.Frame(self.root, bg=self.bg_card)
        card.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        # Create canvas and scrollbar for scrolling content
        self.main_canvas = tk.Canvas(card, bg=self.bg_card, highlightthickness=0)
        scrollbar = tk.Scrollbar(card, orient="vertical", command=self.main_canvas.yview)
        self.scrollable_frame = tk.Frame(self.main_canvas, bg=self.bg_card)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all"))
        )
        
        self.main_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.main_canvas.configure(yscrollcommand=scrollbar.set)
        
        # Add horizontal scrollbar
        h_scrollbar = tk.Scrollbar(card, orient="horizontal", command=self.main_canvas.xview)
        self.main_canvas.configure(xscrollcommand=h_scrollbar.set)
        
        self.main_canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        h_scrollbar.pack(side="bottom", fill="x", before=self.main_canvas)
        
        # Enable mousewheel scrolling
        def _on_mousewheel(event):
            self.main_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        self.main_canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        # Category buttons section
        category_frame = tk.Frame(self.scrollable_frame, bg=self.bg_card)
        category_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        tk.Label(
            category_frame,
            text="Select Component Category",
            font=("Segoe UI", 11, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(0, 10))
        
        # Create button grid for categories
        buttons_container = tk.Frame(category_frame, bg=self.bg_card)
        buttons_container.pack(fill="x")
        
        # Row 1: Components
        row1 = tk.Frame(buttons_container, bg=self.bg_card)
        row1.pack(fill="x", pady=(0, 8))
        
        self.component_var = tk.StringVar(value="Flanges")
        
        self._create_category_button(row1, "🔩 Flanges", "Flanges", 0, 0)
        self._create_category_button(row1, "🔧 Fasteners", "Fasteners", 0, 1)
        self._create_category_button(row1, "⭕ Gaskets", "Gaskets", 0, 2)
        self._create_category_button(row1, "🔌 Piping", "Piping", 0, 3)
        self._create_category_button(row1, "🛢️ Vessels", "Pressure Vessels", 0, 4)
        
        # Row 2: Structural
        row2 = tk.Frame(buttons_container, bg=self.bg_card)
        row2.pack(fill="x", pady=(0, 8))
        
        self._create_category_button(row2, "🏗️ Steel Shapes", "Steel Shapes", 0, 0)
        self._create_category_button(row2, "🪵 Lumber", "Lumber", 0, 1)
        self._create_category_button(row2, "� Steel Framing", "Steel Framing", 0, 2)
        self._create_category_button(row2, "🔴 Rebar", "Rebar", 0, 3)
        self._create_category_button(row2, "📄 Sheet Steel", "Sheet Steel", 0, 4)
        
        # Row 3: Tools (highlighted)
        row3 = tk.Frame(buttons_container, bg=self.bg_card)
        row3.pack(fill="x", pady=(0, 5))
        
        self._create_category_button(row3, "📦 Assembly Package", "Assembly Package", 0, 0, highlight=True, width=18)
        self._create_category_button(row3, "🌊 Flow Calculator", "Flow Calculator", 0, 1, highlight=True, width=18)
        
        # Dynamic options frame
        self.options_frame = tk.Frame(self.scrollable_frame, bg=self.bg_card)
        self.options_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Generate button
        self.gen_btn = tk.Button(
            self.scrollable_frame,
            text="⚙️  Generate STEP File",
            font=("Segoe UI", 10, "bold"),
            bg=self.accent,
            fg="white",
            activebackground="#059669",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=10,
            command=self._generate
        )
        self.gen_btn.pack(pady=(10, 15))
        
        # Status label
        self.status_var = tk.StringVar(value="Ready to generate")
        status_label = tk.Label(
            self.scrollable_frame,
            textvariable=self.status_var,
            font=("Segoe UI", 9),
            bg=self.bg_card,
            fg=self.text_secondary
        )
        status_label.pack(pady=(0, 5))
        
        # File location link (hidden by default)
        self.file_location_frame = tk.Frame(self.scrollable_frame, bg=self.bg_card)
        self.file_location_frame.pack(pady=(0, 10))
        
        self.file_location_label = tk.Label(
            self.file_location_frame,
            text="📁 Open file location",
            font=("Segoe UI", 9, "underline"),
            bg=self.bg_card,
            fg=self.accent,
            cursor="hand2"
        )
        self.file_location_label.pack()
        self.file_location_label.bind("<Button-1>", lambda e: self._open_file_location())
        
        # Hide initially
        self.file_location_frame.pack_forget()
        self.last_generated_path = None
        
        # Initialize options
        self._update_component_options()
    
    def _create_category_button(self, parent, text, value, row, col, highlight=False, width=12):
        """Create a category selection button"""
        def select_category():
            self.component_var.set(value)
            self._update_component_options()
            # Update button styles
            for widget in parent.winfo_children():
                if isinstance(widget, tk.Button):
                    widget.config(
                        bg=self.accent if widget.cget("text") == text and highlight else self.bg_dark if widget.cget("text") == text else self.bg_dark,
                        fg="white" if widget.cget("text") == text else self.text_primary
                    )
        
        is_selected = (value == self.component_var.get())
        
        btn = tk.Button(
            parent,
            text=text,
            font=("Segoe UI", 9, "bold" if highlight else "normal"),
            bg=self.accent if is_selected and highlight else self.bg_dark,
            fg="white" if is_selected else self.text_primary,
            activebackground=self.accent,
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=10,
            pady=12 if highlight else 10,
            width=width,
            command=select_category
        )
        btn.grid(row=row, column=col, padx=4, pady=2, sticky="ew")
        parent.grid_columnconfigure(col, weight=1)
        
        return btn
    
    def _update_component_options(self):
        # Clear existing options
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        
        component = self.component_var.get()
        
        # Hide universal generate button for Flow Calculator and Assembly Package (they have their own)
        if component in ["Flow Calculator", "Assembly Package"]:
            self.gen_btn.pack_forget()
        else:
            self.gen_btn.pack(fill="x", padx=20, pady=(0, 20))
        
        if component == "Flanges":
            self._show_flange_options()
        elif component == "Fasteners":
            self._show_fastener_options()
        elif component == "Gaskets":
            self._show_gasket_options()
        elif component == "Piping":
            self._show_piping_options()
        elif component == "Steel Shapes":
            self._show_steel_options()
        elif component == "Lumber":
            self._show_lumber_options()
        elif component == "Steel Framing":
            self._show_steel_framing_options()
        elif component == "Rebar":
            self._show_rebar_options()
        elif component == "Sheet Steel":
            self._show_sheet_steel_options()
        elif component == "Pressure Vessels":
            self._show_pressure_vessel_options()
        elif component == "Assembly Package":
            self._show_assembly_package_options()
        elif component == "Flow Calculator":
            self._show_flow_calculator_options()
    
    def _show_flange_options(self):
        # Standard selection
        tk.Label(
            self.options_frame,
            text="Flange Standard",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        standards = list(FLANGE_STANDARDS.keys())
        self.flange_standard_var = tk.StringVar(value=standards[0] if standards else "API_6BX")
        standard_dropdown = ttk.Combobox(
            self.options_frame,
            textvariable=self.flange_standard_var,
            values=standards,
            state="readonly",
            width=28
        )
        standard_dropdown.pack(anchor="w", pady=(0, 10))
        standard_dropdown.bind("<<ComboboxSelected>>", lambda e: self._update_flange_sizes())
        
        # Size selection
        tk.Label(
            self.options_frame,
            text="Nominal Size",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        self.flange_size_var = tk.StringVar()
        self.flange_size_dropdown = ttk.Combobox(
            self.options_frame,
            textvariable=self.flange_size_var,
            values=[],
            state="readonly",
            width=28,
            height=15
        )
        self.flange_size_dropdown.pack(anchor="w", pady=(0, 10))
        self.flange_size_dropdown.bind("<<ComboboxSelected>>", lambda e: self._update_flange_pressures())
        
        # Pressure class selection
        tk.Label(
            self.options_frame,
            text="Pressure Class",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        self.flange_pressure_var = tk.StringVar()
        self.flange_pressure_dropdown = ttk.Combobox(
            self.options_frame,
            textvariable=self.flange_pressure_var,
            values=[],
            state="readonly",
            width=28
        )
        self.flange_pressure_dropdown.pack(anchor="w", pady=(0, 10))
        self.flange_pressure_dropdown.bind('<<ComboboxSelected>>', lambda e: self._update_flange_sizes_for_type())
        
        # Flange type selection
        tk.Label(
            self.options_frame,
            text="Flange Type",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        self.flange_type_var = tk.StringVar(value="Weld Neck")
        self.flange_type_dropdown = ttk.Combobox(
            self.options_frame,
            textvariable=self.flange_type_var,
            values=["Weld Neck", "Blind", "Socket Weld", "Slip-On", "Threaded", "Lap Joint"],
            state="readonly",
            width=28
        )
        self.flange_type_dropdown.pack(anchor="w", pady=(0, 10))
        self.flange_type_dropdown.bind('<<ComboboxSelected>>', lambda e: self._update_flange_pressures_for_type())
        
        # Facing type selection (RF or RTJ)
        tk.Label(
            self.options_frame,
            text="Facing Type",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        self.facing_type_var = tk.StringVar(value="Raised Face (RF)")
        self.facing_type_dropdown = ttk.Combobox(
            self.options_frame,
            textvariable=self.facing_type_var,
            values=["Raised Face (RF)", "Ring Joint (RTJ)"],
            state="readonly",
            width=28
        )
        self.facing_type_dropdown.pack(anchor="w", pady=(0, 10))
        
        # Weld bevel option (only for Weld Neck RF)
        self.include_bevel_var = tk.BooleanVar(value=True)
        self.bevel_checkbox = tk.Checkbutton(
            self.options_frame,
            text="Include Weld Bevel (uncheck for piping systems)",
            variable=self.include_bevel_var,
            bg=self.bg_card,
            fg=self.text_primary,
            activebackground=self.bg_card,
            activeforeground=self.text_primary,
            selectcolor=self.bg_dark,
            font=("Segoe UI", 9)
        )
        self.bevel_checkbox.pack(anchor="w", pady=(0, 10))
        
        # Initialize with first standard's data
        self._update_flange_sizes()
        # Ensure pressure class is set before triggering size update
        if self.flange_pressure_var.get():
            self._update_flange_sizes_for_type()
    
    def _get_available_classes_for_flange_type(self, flange_type):
        """Get available pressure classes for a given flange type"""
        if flange_type in ["Weld Neck", "Blind", "Lap Joint"]:
            return ['150', '300', '400', '600', '900', '1500', '2500']
        elif flange_type == "Socket Weld":
            return ['150', '300', '400', '600', '1500']  # No 900, 2500
        elif flange_type == "Slip-On":
            return ['150', '300', '400', '600', '900', '1500']  # No 2500
        elif flange_type == "Threaded":
            return ['150', '300', '400', '600', '900', '1500', '2500']
        return []
    
    def _get_available_sizes_for_flange_type(self, flange_type, pressure_class):
        """Get available sizes for a given flange type and class"""
        try:
            if flange_type == "Socket Weld":
                import socket_weld_flange_data as sw_data
                data_dict = sw_data.SOCKET_WELD_DATA_MAP.get(pressure_class)
                if data_dict:
                    return list(data_dict.keys())
            elif flange_type == "Slip-On":
                import slip_on_flange_data as so_data
                data_dict = so_data.SLIP_ON_DATA_MAP.get(pressure_class)
                if data_dict:
                    return list(data_dict.keys())
            elif flange_type == "Threaded":
                import threaded_flange_data as thd_data
                data_dict = thd_data.THREADED_DATA_MAP.get(pressure_class)
                if data_dict:
                    return list(data_dict.keys())
            else:  # WN, Blind - all sizes from flange_data
                import flange_data
                class_map = {
                    '150': flange_data.CLASS_150_RF_WN,
                    '300': flange_data.CLASS_300_RF_WN,
                    '400': flange_data.CLASS_400_RF_WN,
                    '600': flange_data.CLASS_600_RF_WN,
                    '900': flange_data.CLASS_900_RF_WN,
                    '1500': flange_data.CLASS_1500_RF_WN,
                    '2500': flange_data.CLASS_2500_RF_WN
                }
                data_dict = class_map.get(pressure_class)
                if data_dict:
                    return list(data_dict.keys())
        except Exception as e:
            print(f"Error getting sizes: {e}")
        return []
    
    def _update_flange_pressures_for_type(self):
        """Update available pressure classes based on flange type selection"""
        standard = self.flange_standard_var.get()
        if standard not in ['ASME_B16_5', 'ASME_B16_47A', 'ASME_B16_47B']:
            return  # Only filter for ASME standards
        
        flange_type = self.flange_type_var.get()
        available_classes = self._get_available_classes_for_flange_type(flange_type)
        
        # Update pressure dropdown with filtered classes
        self.flange_pressure_dropdown['values'] = available_classes
        if available_classes:
            current = self.flange_pressure_var.get()
            if current not in available_classes:
                self.flange_pressure_var.set(available_classes[0])
        
        # Update sizes for new class
        self._update_flange_sizes_for_type()
    
    def _update_flange_sizes_for_type(self):
        """Update available sizes based on flange type and class selection"""
        standard = self.flange_standard_var.get()
        if standard not in ['ASME_B16_5', 'ASME_B16_47A', 'ASME_B16_47B']:
            self._update_flange_sizes()  # Use default method for non-ASME
            return
        
        flange_type = self.flange_type_var.get()
        pressure_class = self.flange_pressure_var.get()
        
        available_sizes = self._get_available_sizes_for_flange_type(flange_type, pressure_class)
        available_sizes_sorted = sorted(available_sizes, key=self._size_to_num)
        
        self.flange_size_dropdown['values'] = available_sizes_sorted
        if available_sizes_sorted:
            current = self.flange_size_var.get()
            if current not in available_sizes_sorted:
                self.flange_size_var.set(available_sizes_sorted[0])
    
    def _update_facing_options(self):
        """Update facing options visibility based on flange type"""
        # All flange types support both RF and RTJ
        pass
    
    def _update_flange_sizes(self):
        """Update size dropdown based on selected standard"""
        standard = self.flange_standard_var.get()
        if standard in FLANGE_STANDARDS:
            sizes = sorted(FLANGE_STANDARDS[standard].keys(), key=self._size_to_num)
            self.flange_size_dropdown['values'] = sizes
            if sizes:
                self.flange_size_var.set(sizes[0])
                self._update_flange_pressures()
    
    def _update_flange_pressures(self):
        """Update pressure dropdown based on selected standard and size"""
        standard = self.flange_standard_var.get()
        size = self.flange_size_var.get()
        if standard in FLANGE_STANDARDS and size in FLANGE_STANDARDS[standard]:
            pressures = FLANGE_STANDARDS[standard][size]
            self.flange_pressure_dropdown['values'] = pressures
            if pressures:
                self.flange_pressure_var.set(pressures[0])
    
    def _size_to_num(self, s):
        """Convert size string to numeric value for sorting"""
        s = str(s).replace("-", " ").replace("/", " ")
        parts = s.split()
        try:
            if len(parts) == 1:
                return float(parts[0])
            elif len(parts) == 3:  # e.g. "4 1 16" -> 4.0625
                return float(parts[0]) + float(parts[1]) / float(parts[2])
            else:
                return float(parts[0])
        except:
            return 0
    
    def _show_fastener_options(self):
        # Selection mode
        tk.Label(
            self.options_frame,
            text="Selection Mode",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        self.fastener_mode_var = tk.StringVar(value="By Flange Standard")
        mode_dropdown = ttk.Combobox(
            self.options_frame,
            textvariable=self.fastener_mode_var,
            values=["By Flange Standard", "By Stud Diameter"],
            state="readonly",
            width=28
        )
        mode_dropdown.pack(anchor="w", pady=(0, 10))
        mode_dropdown.bind("<<ComboboxSelected>>", lambda e: self._update_fastener_mode())
        
        # Container for mode-specific options
        self.fastener_options_container = tk.Frame(self.options_frame, bg=self.bg_card)
        self.fastener_options_container.pack(anchor="w", fill="x")
        
        # Show default mode
        self._update_fastener_mode()
        
        # Include matching nut checkbox (outside container so it persists)
        self.fastener_include_matching_var = tk.BooleanVar(value=True)
        checkbox_frame = tk.Frame(self.options_frame, bg=self.bg_card)
        checkbox_frame.pack(anchor="w", pady=(15, 5))
        
        ttk.Checkbutton(
            checkbox_frame,
            text="Include matching nut",
            variable=self.fastener_include_matching_var
        ).pack(side="left")
        
        # Info label
        info_label = tk.Label(
            checkbox_frame,
            text="(nut diameter matches stud)",
            font=("Segoe UI", 8),
            bg=self.bg_card,
            fg=self.text_secondary
        )
        info_label.pack(side="left", padx=(5, 0))
    
    def _update_fastener_mode(self):
        """Switch between flange standard mode and diameter mode."""
        # Clear existing options
        for widget in self.fastener_options_container.winfo_children():
            widget.destroy()
        
        mode = self.fastener_mode_var.get()
        
        if mode == "By Flange Standard":
            self._show_flange_standard_options()
        else:
            self._show_stud_diameter_options()
    
    def _show_flange_standard_options(self):
        """Show options for selecting by flange standard."""
        # Fastener type
        tk.Label(
            self.fastener_options_container,
            text="Stud Type",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        self.fastener_type_var = tk.StringVar(value="B16.5 Stud")
        fastener_dropdown = ttk.Combobox(
            self.fastener_options_container,
            textvariable=self.fastener_type_var,
            values=["B16.5 Stud", "B16.47 Series A Stud", "B16.47 Series B Stud", "API 6B Stud", "API 6BX Stud"],
            state="readonly",
            width=28,
            height=10
        )
        fastener_dropdown.pack(anchor="w", pady=(0, 10))
        fastener_dropdown.bind("<<ComboboxSelected>>", lambda e: self._update_fastener_sizes())
        
        # Size
        tk.Label(
            self.fastener_options_container,
            text="Flange Nominal Size",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        # Helper text
        tk.Label(
            self.fastener_options_container,
            text="(Stud size determined by flange size)",
            font=("Segoe UI", 8),
            bg=self.bg_card,
            fg=self.text_muted
        ).pack(anchor="w", pady=(0, 2))
        
        self.fastener_size_var = tk.StringVar(value="1/2")
        self.fastener_size_dropdown = ttk.Combobox(
            self.fastener_options_container,
            textvariable=self.fastener_size_var,
            values=["1/2", "3/4", "1", "1-1/2", "2"],  # Initial values
            state="readonly",
            width=28,
            height=15
        )
        self.fastener_size_dropdown.pack(anchor="w", pady=(0, 15))
        
        # Pressure class
        tk.Label(
            self.fastener_options_container,
            text="Pressure Class",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        self.fastener_class_var = tk.StringVar(value="150")
        ttk.Combobox(
            self.fastener_options_container,
            textvariable=self.fastener_class_var,
            values=["150", "300", "600", "900", "1500", "2500"],
            state="readonly",
            width=28
        ).pack(anchor="w")
        
        # Initialize sizes for default selection (do this after widgets are created)
        self.root.after(100, self._update_fastener_sizes)
    
    def _show_stud_diameter_options(self):
        """Show options for selecting by stud diameter."""
        # Stud diameter
        tk.Label(
            self.fastener_options_container,
            text="Stud Diameter",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        # All available stud diameters from our nut data
        stud_diameters = [
            "1/4", "5/16", "3/8", "7/16", "1/2", "9/16", "5/8", "3/4", "7/8",
            "1", "1-1/8", "1-1/4", "1-3/8", "1-1/2", "1-3/4", "2", "2-1/4",
            "2-1/2", "2-3/4", "3", "3-1/4", "3-1/2", "3-3/4", "4"
        ]
        
        self.fastener_diameter_var = tk.StringVar(value="1/2")
        ttk.Combobox(
            self.fastener_options_container,
            textvariable=self.fastener_diameter_var,
            values=stud_diameters,
            state="readonly",
            width=28,
            height=15
        ).pack(anchor="w", pady=(0, 10))
        
        # Info note
        tk.Label(
            self.fastener_options_container,
            text="Standard length stud will be generated\n(modify length in CAD software as needed)",
            font=("Segoe UI", 8),
            bg=self.bg_card,
            fg=self.text_muted,
            justify="left"
        ).pack(anchor="w")
    
    def _update_fastener_sizes(self):
        """Update available sizes based on selected fastener standard."""
        fastener_type = self.fastener_type_var.get()
        
        # Import data modules to get available sizes
        import sys
        import os
        script_dir = os.path.dirname(os.path.abspath(__file__))
        sys.path.insert(0, script_dir)
        
        try:
            if fastener_type == "B16.5 Stud":
                from asme_b165_stud_data import B165_CLASS_150_STUDS
                sizes = sorted(B165_CLASS_150_STUDS.keys(), key=self._nps_to_float)
            elif fastener_type == "B16.47 Series A Stud":
                from asme_b165_stud_data import B1647A_CLASS_150_STUDS
                sizes = sorted(B1647A_CLASS_150_STUDS.keys(), key=self._nps_to_float)
            elif fastener_type == "B16.47 Series B Stud":
                from asme_b165_stud_data import B1647B_CLASS_150_STUDS
                sizes = sorted(B1647B_CLASS_150_STUDS.keys(), key=self._nps_to_float)
            elif fastener_type == "API 6B Stud":
                from api_6b_stud_data import API_6B_5000_STUDS
                sizes = sorted(API_6B_5000_STUDS.keys(), key=self._nps_to_float)
            else:  # API 6BX Stud
                from api_6bx_stud_data import API_6BX_10000_STUDS
                sizes = sorted(API_6BX_10000_STUDS.keys(), key=self._nps_to_float)
            
            if hasattr(self, 'fastener_size_dropdown'):
                self.fastener_size_dropdown['values'] = sizes
                if sizes:
                    self.fastener_size_var.set(sizes[0])
        except Exception as e:
            print(f"Error updating fastener sizes: {e}")
            # Fallback to basic sizes
            if hasattr(self, 'fastener_size_dropdown'):
                self.fastener_size_dropdown['values'] = ["1/2", "3/4", "1", "1-1/2", "2"]
                self.fastener_size_var.set("1/2")
    
    def _nps_to_float(self, nps_str):
        """Convert NPS string to float for sorting."""
        try:
            if '-' in nps_str and '/' in nps_str:
                # Handle '1-1/2' format
                parts = nps_str.split('-')
                whole = float(parts[0])
                frac_parts = parts[1].split('/')
                frac = float(frac_parts[0]) / float(frac_parts[1])
                return whole + frac
            elif '/' in nps_str:
                # Handle '1/2' format
                parts = nps_str.split('/')
                return float(parts[0]) / float(parts[1])
            else:
                # Handle '1', '2', etc.
                return float(nps_str)
        except:
            return 0
    
    def _show_gasket_options(self):
        # Gasket type
        tk.Label(
            self.options_frame,
            text="Gasket Type",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        self.gasket_type_var = tk.StringVar(value="Full Face")
        ttk.Combobox(
            self.options_frame,
            textvariable=self.gasket_type_var,
            values=["Full Face", "Flat Ring", "Spiral Wound", "Ring Joint R", "Ring Joint RX"],
            state="readonly",
            width=28
        ).pack(anchor="w", pady=(0, 10))
        
        # Size and class
        tk.Label(
            self.options_frame,
            text="Nominal Size",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        # ALL gasket sizes (matches flange sizes)
        all_gasket_sizes = [
            "1/2", "3/4", "1", "1-1/4", "1-1/2", "2", "2-1/2", "3", "3-1/2", "4", "5", "6",
            "8", "10", "12", "14", "16", "18", "20", "22", "24", "26", "28", "30",
            "32", "34", "36", "42", "48", "54", "60"
        ]
        
        self.gasket_size_var = tk.StringVar(value="2")
        ttk.Combobox(
            self.options_frame,
            textvariable=self.gasket_size_var,
            values=all_gasket_sizes,
            state="readonly",
            width=28
        ).pack(anchor="w", pady=(0, 10))
        
        tk.Label(
            self.options_frame,
            text="Pressure Class",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        self.gasket_class_var = tk.StringVar(value="150")
        ttk.Combobox(
            self.options_frame,
            textvariable=self.gasket_class_var,
            values=["150", "300", "600", "900", "1500", "2500"],
            state="readonly",
            width=28
        ).pack(anchor="w")
    
    def _show_piping_options(self):
        # Fitting type
        tk.Label(
            self.options_frame,
            text="Fitting Type",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        self.piping_type_var = tk.StringVar(value="Elbow 90°")
        ttk.Combobox(
            self.options_frame,
            textvariable=self.piping_type_var,
            values=["Pipe", "Elbow 90°", "Elbow 45°", "180° Return LR", "180° Return SR", "Tee Equal", "Tee Reducing", "Reducer Concentric", "Reducer Eccentric", "Cross"],
            state="readonly",
            width=28
        ).pack(anchor="w", pady=(0, 10))
        
        # NPS and schedule
        tk.Label(
            self.options_frame,
            text="Nominal Pipe Size (NPS)",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        # ALL pipe sizes from 1/2" to 60"
        all_pipe_sizes = [
            "1/2", "3/4", "1", "1-1/4", "1-1/2", "2", "2-1/2", "3", "3-1/2", "4", "5", "6", 
            "8", "10", "12", "14", "16", "18", "20", "22", "24", "26", "28", "30", 
            "32", "34", "36", "42", "48", "54", "60"
        ]
        
        self.piping_nps_var = tk.StringVar(value="2")
        ttk.Combobox(
            self.options_frame,
            textvariable=self.piping_nps_var,
            values=all_pipe_sizes,
            state="readonly",
            width=28
        ).pack(anchor="w", pady=(0, 10))
        
        tk.Label(
            self.options_frame,
            text="Schedule",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        # ALL schedules
        all_schedules = ["5S", "10S", "10", "20", "30", "40", "40S", "60", "80", "80S", "100", "120", "140", "160", "STD", "XS", "XXS"]
        
        self.piping_sch_var = tk.StringVar(value="40")
        ttk.Combobox(
            self.options_frame,
            textvariable=self.piping_sch_var,
            values=all_schedules,
            state="readonly",
            width=28
        ).pack(anchor="w")
    
    def _show_pressure_vessel_options(self):
        """Show options for pressure vessel generation"""
        # Head type selection
        tk.Label(
            self.options_frame,
            text="Head Type",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        self.vessel_head_type_var = tk.StringVar(value="elliptical")
        ttk.Combobox(
            self.options_frame,
            textvariable=self.vessel_head_type_var,
            values=["elliptical", "hemispherical"],
            state="readonly",
            width=28
        ).pack(anchor="w", pady=(0, 10))
        
        # Inside Diameter
        tk.Label(
            self.options_frame,
            text="Inside Diameter (inches)",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        self.vessel_id_var = tk.StringVar(value="48")
        ttk.Entry(
            self.options_frame,
            textvariable=self.vessel_id_var,
            width=30
        ).pack(anchor="w", pady=(0, 10))
        
        # Wall Thickness
        tk.Label(
            self.options_frame,
            text="Wall Thickness (inches)",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        self.vessel_wall_var = tk.StringVar(value="0.5")
        ttk.Entry(
            self.options_frame,
            textvariable=self.vessel_wall_var,
            width=30
        ).pack(anchor="w", pady=(0, 10))
        
        # Shell Length
        tk.Label(
            self.options_frame,
            text="Shell Length - Tan to Tan (inches)",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        self.vessel_length_var = tk.StringVar(value="120")
        ttk.Entry(
            self.options_frame,
            textvariable=self.vessel_length_var,
            width=30
        ).pack(anchor="w", pady=(0, 10))
        
        # Info text
        info_frame = tk.Frame(self.options_frame, bg=self.bg_dark, padx=10, pady=8)
        info_frame.pack(fill="x", pady=(10, 0))
        
        tk.Label(
            info_frame,
            text="💡 Generates cylindrical shell with selected head type on both ends.\n"
                 "   Hemispherical = half sphere, Elliptical = 2:1 ASME standard,\n"
                 "   Torispherical = F&D (flanged & dished), Flat = simple plate.",
            font=("Segoe UI", 8),
            bg=self.bg_dark,
            fg=self.text_muted,
            justify="left"
        ).pack(anchor="w")
    
    def _show_steel_options(self):
        tk.Label(
            self.options_frame,
            text="Steel Shape Type",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        self.steel_type_var = tk.StringVar(value="W-Beam")
        steel_type_combo = ttk.Combobox(
            self.options_frame,
            textvariable=self.steel_type_var,
            values=["W-Beam", "HSS Rectangular", "HSS Round", "Channel", "Angle"],
            state="readonly",
            width=28
        )
        steel_type_combo.pack(anchor="w", pady=(0, 10))
        steel_type_combo.bind("<<ComboboxSelected>>", self._update_steel_sizes)
        
        tk.Label(
            self.options_frame,
            text="Size",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        self.steel_size_var = tk.StringVar(value="W12X26")
        self.steel_size_combo = ttk.Combobox(
            self.options_frame,
            textvariable=self.steel_size_var,
            state="readonly",
            width=28,
            height=15
        )
        self.steel_size_combo.pack(anchor="w", pady=(0, 10))
        self._update_steel_sizes()
        
        tk.Label(
            self.options_frame,
            text="Length (ft)",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        self.steel_length_var = tk.StringVar(value="20")
        ttk.Entry(
            self.options_frame,
            textvariable=self.steel_length_var,
            width=30
        ).pack(anchor="w")
    
    def _update_steel_sizes(self, event=None):
        """Update steel size dropdown based on selected type"""
        shape_type = self.steel_type_var.get()
        
        # Common sizes for each type
        if shape_type == "W-Beam":
            sizes = ["W4X13", "W6X9", "W8X10", "W8X31", "W10X12", "W10X33", "W12X14", "W12X26", "W12X50",
                    "W14X22", "W14X43", "W16X26", "W16X31", "W18X35", "W21X44", "W24X55", "W27X84", "W30X90"]
        elif shape_type == "HSS Rectangular":
            sizes = ["HSS4X4X1/4", "HSS4X4X3/8", "HSS6X6X1/4", "HSS6X6X3/8", "HSS8X4X1/4", "HSS8X4X3/8",
                    "HSS8X8X1/4", "HSS8X8X3/8", "HSS8X8X1/2", "HSS10X10X1/2", "HSS12X12X1/2", "HSS16X16X5/8"]
        elif shape_type == "HSS Round":
            sizes = ["HSS2.375X0.188", "HSS3.500X0.250", "HSS4.500X0.250", "HSS6.625X0.312",
                    "HSS8.625X0.322", "HSS10.000X0.500", "HSS12.750X0.500"]
        elif shape_type == "Channel":
            sizes = ["C3X4.1", "C4X5.4", "C6X8.2", "C8X11.5", "C10X15.3", "C12X20.7", "C15X33.9"]
        elif shape_type == "Angle":
            sizes = ["L2X2X1/4", "L3X3X1/4", "L3X3X3/8", "L4X4X1/4", "L4X4X3/8", "L4X4X1/2",
                    "L6X6X3/8", "L6X6X1/2", "L8X8X1/2"]
        else:
            sizes = []
        
        self.steel_size_combo['values'] = sizes
        if sizes:
            self.steel_size_var.set(sizes[0])
    
    def _show_update_notification(self):
        """Show update notification if available"""
        if UPDATE_AVAILABLE:
            messagebox.showinfo(
                "Update Available",
                f"A new version is available!\n\nCurrent: {VERSION}\nLatest: {LATEST_VERSION}\n\nPlease contact support@equationparadise.com to update.",
                parent=self.root
            )
    
    def _show_lumber_options(self):
        tk.Label(
            self.options_frame,
            text="Lumber Type",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        self.lumber_type_var = tk.StringVar(value="Dimensional")
        lumber_type_combo = ttk.Combobox(
            self.options_frame,
            textvariable=self.lumber_type_var,
            values=["Dimensional", "Wall Studs", "Glulam", "LVL (Microlam)", "PSL (Parallam)", "TJI"],
            state="readonly",
            width=28
        )
        lumber_type_combo.pack(anchor="w", pady=(0, 10))
        lumber_type_combo.bind("<<ComboboxSelected>>", self._update_lumber_sizes)
        
        tk.Label(
            self.options_frame,
            text="Size",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        self.lumber_size_var = tk.StringVar(value="2x4")
        self.lumber_size_combo = ttk.Combobox(
            self.options_frame,
            textvariable=self.lumber_size_var,
            state="readonly",
            width=28,
            height=15
        )
        self.lumber_size_combo.pack(anchor="w", pady=(0, 10))
        self._update_lumber_sizes()
        
        # Length input section
        self.lumber_length_frame = tk.Frame(self.options_frame, bg=self.bg_card)
        self.lumber_length_frame.pack(anchor="w", fill="x", pady=(5, 0))
        
        tk.Label(
            self.lumber_length_frame,
            text="Length (decimal ft OK, e.g. 8.5)",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(0, 2))
        
        # Feet and inches input row
        length_input_frame = tk.Frame(self.lumber_length_frame, bg=self.bg_card)
        length_input_frame.pack(anchor="w", pady=(0, 5))
        
        self.lumber_feet_var = tk.StringVar(value="8")
        feet_entry = ttk.Entry(
            length_input_frame,
            textvariable=self.lumber_feet_var,
            width=8
        )
        feet_entry.pack(side="left")
        
        tk.Label(
            length_input_frame,
            text="ft  +",
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(side="left", padx=(2, 8))
        
        self.lumber_inches_var = tk.StringVar(value="0")
        inches_entry = ttk.Entry(
            length_input_frame,
            textvariable=self.lumber_inches_var,
            width=6
        )
        inches_entry.pack(side="left")
        
        tk.Label(
            length_input_frame,
            text="in",
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(side="left", padx=(2, 0))
        
        # Common length buttons frame
        self.length_buttons_frame = tk.Frame(self.options_frame, bg=self.bg_card)
        self.length_buttons_frame.pack(anchor="w", pady=(5, 10))
        
        self._update_length_buttons()
    
    def _update_length_buttons(self):
        """Update quick length buttons based on lumber type"""
        # Clear existing buttons
        for widget in self.length_buttons_frame.winfo_children():
            widget.destroy()
        
        lumber_type = self.lumber_type_var.get()
        
        if lumber_type == "Wall Studs":
            # Pre-cut stud lengths
            stud_lengths = [
                ("92⅝\"", 92.625),   # 8' ceiling
                ("104⅝\"", 104.625), # 9' ceiling
                ("116⅝\"", 116.625), # 10' ceiling
                ("8'", 96),
                ("9'", 108),
                ("10'", 120),
            ]
            for label, inches in stud_lengths:
                btn = tk.Button(
                    self.length_buttons_frame,
                    text=label,
                    command=lambda i=inches: self._set_lumber_length_inches(i),
                    bg=self.accent,
                    fg="white",
                    relief="flat",
                    padx=4,
                    pady=2,
                    cursor="hand2"
                )
                btn.pack(side="left", padx=2)
        else:
            # Standard lumber lengths in feet
            common_lengths = ["8", "10", "12", "14", "16", "20", "24"]
            for length in common_lengths:
                btn = tk.Button(
                    self.length_buttons_frame,
                    text=f"{length}'",
                    command=lambda l=length: self._set_lumber_length_feet(l),
                    bg=self.accent,
                    fg="white",
                    relief="flat",
                    padx=5,
                    pady=2,
                    cursor="hand2"
                )
                btn.pack(side="left", padx=2)
    
    def _set_lumber_length_feet(self, feet):
        """Set lumber length from feet button"""
        self.lumber_feet_var.set(feet)
        self.lumber_inches_var.set("0")
    
    def _set_lumber_length_inches(self, total_inches):
        """Set lumber length from total inches (for pre-cut studs)"""
        feet = int(total_inches // 12)
        inches = total_inches % 12
        self.lumber_feet_var.set(str(feet))
        # Format inches nicely
        if inches == int(inches):
            self.lumber_inches_var.set(str(int(inches)))
        else:
            self.lumber_inches_var.set(f"{inches:.3f}".rstrip('0').rstrip('.'))
    
    def _update_lumber_sizes(self, event=None):
        """Update lumber size dropdown based on selected type"""
        lumber_type = self.lumber_type_var.get()
        
        if lumber_type == "Dimensional":
            sizes = ["2x4", "2x6", "2x8", "2x10", "2x12", "4x4", "4x6", "4x8", "4x10", "4x12", 
                    "6x6", "6x8", "6x10", "6x12", "8x8", "8x10", "8x12", "10x10", "10x12", "12x12"]
        elif lumber_type == "Wall Studs":
            # Wall studs are typically 2x4 or 2x6
            sizes = ["2x4", "2x6", "2x3"]
        elif lumber_type == "Glulam":
            # Common glulam sizes (width x depth in inches)
            sizes = ["3-1/8x9", "3-1/8x10-1/2", "3-1/8x12", "3-1/8x13-1/2", "3-1/8x15", "3-1/8x16-1/2", "3-1/8x18",
                    "5-1/8x9", "5-1/8x10-1/2", "5-1/8x12", "5-1/8x13-1/2", "5-1/8x15", "5-1/8x16-1/2", "5-1/8x18", "5-1/8x21", "5-1/8x24",
                    "6-3/4x9", "6-3/4x10-1/2", "6-3/4x12", "6-3/4x13-1/2", "6-3/4x15", "6-3/4x16-1/2", "6-3/4x18", "6-3/4x21", "6-3/4x24"]
        elif lumber_type == "LVL (Microlam)":
            # LVL/Microlam sizes (thickness x depth)
            sizes = ["1-3/4x9-1/2", "1-3/4x11-7/8", "1-3/4x14", "1-3/4x16", "1-3/4x18",
                    "3-1/2x9-1/2", "3-1/2x11-7/8", "3-1/2x14", "3-1/2x16", "3-1/2x18", "3-1/2x20", "3-1/2x24",
                    "5-1/4x9-1/2", "5-1/4x11-7/8", "5-1/4x14", "5-1/4x16", "5-1/4x18", "5-1/4x20", "5-1/4x24"]
        elif lumber_type == "PSL (Parallam)":
            # PSL/Parallam sizes
            sizes = ["3-1/2x9-1/4", "3-1/2x11-1/4", "3-1/2x11-7/8", "3-1/2x14", "3-1/2x16", "3-1/2x18",
                    "5-1/4x9-1/4", "5-1/4x11-1/4", "5-1/4x11-7/8", "5-1/4x14", "5-1/4x16", "5-1/4x18",
                    "7x9-1/4", "7x11-1/4", "7x11-7/8", "7x14", "7x16", "7x18"]
        elif lumber_type == "TJI":
            # TJI I-joists (Series + Depth)
            sizes = ["TJI 110  9 1/2", "TJI 110 117/8", "TJI 110 14", "TJI 110 16",
                    "TJI 210 9 1/2", "TJI 210 11 7/8", "TJI 210 14", "TJI 210 16",
                    "TJI 230 9 1/2", "TJI 230 11 7/8", "TJI 230 14", "TJI 230 16",
                    "TJI 360 11 7/8", "TJI 360 14", "TJI 360 16",
                    "TJI 560 11 7/8", "TJI 560 14", "TJI 560 16 "]
        else:
            sizes = []
        
        self.lumber_size_combo['values'] = sizes
        if sizes:
            self.lumber_size_var.set(sizes[0])
        
        # Update length buttons based on lumber type
        if hasattr(self, 'length_buttons_frame'):
            self._update_length_buttons()
    
    def _show_steel_framing_options(self):
        """Show options for CFS steel framing (studs, track, joists)"""
        # Member type selection
        tk.Label(
            self.options_frame,
            text="Member Type",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        self.cfs_type_var = tk.StringVar(value="Stud")
        cfs_type_combo = ttk.Combobox(
            self.options_frame,
            textvariable=self.cfs_type_var,
            values=["Stud", "Track", "Floor Joist"],
            state="readonly",
            width=28
        )
        cfs_type_combo.pack(anchor="w", pady=(0, 10))
        cfs_type_combo.bind("<<ComboboxSelected>>", self._update_cfs_sizes)
        
        # Size selection
        tk.Label(
            self.options_frame,
            text="Size",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        self.cfs_size_var = tk.StringVar(value="362S")
        self.cfs_size_combo = ttk.Combobox(
            self.options_frame,
            textvariable=self.cfs_size_var,
            state="readonly",
            width=28
        )
        self.cfs_size_combo.pack(anchor="w", pady=(0, 10))
        
        # Gauge selection
        tk.Label(
            self.options_frame,
            text="Gauge (mil)",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        self.cfs_gauge_var = tk.StringVar(value="43")
        self.cfs_gauge_combo = ttk.Combobox(
            self.options_frame,
            textvariable=self.cfs_gauge_var,
            values=["33 (20 ga)", "43 (18 ga)", "54 (16 ga)", "68 (14 ga)", "97 (12 ga)"],
            state="readonly",
            width=28
        )
        self.cfs_gauge_combo.pack(anchor="w", pady=(0, 10))
        
        # Length input (same style as lumber)
        tk.Label(
            self.options_frame,
            text="Length (decimal ft OK, e.g. 8.5)",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        length_frame = tk.Frame(self.options_frame, bg=self.bg_card)
        length_frame.pack(anchor="w", pady=(0, 5))
        
        self.cfs_feet_var = tk.StringVar(value="8")
        ttk.Entry(length_frame, textvariable=self.cfs_feet_var, width=8).pack(side="left")
        tk.Label(length_frame, text="ft  +", bg=self.bg_card, fg=self.text_primary).pack(side="left", padx=(2, 8))
        
        self.cfs_inches_var = tk.StringVar(value="0")
        ttk.Entry(length_frame, textvariable=self.cfs_inches_var, width=6).pack(side="left")
        tk.Label(length_frame, text="in", bg=self.bg_card, fg=self.text_primary).pack(side="left", padx=(2, 0))
        
        # Punchouts checkbox
        self.cfs_punchouts_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(
            self.options_frame,
            text="Include punchouts (24\" O.C.)",
            variable=self.cfs_punchouts_var
        ).pack(anchor="w", pady=(10, 5))
        
        # Quick length buttons
        cfs_length_buttons = tk.Frame(self.options_frame, bg=self.bg_card)
        cfs_length_buttons.pack(anchor="w", pady=(5, 10))
        
        for length in ["8", "10", "12", "14", "16", "20"]:
            btn = tk.Button(
                cfs_length_buttons,
                text=f"{length}'",
                command=lambda l=length: self._set_cfs_length(l),
                bg=self.accent,
                fg="white",
                relief="flat",
                padx=5,
                pady=2,
                cursor="hand2"
            )
            btn.pack(side="left", padx=2)
        
        # Initialize sizes
        self._update_cfs_sizes()
    
    def _set_cfs_length(self, feet):
        """Set CFS length from button"""
        self.cfs_feet_var.set(feet)
        self.cfs_inches_var.set("0")
    
    def _update_cfs_sizes(self, event=None):
        """Update CFS size dropdown based on member type"""
        member_type = self.cfs_type_var.get()
        
        if member_type == "Stud":
            sizes = ["250S (2-1/2\")", "350S (3-1/2\")", "362S (3-5/8\")", "400S (4\")", "600S (6\")", "800S (8\")"]
            gauges = ["33 (20 ga)", "43 (18 ga)", "54 (16 ga)", "68 (14 ga)"]
        elif member_type == "Track":
            sizes = ["250T (2-1/2\")", "350T (3-1/2\")", "362T (3-5/8\")", "400T (4\")", "600T (6\")", "800T (8\")"]
            gauges = ["33 (20 ga)", "43 (18 ga)", "54 (16 ga)", "68 (14 ga)"]
        else:  # Floor Joist
            sizes = ["600J (6\")", "800J (8\")", "1000J (10\")", "1200J (12\")", "1400J (14\")"]
            gauges = ["43 (18 ga)", "54 (16 ga)", "68 (14 ga)", "97 (12 ga)"]
        
        self.cfs_size_combo['values'] = sizes
        if sizes:
            self.cfs_size_var.set(sizes[0])
        
        self.cfs_gauge_combo['values'] = gauges
        if gauges:
            self.cfs_gauge_var.set(gauges[0])
    
    def _show_sheet_steel_options(self):
        tk.Label(
            self.options_frame,
            text="Length (inches)",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        self.sheet_length_var = tk.StringVar(value="48")
        ttk.Entry(
            self.options_frame,
            textvariable=self.sheet_length_var,
            width=30
        ).pack(anchor="w", pady=(0, 10))
        
        tk.Label(
            self.options_frame,
            text="Width (inches)",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        self.sheet_width_var = tk.StringVar(value="24")
        ttk.Entry(
            self.options_frame,
            textvariable=self.sheet_width_var,
            width=30
        ).pack(anchor="w", pady=(0, 10))
        
        tk.Label(
            self.options_frame,
            text="Thickness (inches)",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        # Generate thickness values from 1/2" up in 1/8" increments
        thicknesses = []
        for i in range(4, 25):  # 0.5" to 3.0" in 1/8" increments
            thick = i * 0.125
            thicknesses.append(str(thick))
        
        self.sheet_thickness_var = tk.StringVar(value="0.5")
        ttk.Combobox(
            self.options_frame,
            textvariable=self.sheet_thickness_var,
            values=thicknesses,
            state="readonly",
            width=28
        ).pack(anchor="w", pady=(0, 10))
        
        tk.Label(
            self.options_frame,
            text="Bevel Angle (degrees)",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        self.sheet_bevel_angle_var = tk.StringVar(value="30")
        ttk.Combobox(
            self.options_frame,
            textvariable=self.sheet_bevel_angle_var,
            values=["30", "37.5", "45"],
            state="readonly",
            width=28
        ).pack(anchor="w", pady=(0, 10))
        
        tk.Label(
            self.options_frame,
            text="Land (inches)",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        self.sheet_land_var = tk.StringVar(value="0.0625")
        ttk.Combobox(
            self.options_frame,
            textvariable=self.sheet_land_var,
            values=["0.0625", "0.078125", "0.09375", "0.109375", "0.125"],
            state="readonly",
            width=28
        ).pack(anchor="w", pady=(0, 10))
        
        tk.Label(
            self.options_frame,
            text="Beveled Edges",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        # Edge checkboxes frame
        edge_frame = tk.Frame(self.options_frame, bg=self.bg_card)
        edge_frame.pack(anchor="w", pady=(0, 10))
        
        self.sheet_edge1_var = tk.BooleanVar(value=False)
        tk.Checkbutton(
            edge_frame,
            text="Edge 1 (+X)",
            variable=self.sheet_edge1_var,
            bg=self.bg_card,
            fg=self.text_primary,
            selectcolor=self.bg_dark,
            activebackground=self.bg_card,
            activeforeground=self.text_primary
        ).grid(row=0, column=0, sticky="w", padx=(0, 10))
        
        self.sheet_edge2_var = tk.BooleanVar(value=False)
        tk.Checkbutton(
            edge_frame,
            text="Edge 2 (+Y)",
            variable=self.sheet_edge2_var,
            bg=self.bg_card,
            fg=self.text_primary,
            selectcolor=self.bg_dark,
            activebackground=self.bg_card,
            activeforeground=self.text_primary
        ).grid(row=0, column=1, sticky="w")
        
        self.sheet_edge3_var = tk.BooleanVar(value=False)
        tk.Checkbutton(
            edge_frame,
            text="Edge 3 (-X)",
            variable=self.sheet_edge3_var,
            bg=self.bg_card,
            fg=self.text_primary,
            selectcolor=self.bg_dark,
            activebackground=self.bg_card,
            activeforeground=self.text_primary
        ).grid(row=1, column=0, sticky="w", padx=(0, 10))
        
        self.sheet_edge4_var = tk.BooleanVar(value=False)
        tk.Checkbutton(
            edge_frame,
            text="Edge 4 (-Y)",
            variable=self.sheet_edge4_var,
            bg=self.bg_card,
            fg=self.text_primary,
            selectcolor=self.bg_dark,
            activebackground=self.bg_card,
            activeforeground=self.text_primary
        ).grid(row=1, column=1, sticky="w")
    
    def _show_assembly_package_options(self):
        """Phase 1: Assembly Package Generator UI - Drill-down selection"""
        
        # Title and description
        tk.Label(
            self.options_frame,
            text="🔧 Assembly Package Generator",
            font=("Segoe UI", 11, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        tk.Label(
            self.options_frame,
            text="Generate complete piping assemblies with flanges, gaskets, and fasteners",
            font=("Segoe UI", 9),
            bg=self.bg_card,
            fg=self.text_secondary
        ).pack(anchor="w", pady=(0, 10))
        
        # Two-column layout
        columns_frame = tk.Frame(self.options_frame, bg=self.bg_card)
        columns_frame.pack(fill="both", expand=True)
        
        # LEFT COLUMN - Configuration
        left_col = tk.Frame(columns_frame, bg=self.bg_card)
        left_col.pack(side="left", fill="both", expand=True, padx=(0, 15))
        
        # RIGHT COLUMN - Component Selection
        right_col = tk.Frame(columns_frame, bg=self.bg_card)
        right_col.pack(side="left", fill="both", expand=True)
        
        # Drill-down selection frame (LEFT COLUMN)
        tk.Label(
            left_col,
            text="Configuration",
            font=("Segoe UI", 10, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(0, 5))
        
        selection_frame = tk.Frame(left_col, bg=self.bg_card)
        selection_frame.pack(fill="x", pady=(0, 15))
        
        # Pipe Schedule
        tk.Label(
            selection_frame,
            text="Pipe Schedule",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).grid(row=0, column=0, sticky="w", pady=(5, 2))
        
        self.pkg_schedule_var = tk.StringVar(value="Schedule 40")
        schedule_dropdown = ttk.Combobox(
            selection_frame,
            textvariable=self.pkg_schedule_var,
            values=["Schedule 5", "Schedule 10", "Schedule 20", "Schedule 30", "Schedule 40", 
                    "Schedule 60", "Schedule 80", "Schedule 100", "Schedule 120", "Schedule 140", 
                    "Schedule 160", "STD", "XS", "XXS"],
            state="readonly",
            width=28
        )
        schedule_dropdown.grid(row=1, column=0, sticky="w", pady=(0, 10))
        schedule_dropdown.bind("<<ComboboxSelected>>", lambda e: self._update_pkg_sizes())
        
        # Pipe Size
        tk.Label(
            selection_frame,
            text="Pipe Size (NPS)",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).grid(row=2, column=0, sticky="w", pady=(5, 2))
        
        self.pkg_size_var = tk.StringVar(value="4")
        self.pkg_size_dropdown = ttk.Combobox(
            selection_frame,
            textvariable=self.pkg_size_var,
            values=["1/2", "3/4", "1", "1-1/4", "1-1/2", "2", "2-1/2", "3", "4", "6", "8", "10", "12", "14", "16", "18", "20", "24"],
            state="readonly",
            width=28
        )
        self.pkg_size_dropdown.grid(row=3, column=0, sticky="w", pady=(0, 10))
        self.pkg_size_dropdown.bind("<<ComboboxSelected>>", lambda e: self._update_pkg_flange_types())
        
        # Flange Type
        tk.Label(
            selection_frame,
            text="Flange Type",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).grid(row=4, column=0, sticky="w", pady=(5, 2))
        
        self.pkg_flange_type_var = tk.StringVar(value="Weld Neck")
        self.pkg_flange_type_dropdown = ttk.Combobox(
            selection_frame,
            textvariable=self.pkg_flange_type_var,
            values=["Weld Neck", "Slip-On", "Socket Weld", "Threaded", "Blind", "Lap Joint"],
            state="readonly",
            width=28
        )
        self.pkg_flange_type_dropdown.grid(row=5, column=0, sticky="w", pady=(0, 10))
        self.pkg_flange_type_dropdown.bind("<<ComboboxSelected>>", lambda e: self._update_pkg_classes())
        
        # Pressure Class
        tk.Label(
            selection_frame,
            text="Pressure Class",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).grid(row=6, column=0, sticky="w", pady=(5, 2))
        
        self.pkg_class_var = tk.StringVar(value="150")
        self.pkg_class_dropdown = ttk.Combobox(
            selection_frame,
            textvariable=self.pkg_class_var,
            values=["150", "300", "400", "600", "900", "1500", "2500"],
            state="readonly",
            width=28
        )
        self.pkg_class_dropdown.grid(row=7, column=0, sticky="w", pady=(0, 10))
        self.pkg_class_dropdown.bind("<<ComboboxSelected>>", lambda e: self._update_pkg_facings())
        
        # Facing Type
        tk.Label(
            selection_frame,
            text="Facing Type",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).grid(row=8, column=0, sticky="w", pady=(5, 2))
        
        self.pkg_facing_var = tk.StringVar(value="RF")
        self.pkg_facing_dropdown = ttk.Combobox(
            selection_frame,
            textvariable=self.pkg_facing_var,
            values=["RF", "RTJ"],
            state="readonly",
            width=28
        )
        self.pkg_facing_dropdown.grid(row=9, column=0, sticky="w", pady=(0, 15))
        
        # Component Selection Section (RIGHT COLUMN)
        tk.Label(
            right_col,
            text="Components to Generate",
            font=("Segoe UI", 10, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(0, 5))
        
        components_frame = tk.Frame(right_col, bg=self.bg_card)
        components_frame.pack(fill="x", pady=(0, 10))
        
        # Component checkboxes
        self.pkg_pipe_var = tk.BooleanVar(value=True)
        tk.Checkbutton(
            components_frame,
            text="Pipe Segment (12\" length)",
            variable=self.pkg_pipe_var,
            bg=self.bg_card,
            fg=self.text_primary,
            selectcolor=self.bg_dark,
            activebackground=self.bg_card,
            activeforeground=self.text_primary
        ).grid(row=0, column=0, sticky="w", pady=2)
        
        self.pkg_flange_var = tk.BooleanVar(value=True)
        tk.Checkbutton(
            components_frame,
            text="Flange (2 qty)",
            variable=self.pkg_flange_var,
            bg=self.bg_card,
            fg=self.text_primary,
            selectcolor=self.bg_dark,
            activebackground=self.bg_card,
            activeforeground=self.text_primary
        ).grid(row=1, column=0, sticky="w", pady=2)
        
        self.pkg_blind_var = tk.BooleanVar(value=False)
        tk.Checkbutton(
            components_frame,
            text="Blind Flange (1 qty, for testing)",
            variable=self.pkg_blind_var,
            bg=self.bg_card,
            fg=self.text_primary,
            selectcolor=self.bg_dark,
            activebackground=self.bg_card,
            activeforeground=self.text_primary
        ).grid(row=2, column=0, sticky="w", pady=2)
        
        self.pkg_gasket_var = tk.BooleanVar(value=True)
        tk.Checkbutton(
            components_frame,
            text="Gasket (2 qty)",
            variable=self.pkg_gasket_var,
            bg=self.bg_card,
            fg=self.text_primary,
            selectcolor=self.bg_dark,
            activebackground=self.bg_card,
            activeforeground=self.text_primary
        ).grid(row=3, column=0, sticky="w", pady=2)
        
        self.pkg_studs_var = tk.BooleanVar(value=True)
        tk.Checkbutton(
            components_frame,
            text="Studs (full set)",
            variable=self.pkg_studs_var,
            bg=self.bg_card,
            fg=self.text_primary,
            selectcolor=self.bg_dark,
            activebackground=self.bg_card,
            activeforeground=self.text_primary
        ).grid(row=4, column=0, sticky="w", pady=2)
        
        self.pkg_nuts_var = tk.BooleanVar(value=True)
        tk.Checkbutton(
            components_frame,
            text="Heavy Hex Nuts (2 per stud)",
            variable=self.pkg_nuts_var,
            bg=self.bg_card,
            fg=self.text_primary,
            selectcolor=self.bg_dark,
            activebackground=self.bg_card,
            activeforeground=self.text_primary
        ).grid(row=5, column=0, sticky="w", pady=2)
        
        # Select All button
        select_all_btn = tk.Button(
            components_frame,
            text="Select All",
            font=("Segoe UI", 8),
            bg=self.bg_dark,
            fg=self.text_primary,
            activebackground=self.accent,
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=10,
            pady=5,
            command=self._select_all_pkg_components
        )
        select_all_btn.grid(row=6, column=0, sticky="w", pady=(10, 0))
        
        # Generate button (RIGHT COLUMN)
        self.pkg_complete_btn = tk.Button(
            right_col,
            text="⚙️ Generate Complete Package",
            font=("Segoe UI", 10, "bold"),
            bg=self.accent,
            fg="white",
            activebackground="#059669",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=12,
            command=self._generate_pkg_complete
        )
        self.pkg_complete_btn.pack(fill="x", pady=(10, 0))
        
    def _update_pkg_sizes(self):
        """Update available pipe sizes based on schedule (Phase 1 - UI only)"""
        pass  # Phase 2 will implement actual filtering
        
    def _update_pkg_flange_types(self):
        """Update available flange types based on size (Phase 1 - UI only)"""
        pass  # Phase 2 will implement actual filtering
        
    def _update_pkg_classes(self):
        """Update available classes based on flange type (Phase 1 - UI only)"""
        pass  # Phase 2 will implement actual filtering
        
    def _update_pkg_facings(self):
        """Update available facing types based on class (Phase 1 - UI only)"""
        pass  # Phase 2 will implement actual filtering
        
    def _select_all_pkg_components(self):
        """Select all component checkboxes"""
        self.pkg_pipe_var.set(True)
        self.pkg_flange_var.set(True)
        self.pkg_blind_var.set(True)
        self.pkg_gasket_var.set(True)
        self.pkg_studs_var.set(True)
        self.pkg_nuts_var.set(True)
        
    def _generate_pkg_individual(self):
        """Generate selected components as individual files (Phase 2 implementation)"""
        self.status_var.set("⚠️ Phase 1: UI only - Generation logic coming in Phase 2")
        
    def _generate_pkg_complete(self):
        """Generate complete package in organized folder (Phase 2 implementation)"""
        self.status_var.set("⚠️ Phase 1: UI only - Generation logic coming in Phase 2")
    
    def _show_flow_calculator_options(self):
        """Flow and pressure calculator for pipe sizing - ENHANCED WORKFLOW
        
        Proper engineering workflow:
        1. WHAT - Select fluid category/type → get properties & velocity limits
        2. HOW MUCH - Enter min/max flow rates (design point = 70% of max)
        3. CALCULATE SIZE - Recommend pipe sizes based on velocity limits
        4. CONFIRM/ADJUST - User picks pipe size, schedule, material, flange class
        5. ADD FITTINGS - Build list with K-factors for pressure drop
        6. VERIFY - Show min/design/max conditions, warnings
        7. GENERATE - Create CAD parts
        """
        
        # Import enhanced calculator
        from flow_calculator_enhanced import FluidProperties, PipeData, FlowCalculator
        
        # Title and description
        tk.Label(
            self.options_frame,
            text="🌊 Pipe Flow & Sizing Calculator",
            font=("Segoe UI", 11, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        tk.Label(
            self.options_frame,
            text="Specify requirements → Get recommended pipe size → Add fittings → Verify system → Generate parts",
            font=("Segoe UI", 9),
            bg=self.bg_card,
            fg=self.text_secondary,
            wraplength=900,
            justify="left"
        ).pack(anchor="w", pady=(0, 10))
        
        # Three-column layout
        columns_frame = tk.Frame(self.options_frame, bg=self.bg_card)
        columns_frame.pack(fill="both", expand=True)
        
        # LEFT COLUMN - Input parameters (REQUIREMENTS)
        left_frame = tk.Frame(columns_frame, bg=self.bg_card)
        left_frame.pack(side="left", fill="y", padx=(0, 15))
        
        # MIDDLE COLUMN - Results & Recommendations
        middle_frame = tk.Frame(columns_frame, bg=self.bg_card)
        middle_frame.pack(side="left", fill="both", expand=True, padx=(0, 15))
        
        # RIGHT COLUMN - Fittings & Generation
        right_frame = tk.Frame(columns_frame, bg=self.bg_card)
        right_frame.pack(side="left", fill="y")
        
        # ========== STEP 1: FLUID SELECTION (WHAT) ==========
        params_frame = tk.Frame(left_frame, bg=self.bg_card)
        params_frame.pack(fill="both", expand=True)
        
        tk.Label(
            params_frame,
            text="STEP 1: Select Fluid",
            font=("Segoe UI", 10, "bold"),
            bg=self.bg_card,
            fg=self.accent
        ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 5))
        
        # Fluid Category dropdown
        tk.Label(
            params_frame,
            text="Category:",
            font=("Segoe UI", 9),
            bg=self.bg_card,
            fg=self.text_primary
        ).grid(row=1, column=0, sticky="w", padx=(0, 5))
        
        self.fluid_category_var = tk.StringVar(value="Water")
        fluid_categories = list(FluidProperties.get_fluids_by_category().keys())
        self.fluid_category_combo = ttk.Combobox(
            params_frame,
            textvariable=self.fluid_category_var,
            values=fluid_categories,
            state="readonly",
            width=18
        )
        self.fluid_category_combo.grid(row=1, column=1, sticky="w", pady=(0, 5))
        
        # Fluid Type dropdown (updates based on category)
        tk.Label(
            params_frame,
            text="Fluid:",
            font=("Segoe UI", 9),
            bg=self.bg_card,
            fg=self.text_primary
        ).grid(row=2, column=0, sticky="w", padx=(0, 5))
        
        self.fluid_type_var = tk.StringVar(value="Fresh Water")
        initial_fluids = FluidProperties.get_fluids_by_category().get("Water", ["Fresh Water"])
        self.fluid_type_combo = ttk.Combobox(
            params_frame,
            textvariable=self.fluid_type_var,
            values=initial_fluids,
            state="readonly",
            width=25
        )
        self.fluid_type_combo.grid(row=2, column=1, sticky="w", pady=(0, 5))
        
        # Update fluid dropdown when category changes
        def on_category_change(*args):
            category = self.fluid_category_var.get()
            fluids = FluidProperties.get_fluids_by_category().get(category, [])
            self.fluid_type_combo['values'] = fluids
            if fluids:
                self.fluid_type_var.set(fluids[0])
            self._update_fluid_properties_display()
        
        self.fluid_category_var.trace_add("write", on_category_change)
        self.fluid_type_var.trace_add("write", lambda *args: self._update_fluid_properties_display())
        
        # Fluid properties display panel
        self.fluid_props_frame = tk.Frame(params_frame, bg=self.bg_dark, relief="groove", bd=1)
        self.fluid_props_frame.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(5, 10))
        
        self.fluid_props_label = tk.Label(
            self.fluid_props_frame,
            text="Density: 62.4 lb/ft³  |  Viscosity: 1.12 cP\nMax Velocity: 10 ft/s (Liquids)",
            font=("Consolas", 8),
            bg=self.bg_dark,
            fg=self.text_secondary,
            justify="left",
            padx=5,
            pady=3
        )
        self.fluid_props_label.pack(anchor="w")
        
        # ========== STEP 2: OPERATING CONDITIONS ==========
        tk.Label(
            params_frame,
            text="STEP 2: Operating Conditions",
            font=("Segoe UI", 10, "bold"),
            bg=self.bg_card,
            fg=self.accent
        ).grid(row=4, column=0, columnspan=2, sticky="w", pady=(10, 5))
        
        # Temperature
        temp_frame = tk.Frame(params_frame, bg=self.bg_card)
        temp_frame.grid(row=5, column=0, columnspan=2, sticky="w", pady=(0, 5))
        
        tk.Label(temp_frame, text="Temp:", font=("Segoe UI", 9), bg=self.bg_card, fg=self.text_primary).pack(side="left", padx=(0, 5))
        self.temp_var = tk.StringVar(value="100")
        ttk.Entry(temp_frame, textvariable=self.temp_var, width=8).pack(side="left", padx=(0, 3))
        self.temp_unit_var = tk.StringVar(value="°F")
        ttk.Combobox(temp_frame, textvariable=self.temp_unit_var, values=["°F", "°C"], state="readonly", width=4).pack(side="left", padx=(0, 10))
        
        tk.Label(temp_frame, text="Pressure:", font=("Segoe UI", 9), bg=self.bg_card, fg=self.text_primary).pack(side="left", padx=(0, 5))
        self.pressure_var = tk.StringVar(value="150")
        ttk.Entry(temp_frame, textvariable=self.pressure_var, width=8).pack(side="left", padx=(0, 3))
        self.pressure_unit_var = tk.StringVar(value="PSI")
        ttk.Combobox(temp_frame, textvariable=self.pressure_unit_var, values=["PSI", "bar", "kPa"], state="readonly", width=5).pack(side="left")
        
        # ========== STEP 3: FLOW RANGE (HOW MUCH) ==========
        tk.Label(
            params_frame,
            text="STEP 3: Flow Range",
            font=("Segoe UI", 10, "bold"),
            bg=self.bg_card,
            fg=self.accent
        ).grid(row=6, column=0, columnspan=2, sticky="w", pady=(10, 5))
        
        # Min/Max flow inputs
        flow_range_frame = tk.Frame(params_frame, bg=self.bg_card)
        flow_range_frame.grid(row=7, column=0, columnspan=2, sticky="w", pady=(0, 5))
        
        tk.Label(flow_range_frame, text="Min:", font=("Segoe UI", 9), bg=self.bg_card, fg=self.text_primary).pack(side="left", padx=(0, 3))
        self.flow_min_var = tk.StringVar(value="50")
        ttk.Entry(flow_range_frame, textvariable=self.flow_min_var, width=8).pack(side="left", padx=(0, 10))
        
        tk.Label(flow_range_frame, text="Max:", font=("Segoe UI", 9), bg=self.bg_card, fg=self.text_primary).pack(side="left", padx=(0, 3))
        self.flow_max_var = tk.StringVar(value="150")
        ttk.Entry(flow_range_frame, textvariable=self.flow_max_var, width=8).pack(side="left", padx=(0, 5))
        
        self.flow_unit_var = tk.StringVar(value="GPM")
        ttk.Combobox(flow_range_frame, textvariable=self.flow_unit_var, values=["GPM", "GPH", "BBL/D", "CFM", "L/min", "m³/hr"], state="readonly", width=8).pack(side="left")
        
        # Design point note
        tk.Label(
            params_frame,
            text="Design point = 70% of max (process engineering standard)",
            font=("Segoe UI", 8, "italic"),
            bg=self.bg_card,
            fg=self.text_secondary
        ).grid(row=8, column=0, columnspan=2, sticky="w", pady=(0, 10))
        
        # ========== STEP 4: PIPE MATERIAL GRADE ==========
        tk.Label(
            params_frame,
            text="STEP 4: Pipe Material Grade",
            font=("Segoe UI", 10, "bold"),
            bg=self.bg_card,
            fg=self.accent
        ).grid(row=9, column=0, columnspan=2, sticky="w", pady=(5, 5))
        
        # Material Grade Category dropdown
        mat_cat_frame = tk.Frame(params_frame, bg=self.bg_card)
        mat_cat_frame.grid(row=10, column=0, columnspan=2, sticky="w", pady=(0, 5))
        
        tk.Label(mat_cat_frame, text="Type:", font=("Segoe UI", 9), bg=self.bg_card, fg=self.text_primary).pack(side="left", padx=(0, 5))
        
        self.mat_grade_category_var = tk.StringVar(value="Carbon Steel")
        mat_categories = list(FluidProperties.get_material_grades_by_category().keys())
        self.mat_grade_category_combo = ttk.Combobox(
            mat_cat_frame,
            textvariable=self.mat_grade_category_var,
            values=mat_categories,
            state="readonly",
            width=15
        )
        self.mat_grade_category_combo.pack(side="left", padx=(0, 10))
        
        # Material Grade dropdown
        tk.Label(mat_cat_frame, text="Grade:", font=("Segoe UI", 9), bg=self.bg_card, fg=self.text_primary).pack(side="left", padx=(0, 5))
        
        self.mat_grade_var = tk.StringVar(value="A106 Gr B (Carbon Steel)")
        initial_grades = FluidProperties.get_material_grades_by_category().get("Carbon Steel", [])
        self.mat_grade_combo = ttk.Combobox(
            mat_cat_frame,
            textvariable=self.mat_grade_var,
            values=initial_grades,
            state="readonly",
            width=25
        )
        self.mat_grade_combo.pack(side="left")
        
        # Update grade dropdown when category changes
        def on_mat_category_change(*args):
            category = self.mat_grade_category_var.get()
            grades = FluidProperties.get_material_grades_by_category().get(category, [])
            self.mat_grade_combo['values'] = grades
            if grades:
                self.mat_grade_var.set(grades[0])
            self._update_material_properties_display()
        
        self.mat_grade_category_var.trace_add("write", on_mat_category_change)
        self.mat_grade_var.trace_add("write", lambda *args: self._update_material_properties_display())
        
        # Material properties display panel
        self.mat_props_frame = tk.Frame(params_frame, bg=self.bg_dark, relief="groove", bd=1)
        self.mat_props_frame.grid(row=11, column=0, columnspan=2, sticky="ew", pady=(5, 5))
        
        self.mat_props_label = tk.Label(
            self.mat_props_frame,
            text="Spec: ASTM A106 Gr B | Temp: -20 to 800°F\nS=20,000 psi @ 100°F | CA=0.0625\"",
            font=("Consolas", 8),
            bg=self.bg_dark,
            fg=self.text_secondary,
            justify="left",
            padx=5,
            pady=3
        )
        self.mat_props_label.pack(anchor="w")
        
        # Pipe Roughness (for friction calculation)
        rough_frame = tk.Frame(params_frame, bg=self.bg_card)
        rough_frame.grid(row=12, column=0, columnspan=2, sticky="w", pady=(5, 5))
        
        tk.Label(rough_frame, text="Surface:", font=("Segoe UI", 9), bg=self.bg_card, fg=self.text_primary).pack(side="left", padx=(0, 5))
        
        self.pipe_material_var = tk.StringVar(value="Carbon Steel (New)")
        pipe_materials = FluidProperties.get_pipe_material_list()
        ttk.Combobox(
            rough_frame,
            textvariable=self.pipe_material_var,
            values=pipe_materials,
            state="readonly",
            width=22
        ).pack(side="left")
        
        self.roughness_label = tk.Label(
            rough_frame,
            text="ε=0.0018\"",
            font=("Consolas", 8),
            bg=self.bg_card,
            fg=self.text_secondary
        )
        self.roughness_label.pack(side="left", padx=(5, 0))
        
        # Update roughness display when material changes
        def on_material_change(*args):
            material = self.pipe_material_var.get()
            roughness_data = FluidProperties.get_pipe_roughness(material)
            # get_pipe_roughness returns (roughness_inches, description)
            roughness = roughness_data[0] if isinstance(roughness_data, tuple) else roughness_data
            self.roughness_label.config(text=f"ε={roughness:.4f}\"")
        self.pipe_material_var.trace_add("write", on_material_change)
        
        # ========== CALCULATE BUTTON ==========
        calc_btn = tk.Button(
            params_frame,
            text="🔍 Calculate Recommended Pipe Size",
            font=("Segoe UI", 10, "bold"),
            bg=self.accent,
            fg="white",
            activebackground="#059669",
            activeforeground="white",
            relief="raised",
            bd=2,
            cursor="hand2",
            padx=15,
            pady=8,
            command=self._calculate_pipe_sizing
        )
        calc_btn.grid(row=13, column=0, columnspan=2, sticky="ew", pady=(10, 5))
        
        # ========== BYPASS MODE - Skip calculations, just generate ==========
        bypass_frame = tk.Frame(params_frame, bg="#374151", relief="groove", bd=1)
        bypass_frame.grid(row=14, column=0, columnspan=2, sticky="ew", pady=(10, 5))
        
        self.bypass_mode_var = tk.BooleanVar(value=False)
        bypass_check = tk.Checkbutton(
            bypass_frame,
            text="⚡ BYPASS MODE - Skip calculations, just generate",
            variable=self.bypass_mode_var,
            font=("Segoe UI", 9, "bold"),
            bg="#374151",
            fg="#fbbf24",
            selectcolor="#374151",
            activebackground="#374151",
            activeforeground="#fbbf24",
            command=self._toggle_bypass_mode
        )
        bypass_check.pack(anchor="w", padx=5, pady=5)
        
        # Bypass mode controls (hidden by default)
        self.bypass_controls_frame = tk.Frame(bypass_frame, bg="#374151")
        
        # NPS dropdown
        bypass_row1 = tk.Frame(self.bypass_controls_frame, bg="#374151")
        bypass_row1.pack(fill="x", padx=5, pady=2)
        
        tk.Label(bypass_row1, text="NPS:", font=("Segoe UI", 9), bg="#374151", fg=self.text_primary).pack(side="left", padx=(0, 5))
        self.bypass_nps_var = tk.StringVar(value="4")
        ttk.Combobox(
            bypass_row1,
            textvariable=self.bypass_nps_var,
            values=["1/2", "3/4", "1", "1-1/4", "1-1/2", "2", "2-1/2", "3", "4", "6", "8", "10", "12", "14", "16", "18", "20", "24"],
            state="readonly",
            width=8
        ).pack(side="left", padx=(0, 15))
        
        tk.Label(bypass_row1, text="Schedule:", font=("Segoe UI", 9), bg="#374151", fg=self.text_primary).pack(side="left", padx=(0, 5))
        self.bypass_schedule_var = tk.StringVar(value="40")
        ttk.Combobox(
            bypass_row1,
            textvariable=self.bypass_schedule_var,
            values=["5", "10", "20", "30", "STD", "40", "60", "XS", "80", "100", "120", "140", "160", "XXS"],
            state="readonly",
            width=8
        ).pack(side="left")
        
        # Generate button for bypass mode
        self.bypass_gen_btn = tk.Button(
            self.bypass_controls_frame,
            text="⚙️ Generate Selected Size",
            font=("Segoe UI", 9, "bold"),
            bg="#f59e0b",
            fg="black",
            activebackground="#d97706",
            activeforeground="black",
            relief="flat",
            cursor="hand2",
            padx=10,
            pady=5,
            command=self._generate_bypass_mode
        )
        self.bypass_gen_btn.pack(fill="x", padx=5, pady=(5, 5))
        
        # ========== MIDDLE COLUMN: RESULTS ==========
        tk.Label(
            middle_frame,
            text="Pipe Size Recommendations",
            font=("Segoe UI", 10, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(0, 5))
        
        self.flow_results_frame = tk.Frame(middle_frame, bg=self.bg_dark, relief="groove", bd=2)
        self.flow_results_frame.pack(fill="both", expand=True, pady=(0, 10))
        
        self.flow_results_text = tk.Text(
            self.flow_results_frame,
            height=18,
            width=55,
            bg=self.bg_dark,
            fg=self.text_primary,
            font=("Consolas", 9),
            relief="flat",
            padx=10,
            pady=10,
            wrap="word"
        )
        self.flow_results_text.pack(fill="both", expand=True)
        
        # Initial message with new workflow
        self.flow_results_text.insert("1.0", 
            "PIPE SIZING CALCULATOR - Enhanced Workflow\n" +
            "═" * 45 + "\n\n" +
            "1. SELECT FLUID - Choose category and fluid type\n" +
            "2. SET CONDITIONS - Temperature and pressure\n" +
            "3. ENTER FLOW RANGE - Min and max flow rates\n" +
            "4. SELECT MATERIAL - Pipe material for friction\n" +
            "5. CLICK CALCULATE - Get recommended sizes\n\n" +
            "Results will show:\n" +
            "• Recommended pipe size (NPS) with velocity check\n" +
            "• Velocity at MIN, DESIGN (70%), and MAX flow\n" +
            "• Pressure drop per 100 ft at each condition\n" +
            "• Warnings for out-of-range conditions\n\n" +
            "After calculation, add fittings and generate parts!")
        self.flow_results_text.config(state="disabled")
        
        # ========== RIGHT COLUMN: FITTINGS & GENERATION ==========
        tk.Label(
            right_frame,
            text="Fittings & Generation",
            font=("Segoe UI", 10, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(0, 5))
        
        self.flow_gen_frame = tk.Frame(right_frame, bg=self.bg_card)
        self.flow_gen_frame.pack(fill="both", expand=True, pady=(0, 0))
        
        # Initial placeholder message
        tk.Label(
            self.flow_gen_frame,
            text="Run calculation to unlock\nfittings builder & generation",
            font=("Segoe UI", 9),
            bg=self.bg_card,
            fg=self.text_secondary,
            justify="center"
        ).pack(pady=50)
    
    def _update_fluid_properties_display(self):
        """Update the fluid properties display when fluid selection changes"""
        try:
            from flow_calculator_enhanced import FluidProperties, FlowCalculator
            fluid = self.fluid_type_var.get()
            
            # Get temperature in °F
            temp = float(self.temp_var.get()) if hasattr(self, 'temp_var') else 100
            temp_unit = self.temp_unit_var.get() if hasattr(self, 'temp_unit_var') else "°F"
            temp_f = temp if temp_unit == "°F" else (temp * 9/5) + 32
            
            # Get fluid properties
            props = FluidProperties.get_properties(fluid, temp_f, 150)  # Use 150 psi default
            density = props['density']
            viscosity = props['viscosity']
            
            # Get velocity limit
            max_vel, reason = FlowCalculator.get_max_velocity_for_fluid(fluid, density)
            
            # Update display
            props_text = f"ρ: {density:.2f} lb/ft³  |  μ: {viscosity:.2f} cP\n"
            props_text += f"Max V: {max_vel:.0f} ft/s ({reason})"
            self.fluid_props_label.config(text=props_text)
        except Exception as e:
            self.fluid_props_label.config(text=f"Select a fluid to see properties")
    
    def _update_material_properties_display(self):
        """Update the material properties display when grade selection changes"""
        try:
            from flow_calculator_enhanced import FluidProperties
            grade = self.mat_grade_var.get()
            
            # Get temperature in °F
            temp = float(self.temp_var.get()) if hasattr(self, 'temp_var') else 100
            temp_unit = self.temp_unit_var.get() if hasattr(self, 'temp_unit_var') else "°F"
            temp_f = temp if temp_unit == "°F" else (temp * 9/5) + 32
            
            # Get material properties
            mat_props = FluidProperties.get_material_properties(grade, temp_f)
            
            # Update display
            props_text = f"Spec: {mat_props.get('spec', 'N/A')} | Temp: {mat_props['min_temp_f']} to {mat_props['max_temp_f']}°F\n"
            props_text += f"S={mat_props['allowable_stress']:,.0f} psi @ {temp_f:.0f}°F | CA={mat_props['corrosion_allowance']}\""
            self.mat_props_label.config(text=props_text)
        except Exception as e:
            self.mat_props_label.config(text=f"Select a material grade")
    
    def _toggle_bypass_mode(self):
        """Show/hide bypass mode controls"""
        if self.bypass_mode_var.get():
            # Show bypass controls
            self.bypass_controls_frame.pack(fill="x", padx=5, pady=(0, 5))
        else:
            # Hide bypass controls
            self.bypass_controls_frame.pack_forget()
    
    def _generate_bypass_mode(self):
        """Generate pipe directly without flow calculations - BYPASS MODE"""
        from datetime import datetime
        
        nps = self.bypass_nps_var.get()
        schedule = self.bypass_schedule_var.get()
        mat_grade = self.mat_grade_var.get() if hasattr(self, 'mat_grade_var') else "A106 Gr B"
        
        # Convert NPS to float
        if '/' in nps:
            if '-' in nps:  # e.g., "1-1/4"
                parts = nps.split('-')
                nps_float = float(parts[0]) + float(eval(parts[1]))
            else:  # e.g., "1/2"
                nps_float = float(eval(nps))
        else:
            nps_float = float(nps)
        
        # Create a fake recommendation for the generation system
        self.flow_recommendation = {
            'size': nps,
            'schedule': schedule,
            'id': 0,  # Will be looked up
            'vel_design': 0,
            'rating': 0,
            'bypass_mode': True
        }
        self.flow_operating_pressure = float(self.pressure_var.get()) if hasattr(self, 'pressure_var') else 150
        self.flow_temp_f = float(self.temp_var.get()) if hasattr(self, 'temp_var') else 100
        
        # Update results text
        self.flow_results_text.config(state="normal")
        self.flow_results_text.delete("1.0", "end")
        self.flow_results_text.insert("end", "═══ BYPASS MODE ═══\n\n")
        self.flow_results_text.insert("end", f"⚡ Skipping flow calculations\n\n")
        self.flow_results_text.insert("end", f"Selected:\n")
        self.flow_results_text.insert("end", f"  NPS: {nps}\"\n")
        self.flow_results_text.insert("end", f"  Schedule: {schedule}\n")
        self.flow_results_text.insert("end", f"  Material: {mat_grade}\n\n")
        self.flow_results_text.insert("end", f"⚠️ No velocity/pressure drop verification\n")
        self.flow_results_text.insert("end", f"   Use for known good designs only\n\n")
        self.flow_results_text.insert("end", f"Ready to generate components →\n")
        self.flow_results_text.config(state="disabled")
        
        # Show generation options
        self._show_flow_generation_options()
        
        self.status_var.set(f"✓ Bypass mode: {nps}\" Sch {schedule} ready to generate")
    
    def _on_flow_class_change(self, event=None):
        """Handle flange class change - update available flange types and show warnings"""
        new_class = self.flow_flange_class_var.get()
        
        # Update available flange types for this class
        if hasattr(self, 'flange_types_by_class') and hasattr(self, 'flow_flange_type_combo'):
            available_types = self.flange_types_by_class.get(new_class, ["Weld Neck"])
            self.flow_flange_type_combo['values'] = available_types
            
            # If current selection not available, reset to Weld Neck
            if self.flow_flange_type_var.get() not in available_types:
                self.flow_flange_type_var.set("Weld Neck")
        
        # Update the class warning label
        if hasattr(self, 'flow_class_warning_label') and hasattr(self, 'flange_ratings'):
            operating_pressure = getattr(self, 'flow_operating_pressure', 150)
            avg_temp_f = getattr(self, 'flow_avg_temp', 100)
            required_class = getattr(self, 'flow_required_class', "150")
            
            rating = self.flange_ratings.get(new_class, 285)
            
            # Check if selected class is adequate for pressure
            class_order = ["150", "300", "600", "900", "1500", "2500"]
            selected_idx = class_order.index(new_class) if new_class in class_order else 0
            required_idx = class_order.index(required_class) if required_class in class_order else 0
            
            if selected_idx < required_idx:
                # User selected a LOWER class than required - show RED warning
                self.flow_class_warning_label.config(
                    text=f"⚠ WARNING: Class {new_class} ({rating} psi) < Required ({operating_pressure:.0f} psi)!",
                    fg="#dc2626"  # Red
                )
            elif selected_idx > required_idx:
                # User selected HIGHER class - that's fine, show green
                self.flow_class_warning_label.config(
                    text=f"✓ Class {new_class} ({rating} psi) exceeds requirement",
                    fg="#10b981"  # Green
                )
            else:
                # Exact match
                self.flow_class_warning_label.config(
                    text=f"→ Class {new_class} ({rating} psi rated @ {avg_temp_f:.0f}°F)",
                    fg=self.text_secondary
                )
    
    def _update_fittings_estimate(self):
        """Calculate estimated pressure drop from fittings + pipe"""
        try:
            # Get velocity and pipe data from current state
            velocity = getattr(self, 'fittings_velocity', 0)
            pipe_id = getattr(self, 'fittings_pipe_id', 0)
            dp_per_100ft = getattr(self, 'fittings_dp_per_100ft', 0)
            
            # Ensure values are floats, not tuples
            if isinstance(velocity, tuple):
                velocity = float(velocity[0]) if velocity else 0
            if isinstance(pipe_id, tuple):
                pipe_id = float(pipe_id[0]) if pipe_id else 0
            if isinstance(dp_per_100ft, tuple):
                dp_per_100ft = float(dp_per_100ft[0]) if dp_per_100ft else 0
            
            # Get pipe length
            try:
                pipe_length = float(self.pipe_length_var.get())
            except:
                pipe_length = 100.0
            
            # Sum total K-factor from all fittings
            total_k = 0
            fitting_counts = []
            for name, data in self.fitting_estimates.items():
                var = data.get('var')
                if var is None:
                    continue  # Skip if spinbox not created yet
                qty = var.get()
                k = data['k']
                if qty > 0:
                    total_k += qty * k
                    fitting_counts.append(f"  {qty}× {name} (K={k:.2f} each)")
            
            if velocity <= 0 or pipe_id <= 0:
                # No flow data yet - show basic K summary
                summary = "═══ FITTINGS ESTIMATE ═══\n\n"
                summary += "⚠️ Run Flow Calculation first!\n\n"
                summary += f"Total K-factor: {total_k:.2f}\n\n"
                if fitting_counts:
                    summary += "Selected fittings:\n"
                    for fc in fitting_counts:
                        summary += fc + "\n"
                else:
                    summary += "No fittings selected\n"
                
                self.fittings_summary_label.config(text=summary)
                return
            
            # Calculate fittings pressure drop using: ΔP = K × ρ × v² / (2 × 144 × g)
            # Simplified for water at ~62.4 lb/ft³: ΔP ≈ K × v² / 148.8 (psi)
            # More accurate formula: h = K × v²/(2g) ft of head, then convert to psi
            
            gravity = 32.174  # ft/s²
            velocity_fps = velocity  # Already in ft/s
            density = 62.4  # lb/ft³ (water at 60°F) - could be enhanced with actual fluid
            
            # Head loss from fittings (ft of head)
            head_loss_ft = total_k * (velocity_fps ** 2) / (2 * gravity)
            
            # Convert to psi: ΔP = ρ × h × g / 144 = ρ × h / 144 (for water, approx 0.433 psi/ft)
            fittings_dp = head_loss_ft * density / 144  # psi
            
            # Pipe friction pressure drop
            pipe_dp = dp_per_100ft * (pipe_length / 100)
            
            # Total system pressure drop
            total_dp = fittings_dp + pipe_dp
            
            # Calculate equivalent pipe length for fittings (based on v and dp_per_100ft)
            if dp_per_100ft > 0:
                equiv_length = (fittings_dp / dp_per_100ft) * 100
            else:
                equiv_length = 0
            
            # Build summary text
            summary = "═══ SYSTEM PRESSURE DROP ═══\n\n"
            
            if fitting_counts:
                summary += "Fittings:\n"
                for fc in fitting_counts[:6]:  # Show first 6
                    summary += fc + "\n"
                if len(fitting_counts) > 6:
                    summary += f"  ...and {len(fitting_counts)-6} more\n"
                summary += "\n"
            
            summary += f"Total K-factor:    {total_k:.2f}\n"
            summary += f"Equivalent Length: {equiv_length:.0f} ft\n\n"
            
            summary += "PRESSURE DROP:\n"
            summary += f"  Pipe ({pipe_length:.0f} ft):     {pipe_dp:.2f} psi\n"
            summary += f"  Fittings:          {fittings_dp:.2f} psi\n"
            summary += "  " + "─" * 24 + "\n"
            summary += f"  TOTAL SYSTEM:      {total_dp:.2f} psi\n\n"
            
            # Add warnings if applicable
            if total_dp > 50:
                summary += "⚠️ High ΔP - consider larger pipe\n"
            elif total_dp > 25:
                summary += "⚡ Moderate ΔP - verify acceptable\n"
            else:
                summary += "✓ Pressure drop within normal range\n"
            
            self.fittings_summary_label.config(text=summary)
            self.status_var.set(f"✓ System ΔP: {total_dp:.2f} psi (pipe: {pipe_dp:.2f} + fittings: {fittings_dp:.2f})")
            
        except Exception as e:
            self.fittings_summary_label.config(text=f"Error calculating: {str(e)}")
    
    def _update_velocity_for_fluid(self):
        """Update default max velocity based on selected fluid type with engineering limits"""
        # This is now handled by _update_fluid_properties_display()
        pass
    
    def _validate_velocity_input(self, velocity, fluid):
        """Warn user if velocity exceeds safe limits"""
        try:
            from flow_calculator_enhanced import FlowCalculator, FluidProperties
            
            # Get fluid properties
            props = FluidProperties.get_properties(fluid, 100, 150)
            density = props.get('density', 62.4)
            
            # Get industry limit for this fluid
            max_vel, reason = FlowCalculator.get_max_velocity_for_fluid(fluid, density)
            
            if velocity > max_vel * 1.5:  # 50% over limit triggers warning
                return (False, f"⚠️ {velocity:.1f} ft/s exceeds limit ({max_vel:.0f} ft/s) for {fluid}")
            elif velocity > max_vel:
                return (True, f"⚡ Above recommended ({max_vel:.0f} ft/s)")
            else:
                return (True, None)
        except:
            return (True, None)
    
    def _calculate_pipe_sizing(self):
        """Calculate optimum pipe size based on flow range and pressure parameters - ENHANCED VERSION
        
        Uses min/max flow range with design point at 70% of max.
        Shows velocity and pressure drop at all three operating points.
        """
        try:
            from flow_calculator_enhanced import FluidProperties, PipeData, FlowCalculator
            
            # Get input values with new min/max flow range
            flow_min = float(self.flow_min_var.get())
            flow_max = float(self.flow_max_var.get())
            flow_unit = self.flow_unit_var.get()
            pressure = float(self.pressure_var.get())
            pressure_unit = self.pressure_unit_var.get()
            temp = float(self.temp_var.get())
            temp_unit = self.temp_unit_var.get()
            fluid = self.fluid_type_var.get()
            pipe_material = self.pipe_material_var.get()
            
            # Calculate design point (70% of max - process engineering standard)
            flow_design = flow_max * 0.70
            
            # Convert to standard units (GPM, PSI, °F)
            def convert_flow(val):
                conversions = {"GPM": 1, "GPH": 1/60, "BBL/D": 0.0292, "CFM": 7.48, "L/min": 0.264, "m³/hr": 4.403}
                return val * conversions.get(flow_unit, 1)
            
            def convert_pressure(val):
                conversions = {"PSI": 1, "bar": 14.5, "kPa": 0.145}
                return val * conversions.get(pressure_unit, 1)
            
            flow_min_gpm = convert_flow(flow_min)
            flow_design_gpm = convert_flow(flow_design)
            flow_max_gpm = convert_flow(flow_max)
            pressure_psi = convert_pressure(pressure)
            temp_f = temp if temp_unit == "°F" else (temp * 9/5) + 32
            
            # Get fluid properties
            fluid_props = FluidProperties.get_properties(fluid, temp_f, pressure_psi)
            density = fluid_props['density']
            viscosity = fluid_props['viscosity']
            
            # Get pipe roughness (returns tuple: roughness_inches, description)
            roughness_data = FluidProperties.get_pipe_roughness(pipe_material)
            roughness = roughness_data[0] if isinstance(roughness_data, tuple) else roughness_data
            
            # Get max velocity for this fluid
            max_vel, vel_reason = FlowCalculator.get_max_velocity_for_fluid(fluid, density)
            
            # Calculate for different pipe sizes
            pipe_sizes = ["1/2", "3/4", "1", "1-1/4", "1-1/2", "2", "2-1/2", "3", "4", "6", "8", "10", "12"]
            schedules = ["40", "80", "160", "STD", "XS", "XXS"]
            
            results = []
            
            for size in pipe_sizes:
                for schedule in schedules:
                    id_inches = PipeData.get_pipe_id(size, schedule)
                    if id_inches <= 0:
                        continue
                    
                    # Calculate velocities at all three points
                    vel_min = FlowCalculator.calculate_velocity(flow_min_gpm, id_inches)
                    vel_design = FlowCalculator.calculate_velocity(flow_design_gpm, id_inches)
                    vel_max = FlowCalculator.calculate_velocity(flow_max_gpm, id_inches)
                    
                    # Calculate pressure drops
                    dp_min = FlowCalculator.calculate_pressure_drop(flow_min_gpm, id_inches, 100, density, viscosity, roughness)
                    dp_design = FlowCalculator.calculate_pressure_drop(flow_design_gpm, id_inches, 100, density, viscosity, roughness)
                    dp_max = FlowCalculator.calculate_pressure_drop(flow_max_gpm, id_inches, 100, density, viscosity, roughness)
                    
                    # Get schedule pressure rating
                    schedule_rating = FlowCalculator.get_schedule_pressure_rating(schedule, size, temp_f=temp_f)
                    
                    # Check if this size/schedule meets requirements
                    # Velocity at MAX must be <= max velocity limit
                    # Schedule must meet pressure requirement with 1.2x safety factor
                    if vel_max <= max_vel and schedule_rating >= pressure_psi * 1.2:
                        # Calculate Reynolds number at design point
                        reynolds = FlowCalculator.calculate_reynolds_number(flow_design_gpm, id_inches, density, viscosity)
                        flow_regime = FlowCalculator.get_flow_regime(reynolds)
                        
                        results.append({
                            'size': size,
                            'schedule': schedule,
                            'id': id_inches,
                            'vel_min': vel_min,
                            'vel_design': vel_design,
                            'vel_max': vel_max,
                            'dp_min': dp_min,
                            'dp_design': dp_design,
                            'dp_max': dp_max,
                            'reynolds': reynolds,
                            'flow_regime': flow_regime,
                            'rating': schedule_rating,
                            'vel_deviation': abs(vel_design - max_vel * 0.7)  # Target 70% of max velocity
                        })
            
            # Sort by velocity deviation (best match to target velocity)
            results.sort(key=lambda x: x['vel_deviation'])
            
            # Display results
            self.flow_results_text.config(state="normal")
            self.flow_results_text.delete("1.0", "end")
            
            if not results:
                self.flow_results_text.insert("end", "❌ No suitable pipe sizes found.\n\n")
                self.flow_results_text.insert("end", f"Max flow: {flow_max_gpm:.1f} GPM\n")
                self.flow_results_text.insert("end", f"Max velocity limit: {max_vel:.0f} ft/s\n")
                self.flow_results_text.insert("end", f"Pressure: {pressure_psi:.0f} psi\n\n")
                self.flow_results_text.insert("end", "Try:\n• Reducing max flow rate\n• Using a larger max velocity (if safe)\n")
            else:
                best = results[0]
                
                # Check for warnings
                vel_ok_min, warning_min = self._validate_velocity_input(best['vel_min'], fluid)
                vel_ok_design, warning_design = self._validate_velocity_input(best['vel_design'], fluid)
                vel_ok_max, warning_max = self._validate_velocity_input(best['vel_max'], fluid)
                
                self.flow_results_text.insert("end", "═══ RECOMMENDED PIPE SIZE ═══\n\n")
                self.flow_results_text.insert("end", f"  NPS: {best['size']}\"  Schedule: {best['schedule']}\n")
                self.flow_results_text.insert("end", f"  Inside Diameter: {best['id']:.3f}\"\n")
                self.flow_results_text.insert("end", f"  Pressure Rating: {best['rating']:.0f} psi (need {pressure_psi:.0f} psi)\n\n")
                
                self.flow_results_text.insert("end", "═══ OPERATING RANGE ANALYSIS ═══\n\n")
                self.flow_results_text.insert("end", f"                 MIN         DESIGN      MAX\n")
                self.flow_results_text.insert("end", f"  Flow Rate:     {flow_min_gpm:7.1f}     {flow_design_gpm:7.1f}     {flow_max_gpm:7.1f} GPM\n")
                self.flow_results_text.insert("end", f"  Velocity:      {best['vel_min']:7.2f}     {best['vel_design']:7.2f}     {best['vel_max']:7.2f} ft/s\n")
                self.flow_results_text.insert("end", f"  ΔP/100ft:      {best['dp_min']:7.3f}     {best['dp_design']:7.3f}     {best['dp_max']:7.3f} psi\n\n")
                
                # Warnings
                if warning_max:
                    self.flow_results_text.insert("end", f"  ⚠️ MAX: {warning_max}\n")
                if best['vel_min'] < 2.0 and not fluid_props.get('compressible', False):
                    self.flow_results_text.insert("end", f"  ⚠️ MIN: Low velocity ({best['vel_min']:.1f} ft/s) - settling risk\n")
                
                self.flow_results_text.insert("end", f"\n═══ FLUID PROPERTIES @ {temp_f:.0f}°F ═══\n\n")
                self.flow_results_text.insert("end", f"  {fluid}\n")
                self.flow_results_text.insert("end", f"  Density: {density:.2f} lb/ft³\n")
                self.flow_results_text.insert("end", f"  Viscosity: {viscosity:.2f} cP\n")
                self.flow_results_text.insert("end", f"  Reynolds: {best['reynolds']:.0f} ({best['flow_regime']})\n")
                self.flow_results_text.insert("end", f"  Max V: {max_vel:.0f} ft/s ({vel_reason})\n")
                
                # Alternatives
                if len(results) > 1:
                    self.flow_results_text.insert("end", f"\n═══ ALTERNATIVES ═══\n\n")
                    for i, alt in enumerate(results[1:4], 1):
                        self.flow_results_text.insert("end", f"  {i}. {alt['size']}\" Sch {alt['schedule']}: ")
                        self.flow_results_text.insert("end", f"{alt['vel_design']:.1f} ft/s @ design\n")
                
                # Store for generation
                self.flow_recommendation = best
                self.flow_operating_pressure = pressure_psi
                self.flow_temp_f = temp_f
                self.flow_fluid = fluid
                self.flow_fluid_props = fluid_props
                self.flow_min_gpm = flow_min_gpm
                self.flow_design_gpm = flow_design_gpm
                self.flow_max_gpm = flow_max_gpm
                
                # Store for fittings estimator
                self.fittings_velocity = best['vel_design']
                self.fittings_pipe_id = best['id']
                self.fittings_dp_per_100ft = best['dp_design']
                
                # Auto-update fittings estimate if section exists
                if hasattr(self, 'fittings_summary_label'):
                    self._update_fittings_estimate()
                
                # Show generation options
                self._show_flow_generation_options()
            
            self.flow_results_text.config(state="disabled")
            
        except ValueError as e:
            self.flow_results_text.config(state="normal")
            self.flow_results_text.delete("1.0", "end")
            self.flow_results_text.insert("end", f"❌ Error: Invalid input\n\n{str(e)}")
            self.flow_results_text.config(state="disabled")
        except Exception as e:
            self.flow_results_text.config(state="normal")
            self.flow_results_text.delete("1.0", "end")
            self.flow_results_text.insert("end", f"❌ Error: {str(e)}")
            self.flow_results_text.config(state="disabled")
    
    def _show_flow_generation_options(self):
        """Show generation options after calculation - with schedule selection and locked flange class"""
        if not hasattr(self, 'flow_recommendation'):
            return
        
        recommendation = self.flow_recommendation
        operating_pressure = getattr(self, 'flow_operating_pressure', 150)
        min_schedule = recommendation['schedule']
        pipe_size = recommendation['size']
        
        # Store for generation
        self.flow_pipe_size = pipe_size
        self.flow_min_schedule = min_schedule
        
        # Get temperature for pressure rating (use stored value from calculation)
        avg_temp_f = getattr(self, 'flow_temp_f', 100)
        self.flow_avg_temp = avg_temp_f
        
        # ASME B16.5 Flange pressure ratings at temperature (conservative values)
        temp_factor = 1.0
        if avg_temp_f > 100:
            if avg_temp_f <= 200:
                temp_factor = 0.95
            elif avg_temp_f <= 300:
                temp_factor = 0.90
            elif avg_temp_f <= 400:
                temp_factor = 0.85
            elif avg_temp_f <= 500:
                temp_factor = 0.75
            elif avg_temp_f <= 600:
                temp_factor = 0.65
            else:
                temp_factor = 0.55
        
        # ASME B16.5 pressure ratings at ambient temperature (psi)
        self.flange_ratings = {
            "150": int(285 * temp_factor),
            "300": int(740 * temp_factor),
            "600": int(1480 * temp_factor),
            "900": int(2220 * temp_factor),
            "1500": int(3705 * temp_factor),
            "2500": int(6170 * temp_factor)
        }
        
        # Select flange class that meets or exceeds operating pressure with safety margin
        required_rating = operating_pressure * 1.1  # 10% margin for flanges
        recommended_class = "2500"  # Default to highest
        for class_name, rating in self.flange_ratings.items():
            if rating >= required_rating:
                recommended_class = class_name
                break
        self.flow_required_class = recommended_class
        
        # Build list of schedules >= minimum (user can pick heavier)
        schedule_order = ["20", "30", "STD", "40", "60", "XS", "80", "100", "120", "140", "160", "XXS"]
        try:
            min_idx = schedule_order.index(min_schedule)
            available_schedules = schedule_order[min_idx:]
        except ValueError:
            available_schedules = [min_schedule] + schedule_order
        
        # Clear previous generation options
        for widget in self.flow_gen_frame.winfo_children():
            widget.destroy()
        
        # Title
        tk.Label(
            self.flow_gen_frame,
            text="📦 Generate Assembly Package",
            font=("Segoe UI", 11, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(0, 5))
        
        # Pipe Schedule Selection (user can pick heavier than minimum)
        schedule_frame = tk.Frame(self.flow_gen_frame, bg=self.bg_card)
        schedule_frame.pack(fill="x", pady=(0, 10))
        
        tk.Label(
            schedule_frame,
            text="Pipe Schedule:",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(side="left", padx=(0, 10))
        
        self.flow_schedule_var = tk.StringVar(value=min_schedule)
        schedule_dropdown = ttk.Combobox(
            schedule_frame,
            textvariable=self.flow_schedule_var,
            values=available_schedules,
            state="readonly",
            width=10
        )
        schedule_dropdown.pack(side="left", padx=(0, 10))
        
        tk.Label(
            schedule_frame,
            text=f"(Minimum: {min_schedule} - select heavier if desired)",
            font=("Segoe UI", 8, "italic"),
            bg=self.bg_card,
            fg=self.text_secondary
        ).pack(side="left")
        
        # Pressure/Class info (LOCKED - auto-set by schedule pressure rating)
        pressure_frame = tk.Frame(self.flow_gen_frame, bg=self.bg_card)
        pressure_frame.pack(fill="x", pady=(0, 10))
        
        tk.Label(
            pressure_frame,
            text=f"⚠ Operating: {operating_pressure:.0f} psi @ {avg_temp_f:.0f}°F",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.accent
        ).pack(side="left", padx=(0, 15))
        
        # This label will be updated when schedule changes
        self.flow_class_warning_label = tk.Label(
            pressure_frame,
            text=f"→ Flange Class {recommended_class} REQUIRED ({self.flange_ratings[recommended_class]} psi rated)",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg="#dc2626"  # Red to indicate locked/required
        )
        self.flow_class_warning_label.pack(side="left")
        
        # Flange configuration (TYPE and FACING are selectable, CLASS is locked)
        flange_config_frame = tk.Frame(self.flow_gen_frame, bg=self.bg_card)
        flange_config_frame.pack(fill="x", pady=(0, 10))
        
        tk.Label(
            flange_config_frame,
            text="Flange Type:",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).grid(row=0, column=0, sticky="w", padx=(0, 5))
        
        # Define which flange types are available for each pressure class (ASME B16.5)
        self.flange_types_by_class = {
            "150": ["Weld Neck", "Slip-On", "Socket Weld", "Threaded", "Lap Joint"],
            "300": ["Weld Neck", "Slip-On", "Socket Weld", "Threaded", "Lap Joint"],
            "600": ["Weld Neck", "Slip-On", "Socket Weld", "Threaded", "Lap Joint"],
            "900": ["Weld Neck", "Slip-On", "Socket Weld"],  # No Threaded/Lap Joint
            "1500": ["Weld Neck", "Slip-On"],  # Limited options
            "2500": ["Weld Neck"]  # Only Weld Neck (Blind added separately)
        }
        
        # Get initial available flange types based on recommended class
        initial_flange_types = self.flange_types_by_class.get(recommended_class, ["Weld Neck"])
        
        self.flow_flange_type_var = tk.StringVar(value="Weld Neck")
        self.flow_flange_type_combo = ttk.Combobox(
            flange_config_frame,
            textvariable=self.flow_flange_type_var,
            values=initial_flange_types,
            state="readonly",
            width=12
        )
        self.flow_flange_type_combo.grid(row=0, column=1, sticky="w", padx=(0, 15))
        
        tk.Label(
            flange_config_frame,
            text="Class:",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).grid(row=0, column=2, sticky="w", padx=(0, 5))
        
        # Class is now user-selectable (shows recommended but allows override)
        self.flow_flange_class_var = tk.StringVar(value=recommended_class)
        self.flow_class_combo = ttk.Combobox(
            flange_config_frame,
            textvariable=self.flow_flange_class_var,
            values=["150", "300", "600", "900", "1500", "2500"],
            state="readonly",
            width=8
        )
        self.flow_class_combo.grid(row=0, column=3, sticky="w", padx=(0, 15))
        self.flow_class_combo.bind("<<ComboboxSelected>>", self._on_flow_class_change)
        
        tk.Label(
            flange_config_frame,
            text="Facing:",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).grid(row=0, column=4, sticky="w", padx=(0, 5))
        
        self.flow_facing_var = tk.StringVar(value="RF")
        ttk.Combobox(
            flange_config_frame,
            textvariable=self.flow_facing_var,
            values=["RF", "RTJ"],
            state="readonly",
            width=5
        ).grid(row=0, column=5, sticky="w")
        
        # ============================================
        # FITTINGS ESTIMATOR - Quick ΔP estimation
        # ============================================
        fittings_frame = tk.LabelFrame(
            self.flow_gen_frame,
            text="⚡ Fittings Estimator (for ΔP)",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary,
            padx=5,
            pady=5
        )
        fittings_frame.pack(fill="x", pady=(10, 5))
        
        # Common fittings with quantity spinboxes - 2 columns
        fittings_grid = tk.Frame(fittings_frame, bg=self.bg_card)
        fittings_grid.pack(fill="x")
        
        # Define common fittings with K-factors
        self.fitting_estimates = {
            '90° Elbow LR': {'k': 0.30, 'var': None},
            '90° Elbow SR': {'k': 0.60, 'var': None},
            '45° Elbow': {'k': 0.20, 'var': None},
            'Tee (thru)': {'k': 0.20, 'var': None},
            'Tee (branch)': {'k': 1.00, 'var': None},
            'Gate Valve': {'k': 0.17, 'var': None},
            'Globe Valve': {'k': 6.00, 'var': None},
            'Ball Valve': {'k': 0.05, 'var': None},
            'Check Valve': {'k': 2.00, 'var': None},
            'Butterfly Vlv': {'k': 0.35, 'var': None},
            'Control Valve': {'k': 8.00, 'var': None},
            'Reducer': {'k': 0.10, 'var': None},
        }
        
        row = 0
        col = 0
        for fitting_name, data in self.fitting_estimates.items():
            # Label
            tk.Label(
                fittings_grid,
                text=f"{fitting_name}:",
                font=("Segoe UI", 8),
                bg=self.bg_card,
                fg=self.text_secondary,
                width=12,
                anchor="e"
            ).grid(row=row, column=col*2, sticky="e", padx=(0, 3), pady=1)
            
            # Spinbox
            var = tk.IntVar(value=0)
            data['var'] = var
            spin = ttk.Spinbox(
                fittings_grid,
                from_=0,
                to=50,
                textvariable=var,
                width=4,
                command=self._update_fittings_estimate
            )
            spin.grid(row=row, column=col*2+1, sticky="w", padx=(0, 10), pady=1)
            spin.bind('<KeyRelease>', lambda e: self._update_fittings_estimate())
            
            col += 1
            if col >= 2:
                col = 0
                row += 1
        
        # Pipe length input
        length_frame = tk.Frame(fittings_frame, bg=self.bg_card)
        length_frame.pack(fill="x", pady=(5, 0))
        
        tk.Label(
            length_frame,
            text="Est. Pipe Length:",
            font=("Segoe UI", 8),
            bg=self.bg_card,
            fg=self.text_secondary
        ).pack(side="left", padx=(0, 5))
        
        self.pipe_length_var = tk.StringVar(value="100")
        ttk.Entry(length_frame, textvariable=self.pipe_length_var, width=6).pack(side="left", padx=(0, 3))
        tk.Label(length_frame, text="ft", font=("Segoe UI", 8), bg=self.bg_card, fg=self.text_secondary).pack(side="left")
        
        # Recalculate button
        tk.Button(
            length_frame,
            text="🔄 Update",
            font=("Segoe UI", 8),
            bg=self.accent,
            fg="white",
            relief="flat",
            padx=5,
            command=self._update_fittings_estimate
        ).pack(side="left", padx=(15, 0))
        
        # Results summary
        self.fittings_summary_frame = tk.Frame(fittings_frame, bg=self.bg_dark, relief="groove", bd=1)
        self.fittings_summary_frame.pack(fill="x", pady=(5, 0))
        
        self.fittings_summary_label = tk.Label(
            self.fittings_summary_frame,
            text="Enter fitting quantities above → Total system ΔP will update",
            font=("Consolas", 8),
            bg=self.bg_dark,
            fg=self.text_secondary,
            justify="left",
            padx=5,
            pady=3
        )
        self.fittings_summary_label.pack(anchor="w")
        
        # Store reference to recommendation for calculations
        self.fittings_pipe_id = recommendation.get('id', 4.0)
        self.fittings_dp_per_100ft = recommendation.get('dp_design', 0.5)
        
        # ============================================
        # ADD ITEM SYSTEM - Replace checkboxes with smart item adder
        # ============================================
        
        # Initialize build list
        self.flow_build_list = []  # List of dicts: {type, variant, qty, details, display_text}
        
        # Get the current schedule for display
        current_schedule = min_schedule
        
        # Define available components with their variants
        # Note: Pipe/Tee use schedule as variant, not "Standard"
        self.flow_available_components = {
            "Pipe (40ft)": {"variants": [f"Sch {current_schedule}"], "max_qty": 20, "uses_schedule": True},
            "Elbow 90°": {"variants": ["LR", "SR", "3R", "5R", "10R"], "max_qty": 50},
            "Elbow 45°": {"variants": ["LR", "SR", "3R", "5R"], "max_qty": 50},
            "Elbow 22.5°": {"variants": ["LR", "SR"], "max_qty": 50},
            "180° Return": {"variants": ["LR", "SR"], "max_qty": 20},
            "Tee Equal": {"variants": [f"Sch {current_schedule}"], "max_qty": 20, "uses_schedule": True},
            "Tee Reducing": {"variants": [f"Sch {current_schedule}"], "max_qty": 20, "needs_branch_size": True, "uses_schedule": True},
            "Cross Equal": {"variants": [f"Sch {current_schedule}"], "max_qty": 20, "uses_schedule": True},
            "Reducer Concentric": {"variants": [f"Sch {current_schedule}"], "max_qty": 20, "needs_outlet_size": True, "uses_schedule": True},
            "Reducer Eccentric": {"variants": [f"Sch {current_schedule}"], "max_qty": 20, "needs_outlet_size": True, "uses_schedule": True},
            # VALVES (Full Bore) - each valve needs 2 flanges (inlet + outlet)
            "Gate Valve (FB)": {"variants": ["Flanged", "BW (Butt-Weld)"], "max_qty": 20, "needs_flanges": True, "flanges_per_valve": 2},
            "Globe Valve (FB)": {"variants": ["Flanged", "BW (Butt-Weld)"], "max_qty": 20, "needs_flanges": True, "flanges_per_valve": 2},
            "Ball Valve (FB)": {"variants": ["Flanged", "BW (Butt-Weld)", "3-Way Flanged"], "max_qty": 20, "needs_flanges": True, "flanges_per_valve": 2},
            "Check Valve (FB)": {"variants": ["Swing Flanged", "Lift Flanged", "Dual-Plate Flanged"], "max_qty": 20, "needs_flanges": True, "flanges_per_valve": 2},
            "Butterfly Valve (FB)": {"variants": ["Wafer", "Lug"], "max_qty": 20, "needs_flanges": True, "flanges_per_valve": 2},
            "Plug Valve (FB)": {"variants": ["Flanged", "Lubricated Flanged"], "max_qty": 10, "needs_flanges": True, "flanges_per_valve": 2},
            "Control Valve (FB)": {"variants": ["Globe Flanged", "Ball Flanged", "Butterfly Flanged"], "max_qty": 10, "needs_flanges": True, "flanges_per_valve": 2},
            # FLANGE CONNECTIONS (standalone)
            "Flange Connection": {"variants": ["WN-to-WN", "WN-to-Blind", "WN-to-TestBlind", 
                                                "SO-to-SO", "SO-to-Blind", "SO-to-TestBlind",
                                                "SW-to-SW", "SW-to-Blind", "SW-to-TestBlind",
                                                "THD-to-THD", "THD-to-Blind", "THD-to-TestBlind",
                                                "LJ-to-LJ", "LJ-to-Blind", "LJ-to-TestBlind"], 
                                  "max_qty": 20, "is_flange_pair": True},
        }
        
        # Component selection header with add controls
        add_frame = tk.Frame(self.flow_gen_frame, bg=self.bg_card)
        add_frame.pack(fill="x", pady=(10, 5))
        
        tk.Label(
            add_frame,
            text="Add Components:",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(side="left", padx=(0, 10))
        
        # Component type dropdown
        self.flow_add_type_var = tk.StringVar(value="Elbow 90°")
        self.flow_add_type_combo = ttk.Combobox(
            add_frame,
            textvariable=self.flow_add_type_var,
            values=list(self.flow_available_components.keys()),
            state="readonly",
            width=18
        )
        self.flow_add_type_combo.pack(side="left", padx=(0, 5))
        
        # Variant dropdown (updates based on type)
        self.flow_add_variant_var = tk.StringVar(value="LR")
        self.flow_add_variant_combo = ttk.Combobox(
            add_frame,
            textvariable=self.flow_add_variant_var,
            values=["LR", "SR", "3R", "5R", "10R"],
            state="readonly",
            width=12
        )
        self.flow_add_variant_combo.pack(side="left", padx=(0, 5))
        
        # Size dropdown (for reducing tees, reducers) - hidden by default
        self.flow_add_size_frame = tk.Frame(add_frame, bg=self.bg_card)
        tk.Label(self.flow_add_size_frame, text="to", font=("Segoe UI", 8), bg=self.bg_card, fg=self.text_secondary).pack(side="left")
        self.flow_add_size_var = tk.StringVar(value="2")
        self.flow_add_size_combo = ttk.Combobox(
            self.flow_add_size_frame,
            textvariable=self.flow_add_size_var,
            values=["1/2", "3/4", "1", "1-1/4", "1-1/2", "2", "3", "4", "6", "8", "10", "12"],
            state="readonly",
            width=5
        )
        self.flow_add_size_combo.pack(side="left", padx=2)
        tk.Label(self.flow_add_size_frame, text="\"", font=("Segoe UI", 8), bg=self.bg_card, fg=self.text_secondary).pack(side="left")
        # Don't pack yet - shown conditionally
        
        # Face-to-Face input (for valves) - hidden by default
        self.flow_add_f2f_frame = tk.Frame(add_frame, bg=self.bg_card)
        tk.Label(self.flow_add_f2f_frame, text="F2F:", font=("Segoe UI", 8), bg=self.bg_card, fg=self.text_secondary).pack(side="left")
        self.flow_add_f2f_var = tk.StringVar(value="8.0")
        ttk.Entry(self.flow_add_f2f_frame, textvariable=self.flow_add_f2f_var, width=5).pack(side="left", padx=2)
        tk.Label(self.flow_add_f2f_frame, text="\"", font=("Segoe UI", 8), bg=self.bg_card, fg=self.text_secondary).pack(side="left")
        # Don't pack yet - shown for valves only
        
        # Quantity
        tk.Label(add_frame, text="Qty:", font=("Segoe UI", 8), bg=self.bg_card, fg=self.text_secondary).pack(side="left", padx=(5, 2))
        self.flow_add_qty_var = tk.IntVar(value=1)
        self.flow_add_qty_spin = ttk.Spinbox(add_frame, from_=1, to=50, textvariable=self.flow_add_qty_var, width=3)
        self.flow_add_qty_spin.pack(side="left", padx=(0, 5))
        
        # Add button
        add_btn = tk.Button(
            add_frame,
            text="+ Add",
            font=("Segoe UI", 9, "bold"),
            bg=self.accent,
            fg="white",
            relief="flat",
            cursor="hand2",
            padx=10,
            command=self._add_flow_component
        )
        add_btn.pack(side="left", padx=(5, 0))
        
        # Update variant dropdown when type changes
        def on_type_change(*args):
            comp_type = self.flow_add_type_var.get()
            comp_info = self.flow_available_components.get(comp_type, {})
            variants = comp_info.get("variants", ["Standard"])
            
            # Filter Flange Connection variants based on current class
            if comp_type == "Flange Connection":
                current_class = self.flow_flange_class_var.get()
                available_flange_types = self.flange_types_by_class.get(current_class, ["Weld Neck"])
                
                # Build allowed flange connection variants
                filtered_variants = []
                for v in variants:
                    parts = v.split("-to-")
                    flange_a = parts[0] if len(parts) > 0 else "WN"
                    flange_b = parts[1] if len(parts) > 1 else "WN"
                    
                    # Map short codes to full names for checking
                    code_to_name = {"WN": "Weld Neck", "SO": "Slip-On", "SW": "Socket Weld",
                                    "THD": "Threaded", "LJ": "Lap Joint", "Blind": "Blind", "TestBlind": "TestBlind"}
                    
                    flange_a_name = code_to_name.get(flange_a, flange_a)
                    flange_b_name = code_to_name.get(flange_b, flange_b)
                    
                    # Check if both flanges are available (Blind/TestBlind always allowed with any mating flange)
                    a_ok = flange_a_name in available_flange_types or flange_a in ["Blind", "TestBlind"]
                    b_ok = flange_b_name in available_flange_types or flange_b in ["Blind", "TestBlind"]
                    
                    if a_ok and b_ok:
                        filtered_variants.append(v)
                
                variants = filtered_variants if filtered_variants else ["WN-to-WN"]
            
            self.flow_add_variant_combo['values'] = variants
            self.flow_add_variant_var.set(variants[0])
            
            # Update max qty
            max_qty = comp_info.get("max_qty", 50)
            self.flow_add_qty_spin.config(to=max_qty)
            if self.flow_add_qty_var.get() > max_qty:
                self.flow_add_qty_var.set(max_qty)
            
            # Show/hide size selector for reducing components
            if comp_info.get("needs_branch_size") or comp_info.get("needs_outlet_size"):
                # Filter outlet sizes to only show sizes smaller than main pipe
                all_sizes = ["1/2", "3/4", "1", "1-1/4", "1-1/2", "2", "2-1/2", "3", "4", "6", "8", "10", "12", "14", "16", "18", "20", "24"]
                # Convert main pipe size to comparable float
                main_size_str = pipe_size
                if '/' in main_size_str:
                    if '-' in main_size_str:  # e.g. "1-1/4"
                        parts = main_size_str.split('-')
                        main_size_float = float(parts[0]) + float(eval(parts[1]))
                    else:  # e.g. "1/2"
                        main_size_float = float(eval(main_size_str))
                else:
                    main_size_float = float(main_size_str)
                
                # Filter to only smaller sizes
                valid_sizes = []
                for s in all_sizes:
                    if '/' in s:
                        if '-' in s:
                            parts = s.split('-')
                            s_float = float(parts[0]) + float(eval(parts[1]))
                        else:
                            s_float = float(eval(s))
                    else:
                        s_float = float(s)
                    if s_float < main_size_float:
                        valid_sizes.append(s)
                
                if valid_sizes:
                    self.flow_add_size_combo['values'] = valid_sizes
                    self.flow_add_size_var.set(valid_sizes[-1])  # Default to largest valid
                    self.flow_add_size_frame.pack(side="left", padx=(0, 5), before=self.flow_add_qty_spin.master.winfo_children()[0])
                else:
                    # No valid smaller sizes, hide the selector
                    self.flow_add_size_frame.pack_forget()
                self.flow_add_f2f_frame.pack_forget()  # Hide F2F for reducers
            elif comp_info.get("needs_flanges"):
                # Valve selected - show F2F input
                self.flow_add_size_frame.pack_forget()
                # Set default F2F based on valve type and pipe size
                f2f_defaults = {
                    "Gate Valve (FB)": {"1": "5.5", "2": "8.0", "3": "9.5", "4": "11.0", "6": "13.0", "8": "16.0"},
                    "Globe Valve (FB)": {"1": "6.5", "2": "9.5", "3": "12.0", "4": "14.5", "6": "19.0", "8": "23.5"},
                    "Ball Valve (FB)": {"1": "5.0", "2": "7.5", "3": "9.0", "4": "10.5", "6": "13.0", "8": "16.0"},
                    "Check Valve (FB)": {"1": "4.5", "2": "7.0", "3": "8.5", "4": "10.0", "6": "12.5", "8": "15.5"},
                    "Butterfly Valve (FB)": {"1": "2.0", "2": "2.5", "3": "3.0", "4": "3.5", "6": "5.0", "8": "6.0"},
                    "Plug Valve (FB)": {"1": "5.5", "2": "8.0", "3": "9.5", "4": "11.0", "6": "13.5", "8": "17.0"},
                    "Control Valve (FB)": {"1": "8.0", "2": "12.0", "3": "14.0", "4": "16.0", "6": "20.0", "8": "24.0"},
                }
                # Get pipe size (integer portion)
                try:
                    if '/' in pipe_size:
                        ps_key = "1"  # Default for fractional sizes
                    else:
                        ps_key = str(int(float(pipe_size)))
                except:
                    ps_key = "4"
                default_f2f = f2f_defaults.get(comp_type, {}).get(ps_key, "8.0")
                self.flow_add_f2f_var.set(default_f2f)
                self.flow_add_f2f_frame.pack(side="left", padx=(0, 5), before=self.flow_add_qty_spin.master.winfo_children()[0])
            else:
                self.flow_add_size_frame.pack_forget()
                self.flow_add_f2f_frame.pack_forget()
                
        self.flow_add_type_var.trace_add("write", on_type_change)
        
        # Build list display
        tk.Label(
            self.flow_gen_frame,
            text="Build List:",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(10, 2))
        
        # Scrollable build list frame
        list_container = tk.Frame(self.flow_gen_frame, bg=self.bg_dark, relief="sunken", bd=1)
        list_container.pack(fill="both", expand=True, pady=(0, 10))
        
        # Canvas for scrolling
        self.flow_list_canvas = tk.Canvas(list_container, bg=self.bg_dark, highlightthickness=0, height=150)
        scrollbar = ttk.Scrollbar(list_container, orient="vertical", command=self.flow_list_canvas.yview)
        self.flow_list_frame = tk.Frame(self.flow_list_canvas, bg=self.bg_dark)
        
        self.flow_list_canvas.create_window((0, 0), window=self.flow_list_frame, anchor="nw")
        self.flow_list_canvas.configure(yscrollcommand=scrollbar.set)
        
        self.flow_list_canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Configure scroll region when frame changes
        def on_frame_configure(event):
            self.flow_list_canvas.configure(scrollregion=self.flow_list_canvas.bbox("all"))
        self.flow_list_frame.bind("<Configure>", on_frame_configure)
        
        # Empty list message
        self.flow_empty_label = tk.Label(
            self.flow_list_frame,
            text="No components added yet. Use '+ Add' above.",
            font=("Segoe UI", 9, "italic"),
            bg=self.bg_dark,
            fg=self.text_secondary
        )
        self.flow_empty_label.pack(pady=20)
        
        # Summary label
        self.flow_summary_label = tk.Label(
            self.flow_gen_frame,
            text="Total: 0 components",
            font=("Segoe UI", 8),
            bg=self.bg_card,
            fg=self.text_secondary
        )
        self.flow_summary_label.pack(anchor="w")
        
        # Generate button
        self.flow_gen_btn = tk.Button(
            self.flow_gen_frame,
            text=f"⚙️  Generate {pipe_size}\" Sch {min_schedule} Assembly Package",
            font=("Segoe UI", 10, "bold"),
            bg=self.accent,
            fg="white",
            activebackground="#059669",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=10,
            command=self._generate_from_flow_calc
        )
        self.flow_gen_btn.pack(fill="x", pady=(10, 0))
        
        # Update button text AND flange class when schedule changes
        def update_on_schedule_change(*args):
            selected_schedule = self.flow_schedule_var.get()
            self.flow_gen_btn.config(text=f"⚙️  Generate {pipe_size}\" Sch {selected_schedule} Assembly Package")
            
            # Get schedule pressure rating and update required flange class
            from flow_calculator_enhanced import FlowCalculator
            schedule_rating = FlowCalculator.get_schedule_pressure_rating(selected_schedule, pipe_size, temp_f=self.flow_avg_temp)
            
            # Find flange class that meets or exceeds schedule rating
            new_class = "2500"  # Default to highest
            for class_name, rating in self.flange_ratings.items():
                if rating >= schedule_rating:
                    new_class = class_name
                    break
            
            # Update the locked class display and warning label
            self.flow_flange_class_var.set(new_class)
            self.flow_class_label.config(text=new_class)
            self.flow_class_warning_label.config(
                text=f"→ Flange Class {new_class} REQUIRED ({self.flange_ratings[new_class]} psi rated)"
            )
            self.flow_required_class = new_class
            
            # Update available flange types based on new class
            available_types = self.flange_types_by_class.get(new_class, ["Weld Neck"])
            self.flow_flange_type_combo['values'] = available_types
            
            # If current selection is not available in new class, reset to Weld Neck
            current_type = self.flow_flange_type_var.get()
            if current_type not in available_types:
                self.flow_flange_type_var.set("Weld Neck")
            
        self.flow_schedule_var.trace_add("write", update_on_schedule_change)
    
    def _add_flow_component(self):
        """Add a component to the build list"""
        comp_type = self.flow_add_type_var.get()
        variant = self.flow_add_variant_var.get()
        qty = self.flow_add_qty_var.get()
        
        # Get component info
        comp_info = self.flow_available_components.get(comp_type, {})
        
        # Check max qty
        max_qty = comp_info.get("max_qty", 50)
        if qty > max_qty:
            qty = max_qty
            self.flow_add_qty_var.set(max_qty)
        
        # Build display text and details
        details = {}
        if comp_info.get("needs_branch_size") or comp_info.get("needs_outlet_size"):
            outlet_size = self.flow_add_size_var.get()
            details["outlet_size"] = outlet_size
            display_text = f"{qty}x {comp_type} ({variant}) to {outlet_size}\""
        elif comp_info.get("is_flange_pair"):
            # Flange connections include gasket + studs + nuts
            display_text = f"{qty}x {comp_type} ({variant}) + gasket + studs + nuts"
            details["is_flange_pair"] = True
        elif comp_info.get("needs_flanges") and "Flanged" in variant:
            # Valves with flanged ends - note that flanges will be added
            flanges_per = comp_info.get("flanges_per_valve", 2)
            total_flanges = qty * flanges_per
            # Get F2F value
            try:
                f2f_value = float(self.flow_add_f2f_var.get())
            except:
                f2f_value = 8.0
            display_text = f"{qty}x {comp_type} ({variant}) F2F={f2f_value}\" + {total_flanges} flanges"
            details["needs_flanges"] = True
            details["flanges_per_valve"] = flanges_per
            details["face_to_face"] = f2f_value
        elif comp_info.get("needs_flanges") and ("Wafer" in variant or "Lug" in variant):
            # Butterfly valves (wafer/lug) need flanges on pipe side
            try:
                f2f_value = float(self.flow_add_f2f_var.get())
            except:
                f2f_value = 3.5
            display_text = f"{qty}x {comp_type} ({variant}) F2F={f2f_value}\" + {qty * 2} pipe flanges"
            details["needs_flanges"] = True
            details["flanges_per_valve"] = 2
            details["face_to_face"] = f2f_value
        elif comp_info.get("needs_flanges"):
            # BW (Butt-Weld) valves - no flanges but still need F2F
            try:
                f2f_value = float(self.flow_add_f2f_var.get())
            except:
                f2f_value = 8.0
            display_text = f"{qty}x {comp_type} ({variant}) F2F={f2f_value}\""
            details["face_to_face"] = f2f_value
        else:
            display_text = f"{qty}x {comp_type} ({variant})"
        
        # Add to build list
        item = {
            "type": comp_type,
            "variant": variant,
            "qty": qty,
            "details": details,
            "display_text": display_text
        }
        self.flow_build_list.append(item)
        
        # Update display
        self._update_flow_build_list()
        
        # Reset qty to 1
        self.flow_add_qty_var.set(1)
    
    def _remove_flow_component(self, index):
        """Remove a component from the build list"""
        if 0 <= index < len(self.flow_build_list):
            del self.flow_build_list[index]
            self._update_flow_build_list()
    
    def _update_flow_build_list(self):
        """Refresh the build list display"""
        # Clear existing items
        for widget in self.flow_list_frame.winfo_children():
            widget.destroy()
        
        if not self.flow_build_list:
            # Show empty message
            self.flow_empty_label = tk.Label(
                self.flow_list_frame,
                text="No components added yet. Use '+ Add' above.",
                font=("Segoe UI", 9, "italic"),
                bg=self.bg_dark,
                fg=self.text_secondary
            )
            self.flow_empty_label.pack(pady=20)
            self.flow_summary_label.config(text="Total: 0 components")
            return
        
        # Display each item
        total_parts = 0
        for i, item in enumerate(self.flow_build_list):
            item_frame = tk.Frame(self.flow_list_frame, bg=self.bg_dark)
            item_frame.pack(fill="x", padx=5, pady=2)
            
            # Item text
            tk.Label(
                item_frame,
                text=f"• {item['display_text']}",
                font=("Segoe UI", 9),
                bg=self.bg_dark,
                fg=self.text_primary,
                anchor="w"
            ).pack(side="left", fill="x", expand=True)
            
            # Remove button
            remove_btn = tk.Button(
                item_frame,
                text="✕",
                font=("Segoe UI", 8, "bold"),
                bg="#dc2626",
                fg="white",
                relief="flat",
                cursor="hand2",
                padx=5,
                pady=0,
                command=lambda idx=i: self._remove_flow_component(idx)
            )
            remove_btn.pack(side="right")
            
            # Count parts
            qty = item['qty']
            if item['details'].get('is_flange_pair'):
                # Flange pair = 2 flanges + 1 gasket + studs + nuts per connection
                total_parts += qty * 5  # Approximate: 2 flanges + gasket + stud set + nut set
            elif item['details'].get('needs_flanges'):
                # Valve + flanges: valve + (flanges × (flange + gasket + studs + nuts))
                flanges_per = item['details'].get('flanges_per_valve', 2)
                total_parts += qty  # The valves
                total_parts += qty * flanges_per * 4  # Each flange = flange + gasket + studs + nuts
            else:
                total_parts += qty
        
        # Update summary
        self.flow_summary_label.config(text=f"Total: {len(self.flow_build_list)} line items, ~{total_parts} parts")

    def _generate_from_flow_calc(self):
        """Generate assembly based on flow calculator recommendation and build list"""
        if not hasattr(self, 'flow_recommendation'):
            self.status_var.set("⚠️ Please run calculation first")
            return
        
        if not self.flow_build_list:
            self.status_var.set("⚠️ Please add components to the build list first")
            messagebox.showwarning("Empty Build List", "No components to generate.\n\nUse '+ Add' to add components to your build list.")
            return
        
        rec = self.flow_recommendation
        pipe_size = rec['size']
        schedule = self.flow_schedule_var.get()
        flange_type = self.flow_flange_type_var.get()
        flange_class = self.flow_flange_class_var.get()
        facing = self.flow_facing_var.get()
        
        # Convert pipe size to float for generators
        nps_float = float(eval(pipe_size.replace('"', ''))) if '/' in pipe_size else float(pipe_size)
        
        # Create package folder
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        package_name = f"FlowCalc_{pipe_size.replace('/', '-')}in_Sch{schedule}_Class{flange_class}_{facing}_{timestamp}"
        package_path = self.library_path / "Flow_Calculator_Packages" / package_name
        package_path.mkdir(parents=True, exist_ok=True)
        
        generated_files = []
        errors = []
        
        self.status_var.set(f"🔄 Generating {len(self.flow_build_list)} items...")
        self.root.update()
        
        try:
            # Process each item in the build list
            for item in self.flow_build_list:
                comp_type = item['type']
                variant = item['variant']
                qty = item['qty']
                details = item['details']
                
                try:
                    # PIPE
                    if comp_type == "Pipe (40ft)":
                        pipe_path = package_path / "Pipe"
                        pipe_path.mkdir(exist_ok=True)
                        import generate_pipe
                        for i in range(1, qty + 1):
                            pipe_file = pipe_path / f"Pipe_{pipe_size.replace('/', '-')}in_Sch{schedule}_40ft_{i:02d}.step"
                            generate_pipe.generate_pipe(
                                nps=nps_float,
                                schedule=schedule,
                                length_inches=480.0,
                                output_file=str(pipe_file)
                            )
                            generated_files.append(str(pipe_file))
                    
                    # ELBOWS
                    elif comp_type.startswith("Elbow"):
                        elbow_path = package_path / "Elbows"
                        elbow_path.mkdir(exist_ok=True)
                        import generate_elbow
                        
                        # Parse angle from comp_type
                        if "90°" in comp_type:
                            angle = 90.0
                        elif "45°" in comp_type:
                            angle = 45.0
                        elif "22.5°" in comp_type:
                            angle = 22.5
                        else:
                            angle = 90.0
                        
                        # Map variant to elbow_type
                        elbow_type_map = {"LR": "LR", "SR": "SR", "3R": "LR3", "5R": "LR5", "10R": "LR10"}
                        elbow_type = elbow_type_map.get(variant, "LR")
                        
                        for i in range(1, qty + 1):
                            elbow_file = elbow_path / f"Elbow-{angle}deg-{variant}_{pipe_size.replace('/', '-')}in_Sch{schedule}_{i:02d}.step"
                            generate_elbow.generate_elbow(
                                nps=nps_float,
                                schedule=schedule,
                                elbow_type=elbow_type,
                                angle=angle,
                                output_file=str(elbow_file)
                            )
                            generated_files.append(str(elbow_file))
                    
                    # 180° RETURNS
                    elif comp_type == "180° Return":
                        return_path = package_path / "Returns"
                        return_path.mkdir(exist_ok=True)
                        import generate_180_return
                        
                        for i in range(1, qty + 1):
                            return_file = return_path / f"Return180-{variant}_{pipe_size.replace('/', '-')}in_Sch{schedule}_{i:02d}.step"
                            generate_180_return.generate_180_return(
                                nps=nps_float,
                                schedule=schedule,
                                return_type=variant,
                                output_file=str(return_file)
                            )
                            generated_files.append(str(return_file))
                    
                    # TEES
                    elif comp_type == "Tee Equal":
                        tee_path = package_path / "Tees"
                        tee_path.mkdir(exist_ok=True)
                        import generate_tee
                        
                        for i in range(1, qty + 1):
                            tee_file = tee_path / f"Tee-Equal_{pipe_size.replace('/', '-')}in_Sch{schedule}_{i:02d}.step"
                            generate_tee.generate_tee(
                                run_nps=nps_float,
                                run_schedule=schedule,
                                branch_nps=None,
                                branch_schedule=None,
                                output_file=str(tee_file)
                            )
                            generated_files.append(str(tee_file))
                    
                    elif comp_type == "Tee Reducing":
                        tee_path = package_path / "Tees"
                        tee_path.mkdir(exist_ok=True)
                        import generate_tee
                        
                        outlet_size = details.get("outlet_size", "2")
                        branch_float = float(eval(outlet_size.replace('"', ''))) if '/' in outlet_size else float(outlet_size)
                        
                        for i in range(1, qty + 1):
                            tee_file = tee_path / f"Tee-Red_{pipe_size.replace('/', '-')}x{outlet_size.replace('/', '-')}in_Sch{schedule}_{i:02d}.step"
                            generate_tee.generate_tee(
                                run_nps=nps_float,
                                run_schedule=schedule,
                                branch_nps=branch_float,
                                branch_schedule=schedule,
                                output_file=str(tee_file)
                            )
                            generated_files.append(str(tee_file))
                    
                    # CROSSES
                    elif comp_type == "Cross Equal":
                        cross_path = package_path / "Crosses"
                        cross_path.mkdir(exist_ok=True)
                        import generate_cross
                        
                        for i in range(1, qty + 1):
                            cross_file = cross_path / f"Cross-Equal_{pipe_size.replace('/', '-')}in_Sch{schedule}_{i:02d}.step"
                            generate_cross.generate_cross(
                                nps=nps_float,
                                schedule=schedule,
                                output_file=str(cross_file)
                            )
                            generated_files.append(str(cross_file))
                    
                    # REDUCERS
                    elif comp_type == "Reducer Concentric":
                        reducer_path = package_path / "Reducers"
                        reducer_path.mkdir(exist_ok=True)
                        import generate_reducer
                        
                        outlet_size = details.get("outlet_size", "2")
                        smaller_float = float(eval(outlet_size.replace('"', ''))) if '/' in outlet_size else float(outlet_size)
                        
                        for i in range(1, qty + 1):
                            reducer_file = reducer_path / f"Reducer-Con_{pipe_size.replace('/', '-')}x{outlet_size.replace('/', '-')}in_Sch{schedule}_{i:02d}.step"
                            generate_reducer.generate_reducer(
                                large_nps=nps_float,
                                small_nps=smaller_float,
                                schedule=schedule,
                                reducer_type="concentric",
                                output_file=str(reducer_file)
                            )
                            generated_files.append(str(reducer_file))
                    
                    elif comp_type == "Reducer Eccentric":
                        reducer_path = package_path / "Reducers"
                        reducer_path.mkdir(exist_ok=True)
                        import generate_reducer
                        
                        outlet_size = details.get("outlet_size", "2")
                        smaller_float = float(eval(outlet_size.replace('"', ''))) if '/' in outlet_size else float(outlet_size)
                        
                        for i in range(1, qty + 1):
                            reducer_file = reducer_path / f"Reducer-Ecc_{pipe_size.replace('/', '-')}x{outlet_size.replace('/', '-')}in_Sch{schedule}_{i:02d}.step"
                            generate_reducer.generate_reducer(
                                large_nps=nps_float,
                                small_nps=smaller_float,
                                schedule=schedule,
                                reducer_type="eccentric",
                                output_file=str(reducer_file)
                            )
                            generated_files.append(str(reducer_file))
                    
                    # FLANGE CONNECTIONS (includes flange pair + gasket + studs + nuts)
                    elif comp_type == "Flange Connection":
                        flange_path = package_path / "Flanges"
                        flange_path.mkdir(exist_ok=True)
                        gasket_path = package_path / "Gaskets"
                        gasket_path.mkdir(exist_ok=True)
                        fastener_path = package_path / "Fasteners"
                        fastener_path.mkdir(exist_ok=True)
                        
                        # Parse variant: "WN-to-Blind", "SO-to-SO", etc.
                        parts = variant.split("-to-")
                        flange_a_type = parts[0] if len(parts) > 0 else "WN"
                        flange_b_type = parts[1] if len(parts) > 1 else "WN"
                        
                        flange_type_map = {
                            "WN": "Weld Neck", "SO": "Slip-On", "SW": "Socket Weld",
                            "THD": "Threaded", "LJ": "Lap Joint", "Blind": "Blind", "TestBlind": "TestBlind"
                        }
                        
                        for i in range(1, qty + 1):
                            # Generate Flange A
                            self._generate_single_flange(
                                flange_type_map.get(flange_a_type, "Weld Neck"),
                                pipe_size, flange_class, facing, flange_path,
                                f"{flange_a_type}_{pipe_size.replace('/', '-')}in_Class{flange_class}_{facing}_conn{i:02d}_A.step",
                                generated_files, errors
                            )
                            
                            # Generate Flange B
                            self._generate_single_flange(
                                flange_type_map.get(flange_b_type, "Weld Neck"),
                                pipe_size, flange_class, facing, flange_path,
                                f"{flange_b_type}_{pipe_size.replace('/', '-')}in_Class{flange_class}_{facing}_conn{i:02d}_B.step",
                                generated_files, errors
                            )
                            
                            # Generate Gasket
                            try:
                                import generate_gasket
                                gasket_file = gasket_path / f"Gasket_{pipe_size.replace('/', '-')}in_Class{flange_class}_conn{i:02d}.step"
                                generate_gasket.generate_spiral_wound_gasket(
                                    nps=pipe_size,
                                    pressure_class=int(flange_class),
                                    output_dir=str(gasket_path)
                                )
                                generated_files.append(str(gasket_file))
                            except Exception as e:
                                errors.append(f"Gasket conn{i}: {str(e)}")
                            
                            # Generate Studs
                            try:
                                import generate_stud
                                stud_file = fastener_path / f"StudSet_{pipe_size.replace('/', '-')}in_Class{flange_class}_conn{i:02d}.step"
                                generate_stud.generate_stud(
                                    standard='B16.5',
                                    nps=pipe_size,
                                    pressure_class=int(flange_class),
                                    facing_type=facing,
                                    output_dir=str(fastener_path)
                                )
                                generated_files.append(str(stud_file))
                            except Exception as e:
                                errors.append(f"Studs conn{i}: {str(e)}")
                            
                            # Generate Nuts
                            try:
                                import generate_hex_nut
                                nut_file = fastener_path / f"NutSet_{pipe_size.replace('/', '-')}in_Class{flange_class}_conn{i:02d}.step"
                                # Get stud size for this flange size/class
                                from asme_b165_stud_data import get_b165_stud_info
                                stud_info = get_b165_stud_info(pipe_size, int(flange_class), facing)
                                if stud_info:
                                    generate_hex_nut.generate_hex_nut(
                                        nut_type='2h',
                                        nominal_size=stud_info.get('diameter', '3/4'),
                                        output_dir=str(fastener_path)
                                    )
                                    generated_files.append(str(nut_file))
                            except Exception as e:
                                errors.append(f"Nuts conn{i}: {str(e)}")
                    
                    # VALVES (FB) - Generate placeholder valve body + matching flanges
                    elif "Valve (FB)" in comp_type:
                        valve_name = comp_type.replace(" (FB)", "")
                        valve_path = package_path / "Valves"
                        valve_path.mkdir(exist_ok=True)
                        
                        # Map GUI valve type to generator valve type
                        valve_type_map = {
                            "Gate Valve": "gate",
                            "Globe Valve": "globe",
                            "Ball Valve": "ball",
                            "Check Valve": "check",
                            "Butterfly Valve": "butterfly",
                            "Plug Valve": "gate",  # Use gate shape for plug valve
                            "Control Valve": "control"
                        }
                        valve_type = valve_type_map.get(valve_name, "ball")
                        
                        # Get F2F from details
                        f2f = details.get("face_to_face", 8.0)
                        
                        # Generate valve placeholder(s)
                        try:
                            import generate_valve_placeholder
                            
                            for i in range(1, qty + 1):
                                valve_file = valve_path / f"{valve_name.replace(' ', '')}_{pipe_size.replace('/', '-')}in_F2F{f2f}in_Class{flange_class}_{i:02d}.step"
                                generate_valve_placeholder.generate_valve_placeholder(
                                    nps=nps_float,
                                    pressure_class=int(flange_class),
                                    face_to_face=f2f,
                                    valve_type=valve_type,
                                    output_file=str(valve_file)
                                )
                                generated_files.append(str(valve_file))
                        except Exception as e:
                            errors.append(f"{valve_name} body: {str(e)}")
                        
                        # Generate matching flanges if needed
                        if details.get("needs_flanges"):
                            flange_path = package_path / "Flanges"
                            flange_path.mkdir(exist_ok=True)
                            gasket_path = package_path / "Gaskets"
                            gasket_path.mkdir(exist_ok=True)
                            fastener_path = package_path / "Fasteners"
                            fastener_path.mkdir(exist_ok=True)
                            
                            flanges_per = details.get("flanges_per_valve", 2)
                            
                            for i in range(1, qty + 1):
                                for flg_num in range(1, flanges_per + 1):
                                    # Generate WN flange for valve connection
                                    self._generate_single_flange(
                                        "Weld Neck",
                                        pipe_size, flange_class, facing, flange_path,
                                        f"WN_{valve_name.replace(' ', '')}_{i:02d}_Flg{flg_num}_{pipe_size.replace('/', '-')}in_Class{flange_class}.step",
                                        generated_files, errors
                                    )
                                    
                                    # Generate Gasket
                                    try:
                                        import generate_gasket
                                        gasket_file = gasket_path / f"Gasket_{valve_name.replace(' ', '')}_{i:02d}_Flg{flg_num}_{pipe_size.replace('/', '-')}in.step"
                                        generate_gasket.generate_spiral_wound_gasket(
                                            nps=pipe_size,
                                            pressure_class=int(flange_class),
                                            output_dir=str(gasket_path)
                                        )
                                        generated_files.append(str(gasket_file))
                                    except Exception as e:
                                        errors.append(f"Gasket {valve_name} {i} Flg{flg_num}: {str(e)}")
                                    
                                    # Generate Studs
                                    try:
                                        import generate_stud
                                        from asme_b165_stud_data import get_b165_stud_info
                                        stud_info = get_b165_stud_info(pipe_size, int(flange_class), facing)
                                        if stud_info:
                                            generate_stud.generate_stud(
                                                standard='B16.5',
                                                nps=pipe_size,
                                                pressure_class=int(flange_class),
                                                facing_type=facing,
                                                output_dir=str(fastener_path)
                                            )
                                    except Exception as e:
                                        errors.append(f"Studs {valve_name} {i} Flg{flg_num}: {str(e)}")
                                    
                                    # Generate Nuts
                                    try:
                                        import generate_hex_nut
                                        from asme_b165_stud_data import get_b165_stud_info
                                        stud_info = get_b165_stud_info(pipe_size, int(flange_class), facing)
                                        if stud_info:
                                            generate_hex_nut.generate_hex_nut(
                                                nut_type='2h',
                                                nominal_size=stud_info.get('diameter', '3/4'),
                                                output_dir=str(fastener_path)
                                            )
                                    except Exception as e:
                                        errors.append(f"Nuts {valve_name} {i} Flg{flg_num}: {str(e)}")
                
                except Exception as e:
                    errors.append(f"{comp_type} ({variant}): {str(e)}")
            
            # Create README
            readme_path = package_path / "README.txt"
            with open(readme_path, 'w') as f:
                f.write(f"Flow Calculator Assembly Package\n")
                f.write(f"=" * 50 + "\n\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                f.write(f"SPECIFICATIONS:\n")
                f.write(f"  Pipe Size: {pipe_size}\" NPS\n")
                f.write(f"  Schedule: {schedule}\n")
                f.write(f"  Flange Class: {flange_class}\n")
                f.write(f"  Facing: {facing}\n\n")
                f.write(f"BUILD LIST:\n")
                for item in self.flow_build_list:
                    f.write(f"  - {item['display_text']}\n")
                    # Note F2F for valves
                    if item['details'].get('face_to_face'):
                        f.write(f"    → F2F is user-specified (verify with manufacturer)\n")
                f.write(f"\nGENERATED FILES ({len(generated_files)} total):\n")
                for file in generated_files:
                    f.write(f"  - {Path(file).name}\n")
                
                # Add valve note if any valves in build list
                has_valves = any("Valve" in item['type'] for item in self.flow_build_list)
                if has_valves:
                    f.write(f"\n⚠️  VALVE NOTE:\n")
                    f.write(f"  Valve bodies are PLACEHOLDER shapes for layout purposes.\n")
                    f.write(f"  Face-to-Face (F2F) dimensions are user-specified and may vary\n")
                    f.write(f"  between manufacturers. Always verify F2F with actual valve\n")
                    f.write(f"  specifications before finalizing piping layouts.\n")
                
                if errors:
                    f.write(f"\nERRORS:\n")
                    for error in errors:
                        f.write(f"  - {error}\n")
            
            # Success message
            if errors:
                self.status_var.set(f"✅ Generated {len(generated_files)} files with {len(errors)} errors")
                messagebox.showwarning(
                    "Partial Success",
                    f"Generated {len(generated_files)} files successfully.\n\n{len(errors)} components failed:\n" + "\n".join(errors[:5])
                )
            else:
                self.status_var.set(f"✅ Successfully generated {len(generated_files)} files!")
                messagebox.showinfo(
                    "Success",
                    f"Assembly package generated successfully!\n\n{len(generated_files)} files created in:\n{package_path.name}"
                )
            
            # Update file location
            self.last_generated_path = str(package_path)
            self.file_location_frame.pack(pady=(0, 10))
            
        except Exception as e:
            self.status_var.set(f"❌ Error: {str(e)}")
            messagebox.showerror("Generation Error", f"Failed to generate assembly:\n\n{str(e)}")
        self.root.update()
    
    def _generate_single_flange(self, flange_type, pipe_size, flange_class, facing, output_path, filename, generated_files, errors):
        """Helper to generate a single flange"""
        try:
            flange_file = output_path / filename
            
            if flange_type == "Weld Neck":
                import generate_asme_flange
                generate_asme_flange.generate_asme_b16_5_wn_flange(
                    pressure_class=flange_class,
                    size=pipe_size,
                    output_file=str(flange_file),
                    include_bevel=True,
                    series='B16.5'
                )
            elif flange_type == "Blind":
                import generate_asme_flange
                generate_asme_flange.generate_asme_b16_5_blind_flange(
                    pressure_class=flange_class,
                    size=pipe_size,
                    output_file=str(flange_file),
                    series='B16.5'
                )
            elif flange_type == "TestBlind":
                import generate_test_blind
                generate_test_blind.generate_test_blind_flange(
                    pressure_class=flange_class,
                    size=pipe_size,
                    tap_size="3/4",
                    output_file=str(flange_file),
                    series='B16.5'
                )
            elif flange_type == "Slip-On":
                import generate_slip_on_flange
                generate_slip_on_flange.generate_slip_on_flange(
                    nps=pipe_size,
                    pressure_class=int(flange_class),
                    facing=facing,
                    output_dir=str(output_path)
                )
            elif flange_type == "Socket Weld":
                import generate_socket_weld_flange
                generate_socket_weld_flange.generate_socket_weld_flange(
                    nps=pipe_size,
                    pressure_class=int(flange_class),
                    facing=facing,
                    output_dir=str(output_path)
                )
            elif flange_type == "Threaded":
                import generate_threaded_flange
                generate_threaded_flange.generate_threaded_flange(
                    nps=pipe_size,
                    pressure_class=int(flange_class),
                    facing=facing,
                    output_dir=str(output_path)
                )
            elif flange_type == "Lap Joint":
                import generate_lap_joint_flange
                generate_lap_joint_flange.generate_lap_joint_flange(
                    nps=pipe_size,
                    pressure_class=int(flange_class),
                    facing=facing,
                    output_dir=str(output_path)
                )
            
            generated_files.append(str(flange_file))
        except Exception as e:
            errors.append(f"{flange_type} flange: {str(e)}")
    
    def _convert_flow_to_gpm(self, value, unit):
        """Convert flow rate to GPM"""
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
    
    def _convert_pressure_to_psi(self, value, unit):
        """Convert pressure to PSI"""
        conversions = {
            "PSI": 1.0,
            "bar": 14.504,
            "kPa": 0.145,
            "MPa": 145.0
        }
        return value * conversions.get(unit, 1.0)
    
    def _get_pipe_id_estimate(self, nps, schedule):
        """Simplified pipe ID lookup (would use actual pipe_data in full implementation)"""
        # Simplified estimates - should use actual pipe dimension tables
        pipe_ids = {
            ("1", "40"): 1.049, ("1", "80"): 0.957, ("1", "160"): 0.815,
            ("1-1/4", "40"): 1.380, ("1-1/4", "80"): 1.278, ("1-1/4", "160"): 1.160,
            ("1-1/2", "40"): 1.610, ("1-1/2", "80"): 1.500, ("1-1/2", "160"): 1.338,
            ("2", "40"): 2.067, ("2", "80"): 1.939, ("2", "160"): 1.689,
            ("2-1/2", "40"): 2.469, ("2-1/2", "80"): 2.323, ("2-1/2", "160"): 2.125,
            ("3", "40"): 3.068, ("3", "80"): 2.900, ("3", "160"): 2.624,
            ("4", "40"): 4.026, ("4", "80"): 3.826, ("4", "160"): 3.438,
            ("6", "40"): 6.065, ("6", "80"): 5.761, ("6", "160"): 5.187,
            ("8", "40"): 7.981, ("8", "80"): 7.625, ("8", "160"): 7.001,
            ("10", "40"): 10.020, ("10", "80"): 9.562, ("10", "160"): 8.750,
            ("12", "40"): 11.938, ("12", "80"): 11.374, ("12", "160"): 10.750,
        }
        return pipe_ids.get((nps, schedule), 0)
    
    def _get_schedule_pressure_rating(self, schedule, size):
        """Simplified pressure rating (would use actual ASME B31.3 calculations)"""
        # Simplified - actual ratings depend on material, temp, etc.
        ratings = {
            "40": 400,
            "80": 600,
            "160": 1200
        }
        return ratings.get(schedule, 400)
    
    def _show_rebar_options(self):
        tk.Label(
            self.options_frame,
            text="Material Type",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        self.rebar_material_var = tk.StringVar(value="Steel")
        ttk.Combobox(
            self.options_frame,
            textvariable=self.rebar_material_var,
            values=["Steel", "Basalt FRP", "Carbon Fiber (CFRP)", "Fiberglass (GFRP)"],
            state="readonly",
            width=28
        ).pack(anchor="w", pady=(0, 10))
        
        tk.Label(
            self.options_frame,
            text="Rebar Size",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        self.rebar_size_var = tk.StringVar(value="#4")
        ttk.Combobox(
            self.options_frame,
            textvariable=self.rebar_size_var,
            values=["#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9", "#10", "#11", "#12", "#13", "#14", "#14J", "#18", "#18J", "#20", "10M", "15M", "20M", "25M", "30M", "35M", "45M", "55M"],
            state="readonly",
            width=28,
            height=20
        ).pack(anchor="w", pady=(0, 10))
        
        tk.Label(
            self.options_frame,
            text="Length (ft)",
            font=("Segoe UI", 9, "bold"),
            bg=self.bg_card,
            fg=self.text_primary
        ).pack(anchor="w", pady=(5, 2))
        
        self.rebar_length_var = tk.StringVar(value="20")
        ttk.Combobox(
            self.options_frame,
            textvariable=self.rebar_length_var,
            values=["20", "40", "60"],
            state="readonly",
            width=28
        ).pack(anchor="w")
    
    def _generate(self):
        # Check subscription before generating (skip for admins)
        if not self.auth_manager.is_admin() and not self.auth_manager.subscription_active:
            messagebox.showerror(
                "Subscription Required",
                "Your subscription is not active. Please visit equationparadise.com/pricing to subscribe and continue generating parts."
            )
            return
        
        # Recheck if needed (silent, skip for admins)
        if not self.auth_manager.is_admin() and self.auth_manager.needs_recheck():
            try:
                valid = self.auth_manager.validate_token()
                if not valid:
                    self._show_subscription_expired()
                    return
            except Exception as e:
                messagebox.showerror(
                    "Connection Required",
                    "Unable to verify your subscription. Please check your internet connection."
                )
                return
        
        self.gen_btn.config(state="disabled", text="⏳ Generating...")
        self.status_var.set("Generating part...")
        
        component = self.component_var.get()
        
        # Start generation in background thread
        thread = threading.Thread(target=self._run_generation, args=(component,), daemon=True)
        thread.start()
    
    def _run_generation(self, component):
        try:
            if component == "Flanges":
                self._generate_flange()
            elif component == "Fasteners":
                self._generate_fastener()
            elif component == "Gaskets":
                self._generate_gasket()
            elif component == "Piping":
                self._generate_piping()
            elif component == "Steel Shapes":
                self._generate_steel()
            elif component == "Lumber":
                self._generate_lumber()
            elif component == "Steel Framing":
                self._generate_steel_framing()
            elif component == "Rebar":
                self._generate_rebar()
            elif component == "Sheet Steel":
                self._generate_sheet_steel()
            elif component == "Pressure Vessels":
                self._generate_pressure_vessel()
        except Exception as e:
            error_msg = str(e)
            self.root.after(0, lambda: self._generation_error(error_msg))
    
    def _get_output_subfolder(self, category, **params):
        """Determine the correct subfolder path for a component."""
        base_path = self.library_path / category
        
        if category == "Flanges":
            # Flanges organized by standard and pressure rating
            standard = params.get('standard', 'API_6BX')  # Default to API 6BX for now
            pressure = params.get('pressure', '5K_PSI')
            return base_path / standard / pressure
        
        elif category == "Fasteners":
            fastener_type = params.get('type', '')
            if 'Nut' in fastener_type:
                nut_style = 'Standard' if fastener_type == 'Hex Nut' else 'Heavy_Hex'
                return base_path / 'Hex_Nuts' / nut_style
            else:
                # Studs - determine standard from selection
                if 'B16.5' in fastener_type:
                    return base_path / 'Studs' / 'B16_5'
                elif 'API 6B' in fastener_type:
                    return base_path / 'Studs' / 'API_6B'
                else:
                    return base_path / 'Studs' / 'API_6BX'
        
        elif category == "Gaskets":
            gasket_type = params.get('type', 'Full_Face')
            # Remove spaces and standardize name
            folder_name = gasket_type.replace(' ', '_')
            if 'Ring_Joint' in folder_name:
                folder_name = 'Ring_Joint'  # Don't include R/RX in folder name
            return base_path / folder_name
        
        elif category == "Piping":
            fitting_type = params.get('type', 'Elbows_90')
            return base_path / fitting_type
        
        elif category == "Steel":
            shape_type = params.get('type', 'W_Beams')
            return base_path / shape_type
        
        # Default to category folder if no subfolder logic
        return base_path
    
    def _generate_flange(self):
        standard = self.flange_standard_var.get()
        size = self.flange_size_var.get()
        pressure = self.flange_pressure_var.get()
        flange_type = self.flange_type_var.get()
        facing_str = self.facing_type_var.get()
        facing_code = "RTJ" if "Ring Joint" in facing_str else "RF"
        
        type_code = "WN" if flange_type == "Weld Neck" else "BLIND"
        
        # Determine output subfolder
        if standard == 'API_6BX':
            output_path = self._get_output_subfolder(
                "Flanges", 
                standard='API_6BX',
                pressure=f"{pressure.replace('K', 'K_PSI')}"
            )
            
            # Generate API 6BX flange
            try:
                import generate_all_flanges_test as gen
                
                if type_code == "WN":
                    success, message = gen.generate_flange(size, pressure, str(output_path))
                    filename = f"API-6BX-{pressure}-{size.replace('/', '-')}-WN.step"
                else:
                    # Blind flange - call generate_blind directly
                    data_dict = gen.ALL_PRESSURE_CLASSES.get(pressure)
                    if not data_dict or size not in data_dict:
                        self.root.after(0, lambda: self._generation_error(f"Size {size} not available for {pressure}"))
                        return
                    data = data_dict[size]
                    gen.generate_blind_flange(pressure, size, data, str(output_path))
                    filename = f"API-6BX-{pressure}-{size.replace('/', '-')}-BLIND.step"
                    success = True
                    message = "Generated"
                
                if success:
                    self.root.after(0, lambda: self._generation_complete(filename))
                else:
                    self.root.after(0, lambda msg=message: self._generation_error(msg))
            except Exception as e:
                error_msg = f"API 6BX generation error: {str(e)}"
                self.root.after(0, lambda: self._generation_error(error_msg))
                
        elif standard == 'ASME_B16_5' or standard == 'ASME_B16_47A' or standard == 'ASME_B16_47B':
            # Determine series
            if standard == 'ASME_B16_47A':
                series = 'B16.47-A'
                standard_label = 'B16_47A'
            elif standard == 'ASME_B16_47B':
                series = 'B16.47-B'
                standard_label = 'B16_47B'
            else:
                series = 'B16.5'
                standard_label = 'B16_5'
            
            # Get facing type
            facing_str = self.facing_type_var.get()
            facing_code = "RTJ" if "Ring Joint" in facing_str else "RF"
            
            output_path = self._get_output_subfolder(
                "Flanges",
                standard=standard,
                pressure=f"Class_{pressure}"
            )
            
            # Generate ASME flange with appropriate generator
            try:
                # Map flange type to generator and code
                type_mapping = {
                    "Weld Neck": ("WN", None),  # Use old generator
                    "Blind": ("BLIND", None),   # Use old generator
                    "Socket Weld": ("SW", "generate_socket_weld_flange"),
                    "Slip-On": ("SO", "generate_slip_on_flange"),
                    "Threaded": ("THD", "generate_threaded_flange"),
                    "Lap Joint": ("LJ", "generate_lap_joint_flange")
                }
                
                type_code, generator_name = type_mapping.get(flange_type, ("WN", None))
                
                # Handle RTJ flanges with new generators
                if facing_code == "RTJ" and flange_type in ["Weld Neck", "Blind"]:
                    # Use new RTJ generators
                    if flange_type == "Weld Neck":
                        import generate_rtj_flange as rtj_gen
                        filename = f"ASME-{standard_label}-{pressure}-{size.replace('/', '-')}-WN-RTJ.step"
                        full_path = output_path / filename
                        rtj_gen.generate_rtj_flange(size, pressure, series, str(output_path))
                    else:  # Blind
                        import generate_rtj_blind_flange as rtj_blind_gen
                        filename = f"ASME-{standard_label}-{pressure}-{size.replace('/', '-')}-BLIND-RTJ.step"
                        full_path = output_path / filename
                        rtj_blind_gen.generate_rtj_blind_flange(size, pressure, series, str(output_path))
                    
                    self.root.after(0, lambda: self._generation_complete(filename))
                
                # Handle new flange types (SW, SO, Threaded, LJ)
                elif generator_name:
                    # Import the appropriate generator module
                    if generator_name == "generate_socket_weld_flange":
                        import generate_socket_weld_flange as gen_module
                    elif generator_name == "generate_slip_on_flange":
                        import generate_slip_on_flange as gen_module
                    elif generator_name == "generate_threaded_flange":
                        import generate_threaded_flange as gen_module
                    elif generator_name == "generate_lap_joint_flange":
                        import generate_lap_joint_flange as gen_module
                    
                    filename = f"ASME-{standard_label}-{pressure}-{size.replace('/', '-')}-{type_code}-{facing_code}.step"
                    
                    # Call generator with facing parameter
                    if generator_name == "generate_socket_weld_flange":
                        gen_module.generate_socket_weld_flange(size, pressure, facing_code, str(output_path))
                    elif generator_name == "generate_slip_on_flange":
                        gen_module.generate_slip_on_flange(size, pressure, facing_code, str(output_path))
                    elif generator_name == "generate_threaded_flange":
                        gen_module.generate_threaded_flange(size, pressure, facing_code, str(output_path))
                    elif generator_name == "generate_lap_joint_flange":
                        gen_module.generate_lap_joint_flange(size, pressure, facing_code, str(output_path))
                    
                    self.root.after(0, lambda: self._generation_complete(filename))
                
                # Handle old RF WN/Blind generators
                elif facing_code == "RF":
                    import generate_asme_flange as asme_gen
                    
                    if type_code == "BLIND":
                        # Generate blind flange
                        filename = f"ASME-{standard_label}-{pressure}-{size.replace('/', '-')}-BLIND-RF.step"
                        full_path = output_path / filename
                        
                        result = asme_gen.generate_asme_b16_5_blind_flange(
                            pressure_class=pressure,
                            size=size,
                            output_file=str(full_path),
                            series=series
                        )
                    else:
                        # Generate weld neck flange
                        include_bevel = self.include_bevel_var.get()
                        bevel_suffix = "" if include_bevel else "-NoBevel"
                        filename = f"ASME-{standard_label}-{pressure}-{size.replace('/', '-')}-{type_code}-RF{bevel_suffix}.step"
                        full_path = output_path / filename
                        
                        result = asme_gen.generate_asme_b16_5_wn_flange(
                            pressure_class=pressure,
                            size=size,
                            output_file=str(full_path),
                            include_bevel=include_bevel,
                            series=series
                        )
                    
                    if result:
                        self.root.after(0, lambda: self._generation_complete(filename))
                    else:
                        self.root.after(0, lambda: self._generation_error("Generation failed"))
                        
            except Exception as e:
                error_msg = f"ASME flange generation error: {str(e)}"
                self.root.after(0, lambda: self._generation_error(error_msg))
        else:
            self.root.after(0, lambda: self._generation_error(f"Standard {standard} not yet implemented"))
    
    def _generate_fastener(self):
        try:
            mode = self.fastener_mode_var.get()
            include_nut = self.fastener_include_matching_var.get()
            
            generated_files = []
            
            if mode == "By Flange Standard":
                # Original mode - get stud from flange standard
                if not hasattr(self, 'fastener_type_var') or not hasattr(self, 'fastener_size_var'):
                    raise Exception("Please select fastener options first")
                
                fastener_type = self.fastener_type_var.get()
                size = self.fastener_size_var.get()
                pressure_class = int(self.fastener_class_var.get()) if hasattr(self, 'fastener_class_var') else 150
                
                # Determine output subfolder
                output_path = self._get_output_subfolder("Fasteners", type=fastener_type)
                
                # Generate stud
                import generate_stud as stud_gen
                import importlib
                importlib.reload(stud_gen)
                
                if "B16.5" in fastener_type:
                    standard = "B16.5"
                elif "B16.47 Series A" in fastener_type:
                    standard = "B16.47A"
                elif "B16.47 Series B" in fastener_type:
                    standard = "B16.47B"
                elif "API 6B" in fastener_type:
                    standard = "API 6B"
                else:
                    standard = "API 6BX"
                
                stud_filename = stud_gen.generate_stud(standard, size, pressure_class, output_dir=str(output_path))
                generated_files.append(stud_filename)
                
                # Look up the actual stud diameter for this flange size to use for nut generation
                stud_info = self._get_stud_info_for_flange(standard, size, pressure_class)
                if stud_info and 'stud_diameter_inches' in stud_info:
                    # Convert diameter to string format (e.g., 0.5 -> "1/2", 0.625 -> "5/8")
                    nut_size = self._diameter_to_string(stud_info['stud_diameter_inches'])
                else:
                    # Fallback to size if lookup fails
                    nut_size = size
                
            else:
                # By Stud Diameter mode - find longest stud for this diameter
                if not hasattr(self, 'fastener_diameter_var'):
                    raise Exception("Please select stud diameter first")
                
                diameter = self.fastener_diameter_var.get()
                
                # Search all stud data to find longest stud with this diameter
                longest_stud = self._find_longest_stud_for_diameter(diameter)
                
                if not longest_stud:
                    raise Exception(f"No stud data found for diameter {diameter}")
                
                # Determine output subfolder based on found standard
                output_path = self._get_output_subfolder("Fasteners", type=f"{longest_stud['standard']} Stud")
                
                # Generate stud
                import generate_stud as stud_gen
                import importlib
                importlib.reload(stud_gen)
                
                stud_filename = stud_gen.generate_stud(
                    longest_stud['standard'],
                    longest_stud['size'],
                    longest_stud['pressure_class'],
                    output_dir=str(output_path)
                )
                generated_files.append(stud_filename)
                
                # Use diameter for nut generation
                nut_size = diameter
            
            # Generate matching nut if requested
            if include_nut:
                import generate_hex_nut as nut_gen
                import importlib
                importlib.reload(nut_gen)
                nut_filename = nut_gen.generate_hex_nut("standard", nut_size, str(output_path))
                generated_files.append(nut_filename)
            
            # Report completion
            if len(generated_files) == 1:
                self.root.after(0, lambda: self._generation_complete(generated_files[0]))
            else:
                # For multiple files, show basenames but store first full path
                import os
                filenames = " and ".join([os.path.basename(f) for f in generated_files])
                first_path = generated_files[0]
                self.root.after(0, lambda: self._generation_complete_multi(filenames, first_path))
        except Exception as e:
            error_msg = f"Fastener generation error: {str(e)}"
            import traceback
            traceback.print_exc()
            self.root.after(0, lambda: self._generation_error(error_msg))
    
    def _find_longest_stud_for_diameter(self, diameter):
        """Find the longest stud across all standards for a given diameter."""
        import sys
        import os
        script_dir = os.path.dirname(os.path.abspath(__file__))
        sys.path.insert(0, script_dir)
        
        # Convert diameter string to float for comparison
        diameter_float = self._nps_to_float(diameter)
        
        longest = None
        max_length = 0
        
        # Check all B16.5 classes
        from asme_b165_stud_data import (
            B165_CLASS_150_STUDS, B165_CLASS_300_STUDS, B165_CLASS_600_STUDS,
            B165_CLASS_900_STUDS, B165_CLASS_1500_STUDS, B165_CLASS_2500_STUDS
        )
        
        for pressure_class, data_dict in [
            (150, B165_CLASS_150_STUDS), (300, B165_CLASS_300_STUDS),
            (600, B165_CLASS_600_STUDS), (900, B165_CLASS_900_STUDS),
            (1500, B165_CLASS_1500_STUDS), (2500, B165_CLASS_2500_STUDS)
        ]:
            for size, info in data_dict.items():
                stud_dia = info.get('stud_diameter_inches', 0)
                if abs(stud_dia - diameter_float) < 0.001:  # Match with small tolerance
                    length = info.get('stud_length_mm', 0)
                    if length > max_length:
                        max_length = length
                        longest = {
                            'standard': 'B16.5',
                            'size': size,
                            'pressure_class': pressure_class,
                            'diameter': diameter,
                            'length': length
                        }
        
        # Check API 6B
        from api_6b_stud_data import (
            API_6B_2000_STUDS, API_6B_3000_STUDS, API_6B_5000_STUDS,
            API_6B_10000_STUDS, API_6B_15000_STUDS, API_6B_20000_STUDS
        )
        
        for pressure_class, data_dict in [
            (2000, API_6B_2000_STUDS), (3000, API_6B_3000_STUDS),
            (5000, API_6B_5000_STUDS), (10000, API_6B_10000_STUDS),
            (15000, API_6B_15000_STUDS), (20000, API_6B_20000_STUDS)
        ]:
            for size, info in data_dict.items():
                stud_dia = info.get('stud_diameter_inches', 0)
                if abs(stud_dia - diameter_float) < 0.001:  # Match with small tolerance
                    length = info.get('stud_length_mm', 0)
                    if length > max_length:
                        max_length = length
                        longest = {
                            'standard': 'API 6B',
                            'size': size,
                            'pressure_class': pressure_class,
                            'diameter': diameter,
                            'length': length
                        }
        
        # Check API 6BX
        from api_6bx_stud_data import (
            API_6BX_3000_STUDS, API_6BX_5000_STUDS, API_6BX_10000_STUDS,
            API_6BX_15000_STUDS, API_6BX_20000_STUDS
        )
        
        for pressure_class, data_dict in [
            (3000, API_6BX_3000_STUDS), (5000, API_6BX_5000_STUDS),
            (10000, API_6BX_10000_STUDS), (15000, API_6BX_15000_STUDS),
            (20000, API_6BX_20000_STUDS)
        ]:
            for size, info in data_dict.items():
                stud_dia = info.get('stud_diameter_inches', 0)
                if abs(stud_dia - diameter_float) < 0.001:  # Match with small tolerance
                    length = info.get('stud_length_mm', 0)
                    if length > max_length:
                        max_length = length
                        longest = {
                            'standard': 'API 6BX',
                            'size': size,
                            'pressure_class': pressure_class,
                            'diameter': diameter,
                            'length': length
                        }
        
        return longest
    
    def _get_stud_info_for_flange(self, standard, size, pressure_class):
        """Get stud information (including diameter) for a given flange."""
        import sys
        import os
        script_dir = os.path.dirname(os.path.abspath(__file__))
        sys.path.insert(0, script_dir)
        
        try:
            if standard == "B16.5":
                from asme_b165_stud_data import (
                    B165_CLASS_150_STUDS, B165_CLASS_300_STUDS, B165_CLASS_600_STUDS,
                    B165_CLASS_900_STUDS, B165_CLASS_1500_STUDS, B165_CLASS_2500_STUDS
                )
                data_map = {
                    150: B165_CLASS_150_STUDS, 300: B165_CLASS_300_STUDS,
                    600: B165_CLASS_600_STUDS, 900: B165_CLASS_900_STUDS,
                    1500: B165_CLASS_1500_STUDS, 2500: B165_CLASS_2500_STUDS
                }
                if pressure_class in data_map and size in data_map[pressure_class]:
                    return data_map[pressure_class][size]
            
            elif standard == "API 6B":
                from api_6b_stud_data import (
                    API_6B_2000_STUDS, API_6B_3000_STUDS, API_6B_5000_STUDS,
                    API_6B_10000_STUDS, API_6B_15000_STUDS, API_6B_20000_STUDS
                )
                data_map = {
                    2000: API_6B_2000_STUDS, 3000: API_6B_3000_STUDS,
                    5000: API_6B_5000_STUDS, 10000: API_6B_10000_STUDS,
                    15000: API_6B_15000_STUDS, 20000: API_6B_20000_STUDS
                }
                if pressure_class in data_map and size in data_map[pressure_class]:
                    return data_map[pressure_class][size]
            
            elif standard == "API 6BX":
                from api_6bx_stud_data import (
                    API_6BX_3000_STUDS, API_6BX_5000_STUDS, API_6BX_10000_STUDS,
                    API_6BX_15000_STUDS, API_6BX_20000_STUDS
                )
                data_map = {
                    3000: API_6BX_3000_STUDS, 5000: API_6BX_5000_STUDS,
                    10000: API_6BX_10000_STUDS, 15000: API_6BX_15000_STUDS,
                    20000: API_6BX_20000_STUDS
                }
                if pressure_class in data_map and size in data_map[pressure_class]:
                    return data_map[pressure_class][size]
        except Exception as e:
            print(f"Error looking up stud info: {e}")
        
        return None
    
    def _diameter_to_string(self, diameter_inches):
        """Convert diameter in inches (float) to string format like '1/2', '5/8', etc."""
        # Common fractional diameters
        fractions = {
            0.25: "1/4", 0.3125: "5/16", 0.375: "3/8", 0.4375: "7/16",
            0.5: "1/2", 0.5625: "9/16", 0.625: "5/8", 0.75: "3/4", 0.875: "7/8",
            1.0: "1", 1.125: "1-1/8", 1.25: "1-1/4", 1.375: "1-3/8", 1.5: "1-1/2",
            1.75: "1-3/4", 2.0: "2", 2.25: "2-1/4", 2.5: "2-1/2", 2.75: "2-3/4",
            3.0: "3", 3.25: "3-1/4", 3.5: "3-1/2", 3.75: "3-3/4", 4.0: "4"
        }
        
        # Find closest match
        for dia, string in fractions.items():
            if abs(dia - diameter_inches) < 0.001:
                return string
        
        # Fallback to formatted float
        return f"{diameter_inches:.4f}"
    
    def _generate_gasket(self):
        try:
            import generate_gasket as gen
            import importlib
            importlib.reload(gen)
            
            gasket_type = self.gasket_type_var.get()
            size = self.gasket_size_var.get()
            pressure_class = self.gasket_class_var.get()
            
            # Determine output subfolder
            output_path = self._get_output_subfolder("Gaskets", type=gasket_type)
        
            if gasket_type == "Full Face":
                filename = gen.generate_full_face_gasket(size, pressure_class, output_dir=str(output_path))
            elif gasket_type == "Flat Ring":
                filename = gen.generate_flat_ring_gasket(size, pressure_class, output_dir=str(output_path))
            elif gasket_type == "Spiral Wound":
                filename = gen.generate_spiral_wound_gasket(size, pressure_class, output_dir=str(output_path))
            elif "Ring Joint" in gasket_type:
                import generate_ring_joint as rj_gen
                rj_type = gasket_type.split()[-1]  # "R" or "RX"
                filename = rj_gen.generate_ring_joint(size, pressure_class, rj_type, str(output_path))
        
            self.root.after(0, lambda: self._generation_complete(filename))
        except Exception as e:
            error_msg = f"Gasket generation error: {str(e)}"
            self.root.after(0, lambda: self._generation_error(error_msg))
    
    def _generate_piping(self):
        fitting_type = self.piping_type_var.get()
        nps = self.piping_nps_var.get()
        schedule = self.piping_sch_var.get()
        
        # Determine output subfolder - normalize folder names
        folder_type = fitting_type.replace(' ', '_').replace('°', 'deg')
        output_path = self._get_output_subfolder("Piping", type=folder_type)
        output_path.mkdir(parents=True, exist_ok=True)
        
        try:
            # Convert NPS string to float for generators
            nps_float = float(nps.replace('-', '.'))
            
            if "90° Elbow" in fitting_type:
                import generate_elbow as elb_gen
                import importlib
                importlib.reload(elb_gen)
                elbow_filename = f"Elbow-90LR-{nps}-Sch{schedule}.step"
                filename = elb_gen.generate_elbow(nps_float, schedule, angle=90, elbow_type='LR', output_file=str(output_path / elbow_filename))
                self.root.after(0, lambda: self._generation_complete(filename))
                
            elif "45° Elbow" in fitting_type:
                import generate_elbow as elb_gen
                import importlib
                importlib.reload(elb_gen)
                elbow_filename = f"Elbow-45LR-{nps}-Sch{schedule}.step"
                filename = elb_gen.generate_elbow(nps_float, schedule, angle=45, elbow_type='LR', output_file=str(output_path / elbow_filename))
                self.root.after(0, lambda: self._generation_complete(filename))
                
            elif "Tee" in fitting_type:
                import generate_tee as tee_gen
                import importlib
                importlib.reload(tee_gen)
                if "Reducing" in fitting_type:
                    # Need branch size for reducing tee
                    branch_size = nps_float - 0.5 if nps_float > 1 else 0.5
                    tee_filename = f"Tee-Reducing-{nps}x{branch_size}-Sch{schedule}.step"
                    filename = tee_gen.generate_tee(nps_float, schedule, branch_nps=branch_size, branch_schedule=schedule, output_file=str(output_path / tee_filename))
                else:
                    tee_filename = f"Tee-Equal-{nps}-Sch{schedule}.step"
                    filename = tee_gen.generate_tee(nps_float, schedule, branch_nps=None, output_file=str(output_path / tee_filename))
                self.root.after(0, lambda: self._generation_complete(filename))
                
            elif "Reducer" in fitting_type:
                import generate_reducer as red_gen
                import importlib
                importlib.reload(red_gen)
                # Concentric or eccentric
                large_size = nps_float
                small_size = nps_float - 1 if nps_float > 2 else 0.5
                is_eccentric = "Eccentric" in fitting_type
                red_type = "Ecc" if is_eccentric else "Con"
                red_filename = f"Reducer-{red_type}-{nps}x{small_size}-Sch{schedule}.step"
                filename = red_gen.generate_reducer(large_size, schedule, small_size, schedule, reducer_type='eccentric' if is_eccentric else 'concentric', output_file=str(output_path / red_filename))
                self.root.after(0, lambda: self._generation_complete(filename))
                
            elif "Cross" in fitting_type:
                import generate_cross as cross_gen
                import importlib
                importlib.reload(cross_gen)
                cross_filename = f"Cross-{nps}-Sch{schedule}.step"
                filename = cross_gen.generate_cross(nps_float, schedule, output_file=str(output_path / cross_filename))
                self.root.after(0, lambda: self._generation_complete(filename))
            
            elif "180° Return" in fitting_type:
                import generate_180_return as ret_gen
                import importlib
                importlib.reload(ret_gen)
                # Determine LR or SR
                return_type = "LR" if "LR" in fitting_type else "SR"
                ret_filename = f"Return180-{return_type}-NPS{nps}-Sch{schedule}.step"
                filename = ret_gen.generate_180_return(nps_float, schedule, return_type=return_type, output_file=str(output_path / ret_filename))
                self.root.after(0, lambda: self._generation_complete(filename))
                
            else:
                self.root.after(0, lambda: self._generation_error(f"Unknown fitting type: {fitting_type}"))
                
        except Exception as e:
            error_msg = f"Piping generation error: {str(e)}"
            self.root.after(0, lambda: self._generation_error(error_msg))
    
    def _generate_pressure_vessel(self):
        """Generate pressure vessel with cylindrical shell and heads"""
        try:
            import generate_pressure_vessel as pv_gen
            import importlib
            importlib.reload(pv_gen)
            
            head_type = self.vessel_head_type_var.get()
            vessel_id = float(self.vessel_id_var.get())
            wall = float(self.vessel_wall_var.get())
            shell_length = float(self.vessel_length_var.get())
            
            # Output path
            output_dir = self.library_path / "Pressure_Vessels" / head_type.capitalize()
            output_dir.mkdir(parents=True, exist_ok=True)
            
            # Generate filename
            id_str = str(int(vessel_id)) if vessel_id == int(vessel_id) else str(vessel_id).replace('.', '-')
            filename = f"PressureVessel-ID{id_str}-Wall{wall}-L{int(shell_length)}-{head_type[:4].title()}.step"
            output_file = str(output_dir / filename)
            
            result = pv_gen.generate_pressure_vessel(
                ID=vessel_id,
                wall=wall,
                shell_length=shell_length,
                head_type=head_type,
                output_file=output_file
            )
            
            self.root.after(0, lambda: self._generation_complete(result))
            
        except Exception as e:
            error_msg = f"Pressure vessel generation error: {str(e)}"
            self.root.after(0, lambda: self._generation_error(error_msg))
    
    def _generate_steel(self):
        """Generate steel shape (square cut - field welders bevel as needed)"""
        try:
            import generate_steel_shapes as steel_gen
            import importlib
            importlib.reload(steel_gen)  # Force reload to get latest code
            
            designation = self.steel_size_var.get()
            length_ft = float(self.steel_length_var.get())
            length_inches = length_ft * 12  # Keep float precision - don't truncate!
            
            # Map UI selection to folder name
            shape_type_map = {
                "W-Beam": "W_Beams",
                "HSS Rectangular": "HSS_Rectangular",
                "HSS Round": "HSS_Round",
                "Channel": "Channels",
                "Angle": "Angles"
            }
            shape_type = shape_type_map.get(self.steel_type_var.get(), "W_Beams")
            output_dir = self.library_path / "Steel" / shape_type
            output_dir.mkdir(parents=True, exist_ok=True)
            
            # Clean designation for filename
            clean_desig = designation.replace('/', '-').replace('X', 'x')
            filename = f"{clean_desig}-{int(length_ft)}ft.step"
            output_file = str(output_dir / filename)
            
            # Generate shape (always square cut, no bevels)
            result = steel_gen.generate_steel_shape(
                designation=designation,
                length_inches=length_inches,
                end1_bevel=False,
                end2_bevel=False,
                output_file=output_file
            )
            
            if result['success']:
                self.root.after(0, lambda: self._generation_complete(filename))
            else:
                self.root.after(0, lambda: self._generation_error(result['message']))
                
        except Exception as e:
            error_msg = f"Steel generation error: {str(e)}"
            self.root.after(0, lambda: self._generation_error(error_msg))
    
    def _generate_lumber(self):
        # Check lumber type and generate accordingly
        lumber_type = self.lumber_type_var.get()
        size = self.lumber_size_var.get()
        
        # Get length from feet + inches
        feet = float(self.lumber_feet_var.get() or 0)
        inches = float(self.lumber_inches_var.get() or 0)
        length_ft = feet + (inches / 12.0)
        
        try:
            import importlib
            
            if lumber_type == "TJI":
                # Generate TJI I-joist
                import generate_tji as tji_gen
                importlib.reload(tji_gen)
                
                # Determine output folder
                output_path = self.library_path / "Lumber" / "TJI"
                output_path.mkdir(parents=True, exist_ok=True)
                
                # Clean designation for filename
                series_depth = size.replace("TJI ", "").replace(" ", "-").replace("/", "-")
                filename = f"TJI-{series_depth}-{length_ft:.3g}ft.step"
                output_file = str(output_path / filename)
                
                result = tji_gen.generate_tji(
                    designation=size,
                    length_ft=length_ft,
                    output_file=output_file
                )
                
                if result['success']:
                    self.root.after(0, lambda: self._generation_complete(filename))
                else:
                    self.root.after(0, lambda: self._generation_error(result['message']))
                    
            elif lumber_type == "Dimensional":
                import generate_dimensional_lumber as dim_gen
                importlib.reload(dim_gen)
                
                output_path = self.library_path / "Lumber" / "Dimensional"
                output_path.mkdir(parents=True, exist_ok=True)
                
                filename = f"Lumber-{size}-{length_ft:.3g}ft.step"
                output_file = str(output_path / filename)
                
                result = dim_gen.generate_dimensional_lumber(size, length_ft, output_file)
                
                if result['success']:
                    self.root.after(0, lambda: self._generation_complete(filename))
                else:
                    self.root.after(0, lambda: self._generation_error(result['message']))
            
            elif lumber_type == "Wall Studs":
                # Wall studs use dimensional lumber generator, just different folder
                import generate_dimensional_lumber as dim_gen
                importlib.reload(dim_gen)
                
                output_path = self.library_path / "Lumber" / "Wall_Studs"
                output_path.mkdir(parents=True, exist_ok=True)
                
                # Format length nicely for filename
                total_inches = length_ft * 12
                if total_inches == int(total_inches):
                    len_str = f"{int(total_inches)}in"
                else:
                    len_str = f"{total_inches:.3g}in"
                filename = f"Stud-{size}-{len_str}.step"
                output_file = str(output_path / filename)
                
                result = dim_gen.generate_dimensional_lumber(size, length_ft, output_file)
                
                if result['success']:
                    self.root.after(0, lambda: self._generation_complete(filename))
                else:
                    self.root.after(0, lambda: self._generation_error(result['message']))
                    
            elif lumber_type == "Glulam":
                import generate_glulam as glulam_gen
                importlib.reload(glulam_gen)
                
                output_path = self.library_path / "Lumber" / "Glulam"
                output_path.mkdir(parents=True, exist_ok=True)
                
                size_clean = size.replace(" ", "").replace("/", "-")
                filename = f"Glulam-{size_clean}-{length_ft:.3g}ft.step"
                output_file = str(output_path / filename)
                
                result = glulam_gen.generate_glulam(size, length_ft, output_file)
                
                if result['success']:
                    self.root.after(0, lambda: self._generation_complete(filename))
                else:
                    self.root.after(0, lambda: self._generation_error(result['message']))
                    
            elif lumber_type == "LVL (Microlam)":
                import generate_lvl as lvl_gen
                importlib.reload(lvl_gen)
                
                output_path = self.library_path / "Lumber" / "LVL"
                output_path.mkdir(parents=True, exist_ok=True)
                
                size_clean = size.replace(" ", "").replace("/", "-")
                filename = f"LVL-{size_clean}-{length_ft:.3g}ft.step"
                output_file = str(output_path / filename)
                
                result = lvl_gen.generate_lvl(size, length_ft, output_file)
                
                if result['success']:
                    self.root.after(0, lambda: self._generation_complete(filename))
                else:
                    self.root.after(0, lambda: self._generation_error(result['message']))
                    
            elif lumber_type == "PSL (Parallam)":
                import generate_psl as psl_gen
                importlib.reload(psl_gen)
                
                output_path = self.library_path / "Lumber" / "PSL"
                output_path.mkdir(parents=True, exist_ok=True)
                
                size_clean = size.replace(" ", "").replace("/", "-")
                filename = f"PSL-{size_clean}-{length_ft:.3g}ft.step"
                output_file = str(output_path / filename)
                
                result = psl_gen.generate_psl(size, length_ft, output_file)
                
                if result['success']:
                    self.root.after(0, lambda: self._generation_complete(filename))
                else:
                    self.root.after(0, lambda: self._generation_error(result['message']))
            else:
                self.root.after(0, lambda: self._generation_error(f"Unknown lumber type: {lumber_type}"))
                    
        except Exception as e:
            error_msg = f"Lumber generation error: {str(e)}"
            self.root.after(0, lambda: self._generation_error(error_msg))
    
    def _generate_steel_framing(self):
        """Generate CFS steel framing (studs, track, joists)"""
        try:
            import generate_cfs_framing as cfs_gen
            import importlib
            importlib.reload(cfs_gen)
            
            member_type = self.cfs_type_var.get()
            size_full = self.cfs_size_var.get()
            gauge_full = self.cfs_gauge_var.get()
            
            # Extract size code (e.g., "362S" from "362S (3-5/8\")")
            size = size_full.split()[0]
            # Extract gauge (e.g., "43" from "43 (18 ga)")
            gauge = gauge_full.split()[0]
            
            # Get length
            feet = float(self.cfs_feet_var.get() or 0)
            inches = float(self.cfs_inches_var.get() or 0)
            length_ft = feet + (inches / 12.0)
            
            with_punchouts = self.cfs_punchouts_var.get()
            
            # Determine output folder
            if member_type == "Floor Joist":
                folder = "Floor_Joists"
            else:
                folder = member_type + "s"  # "Studs" or "Tracks"
            
            output_path = self.library_path / "Steel_Framing" / folder
            output_path.mkdir(parents=True, exist_ok=True)
            
            # Generate based on type
            if member_type == "Stud":
                len_str = f"{length_ft:.3g}".replace('.', '-')
                filename = f"Stud-{size}-{gauge}-{len_str}ft.step"
                output_file = str(output_path / filename)
                result = cfs_gen.generate_cfs_stud(
                    size, gauge, length_ft,
                    with_punchouts=with_punchouts,
                    output_file=output_file
                )
            elif member_type == "Track":
                len_str = f"{length_ft:.3g}".replace('.', '-')
                filename = f"Track-{size}-{gauge}-{len_str}ft.step"
                output_file = str(output_path / filename)
                result = cfs_gen.generate_cfs_track(
                    size, gauge, length_ft,
                    output_file=output_file
                )
            else:  # Floor Joist
                len_str = f"{length_ft:.3g}".replace('.', '-')
                filename = f"Joist-{size}-{gauge}-{len_str}ft.step"
                output_file = str(output_path / filename)
                result = cfs_gen.generate_cfs_joist(
                    size, gauge, length_ft,
                    with_punchouts=with_punchouts,
                    output_file=output_file
                )
            
            if result['success']:
                self.root.after(0, lambda: self._generation_complete(filename))
            else:
                self.root.after(0, lambda: self._generation_error(result['message']))
                
        except Exception as e:
            error_msg = f"Steel framing generation error: {str(e)}"
            self.root.after(0, lambda: self._generation_error(error_msg))
    
    def _generate_rebar(self):
        try:
            import generate_rebar as rebar_gen
            import importlib
            importlib.reload(rebar_gen)
            
            bar_size = self.rebar_size_var.get()
            material = self.rebar_material_var.get()
            length_ft = float(self.rebar_length_var.get())
            
            # Determine output folder with material subfolder
            material_folder = material.replace(" ", "").replace("(", "").replace(")", "")
            output_path = self.library_path / "Rebar" / material_folder
            output_path.mkdir(parents=True, exist_ok=True)
            
            bar_clean = bar_size.replace("#", "No").replace("/", "-")
            mat_prefix = material.split()[0]  # Steel, Basalt, Carbon, Fiberglass
            filename = f"Rebar-{mat_prefix}-{bar_clean}-{length_ft:.3g}ft.step"
            output_file = str(output_path / filename)
            
            result = rebar_gen.generate_rebar(bar_size, length_ft, material, output_file)
            
            if result['success']:
                self.root.after(0, lambda: self._generation_complete(filename))
            else:
                self.root.after(0, lambda: self._generation_error(result['message']))
                
        except Exception as e:
            error_msg = f"Rebar generation error: {str(e)}"
            self.root.after(0, lambda: self._generation_error(error_msg))
    
    def _generate_sheet_steel(self):
        """Generate sheet steel plate with optional edge bevels"""
        try:
            import generate_sheet_steel as sheet_gen
            import importlib
            importlib.reload(sheet_gen)  # Force reload to get latest code
            
            length_inches = float(self.sheet_length_var.get())
            width_inches = float(self.sheet_width_var.get())
            thickness_inches = float(self.sheet_thickness_var.get())
            bevel_angle = float(self.sheet_bevel_angle_var.get())
            land_inches = float(self.sheet_land_var.get())
            
            # Get edge selections
            bevel_edge1 = self.sheet_edge1_var.get()
            bevel_edge2 = self.sheet_edge2_var.get()
            bevel_edge3 = self.sheet_edge3_var.get()
            bevel_edge4 = self.sheet_edge4_var.get()
            
            # Determine output folder
            output_path = self.library_path / "Sheet_Steel"
            output_path.mkdir(parents=True, exist_ok=True)
            
            # Generate filename
            bevel_str = ""
            if any([bevel_edge1, bevel_edge2, bevel_edge3, bevel_edge4]):
                edges = []
                if bevel_edge1: edges.append("E1")
                if bevel_edge2: edges.append("E2")
                if bevel_edge3: edges.append("E3")
                if bevel_edge4: edges.append("E4")
                bevel_str = f"-{int(bevel_angle)}deg-{''.join(edges)}"
            
            filename = f"Sheet-{length_inches:.3g}x{width_inches:.3g}x{thickness_inches:.3g}{bevel_str}.step"
            output_file = str(output_path / filename)
            
            result = sheet_gen.generate_sheet_steel(
                length_inches=length_inches,
                width_inches=width_inches,
                thickness_inches=thickness_inches,
                bevel_angle=bevel_angle,
                land_inches=land_inches,
                bevel_edge1=bevel_edge1,
                bevel_edge2=bevel_edge2,
                bevel_edge3=bevel_edge3,
                bevel_edge4=bevel_edge4,
                output_file=output_file
            )
            
            if result['success']:
                # Pass full path for the file location link
                self.root.after(0, lambda: self._generation_complete_multi(filename, output_file))
            else:
                self.root.after(0, lambda: self._generation_error(result['message']))
                
        except Exception as e:
            error_msg = f"Sheet steel generation error: {str(e)}"
            self.root.after(0, lambda: self._generation_error(error_msg))
    
    def _generation_complete(self, filename):
        self.status_var.set(f"✅ Created: {filename}")
        self.gen_btn.config(state="normal", text="⚙️  Generate STEP File")
        
        # Store the path and show the clickable link
        self.last_generated_path = filename
        self.file_location_frame.pack(pady=(0, 10))
    
    def _generation_complete_multi(self, display_name, file_path):
        """Handle completion for multiple files with proper path."""
        self.status_var.set(f"✅ Created: {display_name}")
        self.gen_btn.config(state="normal", text="⚙️  Generate STEP File")
        
        # Store the full path of first file for the link
        self.last_generated_path = file_path
        self.file_location_frame.pack(pady=(0, 10))
    
    def _generation_error(self, error_msg):
        self.status_var.set(f"❌ {error_msg[:60]}")
        self.gen_btn.config(state="normal", text="⚙️  Generate STEP File")
        # Hide the link on error
        self.file_location_frame.pack_forget()
    
    def _open_file_location(self):
        """Open Windows Explorer to the location of the last generated file."""
        if self.last_generated_path:
            import subprocess
            import os
            from pathlib import Path
            
            # Handle both single file path and "file1 and file2" format
            if " and " in self.last_generated_path:
                # Multiple files - extract first file path
                first_file = self.last_generated_path.split(" and ")[0].strip()
                file_path = Path(first_file)
            else:
                # Single file - the path should already be absolute from generators
                file_path = Path(self.last_generated_path)
            
            # Normalize the path
            file_path = file_path.resolve()
            
            # Open Explorer and select the file
            if file_path.exists():
                subprocess.Popen(f'explorer /select,"{file_path}"')
            else:
                # Fallback: just open the directory
                folder_path = file_path.parent
                if folder_path.exists():
                    os.startfile(str(folder_path))
                else:
                    # Last resort - show error in status
                    self.status_var.set(f"❌ File not found: {file_path}")


def main(auth_manager):
    """Main function that receives authenticated auth_manager"""
    root = tk.Tk()
    app = CADGeneratorApp(root, auth_manager)
    root.mainloop()


if __name__ == "__main__":
    # Silent auto-update check - downloads updates automatically
    needs_restart = silent_auto_update()
    
    if needs_restart:
        # The main script was updated - restart the application
        print("Restarting with updated version...")
        import subprocess
        python_exe = sys.executable
        script_path = os.path.abspath(__file__)
        subprocess.Popen([python_exe, script_path])
        sys.exit(0)
    
    # Build complete flange lookup tables
    build_complete_flange_lookup()
    # Use authentication wrapper
    require_authentication(main)
