# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wifipassword.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import debugmode
from PyQt5.QtCore import Qt
class Ui_wifipassword(object):
    def setupUi(self, wifipassword):
        wifipassword.setObjectName("wifipassword")
        wifipassword.resize(480, 320)
        if(debugmode.debug==False):
            wifipassword.setWindowFlags( Qt.Window|Qt.FramelessWindowHint)
            wifipassword.showFullScreen()
        font = QtGui.QFont()
        font.setPointSize(11)
        wifipassword.setFont(font)
        wifipassword.setAutoFillBackground(False)
        wifipassword.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.centralwidget = QtWidgets.QWidget(wifipassword)
        self.centralwidget.setObjectName("centralwidget")
        self.wifilabel = QtWidgets.QLabel(self.centralwidget)
        self.wifilabel.setGeometry(QtCore.QRect(20, 20, 175, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.wifilabel.setFont(font)
        self.wifilabel.setAutoFillBackground(False)
        self.wifilabel.setStyleSheet("color: rgb(238, 238, 236);")
        self.wifilabel.setObjectName("wifilabel")
        self.wificode = QtWidgets.QLineEdit(self.centralwidget)
        self.wificode.setGeometry(QtCore.QRect(20, 50, 280, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.wificode.setFont(font)
        self.wificode.setStyleSheet("color: rgb(238, 238, 236);\n"
"background-color: rgb(114, 159, 207);")
        self.wificode.setInputMethodHints(QtCore.Qt.ImhNone)
        self.wificode.setInputMask("")
        self.wificode.setText("")
        self.wificode.setFrame(True)
        self.wificode.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.wificode.setObjectName("wificode")
        self.wifiname = QtWidgets.QLabel(self.centralwidget)
        self.wifiname.setGeometry(QtCore.QRect(195, 20, 181, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.wifiname.setFont(font)
        self.wifiname.setStyleSheet("color: rgb(238, 238, 236);")
        self.wifiname.setText("")
        self.wifiname.setObjectName("wifiname")
        self.codedone = QtWidgets.QPushButton(self.centralwidget)
        self.codedone.setGeometry(QtCore.QRect(320, 50, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.codedone.setFont(font)
        self.codedone.setStyleSheet("background-color: rgb(196, 160, 0);")
        self.codedone.setObjectName("codedone")
        self.frame_numeric = QtWidgets.QFrame(self.centralwidget)
        self.frame_numeric.setGeometry(QtCore.QRect(0, 85, 480, 235))
        self.frame_numeric.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.frame_numeric.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"border-radius: 25px;\n"
"")
        self.frame_numeric.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_numeric.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_numeric.setObjectName("frame_numeric")
        self.frame_3 = QtWidgets.QFrame(self.frame_numeric)
        self.frame_3.setGeometry(QtCore.QRect(0, 15, 480, 220))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.btn1 = QtWidgets.QPushButton(self.frame_3)
        self.btn1.setGeometry(QtCore.QRect(22, 0, 35, 35))
        self.btn1.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btn1.setObjectName("btn1")
        self.btn4 = QtWidgets.QPushButton(self.frame_3)
        self.btn4.setGeometry(QtCore.QRect(142, 0, 35, 35))
        self.btn4.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btn4.setObjectName("btn4")
        self.btn7 = QtWidgets.QPushButton(self.frame_3)
        self.btn7.setGeometry(QtCore.QRect(262, 0, 35, 35))
        self.btn7.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btn7.setObjectName("btn7")
        self.btn2 = QtWidgets.QPushButton(self.frame_3)
        self.btn2.setGeometry(QtCore.QRect(62, 0, 35, 35))
        self.btn2.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btn2.setObjectName("btn2")
        self.btn5 = QtWidgets.QPushButton(self.frame_3)
        self.btn5.setGeometry(QtCore.QRect(182, 0, 35, 35))
        self.btn5.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btn5.setObjectName("btn5")
        self.btn8 = QtWidgets.QPushButton(self.frame_3)
        self.btn8.setGeometry(QtCore.QRect(302, 0, 35, 35))
        self.btn8.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btn8.setObjectName("btn8")
        self.btn3 = QtWidgets.QPushButton(self.frame_3)
        self.btn3.setGeometry(QtCore.QRect(102, 0, 35, 35))
        self.btn3.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btn3.setObjectName("btn3")
        self.btn6 = QtWidgets.QPushButton(self.frame_3)
        self.btn6.setGeometry(QtCore.QRect(222, 0, 35, 35))
        self.btn6.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btn6.setObjectName("btn6")
        self.btn9 = QtWidgets.QPushButton(self.frame_3)
        self.btn9.setGeometry(QtCore.QRect(342, 0, 35, 35))
        self.btn9.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btn9.setObjectName("btn9")
        self.btn0 = QtWidgets.QPushButton(self.frame_3)
        self.btn0.setGeometry(QtCore.QRect(382, 0, 35, 35))
        self.btn0.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btn0.setObjectName("btn0")
        self.btnDelete = QtWidgets.QPushButton(self.frame_3)
        self.btnDelete.setGeometry(QtCore.QRect(382, 80, 75, 35))
        self.btnDelete.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.460227, y1:0, x2:0.466, y2:1, stop:0 rgba(187, 152, 9, 255), stop:0.704545 rgba(234, 181, 19, 255));")
        self.btnDelete.setObjectName("btnDelete")
        self.btnEnter = QtWidgets.QPushButton(self.frame_3)
        self.btnEnter.setGeometry(QtCore.QRect(382, 120, 75, 32))
        self.btnEnter.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.460227, y1:0, x2:0.466, y2:1, stop:0 rgba(187, 152, 9, 255), stop:0.704545 rgba(234, 181, 19, 255));")
        self.btnEnter.setObjectName("btnEnter")
        self.btncaps = QtWidgets.QPushButton(self.frame_3)
        self.btncaps.setGeometry(QtCore.QRect(22, 160, 75, 35))
        self.btncaps.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.460227, y1:0, x2:0.466, y2:1, stop:0 rgba(187, 152, 9, 255), stop:0.704545 rgba(234, 181, 19, 255));")
        self.btncaps.setObjectName("btncaps")
        self.btndash = QtWidgets.QPushButton(self.frame_3)
        self.btndash.setGeometry(QtCore.QRect(422, 0, 35, 35))
        self.btndash.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btndash.setObjectName("btndash")
        self.btnq = QtWidgets.QPushButton(self.frame_3)
        self.btnq.setGeometry(QtCore.QRect(22, 40, 35, 35))
        self.btnq.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnq.setObjectName("btnq")
        self.btnw = QtWidgets.QPushButton(self.frame_3)
        self.btnw.setGeometry(QtCore.QRect(62, 40, 35, 35))
        self.btnw.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnw.setObjectName("btnw")
        self.btne = QtWidgets.QPushButton(self.frame_3)
        self.btne.setGeometry(QtCore.QRect(102, 40, 35, 35))
        self.btne.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btne.setObjectName("btne")
        self.btnr = QtWidgets.QPushButton(self.frame_3)
        self.btnr.setGeometry(QtCore.QRect(142, 40, 35, 35))
        self.btnr.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnr.setObjectName("btnr")
        self.btnt = QtWidgets.QPushButton(self.frame_3)
        self.btnt.setGeometry(QtCore.QRect(182, 40, 35, 35))
        self.btnt.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnt.setObjectName("btnt")
        self.btny = QtWidgets.QPushButton(self.frame_3)
        self.btny.setGeometry(QtCore.QRect(222, 40, 35, 35))
        self.btny.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btny.setObjectName("btny")
        self.btnu = QtWidgets.QPushButton(self.frame_3)
        self.btnu.setGeometry(QtCore.QRect(262, 40, 35, 35))
        self.btnu.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnu.setObjectName("btnu")
        self.btni = QtWidgets.QPushButton(self.frame_3)
        self.btni.setGeometry(QtCore.QRect(302, 40, 35, 35))
        self.btni.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btni.setObjectName("btni")
        self.btno = QtWidgets.QPushButton(self.frame_3)
        self.btno.setGeometry(QtCore.QRect(342, 40, 35, 35))
        self.btno.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btno.setObjectName("btno")
        self.btnp = QtWidgets.QPushButton(self.frame_3)
        self.btnp.setGeometry(QtCore.QRect(382, 40, 35, 35))
        self.btnp.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnp.setObjectName("btnp")
        self.btnsqopen = QtWidgets.QPushButton(self.frame_3)
        self.btnsqopen.setGeometry(QtCore.QRect(422, 40, 35, 35))
        self.btnsqopen.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnsqopen.setObjectName("btnsqopen")
        self.btna = QtWidgets.QPushButton(self.frame_3)
        self.btna.setGeometry(QtCore.QRect(22, 80, 35, 35))
        self.btna.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btna.setObjectName("btna")
        self.btns = QtWidgets.QPushButton(self.frame_3)
        self.btns.setGeometry(QtCore.QRect(62, 80, 35, 35))
        self.btns.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btns.setObjectName("btns")
        self.btnd = QtWidgets.QPushButton(self.frame_3)
        self.btnd.setGeometry(QtCore.QRect(102, 80, 35, 35))
        self.btnd.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnd.setObjectName("btnd")
        self.btnf = QtWidgets.QPushButton(self.frame_3)
        self.btnf.setGeometry(QtCore.QRect(142, 80, 35, 35))
        self.btnf.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnf.setObjectName("btnf")
        self.btng = QtWidgets.QPushButton(self.frame_3)
        self.btng.setGeometry(QtCore.QRect(182, 80, 35, 35))
        self.btng.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btng.setObjectName("btng")
        self.btnh = QtWidgets.QPushButton(self.frame_3)
        self.btnh.setGeometry(QtCore.QRect(222, 80, 35, 35))
        self.btnh.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnh.setObjectName("btnh")
        self.btnj = QtWidgets.QPushButton(self.frame_3)
        self.btnj.setGeometry(QtCore.QRect(262, 80, 35, 35))
        self.btnj.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnj.setObjectName("btnj")
        self.btnk = QtWidgets.QPushButton(self.frame_3)
        self.btnk.setGeometry(QtCore.QRect(302, 80, 35, 35))
        self.btnk.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnk.setObjectName("btnk")
        self.btnl = QtWidgets.QPushButton(self.frame_3)
        self.btnl.setGeometry(QtCore.QRect(342, 80, 35, 35))
        self.btnl.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnl.setObjectName("btnl")
        self.btnz = QtWidgets.QPushButton(self.frame_3)
        self.btnz.setGeometry(QtCore.QRect(22, 120, 35, 35))
        self.btnz.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnz.setObjectName("btnz")
        self.btnx = QtWidgets.QPushButton(self.frame_3)
        self.btnx.setGeometry(QtCore.QRect(62, 120, 35, 35))
        self.btnx.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnx.setObjectName("btnx")
        self.btnc = QtWidgets.QPushButton(self.frame_3)
        self.btnc.setGeometry(QtCore.QRect(102, 120, 35, 35))
        self.btnc.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnc.setObjectName("btnc")
        self.btnv = QtWidgets.QPushButton(self.frame_3)
        self.btnv.setGeometry(QtCore.QRect(142, 120, 35, 35))
        self.btnv.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnv.setObjectName("btnv")
        self.btnb = QtWidgets.QPushButton(self.frame_3)
        self.btnb.setGeometry(QtCore.QRect(182, 120, 35, 35))
        self.btnb.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnb.setObjectName("btnb")
        self.btnn = QtWidgets.QPushButton(self.frame_3)
        self.btnn.setGeometry(QtCore.QRect(222, 120, 35, 35))
        self.btnn.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnn.setObjectName("btnn")
        self.btnm = QtWidgets.QPushButton(self.frame_3)
        self.btnm.setGeometry(QtCore.QRect(262, 120, 35, 35))
        self.btnm.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnm.setObjectName("btnm")
        self.btncoma = QtWidgets.QPushButton(self.frame_3)
        self.btncoma.setGeometry(QtCore.QRect(302, 120, 35, 35))
        self.btncoma.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btncoma.setObjectName("btncoma")
        self.btndot = QtWidgets.QPushButton(self.frame_3)
        self.btndot.setGeometry(QtCore.QRect(342, 120, 35, 35))
        self.btndot.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btndot.setObjectName("btndot")
        self.btnspace = QtWidgets.QPushButton(self.frame_3)
        self.btnspace.setGeometry(QtCore.QRect(102, 160, 75, 35))
        self.btnspace.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnspace.setText("")
        self.btnspace.setObjectName("btnspace")
        self.btninvopen = QtWidgets.QPushButton(self.frame_3)
        self.btninvopen.setGeometry(QtCore.QRect(182, 160, 35, 35))
        self.btninvopen.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btninvopen.setObjectName("btninvopen")
        self.btnequal = QtWidgets.QPushButton(self.frame_3)
        self.btnequal.setGeometry(QtCore.QRect(222, 160, 35, 35))
        self.btnequal.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnequal.setObjectName("btnequal")
        self.btnspclose = QtWidgets.QPushButton(self.frame_3)
        self.btnspclose.setGeometry(QtCore.QRect(262, 160, 35, 35))
        self.btnspclose.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnspclose.setObjectName("btnspclose")
        self.btnscolon = QtWidgets.QPushButton(self.frame_3)
        self.btnscolon.setGeometry(QtCore.QRect(342, 160, 35, 35))
        self.btnscolon.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnscolon.setObjectName("btnscolon")
        self.btnbslash = QtWidgets.QPushButton(self.frame_3)
        self.btnbslash.setGeometry(QtCore.QRect(302, 160, 35, 35))
        self.btnbslash.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnbslash.setObjectName("btnbslash")
        self.btnfslash = QtWidgets.QPushButton(self.frame_3)
        self.btnfslash.setGeometry(QtCore.QRect(422, 160, 35, 35))
        self.btnfslash.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnfslash.setObjectName("btnfslash")
        self.btninvclose = QtWidgets.QPushButton(self.frame_3)
        self.btninvclose.setGeometry(QtCore.QRect(382, 160, 35, 35))
        self.btninvclose.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btninvclose.setObjectName("btninvclose")
        self.txtKeyboard = QtWidgets.QLineEdit(self.frame_numeric)
        self.txtKeyboard.setGeometry(QtCore.QRect(85, 0, 250, 10))
        self.txtKeyboard.setStyleSheet("color: rgb(52, 101, 164);")
        self.txtKeyboard.setObjectName("txtKeyboard")
        self.frame_5 = QtWidgets.QFrame(self.frame_numeric)
        self.frame_5.setGeometry(QtCore.QRect(485, 15, 480, 220))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.btnex = QtWidgets.QPushButton(self.frame_5)
        self.btnex.setGeometry(QtCore.QRect(22, 0, 35, 35))
        self.btnex.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnex.setObjectName("btnex")
        self.btndollar = QtWidgets.QPushButton(self.frame_5)
        self.btndollar.setGeometry(QtCore.QRect(142, 0, 35, 35))
        self.btndollar.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btndollar.setObjectName("btndollar")
        self.btnand = QtWidgets.QPushButton(self.frame_5)
        self.btnand.setGeometry(QtCore.QRect(262, 0, 35, 35))
        self.btnand.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnand.setObjectName("btnand")
        self.btnat = QtWidgets.QPushButton(self.frame_5)
        self.btnat.setGeometry(QtCore.QRect(62, 0, 35, 35))
        self.btnat.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnat.setObjectName("btnat")
        self.btnpercent = QtWidgets.QPushButton(self.frame_5)
        self.btnpercent.setGeometry(QtCore.QRect(182, 0, 35, 35))
        self.btnpercent.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnpercent.setObjectName("btnpercent")
        self.btnasteric = QtWidgets.QPushButton(self.frame_5)
        self.btnasteric.setGeometry(QtCore.QRect(302, 0, 35, 35))
        self.btnasteric.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnasteric.setObjectName("btnasteric")
        self.btnhash = QtWidgets.QPushButton(self.frame_5)
        self.btnhash.setGeometry(QtCore.QRect(102, 0, 35, 35))
        self.btnhash.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnhash.setObjectName("btnhash")
        self.btncarat = QtWidgets.QPushButton(self.frame_5)
        self.btncarat.setGeometry(QtCore.QRect(222, 0, 35, 35))
        self.btncarat.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btncarat.setObjectName("btncarat")
        self.btnpbopen = QtWidgets.QPushButton(self.frame_5)
        self.btnpbopen.setGeometry(QtCore.QRect(342, 0, 35, 35))
        self.btnpbopen.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnpbopen.setObjectName("btnpbopen")
        self.btnpbclose = QtWidgets.QPushButton(self.frame_5)
        self.btnpbclose.setGeometry(QtCore.QRect(382, 0, 35, 35))
        self.btnpbclose.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnpbclose.setObjectName("btnpbclose")
        self.btnDelete2 = QtWidgets.QPushButton(self.frame_5)
        self.btnDelete2.setGeometry(QtCore.QRect(382, 80, 75, 35))
        self.btnDelete2.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.460227, y1:0, x2:0.466, y2:1, stop:0 rgba(187, 152, 9, 255), stop:0.704545 rgba(234, 181, 19, 255));")
        self.btnDelete2.setObjectName("btnDelete2")
        self.btnEnter2 = QtWidgets.QPushButton(self.frame_5)
        self.btnEnter2.setGeometry(QtCore.QRect(382, 120, 75, 32))
        self.btnEnter2.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.460227, y1:0, x2:0.466, y2:1, stop:0 rgba(187, 152, 9, 255), stop:0.704545 rgba(234, 181, 19, 255));")
        self.btnEnter2.setObjectName("btnEnter2")
        self.btncaps2 = QtWidgets.QPushButton(self.frame_5)
        self.btncaps2.setGeometry(QtCore.QRect(22, 160, 75, 35))
        self.btncaps2.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.460227, y1:0, x2:0.466, y2:1, stop:0 rgba(187, 152, 9, 255), stop:0.704545 rgba(234, 181, 19, 255));")
        self.btncaps2.setObjectName("btncaps2")
        self.btnuscore = QtWidgets.QPushButton(self.frame_5)
        self.btnuscore.setGeometry(QtCore.QRect(422, 0, 35, 35))
        self.btnuscore.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnuscore.setObjectName("btnuscore")
        self.btnQ = QtWidgets.QPushButton(self.frame_5)
        self.btnQ.setGeometry(QtCore.QRect(22, 40, 35, 35))
        self.btnQ.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnQ.setObjectName("btnQ")
        self.btnW = QtWidgets.QPushButton(self.frame_5)
        self.btnW.setGeometry(QtCore.QRect(62, 40, 35, 35))
        self.btnW.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnW.setObjectName("btnW")
        self.btnE = QtWidgets.QPushButton(self.frame_5)
        self.btnE.setGeometry(QtCore.QRect(102, 40, 35, 35))
        self.btnE.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnE.setObjectName("btnE")
        self.btnR = QtWidgets.QPushButton(self.frame_5)
        self.btnR.setGeometry(QtCore.QRect(142, 40, 35, 35))
        self.btnR.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnR.setObjectName("btnR")
        self.btnT = QtWidgets.QPushButton(self.frame_5)
        self.btnT.setGeometry(QtCore.QRect(182, 40, 35, 35))
        self.btnT.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnT.setObjectName("btnT")
        self.btnY = QtWidgets.QPushButton(self.frame_5)
        self.btnY.setGeometry(QtCore.QRect(222, 40, 35, 35))
        self.btnY.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnY.setObjectName("btnY")
        self.btnU = QtWidgets.QPushButton(self.frame_5)
        self.btnU.setGeometry(QtCore.QRect(262, 40, 35, 35))
        self.btnU.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnU.setObjectName("btnU")
        self.btnI = QtWidgets.QPushButton(self.frame_5)
        self.btnI.setGeometry(QtCore.QRect(302, 40, 35, 35))
        self.btnI.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnI.setObjectName("btnI")
        self.btnO = QtWidgets.QPushButton(self.frame_5)
        self.btnO.setGeometry(QtCore.QRect(342, 40, 35, 35))
        self.btnO.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnO.setObjectName("btnO")
        self.btnP = QtWidgets.QPushButton(self.frame_5)
        self.btnP.setGeometry(QtCore.QRect(382, 40, 35, 35))
        self.btnP.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnP.setObjectName("btnP")
        self.btncrlopen = QtWidgets.QPushButton(self.frame_5)
        self.btncrlopen.setGeometry(QtCore.QRect(422, 40, 35, 35))
        self.btncrlopen.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btncrlopen.setObjectName("btncrlopen")
        self.btnA = QtWidgets.QPushButton(self.frame_5)
        self.btnA.setGeometry(QtCore.QRect(22, 80, 35, 35))
        self.btnA.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnA.setObjectName("btnA")
        self.btnS = QtWidgets.QPushButton(self.frame_5)
        self.btnS.setGeometry(QtCore.QRect(62, 80, 35, 35))
        self.btnS.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnS.setObjectName("btnS")
        self.btnD = QtWidgets.QPushButton(self.frame_5)
        self.btnD.setGeometry(QtCore.QRect(102, 80, 35, 35))
        self.btnD.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnD.setObjectName("btnD")
        self.btnF = QtWidgets.QPushButton(self.frame_5)
        self.btnF.setGeometry(QtCore.QRect(142, 80, 35, 35))
        self.btnF.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnF.setObjectName("btnF")
        self.btnG = QtWidgets.QPushButton(self.frame_5)
        self.btnG.setGeometry(QtCore.QRect(182, 80, 35, 35))
        self.btnG.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnG.setObjectName("btnG")
        self.btnH = QtWidgets.QPushButton(self.frame_5)
        self.btnH.setGeometry(QtCore.QRect(222, 80, 35, 35))
        self.btnH.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnH.setObjectName("btnH")
        self.btnJ = QtWidgets.QPushButton(self.frame_5)
        self.btnJ.setGeometry(QtCore.QRect(262, 80, 35, 35))
        self.btnJ.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnJ.setObjectName("btnJ")
        self.btnK = QtWidgets.QPushButton(self.frame_5)
        self.btnK.setGeometry(QtCore.QRect(302, 80, 35, 35))
        self.btnK.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnK.setObjectName("btnK")
        self.btnL = QtWidgets.QPushButton(self.frame_5)
        self.btnL.setGeometry(QtCore.QRect(342, 80, 35, 35))
        self.btnL.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnL.setObjectName("btnL")
        self.btnZ = QtWidgets.QPushButton(self.frame_5)
        self.btnZ.setGeometry(QtCore.QRect(22, 120, 35, 35))
        self.btnZ.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnZ.setObjectName("btnZ")
        self.btnX = QtWidgets.QPushButton(self.frame_5)
        self.btnX.setGeometry(QtCore.QRect(62, 120, 35, 35))
        self.btnX.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnX.setObjectName("btnX")
        self.btnC = QtWidgets.QPushButton(self.frame_5)
        self.btnC.setGeometry(QtCore.QRect(102, 120, 35, 35))
        self.btnC.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnC.setObjectName("btnC")
        self.btnV = QtWidgets.QPushButton(self.frame_5)
        self.btnV.setGeometry(QtCore.QRect(142, 120, 35, 35))
        self.btnV.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnV.setObjectName("btnV")
        self.btnB = QtWidgets.QPushButton(self.frame_5)
        self.btnB.setGeometry(QtCore.QRect(182, 120, 35, 35))
        self.btnB.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnB.setObjectName("btnB")
        self.btnN = QtWidgets.QPushButton(self.frame_5)
        self.btnN.setGeometry(QtCore.QRect(222, 120, 35, 35))
        self.btnN.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnN.setObjectName("btnN")
        self.btnM = QtWidgets.QPushButton(self.frame_5)
        self.btnM.setGeometry(QtCore.QRect(262, 120, 35, 35))
        self.btnM.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnM.setObjectName("btnM")
        self.btnabopen = QtWidgets.QPushButton(self.frame_5)
        self.btnabopen.setGeometry(QtCore.QRect(302, 120, 35, 35))
        self.btnabopen.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnabopen.setObjectName("btnabopen")
        self.btnabclose = QtWidgets.QPushButton(self.frame_5)
        self.btnabclose.setGeometry(QtCore.QRect(342, 120, 35, 35))
        self.btnabclose.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnabclose.setObjectName("btnabclose")
        self.btnspace2 = QtWidgets.QPushButton(self.frame_5)
        self.btnspace2.setGeometry(QtCore.QRect(102, 160, 75, 35))
        self.btnspace2.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnspace2.setText("")
        self.btnspace2.setObjectName("btnspace2")
        self.btntilta = QtWidgets.QPushButton(self.frame_5)
        self.btntilta.setGeometry(QtCore.QRect(182, 160, 35, 35))
        self.btntilta.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btntilta.setObjectName("btntilta")
        self.btnplus = QtWidgets.QPushButton(self.frame_5)
        self.btnplus.setGeometry(QtCore.QRect(222, 160, 35, 35))
        self.btnplus.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnplus.setObjectName("btnplus")
        self.btncrlclose = QtWidgets.QPushButton(self.frame_5)
        self.btncrlclose.setGeometry(QtCore.QRect(262, 160, 35, 35))
        self.btncrlclose.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btncrlclose.setObjectName("btncrlclose")
        self.btncolon = QtWidgets.QPushButton(self.frame_5)
        self.btncolon.setGeometry(QtCore.QRect(342, 160, 35, 35))
        self.btncolon.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btncolon.setObjectName("btncolon")
        self.btnpipe = QtWidgets.QPushButton(self.frame_5)
        self.btnpipe.setGeometry(QtCore.QRect(302, 160, 35, 35))
        self.btnpipe.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnpipe.setObjectName("btnpipe")
        self.btnqm = QtWidgets.QPushButton(self.frame_5)
        self.btnqm.setGeometry(QtCore.QRect(422, 160, 35, 35))
        self.btnqm.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btnqm.setObjectName("btnqm")
        self.btndqoutes = QtWidgets.QPushButton(self.frame_5)
        self.btndqoutes.setGeometry(QtCore.QRect(382, 160, 35, 35))
        self.btndqoutes.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.534091, y1:0, x2:0.522727, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.579545 rgba(135, 135, 135, 255));\n"
