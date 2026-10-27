import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class HatebookApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Configure main window properties
        self.title("Hatebook")
        self.geometry("450x650")
        self.resizable(False, False)
        
        # In-memory dictionary acting as a volatile local database
        self.user_database = {}
        # Tracks the currently authenticated user session
        self.current_user = None
        
        # Main container to stack and switch multiple frames (pages)
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        
        # Initialize dictionary to hold references to the pages
        self.frames = {}
        
        # Instantiate and store the three application pages
        self.frames["PageI"] = RegistrationPage(parent=self.container, controller=self)
        self.frames["PageII"] = LoginPage(parent=self.container, controller=self)
        self.frames["PageIII"] = HomePage(parent=self.container, controller=self)
        
        # Position all pages on top of each other using grid layout
        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")
            
        # Set uniform weight so rows/columns stretch inside the main container
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        # Start the application path at the Registration Screen (Page I)
        self.show_frame("PageI")
        
    def show_frame(self, page_name):
        """Switches the visible interface to the requested frame."""
        frame = self.frames[page_name]
        
        # Dynamically inject the username header if navigating to the Home Screen
        if page_name == "PageIII" and self.current_user:
            frame.update_welcome_message(self.current_user["first_name"])
            
        frame.tkraise()


class RegistrationPage(tk.Frame):
    """Page I: Account registration interface based on light theme layout."""
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f0f2f5")
        self.controller = controller
        
        # Main Title Header
        title_label = tk.Label(self, text="Create a new account", font=("Helvetica", 22, "bold"), bg="#f0f2f5", fg="#1c1e21")
        title_label.pack(pady=(25, 2))
        
        subtitle_label = tk.Label(self, text="It's quick and easy.", font=("Helvetica", 12), bg="#f0f2f5", fg="#606770")
        subtitle_label.pack(pady=(0, 15))
        
        # Entry form grid layout container
        form_frame = tk.Frame(self, bg="#f0f2f5")
        form_frame.pack(pady=10)
        
        # First Name and Surname Fields
        self.first_name_entry = ttk.Entry(form_frame, width=18, font=("Helvetica", 11))
        self.first_name_entry.insert(0, "First name")
        self.first_name_entry.grid(row=0, column=0, padx=5, pady=5)
        
        self.surname_entry = ttk.Entry(form_frame, width=18, font=("Helvetica", 11))
        self.surname_entry.insert(0, "Surname")
        self.surname_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Contact and Password Fields
        self.contact_entry = ttk.Entry(form_frame, width=38, font=("Helvetica", 11))
        self.contact_entry.insert(0, "Mobile number or email address")
        self.contact_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        
        self.password_entry = ttk.Entry(form_frame, width=38, font=("Helvetica", 11), show="")
        self.password_entry.insert(0, "New password")
        self.password_entry.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        
        # Bind focus events to clean up structural placeholders automatically
        self.first_name_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(self.first_name_entry, "First name"))
        self.surname_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(self.surname_entry, "Surname"))
        self.contact_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(self.contact_entry, "Mobile number or email address"))
        self.password_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(self.password_entry, "New password", is_pass=True))
        
        # Date of Birth Selectors
        dob_label = tk.Label(self, text="Date of birth", font=("Helvetica", 10, "bold"), bg="#f0f2f5", fg="#606770")
        dob_label.pack(anchor="w", padx=45, pady=(10, 2))
        
        dob_frame = tk.Frame(self, bg="#f0f2f5")
        dob_frame.pack(pady=2)
        
        days = [str(i) for i in range(1, 32)]
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        years = [str(i) for i in range(2026, 1904, -1)]
        
        self.day_combo = ttk.Combobox(dob_frame, values=days, width=8, state="readonly")
        self.day_combo.set("17")
        self.day_combo.grid(row=0, column=0, padx=5)
        
        self.month_combo = ttk.Combobox(dob_frame, values=months, width=8, state="readonly")
        self.month_combo.set("Jan")
        self.month_combo.grid(row=0, column=1, padx=5)
        
        self.year_combo = ttk.Combobox(dob_frame, values=years, width=8, state="readonly")
        self.year_combo.set("1995")
        self.year_combo.grid(row=0, column=2, padx=5)
        
        # Gender Selection Module
        gender_label = tk.Label(self, text="Gender", font=("Helvetica", 10, "bold"), bg="#f0f2f5", fg="#606770")
        gender_label.pack(anchor="w", padx=45, pady=(10, 2))
        
        gender_frame = tk.Frame(self, bg="#f0f2f5")
        gender_frame.pack(pady=2)
        
        self.gender_var = tk.StringVar(value="Female")
        
        rb_female = tk.Radiobutton(gender_frame, text="Female", variable=self.gender_var, value="Female", bg="#f0f2f5", font=("Helvetica", 10))
        rb_female.grid(row=0, column=0, padx=15)
        
        rb_male = tk.Radiobutton(gender_frame, text="Male", variable=self.gender_var, value="Male", bg="#f0f2f5", font=("Helvetica", 10))
        rb_male.grid(row=0, column=1, padx=15)
        
        rb_custom = tk.Radiobutton(gender_frame, text="Custom", variable=self.gender_var, value="Custom", bg="#f0f2f5", font=("Helvetica", 10))
        rb_custom.grid(row=0, column=02, padx=15)
        
        # Regulatory Terms Disclaimer Note
        terms_text = "By clicking Sign Up, you agree to our Terms, Data Policy\nand Cookies Policy. You may receive SMS notifications from us."
        terms_label = tk.Label(self, text=terms_text, font=("Helvetica", 8), bg="#f0f2f5", fg="#777777", justify="center")
        terms_label.pack(pady=15)
        
        # Submission Confirmation Buttons
        signup_btn = tk.Button(self, text="Sign Up", bg="#00a400", fg="white", font=("Helvetica", 13, "bold"), width=18, bd=0, cursor="hand2", command=self.register_user)
        signup_btn.pack(pady=5)
        
        # Secondary Navigation to Login Route
        login_redirect_btn = tk.Button(self, text="Already have an account?", font=("Helvetica", 10, "underline"), bg="#f0f2f5", fg="#1877f2", bd=0, cursor="hand2", command=lambda: self.controller.show_frame("PageII"))
        login_redirect_btn.pack(pady=10)

    def clear_placeholder(self, entry, placeholder, is_pass=False):
        """Clears field placeholders systematically on selection focus events."""
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            if is_pass:
                entry.config(show="*")

    def register_user(self):
        """Validates fields inputs and registers user accounts inside local engine state."""
        fname = self.first_name_entry.get().strip()
        sname = self.surname_entry.get().strip()
        contact = self.contact_entry.get().strip()
        password = self.password_entry.get().strip()
        
        # Ensure fields do not contain initial placeholders or empty entries
        if fname in ("", "First name") or contact in ("", "Mobile number or email address") or password in ("", "New password"):
            messagebox.showerror("Validation Error", "Please complete all fields to register your account.")
            return
            
        # Store user payload structure inside the simulated database memory
        self.controller.user_database[contact] = {
            "first_name": fname,
            "surname": sname,
            "password": password,
            "dob": f"{self.day_combo.get()}-{self.month_combo.get()}-{self.year_combo.get()}",
            "gender": self.gender_var.get()
        }
        
        messagebox.showinfo("Registration Successful", f"Account for {fname} successfully generated! Proceeding to Login.")
        self.controller.show_frame("PageII")


