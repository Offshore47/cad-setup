"""
CAD Generator Authentication Module
Handles login, token management, and subscription validation
"""
import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json
import os
from pathlib import Path
from datetime import datetime, timedelta
import threading
import time

# API Configuration
API_BASE_URL = "https://equationparadise.com/api"  # Production
# API_BASE_URL = "http://localhost:5000/api"  # Development

TOKEN_FILE = Path.home() / ".equationparadise" / "token.json"

# Admin emails that bypass subscription checks
ADMIN_EMAILS = [
    "staff@equationparadise.com",
    "jeff@equationparadise.com",
    "admin@equationparadise.com"
]

class AuthManager:
    """Manages authentication and subscription validation"""
    
    def __init__(self):
        self.token = None
        self.email = None
        self.subscription_active = False
        self.subscription_expires = None
        self.last_check = None
        self._load_token()
    
    def _load_token(self):
        """Load stored authentication token"""
        try:
            if TOKEN_FILE.exists():
                with open(TOKEN_FILE, 'r') as f:
                    data = json.load(f)
                    self.token = data.get('token')
                    self.email = data.get('email')
                    self.subscription_active = data.get('subscription_active', False)
                    expires_str = data.get('subscription_expires')
                    if expires_str:
                        self.subscription_expires = datetime.fromisoformat(expires_str)
        except Exception as e:
            print(f"Error loading token: {e}")
            self.token = None
    
    def _save_token(self):
        """Save authentication token to disk"""
        try:
            TOKEN_FILE.parent.mkdir(exist_ok=True)
            with open(TOKEN_FILE, 'w') as f:
                json.dump({
                    'token': self.token,
                    'email': self.email,
                    'subscription_active': self.subscription_active,
                    'subscription_expires': self.subscription_expires.isoformat() if self.subscription_expires else None,
                    'last_updated': datetime.now().isoformat()
                }, f)
        except Exception as e:
            print(f"Error saving token: {e}")
    
    def is_admin(self):
        """Check if current user is an admin (bypasses subscription checks)"""
        return self.email and self.email.lower() in [e.lower() for e in ADMIN_EMAILS]
    
    def validate_token(self):
        """
        Validate stored token with API.
        Returns True if valid and subscription active, False otherwise.
        """
        if not self.token:
            return False
        
        # Admin bypass - always grant access
        if self.is_admin():
            print(f"Admin access granted for {self.email}")
            return True
        
        try:
            response = requests.post(
                f"{API_BASE_URL}/auth/validate-token",
                headers={"Authorization": f"Bearer {self.token}"},
                timeout=5
            )
            
            if response.status_code == 200:
                data = response.json()
                self.subscription_active = data.get('subscription_active', False)
                expires_str = data.get('subscription_expires')
                if expires_str:
                    self.subscription_expires = datetime.fromisoformat(expires_str)
                self.last_check = datetime.now()
                self._save_token()
                return self.subscription_active
            else:
                # Token invalid or subscription expired
                return False
                
        except requests.exceptions.RequestException as e:
            # Network error - treat as offline
            print(f"Network error validating token: {e}")
            raise ConnectionError("Cannot connect to authentication server")
    
    def login(self, email, password):
        """
        Authenticate user with email/password.
        Returns True if successful, raises exception with error message if not.
        """
        try:
            response = requests.post(
                f"{API_BASE_URL}/auth/login",
                json={"email": email, "password": password},
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                self.token = data.get('token')
                self.email = email  # Store the login email
                self.subscription_active = data.get('subscription_active', False)
                expires_str = data.get('subscription_expires')
                if expires_str:
                    self.subscription_expires = datetime.fromisoformat(expires_str)
                self.last_check = datetime.now()
                self._save_token()
                return True
            else:
                error_data = response.json()
                error_msg = error_data.get('error', 'Login failed')
                raise ValueError(error_msg)
                
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Cannot connect to authentication server: {e}")
    
    def logout(self):
        """Clear stored authentication"""
        self.token = None
        self.email = None
        self.subscription_active = False
        self.subscription_expires = None
        if TOKEN_FILE.exists():
            TOKEN_FILE.unlink()
    
    def needs_recheck(self):
        """Check if subscription validation needs refresh (15 minute intervals)"""
        if not self.last_check:
            return True
        return (datetime.now() - self.last_check) > timedelta(minutes=15)


class LoginWindow:
    """Login window for CAD Generator"""
    
    def __init__(self, on_success_callback):
        self.on_success = on_success_callback
        self.auth_manager = AuthManager()
        
        # Create main window
        self.root = tk.Tk()
        self.root.title("Equation Paradise - CAD Generator Login")
        
        # Set window size with proper padding - FIXED HEIGHT to prevent cutoff
        window_width = 450
        window_height = 500  # Increased to ensure all content visible
        
        # Center window on screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.root.resizable(False, False)  # Fixed size to prevent layout issues
        
        # Dark theme colors
        bg_dark = "#1a1a22"
        bg_card = "#2a2a35"
        text_primary = "#f8fafc"
        text_secondary = "#94a3b8"
        accent = "#10b981"
        
        self.root.configure(bg=bg_dark)
        
        # Main container with proper padding
        main_frame = tk.Frame(self.root, bg=bg_dark)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Logo/Header
        header_frame = tk.Frame(main_frame, bg=bg_dark)
        header_frame.pack(pady=(0, 20))
        
        logo_label = tk.Label(
            header_frame,
            text="⚡ Equation Paradise",
            font=("Segoe UI", 18, "bold"),
            bg=bg_dark,
            fg=text_primary
        )
        logo_label.pack()
        
        subtitle = tk.Label(
            header_frame,
            text="CAD Generator Authentication",
            font=("Segoe UI", 10),
            bg=bg_dark,
            fg=text_secondary
        )
        subtitle.pack(pady=(5, 0))
        
        # Card container
        card_frame = tk.Frame(main_frame, bg=bg_card, relief=tk.FLAT)
        card_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Card content with padding
        content_frame = tk.Frame(card_frame, bg=bg_card)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=25, pady=25)
        
        # Title
        title = tk.Label(
            content_frame,
            text="Sign In Required",
            font=("Segoe UI", 14, "bold"),
            bg=bg_card,
            fg=text_primary
        )
        title.pack(pady=(0, 5))
        
        subtitle2 = tk.Label(
            content_frame,
            text="Active subscription required to generate CAD parts",
            font=("Segoe UI", 9),
            bg=bg_card,
            fg=text_secondary
        )
        subtitle2.pack(pady=(0, 20))
        
        # Email field
        email_label = tk.Label(
            content_frame,
            text="Email",
            font=("Segoe UI", 9, "bold"),
            bg=bg_card,
            fg=text_secondary
        )
        email_label.pack(anchor='w', pady=(0, 5))
        
        self.email_entry = tk.Entry(
            content_frame,
            font=("Segoe UI", 10),
            bg="#1a1a22",
            fg=text_primary,
            insertbackground=text_primary,
            relief=tk.FLAT,
            bd=0,
            highlightthickness=1,
            highlightbackground="#3a3a45",
            highlightcolor=accent
        )
        self.email_entry.pack(fill=tk.X, ipady=8, pady=(0, 15))
        
        # Password field
        password_label = tk.Label(
            content_frame,
            text="Password",
            font=("Segoe UI", 9, "bold"),
            bg=bg_card,
            fg=text_secondary
        )
        password_label.pack(anchor='w', pady=(0, 5))
        
        self.password_entry = tk.Entry(
            content_frame,
            font=("Segoe UI", 10),
            bg="#1a1a22",
            fg=text_primary,
            insertbackground=text_primary,
            show="●",
            relief=tk.FLAT,
            bd=0,
            highlightthickness=1,
            highlightbackground="#3a3a45",
            highlightcolor=accent
        )
        self.password_entry.pack(fill=tk.X, ipady=8, pady=(0, 20))
        
        # Error message label (hidden by default)
        self.error_label = tk.Label(
            content_frame,
            text="",
            font=("Segoe UI", 9),
            bg=bg_card,
            fg="#ef4444",
            wraplength=350
        )
        self.error_label.pack(pady=(0, 10))
        
        # Login button
        self.login_btn = tk.Button(
            content_frame,
            text="Sign In",
            font=("Segoe UI", 10, "bold"),
            bg=accent,
            fg="white",
            activebackground="#059669",
            activeforeground="white",
            relief=tk.FLAT,
            bd=0,
            cursor="hand2",
            command=self._attempt_login
        )
        self.login_btn.pack(fill=tk.X, ipady=10, pady=(0, 15))
        
        # Footer links
        footer_frame = tk.Frame(content_frame, bg=bg_card)
        footer_frame.pack(pady=(10, 0))
        
        forgot_link = tk.Label(
            footer_frame,
            text="Forgot password?",
            font=("Segoe UI", 9, "underline"),
            bg=bg_card,
            fg=accent,
            cursor="hand2"
        )
        forgot_link.pack(side=tk.LEFT, padx=5)
        forgot_link.bind("<Button-1>", lambda e: self._open_url("https://equationparadise.com/forgot-password"))
        
        separator = tk.Label(
            footer_frame,
            text="|",
            font=("Segoe UI", 9),
            bg=bg_card,
            fg=text_secondary
        )
        separator.pack(side=tk.LEFT, padx=5)
        
        signup_link = tk.Label(
            footer_frame,
            text="Create account",
            font=("Segoe UI", 9, "underline"),
            bg=bg_card,
            fg=accent,
            cursor="hand2"
        )
        signup_link.pack(side=tk.LEFT, padx=5)
        signup_link.bind("<Button-1>", lambda e: self._open_url("https://equationparadise.com/register"))
        
        # Bind Enter key to login
        self.root.bind('<Return>', lambda e: self._attempt_login())
        
        # Focus email field
        self.email_entry.focus()
    
    def _attempt_login(self):
        """Attempt to log in user"""
        email = self.email_entry.get().strip()
        password = self.password_entry.get()
        
        if not email or not password:
            self._show_error("Please enter both email and password")
            return
        
        # Disable button during login
        self.login_btn.config(state='disabled', text="Signing in...")
        self.error_label.config(text="")
        
        # Perform login in background thread
        def login_thread():
            try:
                success = self.auth_manager.login(email, password)
                if success:
                    if self.auth_manager.subscription_active:
                        self.root.after(0, self._login_success)
                    else:
                        self.root.after(0, lambda: self._show_error(
                            "Subscription expired. Please renew your subscription at equationparadise.com"
                        ))
                        self.root.after(0, lambda: self.login_btn.config(state='normal', text="Sign In"))
            except ValueError as e:
                self.root.after(0, lambda: self._show_error(str(e)))
                self.root.after(0, lambda: self.login_btn.config(state='normal', text="Sign In"))
            except ConnectionError as e:
                self.root.after(0, lambda: self._show_error(
                    "Cannot connect to server. Please check your internet connection."
                ))
                self.root.after(0, lambda: self.login_btn.config(state='normal', text="Sign In"))
        
        thread = threading.Thread(target=login_thread, daemon=True)
        thread.start()
    
    def _show_error(self, message):
        """Display error message"""
        self.error_label.config(text=message)
    
    def _login_success(self):
        """Handle successful login"""
        self.root.destroy()
        if self.on_success:
            self.on_success(self.auth_manager)
    
    def _open_url(self, url):
        """Open URL in browser"""
        import webbrowser
        webbrowser.open(url)
    
    def show(self):
        """Display login window"""
        self.root.mainloop()


def require_authentication(callback):
    """
    Decorator/function to require authentication before running callback.
    Shows login screen if needed, then calls callback with AuthManager.
    
    Usage:
        def run_generator(auth_manager):
            # Your generator code here
            pass
        
        require_authentication(run_generator)
    """
    auth_manager = AuthManager()
    
    # Try silent validation first
    try:
        if auth_manager.token and auth_manager.validate_token():
            # Already authenticated and subscription active
            callback(auth_manager)
            return
    except ConnectionError:
        # Offline - need to show error
        pass
    
    # Need to show login
    login_window = LoginWindow(callback)
    login_window.show()


# Example usage
if __name__ == "__main__":
    def on_authenticated(auth_manager):
        print(f"✓ Authenticated successfully!")
        print(f"  Subscription active: {auth_manager.subscription_active}")
        print(f"  Expires: {auth_manager.subscription_expires}")
    
    require_authentication(on_authenticated)
