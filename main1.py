import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from Widget.logininterface import AccountPage_login


 
def main():
    app = QApplication(sys.argv)
    home = AccountPage_login()
    home.show()
    app.exec_()


if __name__ == '__main__':
    main()

