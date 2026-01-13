"""
CAD Generator Auto-Updater
Silently checks for updates and downloads new files on startup.
"""
import os
import sys
import json
import hashlib
import threading
from pathlib import Path
from datetime import datetime, timedelta

# Try to import requests, gracefully handle if not available
try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

# Configuration
GITHUB_RAW_BASE = "https://raw.githubusercontent.com/Offshore47/cad-setup/main"
VERSION_URL = f"{GITHUB_RAW_BASE}/version.json"
UPDATE_CHECK_INTERVAL = timedelta(hours=1)  # Don't check more than once per hour

# Files that should be auto-updated (core functionality files)
UPDATABLE_FILES = [
    "cad_generator_gui_v1.3.0.py",
    "cad_auth.py",
    "cad_updater.py",
    "flow_calculator_enhanced.py",
    "flange_data.py",
    "gasket_data.py",
    "heavy_hex_nut_data.py",
    "asme_b165_stud_data.py",
    "api_6b_stud_data.py",
    "api_6bx_stud_data.py",
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
]

class AutoUpdater:
    """
    Silent auto-updater that checks GitHub for new versions
    and updates local files without user interaction.
    """
    
    def __init__(self, scripts_dir=None):
        """
        Initialize the updater.
        
        Args:
            scripts_dir: Directory containing the scripts. If None, uses the
                        directory containing this file.
        """
        if scripts_dir:
            self.scripts_dir = Path(scripts_dir)
        else:
            self.scripts_dir = Path(__file__).parent
        
        self.state_file = Path.home() / ".equationparadise" / "updater_state.json"
        self.state = self._load_state()
        self.update_log = []
    
    def _load_state(self):
        """Load updater state from disk."""
        try:
            if self.state_file.exists():
                with open(self.state_file, 'r') as f:
                    return json.load(f)
        except Exception:
            pass
        return {
            "last_check": None,
            "last_version": None,
            "file_hashes": {}
        }
    
    def _save_state(self):
        """Save updater state to disk."""
        try:
            self.state_file.parent.mkdir(exist_ok=True)
            with open(self.state_file, 'w') as f:
                json.dump(self.state, f, indent=2)
        except Exception as e:
            print(f"[Updater] Could not save state: {e}")
    
    def _should_check(self):
        """Determine if we should check for updates based on interval."""
        last_check = self.state.get("last_check")
        if not last_check:
            return True
        
        try:
            last_dt = datetime.fromisoformat(last_check)
            return (datetime.now() - last_dt) > UPDATE_CHECK_INTERVAL
        except Exception:
            return True
    
    def _get_file_hash(self, filepath):
        """Calculate MD5 hash of a file."""
        try:
            with open(filepath, 'rb') as f:
                return hashlib.md5(f.read()).hexdigest()
        except Exception:
            return None
    
    def _fetch_version_info(self):
        """Fetch version info from GitHub."""
        if not HAS_REQUESTS:
            return None
        
        try:
            response = requests.get(VERSION_URL, timeout=5)
            if response.status_code == 200:
                return response.json()
        except Exception:
            pass
        return None
    
    def _download_file(self, filename):
        """Download a file from GitHub."""
        if not HAS_REQUESTS:
            return None
        
        url = f"{GITHUB_RAW_BASE}/{filename}"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response.text
        except Exception:
            pass
        return None
    
    def _update_file(self, filename, content):
        """Update a local file with new content."""
        filepath = self.scripts_dir / filename
        try:
            # Create backup
            if filepath.exists():
                backup_path = filepath.with_suffix('.py.bak')
                try:
                    backup_path.write_text(filepath.read_text(encoding='utf-8'), encoding='utf-8')
                except Exception:
                    pass
            
            # Write new content
            filepath.write_text(content, encoding='utf-8')
            
            # Update hash in state
            self.state["file_hashes"][filename] = self._get_file_hash(filepath)
            return True
        except Exception as e:
            print(f"[Updater] Failed to update {filename}: {e}")
            return False
    
    def check_and_update(self, silent=True):
        """
        Check for updates and apply them.
        
        Args:
            silent: If True, don't print status messages.
        
        Returns:
            dict with 'updated' (bool) and 'files' (list of updated filenames)
        """
        result = {"updated": False, "files": [], "error": None}
        
        if not HAS_REQUESTS:
            result["error"] = "requests module not available"
            return result
        
        # Check interval
        if not self._should_check():
            if not silent:
                print("[Updater] Skipping check (checked recently)")
            return result
        
        if not silent:
            print("[Updater] Checking for updates...")
        
        # Fetch version info
        version_info = self._fetch_version_info()
        
        # Update last check time
        self.state["last_check"] = datetime.now().isoformat()
        
        if not version_info:
            # No version.json available, fall back to hash-based updates
            result = self._update_by_hash(silent)
        else:
            # Use version.json for updates
            result = self._update_from_version_info(version_info, silent)
        
        self._save_state()
        return result
    
    def _update_by_hash(self, silent=True):
        """Update files by comparing hashes with GitHub versions."""
        result = {"updated": False, "files": [], "error": None}
        
        for filename in UPDATABLE_FILES:
            local_path = self.scripts_dir / filename
            
            # Get local hash
            local_hash = self._get_file_hash(local_path) if local_path.exists() else None
            
            # Download file from GitHub
            content = self._download_file(filename)
            if not content:
                continue
            
            # Calculate remote hash
            remote_hash = hashlib.md5(content.encode('utf-8')).hexdigest()
            
            # Compare and update if different
            if local_hash != remote_hash:
                if self._update_file(filename, content):
                    result["files"].append(filename)
                    result["updated"] = True
                    if not silent:
                        print(f"[Updater] Updated: {filename}")
        
        return result
    
    def _update_from_version_info(self, version_info, silent=True):
        """Update files based on version.json manifest."""
        result = {"updated": False, "files": [], "error": None}
        
        remote_version = version_info.get("version")
        file_hashes = version_info.get("files", {})
        
        if not silent:
            print(f"[Updater] Remote version: {remote_version}")
        
        for filename, remote_hash in file_hashes.items():
            if filename not in UPDATABLE_FILES:
                continue
            
            local_path = self.scripts_dir / filename
            local_hash = self._get_file_hash(local_path) if local_path.exists() else None
            
            if local_hash != remote_hash:
                content = self._download_file(filename)
                if content and self._update_file(filename, content):
                    result["files"].append(filename)
                    result["updated"] = True
                    if not silent:
                        print(f"[Updater] Updated: {filename}")
        
        self.state["last_version"] = remote_version
        return result
    
    def run_async(self, callback=None):
        """
        Run update check in background thread.
        
        Args:
            callback: Optional function to call with result when done.
        """
        def _run():
            result = self.check_and_update(silent=True)
            if callback:
                callback(result)
        
        thread = threading.Thread(target=_run, daemon=True)
        thread.start()
        return thread


def check_for_updates(scripts_dir=None, silent=True, async_mode=True, callback=None):
    """
    Convenience function to check for updates.
    
    Args:
        scripts_dir: Directory containing scripts (default: auto-detect)
        silent: If True, don't print status messages
        async_mode: If True, run in background thread
        callback: Function to call when async update completes
    
    Returns:
        If async_mode=True: Thread object
        If async_mode=False: dict with update results
    """
    updater = AutoUpdater(scripts_dir)
    
    if async_mode:
        return updater.run_async(callback)
    else:
        return updater.check_and_update(silent=silent)


# Entry point for testing
if __name__ == "__main__":
    print("CAD Generator Auto-Updater")
    print("=" * 40)
    
    updater = AutoUpdater()
    result = updater.check_and_update(silent=False)
    
    if result["updated"]:
        print(f"\n✓ Updated {len(result['files'])} files:")
        for f in result["files"]:
            print(f"  - {f}")
    elif result["error"]:
        print(f"\n✗ Error: {result['error']}")
    else:
        print("\n✓ All files are up to date!")
