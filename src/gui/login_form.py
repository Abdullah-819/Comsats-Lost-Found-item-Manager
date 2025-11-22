import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

# Dummy dashboard for testing
try:
    from .dashboard import Dashboard
except ImportError:
    try:
        from dashboard import Dashboard
    except ImportError:
        class Dashboard:
            def __init__(self, root):
                root.title("Dashboard")
                tk.Label(root, text="Dashboard Loaded!", font=("Arial", 20)).pack(pady=50)

class LoginForm:
    def __init__(self, root):
        self.root = root
        self.root.title("CUI Lost & Found - Login")
        self.root.geometry("900x600") 
        self.root.minsize(600, 450)
        self.root.configure(bg="black")

        # 1. Setup Canvas
        self.canvas = tk.Canvas(root, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # 2. Load Background Image
        self.bg_image_original = None
        try:
            PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
            IMAGE_PATH = os.path.join(PROJECT_ROOT, 'images', 'login_bg.jpg')
            
            if os.path.exists(IMAGE_PATH):
                self.bg_image_original = Image.open(IMAGE_PATH)
                self.bg_photo = ImageTk.PhotoImage(self.bg_image_original)
                self.bg_image_id = self.canvas.create_image(0, 0, anchor="nw", image=self.bg_photo)
            else:
                print(f"Image not found at: {IMAGE_PATH}")
                self.canvas.configure(bg="#3498db") # Fallback Blue
                
        except Exception as e:
            print(f"Background Error: {e}")
            self.canvas.configure(bg="#3498db")

        # 3. Create Login Card Frame
        self.login_frame = tk.Frame(self.canvas, bg="white", bd=0, relief="flat")
        
        # Title
        tk.Label(self.login_frame, text="USER LOGIN", font=("Segoe UI", 18, "bold"), 
                 bg="white", fg="#333").pack(pady=(30, 10))

        # Input Container
        form_content = tk.Frame(self.login_frame, bg="white")
        form_content.pack(padx=40, pady=20)

        # Username
        tk.Label(form_content, text="Username:", font=("Segoe UI", 11), bg="white", anchor="w").grid(row=0, column=0, sticky="w", pady=5)
        self.username_entry = ttk.Entry(form_content, font=("Segoe UI", 11), width=28)
        self.username_entry.grid(row=1, column=0, pady=(0, 15))

        # Password
        tk.Label(form_content, text="Password:", font=("Segoe UI", 11), bg="white", anchor="w").grid(row=2, column=0, sticky="w", pady=5)
        self.password_entry = ttk.Entry(form_content, show="*", font=("Segoe UI", 11), width=28)
        self.password_entry.grid(row=3, column=0, pady=(0, 25))

        # Button
        self.login_btn = tk.Button(
            self.login_frame, text="LOGIN", font=("Segoe UI", 11, "bold"),
            bg="#4CAF50", fg="white", activebackground="#45a049",
            cursor="hand2", width=22, height=2, bd=0, 
            command=self.login
        )
        self.login_btn.pack(pady=(0, 40))
        
        # Hover Effects
        self.login_btn.bind("<Enter>", lambda e: self.login_btn.config(bg="#45a049"))
        self.login_btn.bind("<Leave>", lambda e: self.login_btn.config(bg="#4CAF50"))

        # 4. Place Frame on Canvas (Centered)
        self.login_window_id = self.canvas.create_window(
            450, 300, window=self.login_frame, anchor="center"
        )

        # 5. Bind Resize Event
        self.root.bind("<Configure>", self.resize_ui)

    def resize_ui(self, event):
        # --- THE FIX IS HERE ---
        # Only resize if the event comes from the main window (root)
        if event.widget == self.root:
            w = event.width
            h = event.height

            # Resize background image
            if self.bg_image_original:
                img = self.bg_image_original.resize((w, h), Image.Resampling.LANCZOS)
                self.bg_photo = ImageTk.PhotoImage(img)
                self.canvas.itemconfig(self.bg_image_id, image=self.bg_photo)

            # Re-center the login card
            self.canvas.coords(self.login_window_id, w // 2, h // 2)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username == "admin" and password == "admin":
            self.root.destroy()
            try:
                dashboard_root = tk.Tk()
                Dashboard(dashboard_root)
                dashboard_root.mainloop()
            except Exception as e:
                messagebox.showerror("Error", f"Could not load dashboard: {e}")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginForm(root)
    root.mainloop()