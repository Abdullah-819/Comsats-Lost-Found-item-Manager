import tkinter as tk
from .report_lost_form import ReportLostForm
from .report_found_form import ReportFoundForm

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("CUI Lost & Found - Dashboard")
        self.root.geometry("800x600")
        
        tk.Label(root, text="Welcome to the Dashboard", font=("Arial", 20)).pack(pady=20)
        
        # Buttons to open forms
        tk.Button(root, text="Report Lost Item", command=self.open_lost_form).pack(pady=10)
        tk.Button(root, text="Report Found Item", command=self.open_found_form).pack(pady=10)
        tk.Button(root, text="View Matches").pack(pady=10)
        tk.Button(root, text="Admin Panel").pack(pady=10)
        
        # Footer
        tk.Label(root, text="Author: Abdullah Rana", font=("Arial", 10), fg="gray").pack(side="bottom", pady=10)
    
    def open_lost_form(self):
        lost_root = tk.Toplevel(self.root)
        ReportLostForm(lost_root)
    
    def open_found_form(self):
        found_root = tk.Toplevel(self.root)
        ReportFoundForm(found_root)
