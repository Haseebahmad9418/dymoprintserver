# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'networktryagain.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import debugmode


class Ui_networktryagain(object):
    def setupUi(self, networktryagain):
        networktryagain.setObjectName("networktryagain")
        networktryagain.resize(480, 320)
        networktryagain.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.centralwidget = QtWidgets.QWidget(networktryagain)
        self.centralwidget.setObjectName("centralwidget")
        self.networktryagainlabel = QtWidgets.QLabel(self.centralwidget)
        self.networktryagainlabel.setGeometry(QtCore.QRect(20, 30, 440, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.networktryagainlabel.setFont(font)
        self.networktryagainlabel.setStyleSheet("color: rgb(238, 238, 236);")
        self.networktryagainlabel.setScaledContents(True)
        self.networktryagainlabel.setObjectName("networktryagainlabel")
        self.networktabutton = QtWidgets.QPushButton(self.centralwidget)
        self.networktabutton.setGeometry(QtCore.QRect(90, 120, 300, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.networktabutton.setFont(font)
        self.networktabutton.setStyleSheet("background-color: rgb(196, 160, 0);")
        self.networktabutton.setObjectName("networktabutton")
        self.networktryagainlabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.networktryagainlabel_2.setGeometry(QtCore.QRect(100, 70, 280, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.networktryagainlabel_2.setFont(font)
        self.networktryagainlabel_2.setStyleSheet("color: rgb(238, 238, 236);")
        self.networktryagainlabel_2.setScaledContents(True)
        self.networktryagainlabel_2.setObjectName("networktryagainlabel_2")
        if(debugmode.debug==False):
            networktryagain.setWindowFlags( Qt.Window|Qt.FramelessWindowHint)
            networktryagain.showFullScreen()
        networktryagain.setCentralWidget(self.centralwidget)

        self.retranslateUi(networktryagain)
        QtCore.QMetaObject.connectSlotsByName(networktryagain)

    def retranslateUi(self, networktryagain):
        _translate = QtCore.QCoreApplication.translate
        networktryagain.setWindowTitle(_translate("networktryagain", "MainWindow"))
        self.networktryagainlabel.setText(_translate("networktryagain", "Sorry, we are unable to connect to High5.id."))
        self.networktabutton.setText(_translate("networktryagain", "Try Again"))
        self.networktryagainlabel_2.setText(_translate("networktryagain", "Please call 514 743 1628"))

