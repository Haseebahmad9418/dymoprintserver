# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updateready.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import debugmode


class Ui_readyupdate(object):
    def setupUi(self, readyupdate):
        readyupdate.setObjectName("readyupdate")
        readyupdate.resize(480, 320)
        readyupdate.setAutoFillBackground(False)
        readyupdate.setStyleSheet("background-color: rgb(52, 101, 164);")
        if(debugmode.debug==False):
            readyupdate.setWindowFlags( Qt.Window|Qt.FramelessWindowHint)
            readyupdate.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(readyupdate)
        self.centralwidget.setObjectName("centralwidget")
        self.conect = QtWidgets.QLabel(self.centralwidget)
        self.conect.setGeometry(QtCore.QRect(185, 70, 110, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.conect.setFont(font)
        self.conect.setStyleSheet("color: rgb(238, 238, 236);")
        self.conect.setObjectName("conect")
        self.restaring = QtWidgets.QLabel(self.centralwidget)
        self.restaring.setGeometry(QtCore.QRect(140, 120, 200, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.restaring.setFont(font)
        self.restaring.setAutoFillBackground(True)
        self.restaring.setStyleSheet("color: rgb(238, 238, 236);")
        self.restaring.setAlignment(QtCore.Qt.AlignCenter)
        self.restaring.setObjectName("restaring")
        readyupdate.setCentralWidget(self.centralwidget)

        self.retranslateUi(readyupdate)
        QtCore.QMetaObject.connectSlotsByName(readyupdate)

    def retranslateUi(self, readyupdate):
        _translate = QtCore.QCoreApplication.translate
        readyupdate.setWindowTitle(_translate("readyupdate", "MainWindow"))
        self.conect.setText(_translate("readyupdate", "Update ready!"))
        self.restaring.setText(_translate("readyupdate", "Restarting in 5 seconds..."))

