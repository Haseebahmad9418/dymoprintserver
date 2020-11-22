# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import debugmode


class Ui_logo(object):
    def setupUi(self, logo):
        logo.setObjectName("logo")
        logo.setWindowModality(QtCore.Qt.WindowModal)
        logo.resize(480, 320)
        logo.setAutoFillBackground(False)
        logo.setStyleSheet("background-color: rgb(52, 101, 164);")
        if(debugmode.debug==False):
            logo.setWindowFlags( Qt.Window|Qt.FramelessWindowHint)
            logo.showFullScreen()
        logo.setDockOptions(QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(logo)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(90, 10, 300, 300))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label1.sizePolicy().hasHeightForWidth())
        self.label1.setSizePolicy(sizePolicy)
        self.label1.setAutoFillBackground(False)
        self.label1.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.label1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label1.setLineWidth(0)
        self.label1.setMidLineWidth(0)
        self.label1.setText("")
        self.label1.setPixmap(QtGui.QPixmap(debugmode.dpath+"Server/a.png"))
        self.label1.setScaledContents(True)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setWordWrap(False)
        self.label1.setObjectName("label1")
        self.versionfixed = QtWidgets.QLabel(self.centralwidget)
        self.versionfixed.setGeometry(QtCore.QRect(0, 0, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.versionfixed.setFont(font)
        self.versionfixed.setAlignment(QtCore.Qt.AlignCenter)
        self.versionfixed.setObjectName("versionfixed")
        self.tempversion = QtWidgets.QLabel(self.centralwidget)
        self.tempversion.setGeometry(QtCore.QRect(20, 0, 40, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tempversion.setFont(font)
        try:
            tempvf=debugmode.dpath+"pidata/version.txt"
            file= open(tempvf,'r')
            for line in file:
                feilds=line.split("; ")
                temp_v=feilds[0]
                self.tempversion.setText(temp_v)
        except:
            pass
        self.tempversion.setAlignment(QtCore.Qt.AlignCenter)
        self.tempversion.setObjectName("tempversion")
        logo.setCentralWidget(self.centralwidget)

        self.retranslateUi(logo)
        QtCore.QMetaObject.connectSlotsByName(logo)

    def retranslateUi(self, logo):
        _translate = QtCore.QCoreApplication.translate
        logo.setWindowTitle(_translate("logo", "MainWindow"))
        self.versionfixed.setText(_translate("logo", " V "))

