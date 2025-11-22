from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QSize
import sys
import os

# --- LOGIN FORM ---
class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CUI Lost & Found - Login")
        self.setGeometry(200, 100, 900, 600)
        self.setMinimumSize(600, 450)

        # --- Background Image ---
        self.bg_label = QLabel(self)
        self.bg_label.setScaledContents(True)  # scales automatically
        self.bg_label.setGeometry(0, 0, self.width(), self.height())

        PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        IMAGE_PATH = os.path.join(PROJECT_ROOT, "images", "login_bg.jpg")
        if os.path.exists(IMAGE_PATH):
            self.bg_pixmap = QPixmap(IMAGE_PATH)
            self.bg_label.setPixmap(self.bg_pixmap)
        else:
            self.bg_label.setStyleSheet("background-color: #3498db;")  # fallback color

        # --- Semi-transparent login card ---
        self.card = QLabel(self)
        self.card.setStyleSheet(
            "background-color: rgba(255, 255, 255, 200); border-radius: 15px;"
        )
        self.card.setFixedSize(400, 300)
        self.center_card()

        # --- Widgets inside card ---
        self.username = QLineEdit(self.card)
        self.username.setPlaceholderText("Username")
        self.username.setGeometry(50, 80, 300, 40)

        self.password = QLineEdit(self.card)
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password.setGeometry(50, 140, 300, 40)

        self.login_btn = QPushButton("Login", self.card)
        self.login_btn.setGeometry(100, 200, 200, 50)
        self.login_btn.setStyleSheet(
            """
            QPushButton {
                background-color: #4CAF50; color: white; font-weight: bold;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            """
        )
        self.login_btn.clicked.connect(self.login)

        # --- Resize event ---
        self.resizeEvent = self.on_resize

    def center_card(self):
        """Centers the login card in the window."""
        window_width = self.width()
        window_height = self.height()
        card_width = self.card.width()
        card_height = self.card.height()
        self.card.move(
            (window_width - card_width) // 2, (window_height - card_height) // 2
        )

    def on_resize(self, event):
        """Handle window resize: scale background and center card."""
        if hasattr(self, 'bg_pixmap'):
            self.bg_label.setPixmap(self.bg_pixmap.scaled(
                self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding
            ))
        self.bg_label.setGeometry(0, 0, self.width(), self.height())
        self.center_card()

    def login(self):
        """Login verification."""
        username = self.username.text()
        password = self.password.text()
        if username == "admin" and password == "admin":
            self.close()
            try:
                from dashboard import DashboardWindow
                self.dashboard = DashboardWindow()
                self.dashboard.show()
            except Exception as e:
                print(f"Error opening Dashboard: {e}")
        else:
            print("Invalid credentials")

# --- RUN APP ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginForm()
    window.show()
    sys.exit(app.exec())