class LoginPage(tk.Frame):
    """Page II: Modern clean design Login Panel built with Dark Mode colors."""
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#18191a")
        self.controller = controller
        
        # Top Visual Branding Graphics Banner
        banner_frame = tk.Frame(self, bg="#242526", height=140)
        banner_frame.pack(fill="x", side="top")
        banner_frame.pack_propagate(False)
        
        brand_label = tk.Label(banner_frame, text="f", font=("Helvetica", 50, "bold"), bg="#242526", fg="white")
        brand_label.pack(pady=(15, 0))
        
        # Form Submission Input Elements
        self.login_user_entry = ttk.Entry(self, width=32, font=("Helvetica", 12))
        self.login_user_entry.insert(0, "Phone number or email address")
        self.login_user_entry.pack(pady=(40, 10))
        
        self.login_pass_entry = ttk.Entry(self, width=32, font=("Helvetica", 12), show="")
        self.login_pass_entry.insert(0, "Password")
        self.login_pass_entry.pack(pady=10)
        
        # Dynamic interface events handling
                # Bind focus events to clear placeholders automatically when clicked
        self.login_user_entry.bind("<FocusIn>", lambda e: self.clear_field(self.login_user_entry, "Phone number or email address"))
        self.login_pass_entry.bind("<FocusIn>", lambda e: self.clear_field(self.login_pass_entry, "Password", is_pass=True))
        
        # Action Confirmation Controls
        login_btn = tk.Button(self, text="Log In", bg="#1877f2", fg="white", font=("Helvetica", 12, "bold"), width=30, bd=0, cursor="hand2", command=self.authenticate)
        login_btn.pack(pady=15)
        
        forgot_btn = tk.Button(self, text="Forgotten Password?", font=("Helvetica", 10), bg="#18191a", fg="#2e89ff", bd=0, cursor="hand2", command=lambda: messagebox.showinfo("Reset link", "A password reset link was dispatched to your address."))
        forgot_btn.pack(pady=5)
        
        back_btn = tk.Button(self, text="Back to Registration", font=("Helvetica", 10), bg="#18191a", fg="#b0b3b8", bd=0, cursor="hand2", command=lambda: self.controller.show_frame("PageI"))
        back_btn.pack(pady=5)
        
        # Separation line element
        separator = tk.Frame(self, bg="#3a3b3c", height=1, width=280)
        separator.pack(pady=25)
        
        # Account Creation Quick-Link Button
        create_account_btn = tk.Button(self, text="Create New Account", bg="#3a3b3c", fg="#e4e6eb", font=("Helvetica", 11, "bold"), width=24, bd=0, cursor="hand2", command=lambda: self.controller.show_frame("PageI"))
        create_account_btn.pack()

    def clear_field(self, entry, placeholder, is_pass=False):
        """Resets inputs text directly upon field entry initialization."""
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            if is_pass:
                entry.config(show="*")

    def authenticate(self):
        """Compares user inputs credentials against memory registry entries."""
        username = self.login_user_entry.get().strip()
        password = self.login_pass_entry.get().strip()
        
        db = self.controller.user_database
        if username in db and db[username]["password"] == password:
            self.controller.current_user = db[username]
            messagebox.showinfo("Access Granted", f"Welcome back, {db[username]['first_name']}!")
            self.controller.show_frame("PageIII")
        else:
            messagebox.showerror("Authentication Failed", "Invalid username or password configuration credentials provided.")


