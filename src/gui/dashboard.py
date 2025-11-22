import tkinter as tk
from tkinter import ttk, messagebox

# Try importing the actual forms, otherwise use dummy functions for testing
try:
    from .report_lost_form import ReportLostForm
    from .report_found_form import ReportFoundForm
except ImportError:
    # Dummy placeholders if files don't exist yet
    def ReportLostForm(root):
        tk.Label(root, text="Lost Form Placeholder").pack()
    def ReportFoundForm(root):
        tk.Label(root, text="Found Form Placeholder").pack()

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("CUI Lost & Found - Dashboard")
        self.root.geometry("1000x600")
        self.root.minsize(800, 500)
        
        # Colors
        self.colors = {
            "sidebar_bg": "#2c3e50",      # Dark Blue-Grey
            "sidebar_fg": "#ecf0f1",      # White-ish
            "main_bg": "#f4f6f7",         # Light Grey
            "accent": "#4CAF50",          # Green
            "card_bg": "#ffffff"          # White
        }

        # --- LAYOUT STRUCTURE ---
        # 1. Sidebar (Left)
        self.sidebar = tk.Frame(root, bg=self.colors["sidebar_bg"], width=250)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False) 

        # 2. Main Content (Right)
        self.main_area = tk.Frame(root, bg=self.colors["main_bg"])
        self.main_area.pack(side="right", fill="both", expand=True)

        # --- BUILD UI ---
        self.create_sidebar()
        self.create_header()
        self.create_dashboard_cards()

    def create_sidebar(self):
        # App Logo / Title
        lbl_title = tk.Label(
            self.sidebar, 
            text="CUI\nLost & Found", 
            font=("Segoe UI", 20, "bold"), 
            bg=self.colors["sidebar_bg"], 
            fg=self.colors["accent"]
        )
        lbl_title.pack(pady=(30, 40))

        # Navigation Buttons
        # ERROR WAS HERE: These buttons call functions that must exist!
        self.create_nav_btn("Dashboard", self.show_dashboard)
        self.create_nav_btn("View Matches", self.show_matches)
        self.create_nav_btn("Admin Panel", self.show_admin)
        
        # Spacer
        tk.Frame(self.sidebar, bg=self.colors["sidebar_bg"]).pack(fill="y", expand=True)

        # Footer
        btn_logout = tk.Button(
            self.sidebar, 
            text="Logout", 
            bg="#c0392b", fg="white", 
            font=("Segoe UI", 10, "bold"),
            bd=0, cursor="hand2",
            command=self.logout
        )
        btn_logout.pack(fill="x", padx=20, pady=10)

        lbl_author = tk.Label(
            self.sidebar, 
            text="Dev: Abdullah Rana", 
            font=("Arial", 8), 
            bg=self.colors["sidebar_bg"], 
            fg="#95a5a6"
        )
        lbl_author.pack(side="bottom", pady=10)

    def create_nav_btn(self, text, command):
        btn = tk.Button(
            self.sidebar, 
            text=f"  {text}", 
            font=("Segoe UI", 12), 
            bg=self.colors["sidebar_bg"], 
            fg=self.colors["sidebar_fg"], 
            activebackground=self.colors["accent"],
            activeforeground="white",
            bd=0, anchor="w", cursor="hand2",
            command=command
        )
        btn.pack(fill="x", pady=2, padx=0)
        
        # Hover effect
        def on_enter(e):
            if e.widget['bg'] != self.colors["accent"]:
                e.widget['bg'] = "#34495e"
        def on_leave(e):
            if e.widget['bg'] != self.colors["accent"]:
                e.widget['bg'] = self.colors["sidebar_bg"]
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

    def create_header(self):
        header_frame = tk.Frame(self.main_area, bg="white", height=60)
        header_frame.pack(fill="x")
        header_frame.pack_propagate(False)

        lbl_header = tk.Label(
            header_frame, 
            text="Dashboard Overview", 
            font=("Segoe UI", 16, "bold"), 
            bg="white", fg="#333"
        )
        lbl_header.pack(side="left", padx=20)

        # Stats Bar
        stats_frame = tk.Frame(self.main_area, bg=self.colors["main_bg"])
        stats_frame.pack(fill="x", padx=20, pady=20)

        self.create_stat_box(stats_frame, "Items Lost", "12", "#e74c3c", 0)
        self.create_stat_box(stats_frame, "Items Found", "8", "#27ae60", 1)
        self.create_stat_box(stats_frame, "Resolved", "5", "#2980b9", 2)

    def create_stat_box(self, parent, title, count, color, col_idx):
        frame = tk.Frame(parent, bg="white", bd=1, relief="solid")
        frame.grid(row=0, column=col_idx, padx=10, sticky="ew")
        parent.grid_columnconfigure(col_idx, weight=1)

        tk.Label(frame, text=count, font=("Arial", 24, "bold"), fg=color, bg="white").pack(pady=(10, 0))
        tk.Label(frame, text=title, font=("Arial", 10), fg="#7f8c8d", bg="white").pack(pady=(0, 10))

    def create_dashboard_cards(self):
        cards_container = tk.Frame(self.main_area, bg=self.colors["main_bg"])
        cards_container.pack(fill="both", expand=True, padx=30, pady=10)

        self.create_action_card(cards_container, "REPORT LOST ITEM", "Click here if you have lost something.", "#e74c3c", self.open_lost_form)
        self.create_action_card(cards_container, "REPORT FOUND ITEM", "Click here if you found an item.", "#27ae60", self.open_found_form)

    def create_action_card(self, parent, title, subtitle, color, command):
        card = tk.Frame(parent, bg="white", bd=0, cursor="hand2")
        card.pack(fill="x", pady=10, ipady=10)

        strip = tk.Frame(card, bg=color, width=10)
        strip.pack(side="left", fill="y")

        content = tk.Frame(card, bg="white")
        content.pack(side="left", padx=20)

        tk.Label(content, text=title, font=("Segoe UI", 14, "bold"), fg="#333", bg="white", anchor="w").pack(fill="x")
        tk.Label(content, text=subtitle, font=("Segoe UI", 10), fg="#7f8c8d", bg="white", anchor="w").pack(fill="x")
        tk.Label(card, text="➔", font=("Arial", 20), fg="#bdc3c7", bg="white").pack(side="right", padx=20)

        for widget in [card, content, strip]:
            widget.bind("<Button-1>", lambda e: command())

    # --- FORM ACTIONS ---
    def open_lost_form(self):
        lost_root = tk.Toplevel(self.root)
        ReportLostForm(lost_root)

    def open_found_form(self):
        found_root = tk.Toplevel(self.root)
        ReportFoundForm(found_root)

    # --- THE MISSING FUNCTIONS THAT CAUSED THE ERROR ---
    def show_dashboard(self):
        messagebox.showinfo("Info", "You are already on the Dashboard")

    def show_matches(self):
        messagebox.showinfo("Info", "Matches Screen under construction")

    def show_admin(self):
        messagebox.showinfo("Info", "Admin Panel under construction")

    def logout(self):
        if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Dashboard(root)
    root.mainloop()