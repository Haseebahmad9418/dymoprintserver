# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'authcode.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import debugmode


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        if(debugmode.debug==False):
            MainWindow.setWindowFlags( Qt.Window|Qt.FramelessWindowHint)
            MainWindow.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 480, 320))
        self.frame.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.txtPassword = QtWidgets.QLineEdit(self.frame)
        self.txtPassword.setGeometry(QtCore.QRect(80, 60, 150, 40))
        self.txtPassword.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.txtPassword.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.txtPassword.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.txtPassword.setFrame(False)
        self.txtPassword.setAlignment(QtCore.Qt.AlignCenter)
        self.txtPassword.setObjectName("txtPassword")
        self.label2 = QtWidgets.QLabel(self.frame)
        self.label2.setGeometry(QtCore.QRect(30, 20, 420, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.pb1 = QtWidgets.QPushButton(self.frame)
        self.pb1.setGeometry(QtCore.QRect(250, 60, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pb1.setFont(font)
        self.pb1.setStyleSheet("background-color: rgb(196, 160, 0);")
        self.pb1.setObjectName("pb1")
        self.frame_numeric = QtWidgets.QFrame(self.centralwidget)
        self.frame_numeric.setGeometry(QtCore.QRect(260, 400, 250, 200))
        self.frame_numeric.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.frame_numeric.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"border-radius: 25px;\n"
"")
        self.frame_numeric.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_numeric.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_numeric.setObjectName("frame_numeric")
        self.frame_3 = QtWidgets.QFrame(self.frame_numeric)
        self.frame_3.setGeometry(QtCore.QRect(0, 50, 250, 150))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.btn1 = QtWidgets.QPushButton(self.frame_3)
        self.btn1.setGeometry(QtCore.QRect(5, 5, 40, 40))
        self.btn1.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btn1.setObjectName("btn1")
        self.btn4 = QtWidgets.QPushButton(self.frame_3)
        self.btn4.setGeometry(QtCore.QRect(5, 55, 40, 40))
        self.btn4.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btn4.setObjectName("btn4")
        self.btn7 = QtWidgets.QPushButton(self.frame_3)
        self.btn7.setGeometry(QtCore.QRect(5, 105, 40, 40))
        self.btn7.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btn7.setObjectName("btn7")
        self.btn2 = QtWidgets.QPushButton(self.frame_3)
        self.btn2.setGeometry(QtCore.QRect(55, 5, 40, 40))
        self.btn2.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btn2.setObjectName("btn2")
        self.btn5 = QtWidgets.QPushButton(self.frame_3)
        self.btn5.setGeometry(QtCore.QRect(55, 55, 40, 40))
        self.btn5.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btn5.setObjectName("btn5")
        self.btn8 = QtWidgets.QPushButton(self.frame_3)
        self.btn8.setGeometry(QtCore.QRect(55, 105, 40, 40))
        self.btn8.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btn8.setObjectName("btn8")
        self.btn3 = QtWidgets.QPushButton(self.frame_3)
        self.btn3.setGeometry(QtCore.QRect(105, 5, 40, 40))
        self.btn3.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btn3.setObjectName("btn3")
        self.btn6 = QtWidgets.QPushButton(self.frame_3)
        self.btn6.setGeometry(QtCore.QRect(105, 55, 40, 40))
        self.btn6.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btn6.setObjectName("btn6")
        self.btn9 = QtWidgets.QPushButton(self.frame_3)
        self.btn9.setGeometry(QtCore.QRect(105, 105, 40, 40))
        self.btn9.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btn9.setObjectName("btn9")
        self.btn0 = QtWidgets.QPushButton(self.frame_3)
        self.btn0.setGeometry(QtCore.QRect(155, 105, 40, 40))
        self.btn0.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btn0.setObjectName("btn0")
        self.btnDelete = QtWidgets.QPushButton(self.frame_3)
        self.btnDelete.setGeometry(QtCore.QRect(155, 5, 90, 40))
        self.btnDelete.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.460227, y1:0, x2:0.466, y2:1, stop:0 rgba(187, 152, 9, 255), stop:0.704545 rgba(234, 181, 19, 255));")
        self.btnDelete.setObjectName("btnDelete")
        self.btnEnter = QtWidgets.QPushButton(self.frame_3)
        self.btnEnter.setGeometry(QtCore.QRect(155, 55, 90, 40))
        self.btnEnter.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.460227, y1:0, x2:0.466, y2:1, stop:0 rgba(187, 152, 9, 255), stop:0.704545 rgba(234, 181, 19, 255));")
        self.btnEnter.setObjectName("btnEnter")
        self.btnx = QtWidgets.QPushButton(self.frame_3)
        self.btnx.setGeometry(QtCore.QRect(205, 105, 40, 40))
        self.btnx.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.460227, y1:0, x2:0.466, y2:1, stop:0 rgba(187, 152, 9, 255), stop:0.704545 rgba(234, 181, 19, 255));\n"
"background-color: rgb(204, 0, 0);")
        self.btnx.setObjectName("btnx")
        self.txtKeyboard = QtWidgets.QLineEdit(self.frame_numeric)
        self.txtKeyboard.setGeometry(QtCore.QRect(0, 0, 250, 40))
        self.txtKeyboard.setStyleSheet("color: rgb(52, 101, 164);")
        self.txtKeyboard.setObjectName("txtKeyboard")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#eeeeec;\">What is the kiosk code for this device?</span></p></body></html>"))
        self.pb1.setText(_translate("MainWindow", "Done"))
        self.btn1.setText(_translate("MainWindow", "1"))
        self.btn4.setText(_translate("MainWindow", "4"))
        self.btn7.setText(_translate("MainWindow", "7"))
        self.btn2.setText(_translate("MainWindow", "2"))
        self.btn5.setText(_translate("MainWindow", "5"))
        self.btn8.setText(_translate("MainWindow", "8"))
        self.btn3.setText(_translate("MainWindow", "3"))
        self.btn6.setText(_translate("MainWindow", "6"))
        self.btn9.setText(_translate("MainWindow", "9"))
        self.btn0.setText(_translate("MainWindow", "0"))
        self.btnDelete.setText(_translate("MainWindow", "DELETE"))
        self.btnEnter.setText(_translate("MainWindow", "ENTER"))
        self.btnx.setText(_translate("MainWindow", "X"))

