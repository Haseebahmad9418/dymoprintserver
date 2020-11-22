# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkingupdates.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import debugmode



class Ui_checkingupdates(object):
    def setupUi(self, checkingupdates):
        checkingupdates.setObjectName("checkingupdates")
        checkingupdates.resize(480, 320)
        checkingupdates.setAutoFillBackground(False)
        checkingupdates.setStyleSheet("background-color: rgb(52, 101, 164);")
        if(debugmode.debug==False):
            checkingupdates.setWindowFlags( Qt.Window|Qt.FramelessWindowHint)
            checkingupdates.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(checkingupdates)
        self.centralwidget.setObjectName("centralwidget")
        self.conect = QtWidgets.QLabel(self.centralwidget)
        self.conect.setGeometry(QtCore.QRect(170, 70, 140, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.conect.setFont(font)
        self.conect.setStyleSheet("color: rgb(238, 238, 236);")
        self.conect.setObjectName("conect")
        self.chkupdates = QtWidgets.QLabel(self.centralwidget)
        self.chkupdates.setGeometry(QtCore.QRect(155, 120, 170, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.chkupdates.setFont(font)
        self.chkupdates.setAutoFillBackground(True)
        self.chkupdates.setStyleSheet("color: rgb(238, 238, 236);")
        self.chkupdates.setObjectName("chkupdates")
        checkingupdates.setCentralWidget(self.centralwidget)

        self.retranslateUi(checkingupdates)
        QtCore.QMetaObject.connectSlotsByName(checkingupdates)

    def retranslateUi(self, checkingupdates):
        _translate = QtCore.QCoreApplication.translate
        checkingupdates.setWindowTitle(_translate("checkingupdates", "MainWindow"))
        self.conect.setText(_translate("checkingupdates", "You are connected!"))
        self.chkupdates.setText(_translate("checkingupdates", "Checking for updates..."))

