from src.gui.login_form import LoginForm
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginForm(root)
    root.mainloop()