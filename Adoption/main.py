from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
import sys
import os

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_path = os.path.join(os.path.dirname(__file__), "GUI", "login.ui")
        uic.loadUi(ui_path, self)

class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_path = os.path.join(os.path.dirname(__file__), "GUI", "register.ui")
        uic.loadUi(ui_path, self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec())