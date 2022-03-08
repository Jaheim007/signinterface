from PyQt5.QtWidgets import QMainWindow, QApplication
from Widget.login import Ui_MainWindow


class AccountPage_login(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)