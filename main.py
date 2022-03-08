import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from Widget.userlnterface import AccountPage_user


 
def main():
    app = QApplication(sys.argv)
    home = AccountPage_user()
    home.show()
    app.exec_()


if __name__ == '__main__':
    main()