class HomePage(tk.Frame):
    """Page III: Logged secure application home dashboard containing features grid."""
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#e9ebee")
        self.controller = controller
        
        # Classic Top Blue Navigation Header bar
        self.nav_bar = tk.Frame(self, bg="#3b5998", height=55)
        self.nav_bar.pack(fill="x", side="top")
        self.nav_bar.pack_propagate(False)
        
        # Welcome message reference object label
        self.welcome_label = tk.Label(self.nav_bar, text="Hello, User", font=("Helvetica", 12, "bold"), bg="#3b5998", fg="white")
        self.welcome_label.pack(side="left", padx=15)
        
        logout_btn = tk.Button(self.nav_bar, text="Log Out", font=("Helvetica", 10, "bold"), bg="#4e69a2", fg="white", bd=0, padx=10, cursor="hand2", command=self.terminate_session)
        logout_btn.pack(side="right", padx=15)
        
        # Core Content Grid Panel Container
        grid_container = tk.Frame(self, bg="#e9ebee")
        grid_container.pack(expand=True, fill="both", padx=30, pady=30)
        
        # Dashboard items collection matrix data list configuration
        features = [
            ("📰 News Feed", "Browse user timelines and posts."),
            ("👤 Profile", "Update account settings and configurations."),
            ("👥 Friends", "Connect and track networks connections."),
            ("💬 Messages", "Review conversation text streams logs."),
            ("📍 Places", "Geolocate and discover local check-ins."),
            ("👨‍👩‍👧‍👦 Groups", "Manage structured collective interests hub."),
            ("📅 Events", "Track calendars events schedules."),
            ("📷 Photos", "Review and upload images data streams."),
            ("⚡ Chat", "Initiate immediate connection live channels.")
        ]
        
        # Build systematic functional buttons across coordinate positions loop structure
        for index, (title, description) in enumerate(features):
            row_idx = index // 3
            col_idx = index % 3
            
            # Encapsulated component widget cards structures definition modules
            card = tk.Button(grid_container, text=title, font=("Helvetica", 11, "bold"), bg="white", fg="#3b5998", relief="groove", bd=1, width=11, height=4, cursor="hand2", command=lambda t=title, d=description: messagebox.showinfo(t, d))
            card.grid(row=row_idx, column=col_idx, padx=8, pady=8, sticky="nsew")
            
        # Configure matrix elastic grid layout definitions variables
        for i in range(3):
            grid_container.grid_rowconfigure(i, weight=1)
            grid_container.grid_columnconfigure(i, weight=1)

    def update_welcome_message(self, name):
        """Updates text fields configurations headers with personalized data context."""
        self.welcome_label.config(text=f"Hello, {name}")

    def terminate_session(self):
        """Clears secure operational sessions scope pointers and drops users to landing screens."""
        self.controller.current_user = None
        self.controller.show_frame("PageII")


if __name__ == "__main__":
    app = HatebookApp()
    app.mainloop()
