import tkinter as tk
from tkinter import messagebox

class ReportLostForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Report Lost Item")
        self.root.geometry("400x400")
        
        # Item name
        tk.Label(root, text="Item Name:").pack(pady=5)
        self.item_name_entry = tk.Entry(root)
        self.item_name_entry.pack(pady=5)
        
        # Description
        tk.Label(root, text="Description:").pack(pady=5)
        self.description_entry = tk.Entry(root)
        self.description_entry.pack(pady=5)
        
        # Contact
        tk.Label(root, text="Contact Info:").pack(pady=5)
        self.contact_entry = tk.Entry(root)
        self.contact_entry.pack(pady=5)
        
        # Submit button
        tk.Button(root, text="Submit", command=self.submit).pack(pady=20)
    
    def submit(self):
        item_name = self.item_name_entry.get()
        description = self.description_entry.get()
        contact = self.contact_entry.get()
        
        # Dummy submission (we'll hook item_manager later)
        if item_name and description and contact:
            messagebox.showinfo("Success", f"Lost item '{item_name}' reported!")
            self.root.destroy()
        else:
            messagebox.showerror("Error", "Please fill all fields")
