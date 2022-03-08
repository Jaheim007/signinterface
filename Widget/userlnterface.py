from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from Widget.logininterface import AccountPage_login
from Widget.user import Ui_MainWindow

class AccountPage_user(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.sumbit_btn.clicked.connect(self.log)

    def log(self):
        firstname = self.firstnameline.text()
        lastname = self.lastnameline.text()
        user_email = self.emailline.text()
        mdp = self.motdepasseline.text()
        cmdp = self.confrimeline.text()

        if firstname == "" or lastname == "" or user_email == "":
            label = self.correction.setText("<font color=red>Mauvaise Information</font>")

        elif cmdp != mdp:
            label = self.correction.setText("<font color=red>Mauvaise mdp</font>")
        
        else:
        
            self.win = AccountPage_login()
            self.win.show()