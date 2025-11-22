import tkinter as tk

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("CUI Lost & Found - Dashboard")
        self.root.geometry("800x600")
        
        tk.Label(root, text="Welcome to CUI, SWL Lost & Found Items Manager", font=("Arial", 20)).pack(pady=20)
        # Placeholder buttons for other forms

        tk.Button(root, text="Report Lost Item").pack(pady=10)
        tk.Button(root, text="Report Found Item").pack(pady=10)
        tk.Button(root, text="View Matches").pack(pady=10)
        tk.Button(root, text="Admin Panel").pack(pady=10)
# footer creation for 
        tk.Label(root, text="Author: Abdullah Rana", font=("Arial", 10), fg="gray").pack(side="bottom", pady=10)