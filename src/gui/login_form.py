import tkinter as tk
from tkinter import messagebox
from .dashboard import Dashboard

class LoginForm:
    def __init__(self, root):
        self.root = root
        self.root.title("CUI Lost & Found - Login")
        self.root.geometry("400x300")
        
        # Username
        tk.Label(root, text="Username:").pack(pady=10)
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=5)
        
        # Password
        tk.Label(root, text="Password:").pack(pady=10)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack(pady=5)
        
        # Login button
        tk.Button(root, text="Login", command=self.login).pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Dummy check (we'll replace with user_manager later)
        if username == "admin" and password == "admin":
            self.root.destroy()
            dashboard_root = tk.Tk()
            Dashboard(dashboard_root)
            dashboard_root.mainloop()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")


if __name__ == "__main__":
    root = tk.Tk()
    LoginForm(root)
    root.mainloop()
