# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'authtryagain.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt , QTimer
import debugmode
from PyQt5.QtCore import Qt


class Ui_authtryagain(object):
    def setupUi(self, authtryagain):
        authtryagain.setObjectName("authtryagain")
        authtryagain.resize(480, 320)
        authtryagain.setStyleSheet("background-color: rgb(52, 101, 164);")
        if(debugmode.debug==False):
            authtryagain.setWindowFlags( Qt.Window|Qt.FramelessWindowHint)
            authtryagain.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(authtryagain)
        self.centralwidget.setObjectName("centralwidget")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(50, 30, 380, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label3.setFont(font)
        self.label3.setStyleSheet("color: rgb(238, 238, 236);")
        self.label3.setScaledContents(True)
        self.label3.setObjectName("label3")
        self.pb2 = QtWidgets.QPushButton(self.centralwidget)
        self.pb2.setGeometry(QtCore.QRect(90, 80, 300, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pb2.setFont(font)
        self.pb2.setStyleSheet("background-color: rgb(196, 160, 0);")
        self.pb2.setObjectName("pb2")
        authtryagain.setCentralWidget(self.centralwidget)

        self.retranslateUi(authtryagain)
        QtCore.QMetaObject.connectSlotsByName(authtryagain)

    def retranslateUi(self, authtryagain):
        _translate = QtCore.QCoreApplication.translate
        authtryagain.setWindowTitle(_translate("authtryagain", "MainWindow"))
        self.label3.setText(_translate("authtryagain", "Sorry, that kiosk code is not known"))
        self.pb2.setText(_translate("authtryagain", "Try Again"))

