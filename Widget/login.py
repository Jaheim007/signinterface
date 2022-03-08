# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1224, 829)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-6, -5, 1231, 841))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/Static/sea-g917318aa2_640.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(360, 120, 521, 621))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"background-color: rgb(85, 170, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.header = QtWidgets.QLabel(self.frame_2)
        self.header.setGeometry(QtCore.QRect(160, 50, 191, 51))
        self.header.setStyleSheet("font: 25 20pt \"Segoe UI Light\";\n"
"text-decoration: underline;")
        self.header.setObjectName("header")
        self.Lastnamelabel = QtWidgets.QLabel(self.frame_2)
        self.Lastnamelabel.setGeometry(QtCore.QRect(50, 140, 151, 31))
        self.Lastnamelabel.setObjectName("Lastnamelabel")
        self.motdepasselabel = QtWidgets.QLabel(self.frame_2)
        self.motdepasselabel.setGeometry(QtCore.QRect(50, 270, 151, 31))
        self.motdepasselabel.setObjectName("motdepasselabel")
        self.lastnameline = QtWidgets.QLineEdit(self.frame_2)
        self.lastnameline.setGeometry(QtCore.QRect(50, 190, 391, 41))
        self.lastnameline.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:none;")
        self.lastnameline.setObjectName("lastnameline")
        self.motdepasseline = QtWidgets.QLineEdit(self.frame_2)
        self.motdepasseline.setGeometry(QtCore.QRect(50, 330, 391, 41))
        self.motdepasseline.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:none;")
        self.motdepasseline.setObjectName("motdepasseline")
        self.sumbit_btn = QtWidgets.QPushButton(self.frame_2)
        self.sumbit_btn.setGeometry(QtCore.QRect(180, 500, 131, 41))
        self.sumbit_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border-radius:none;")
        self.sumbit_btn.setAutoDefault(False)
        self.sumbit_btn.setDefault(True)
        self.sumbit_btn.setFlat(False)
        self.sumbit_btn.setObjectName("sumbit_btn")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(50, 400, 381, 20))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Connexion</p></body></html>"))
        self.Lastnamelabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Username</span></p></body></html>"))
        self.motdepasselabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Mot de passe</span></p></body></html>"))
        self.sumbit_btn.setText(_translate("MainWindow", "Sumbit"))
import resources1_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
