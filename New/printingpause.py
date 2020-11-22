# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'printingpause.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import debugmode
class Ui_printingpause(object):
    def setupUi(self, printingpause):
        printingpause.setObjectName("printingpause")
        printingpause.resize(480, 320)
        printingpause.setAutoFillBackground(False)
        printingpause.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.centralwidget = QtWidgets.QWidget(printingpause)
        self.centralwidget.setObjectName("centralwidget")
        self.paused3 = QtWidgets.QLabel(self.centralwidget)
        self.paused3.setGeometry(QtCore.QRect(140, 100, 240, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.paused3.setFont(font)
        self.paused3.setAutoFillBackground(False)
        self.paused3.setStyleSheet("color: rgb(238, 238, 236);")
        self.paused3.setObjectName("paused3")
        self.pb3 = QtWidgets.QPushButton(self.centralwidget)
        self.pb3.setGeometry(QtCore.QRect(140, 160, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pb3.setFont(font)
        self.pb3.setStyleSheet("background-color: rgb(196, 160, 0);")
        self.pb3.setObjectName("pb3")
        self.device = QtWidgets.QLabel(self.centralwidget)
        self.device.setGeometry(QtCore.QRect(100, 10, 280, 20))
        self.device.setAutoFillBackground(False)
        self.device.setStyleSheet("color: rgb(186, 189, 182);")
        self.device.setText("")
        self.device.setObjectName("device")
        self.device.setAlignment(QtCore.Qt.AlignCenter)
#         self.label4 = QtWidgets.QLabel(self.centralwidget)
#         self.label4.setGeometry(QtCore.QRect(125, 10, 55, 20))
#         self.label4.setAutoFillBackground(False)
#         self.label4.setStyleSheet("color: rgb(186, 189, 182);")
#         self.label4.setObjectName("label4")
#         self.label5 = QtWidgets.QLabel(self.centralwidget)
#         self.label5.setGeometry(QtCore.QRect(75, 40, 95, 20))
#         self.label5.setStyleSheet("color: rgb(186, 189, 182);")
#         self.label5.setObjectName("label5")
        self.org = QtWidgets.QLabel(self.centralwidget)
        self.org.setGeometry(QtCore.QRect(100, 40, 280, 20))
        self.org.setStyleSheet("color: rgb(186, 189, 182);")
        self.org.setText("")
        self.org.setObjectName("org")
        self.org.setAlignment(QtCore.Qt.AlignCenter)
        if(debugmode.debug==False):
            printingpause.setWindowFlags( Qt.Window|Qt.FramelessWindowHint)
            printingpause.showFullScreen()
        printingpause.setCentralWidget(self.centralwidget)

        self.retranslateUi(printingpause)
        QtCore.QMetaObject.connectSlotsByName(printingpause)

    def retranslateUi(self, printingpause):
        _translate = QtCore.QCoreApplication.translate
        printingpause.setWindowTitle(_translate("printingpause", "MainWindow"))
        self.paused3.setText(_translate("printingpause", "PRINTING IS PAUSED"))
        self.pb3.setText(_translate("printingpause", "Continue"))
#        self.label4.setText(_translate("printingpause", "Device:"))
#        self.label5.setText(_translate("printingpause", "Organization:"))