"")
        self.btndqoutes.setObjectName("btndqoutes")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(485, 70, 380, 150))
        self.frame.setStyleSheet("border-radius:10px;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.msg = QtWidgets.QLabel(self.frame)
        self.msg.setGeometry(QtCore.QRect(0, 110, 380, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.msg.setFont(font)
        self.msg.setStyleSheet("color: rgb(238, 238, 236);")
        self.msg.setAlignment(QtCore.Qt.AlignCenter)
        self.msg.setObjectName("msg")
        self.gif = QtWidgets.QLabel(self.frame)
        self.gif.setGeometry(QtCore.QRect(150, 30, 70, 70))
        self.gif.setText("")
        gifpath=debugmode.dpath+"Server/circle spinner.gif"
        #self.gif.setPixmap(QtGui.QPixmap(gifpath))
        self.gif.setScaledContents(True)
        self.gif.setAlignment(QtCore.Qt.AlignCenter)
        self.gif.setObjectName("gif")
        self.gif1 = QMovie(gifpath)
        self.gif.setMovie(self.gif1)
        self.gif1.start()
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(440, 20, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.cancel.setFont(font)
        self.cancel.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.cancel.setObjectName("cancel")
        wifipassword.setCentralWidget(self.centralwidget)

        self.retranslateUi(wifipassword)
        QtCore.QMetaObject.connectSlotsByName(wifipassword)

    def retranslateUi(self, wifipassword):
        _translate = QtCore.QCoreApplication.translate
        wifipassword.setWindowTitle(_translate("wifipassword", "MainWindow"))
        self.wifilabel.setText(_translate("wifipassword", "Enter the password for:"))
        self.codedone.setText(_translate("wifipassword", "Done"))
        self.btn1.setText(_translate("wifipassword", "1"))
        self.btn4.setText(_translate("wifipassword", "4"))
        self.btn7.setText(_translate("wifipassword", "7"))
        self.btn2.setText(_translate("wifipassword", "2"))
        self.btn5.setText(_translate("wifipassword", "5"))
        self.btn8.setText(_translate("wifipassword", "8"))
        self.btn3.setText(_translate("wifipassword", "3"))
        self.btn6.setText(_translate("wifipassword", "6"))
        self.btn9.setText(_translate("wifipassword", "9"))
        self.btn0.setText(_translate("wifipassword", "0"))
        self.btnDelete.setText(_translate("wifipassword", "Bspace"))
        self.btnEnter.setText(_translate("wifipassword", "ENTER"))
        self.btncaps.setText(_translate("wifipassword", "Caps"))
        self.btndash.setText(_translate("wifipassword", "-"))
        self.btnq.setText(_translate("wifipassword", "q"))
        self.btnw.setText(_translate("wifipassword", "w"))
        self.btne.setText(_translate("wifipassword", "e"))
        self.btnr.setText(_translate("wifipassword", "r"))
        self.btnt.setText(_translate("wifipassword", "t"))
        self.btny.setText(_translate("wifipassword", "y"))
        self.btnu.setText(_translate("wifipassword", "u"))
        self.btni.setText(_translate("wifipassword", "i"))
        self.btno.setText(_translate("wifipassword", "o"))
        self.btnp.setText(_translate("wifipassword", "p"))
        self.btnsqopen.setText(_translate("wifipassword", "["))
        self.btna.setText(_translate("wifipassword", "a"))
        self.btns.setText(_translate("wifipassword", "s"))
        self.btnd.setText(_translate("wifipassword", "d"))
        self.btnf.setText(_translate("wifipassword", "f"))
        self.btng.setText(_translate("wifipassword", "g"))
        self.btnh.setText(_translate("wifipassword", "h"))
        self.btnj.setText(_translate("wifipassword", "j"))
        self.btnk.setText(_translate("wifipassword", "k"))
        self.btnl.setText(_translate("wifipassword", "l"))
        self.btnz.setText(_translate("wifipassword", "z"))
        self.btnx.setText(_translate("wifipassword", "x"))
        self.btnc.setText(_translate("wifipassword", "c"))
        self.btnv.setText(_translate("wifipassword", "v"))
        self.btnb.setText(_translate("wifipassword", "b"))
        self.btnn.setText(_translate("wifipassword", "n"))
        self.btnm.setText(_translate("wifipassword", "m"))
        self.btncoma.setText(_translate("wifipassword", ","))
        self.btndot.setText(_translate("wifipassword", "."))
        self.btninvopen.setText(_translate("wifipassword", "`"))
        self.btnequal.setText(_translate("wifipassword", "="))
        self.btnspclose.setText(_translate("wifipassword", "]"))
        self.btnscolon.setText(_translate("wifipassword", ";"))
        self.btnbslash.setText(_translate("wifipassword", "\\"))
        self.btnfslash.setText(_translate("wifipassword", "/"))
        self.btninvclose.setText(_translate("wifipassword", "\'"))
        self.btnex.setText(_translate("wifipassword", "!"))
        self.btndollar.setText(_translate("wifipassword", "$"))
        self.btnand.setText(_translate("wifipassword", "&&"))
        self.btnat.setText(_translate("wifipassword", "@"))
        self.btnpercent.setText(_translate("wifipassword", "%"))
        self.btnasteric.setText(_translate("wifipassword", "*"))
        self.btnhash.setText(_translate("wifipassword", "#"))
        self.btncarat.setText(_translate("wifipassword", "^"))
        self.btnpbopen.setText(_translate("wifipassword", "("))
        self.btnpbclose.setText(_translate("wifipassword", ")"))
        self.btnDelete2.setText(_translate("wifipassword", "Bspace"))
        self.btnEnter2.setText(_translate("wifipassword", "ENTER"))
        self.btncaps2.setText(_translate("wifipassword", "Caps"))
        self.btnuscore.setText(_translate("wifipassword", "_"))
        self.btnQ.setText(_translate("wifipassword", "Q"))
        self.btnW.setText(_translate("wifipassword", "W"))
        self.btnE.setText(_translate("wifipassword", "E"))
        self.btnR.setText(_translate("wifipassword", "R"))
        self.btnT.setText(_translate("wifipassword", "T"))
        self.btnY.setText(_translate("wifipassword", "Y"))
        self.btnU.setText(_translate("wifipassword", "U"))
        self.btnI.setText(_translate("wifipassword", "I"))
        self.btnO.setText(_translate("wifipassword", "O"))
        self.btnP.setText(_translate("wifipassword", "P"))
        self.btncrlopen.setText(_translate("wifipassword", "{"))
        self.btnA.setText(_translate("wifipassword", "A"))
        self.btnS.setText(_translate("wifipassword", "S"))
        self.btnD.setText(_translate("wifipassword", "D"))
        self.btnF.setText(_translate("wifipassword", "F"))
        self.btnG.setText(_translate("wifipassword", "G"))
        self.btnH.setText(_translate("wifipassword", "H"))
        self.btnJ.setText(_translate("wifipassword", "J"))
        self.btnK.setText(_translate("wifipassword", "K"))
        self.btnL.setText(_translate("wifipassword", "L"))
        self.btnZ.setText(_translate("wifipassword", "Z"))
        self.btnX.setText(_translate("wifipassword", "X"))
        self.btnC.setText(_translate("wifipassword", "C"))
        self.btnV.setText(_translate("wifipassword", "V"))
        self.btnB.setText(_translate("wifipassword", "B"))
        self.btnN.setText(_translate("wifipassword", "N"))
        self.btnM.setText(_translate("wifipassword", "M"))
        self.btnabopen.setText(_translate("wifipassword", "<"))
        self.btnabclose.setText(_translate("wifipassword", ">"))
        self.btntilta.setText(_translate("wifipassword", "~"))
        self.btnplus.setText(_translate("wifipassword", "+"))
        self.btncrlclose.setText(_translate("wifipassword", "}"))
        self.btncolon.setText(_translate("wifipassword", ":"))
        self.btnpipe.setText(_translate("wifipassword", "|"))
        self.btnqm.setText(_translate("wifipassword", "?"))
        self.btndqoutes.setText(_translate("wifipassword", "\""))
        self.msg.setText(_translate("wifipassword", "Trying to connect Wifi"))
        self.cancel.setText(_translate("wifipassword", "X"))
        

