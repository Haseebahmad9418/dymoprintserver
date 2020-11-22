# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wifitryagain.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import debugmode



class Ui_wifitryagain(object):
    def setupUi(self, wifitryagain):
        wifitryagain.setObjectName("wifitryagain")
        wifitryagain.resize(480, 320)
        wifitryagain.setStyleSheet("background-color: rgb(52, 101, 164);")
        if(debugmode.debug==False):
            wifitryagain.setWindowFlags( Qt.Window|Qt.FramelessWindowHint)
            wifitryagain.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(wifitryagain)
        self.centralwidget.setObjectName("centralwidget")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(80, 30, 350, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label3.setFont(font)
        self.label3.setStyleSheet("color: rgb(238, 238, 236);")
        self.label3.setScaledContents(True)
        self.label3.setObjectName("label3")
        self.wifitabutton = QtWidgets.QPushButton(self.centralwidget)
        self.wifitabutton.setGeometry(QtCore.QRect(90, 80, 300, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.wifitabutton.setFont(font)
        self.wifitabutton.setStyleSheet("background-color: rgb(196, 160, 0);")
        self.wifitabutton.setObjectName("wifitabutton")
        wifitryagain.setCentralWidget(self.centralwidget)

        self.retranslateUi(wifitryagain)
        QtCore.QMetaObject.connectSlotsByName(wifitryagain)

    def retranslateUi(self, wifitryagain):
        _translate = QtCore.QCoreApplication.translate
        wifitryagain.setWindowTitle(_translate("wifitryagain", "MainWindow"))
        self.label3.setText(_translate("wifitryagain", "Sorry, that wifi password is incorrect"))
        self.wifitabutton.setText(_translate("wifitryagain", "Try Again"))

