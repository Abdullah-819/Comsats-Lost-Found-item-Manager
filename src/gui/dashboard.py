import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# Try importing the actual forms, otherwise use dummy functions for testing
try:
    from .report_lost_form import ReportLostForm
    from .report_found_form import ReportFoundForm
except ImportError:
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
            "sidebar_bg": "#2c3e50",
            "sidebar_fg": "#ecf0f1",
            "main_bg": "#f4f6f7",
            "accent": "#4CAF50",
            "card_bg": "#ffffff"
        }

        # --- LAYOUT ---
        self.sidebar = tk.Frame(root, bg=self.colors["sidebar_bg"], width=250)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        self.main_area = tk.Frame(root, bg=self.colors["main_bg"])
        self.main_area.pack(side="right", fill="both", expand=True)

        # --- BUILD UI ---
        self.create_sidebar()
        self.create_main_area_background()
        self.create_header()
        self.create_dashboard_cards()

        # Bind resize event to dynamically adjust background
        self.root.bind("<Configure>", self.resize_background)

    # --- SIDEBAR ---
    def create_sidebar(self):
        lbl_title = tk.Label(
            self.sidebar,
            text="CUI\nLost & Found",
            font=("Segoe UI", 20, "bold"),
            bg=self.colors["sidebar_bg"],
            fg=self.colors["accent"]
        )
        lbl_title.pack(pady=(30, 40))

        self.create_nav_btn("Dashboard", self.show_dashboard)
        self.create_nav_btn("View Matches", self.show_matches)
        self.create_nav_btn("Admin Panel", self.show_admin)

        tk.Frame(self.sidebar, bg=self.colors["sidebar_bg"]).pack(fill="y", expand=True)

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

        def on_enter(e):
            if e.widget['bg'] != self.colors["accent"]:
                e.widget['bg'] = "#34495e"
        def on_leave(e):
            if e.widget['bg'] != self.colors["accent"]:
                e.widget['bg'] = self.colors["sidebar_bg"]
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

    # --- MAIN AREA BACKGROUND ---
    def create_main_area_background(self):
        try:
            PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
            IMAGE_PATH = os.path.join(PROJECT_ROOT, 'images', 'dashboard_bg.jpg')  # Your JPG here

            if os.path.exists(IMAGE_PATH):
                self.bg_image_original = Image.open(IMAGE_PATH)
            else:
                print(f"Dashboard background image not found: {IMAGE_PATH}")
                self.bg_image_original = None
        except Exception as e:
            print("Error loading main background image:", e)
            self.bg_image_original = None

        # Create canvas to hold background and widgets
        self.main_canvas = tk.Canvas(self.main_area, highlightthickness=0)
        self.main_canvas.pack(fill="both", expand=True)

        # Frame to hold all content on top of background
        self.main_frame = tk.Frame(self.main_canvas, bg="", bd=0)
        self.main_window = self.main_canvas.create_window(0, 0, anchor="nw", window=self.main_frame)

        # Set initial background if exists
        if self.bg_image_original:
            w, h = self.main_area.winfo_width() or 800, self.main_area.winfo_height() or 600
            img_resized = self.bg_image_original.resize((w, h), Image.Resampling.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(img_resized)
            self.bg_image_id = self.main_canvas.create_image(0, 0, anchor="nw", image=self.bg_photo)

    # --- HEADER ---
    def create_header(self):
        header_frame = tk.Frame(self.main_frame, bg="white", height=60)
        header_frame.pack(fill="x")
        header_frame.pack_propagate(False)

        lbl_header = tk.Label(
            header_frame,
            text="Dashboard Overview",
            font=("Segoe UI", 16, "bold"),
            bg="white", fg="#333"
        )
        lbl_header.pack(side="left", padx=20)

        # Stats frame on top of background
        self.stats_frame = tk.Frame(self.main_frame, bg="", bd=0)
        self.stats_frame.pack(fill="x", padx=20, pady=20)

        self.create_stat_box(self.stats_frame, "Items Lost", "12", "#e74c3c", 0)
        self.create_stat_box(self.stats_frame, "Items Found", "8", "#27ae60", 1)
        self.create_stat_box(self.stats_frame, "Resolved", "5", "#2980b9", 2)

    # --- STAT BOX ---
    def create_stat_box(self, parent, title, count, color, col_idx):
        frame = tk.Frame(parent, bg="white", bd=1, relief="solid")
        frame.grid(row=0, column=col_idx, padx=10, sticky="ew")
        parent.grid_columnconfigure(col_idx, weight=1)

        tk.Label(frame, text=count, font=("Arial", 24, "bold"), fg=color, bg="white").pack(pady=(10, 0))
        tk.Label(frame, text=title, font=("Arial", 10), fg="#7f8c8d", bg="white").pack(pady=(0, 10))

    # --- DASHBOARD CARDS ---
    def create_dashboard_cards(self):
        cards_container = tk.Frame(self.main_frame, bg="", bd=0)
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

    # --- NAVIGATION ---
    def show_dashboard(self):
        messagebox.showinfo("Info", "You are already on the Dashboard")

    def show_matches(self):
        messagebox.showinfo("Info", "Matches Screen under construction")

    def show_admin(self):
        messagebox.showinfo("Info", "Admin Panel under construction")

    def logout(self):
        if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
            self.root.destroy()

    # --- DYNAMIC RESIZE ---
    def resize_background(self, event):
        if self.bg_image_original:
            w, h = event.width - 250, event.height  # subtract sidebar width
            if w <= 0: w = 800
            if h <= 0: h = 500
            img_resized = self.bg_image_original.resize((w, h), Image.Resampling.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(img_resized)
            self.main_canvas.itemconfig(self.bg_image_id, image=self.bg_photo)
        # Resize the frame window
        self.main_canvas.coords(self.main_window, 0, 0)
        self.main_canvas.itemconfig(self.main_window, width=event.width-250, height=event.height)

if __name__ == "__main__":
    root = tk.Tk()
    app = Dashboard(root)
    root.mainloop()
