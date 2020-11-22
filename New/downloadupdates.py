# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'downloadupdates.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import debugmode


class Ui_downloadupdates(object):
    def setupUi(self, downloadupdates):
        downloadupdates.setObjectName("downloadupdates")
        downloadupdates.resize(480, 320)
        downloadupdates.setAutoFillBackground(False)
        downloadupdates.setStyleSheet("background-color: rgb(52, 101, 164);")
        if(debugmode.debug==False):
            downloadupdates.setWindowFlags( Qt.Window|Qt.FramelessWindowHint)
            downloadupdates.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(downloadupdates)
        self.centralwidget.setObjectName("centralwidget")
        self.conect = QtWidgets.QLabel(self.centralwidget)
        self.conect.setGeometry(QtCore.QRect(170, 70, 161, 30))
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
        self.chkupdates.setAlignment(QtCore.Qt.AlignCenter)
        self.chkupdates.setObjectName("chkupdates")
        downloadupdates.setCentralWidget(self.centralwidget)

        self.retranslateUi(downloadupdates)
        QtCore.QMetaObject.connectSlotsByName(downloadupdates)

    def retranslateUi(self, downloadupdates):
        _translate = QtCore.QCoreApplication.translate
        downloadupdates.setWindowTitle(_translate("downloadupdates", "MainWindow"))
        self.conect.setText(_translate("downloadupdates", "An update is available"))
        self.chkupdates.setText(_translate("downloadupdates", "Downloading now..."))

