import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from .dashboard import Dashboard

class LoginForm:
    def __init__(self, root):
        self.root = root
        self.root.title("CUI Lost & Found - Login")
        self.root.geometry("500x350")
        self.root.resizable(False, False)

        # Load background image
        bg_image = Image.open("images/login_bg.jpg")
        bg_image = bg_image.resize((500, 350))  # Resize to window size
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        # Create a canvas to place the background
        self.canvas = tk.Canvas(root, width=500, height=350)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Frame for login fields
        self.frame = tk.Frame(root, bg="white", bd=2, relief="ridge")
        self.frame.place(relx=0.5, rely=0.5, anchor="center", width=350, height=200)

        # Username
        tk.Label(self.frame, text="Username:", bg="white", font=("Arial", 12)).place(x=20, y=20)
        self.username_entry = ttk.Entry(self.frame, font=("Arial", 12))
        self.username_entry.place(x=120, y=20, width=200)

        # Password
        tk.Label(self.frame, text="Password:", bg="white", font=("Arial", 12)).place(x=20, y=70)
        self.password_entry = ttk.Entry(self.frame, show="*", font=("Arial", 12))
        self.password_entry.place(x=120, y=70, width=200)

        # Login button
        self.login_btn = ttk.Button(self.frame, text="Login", command=self.login)
        self.login_btn.place(x=120, y=120, width=200)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "Abdullah" and password == "123":
            self.root.destroy()
            dashboard_root = tk.Tk()
            Dashboard(dashboard_root)
            dashboard_root.mainloop()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginForm(root)
    root.mainloop()
