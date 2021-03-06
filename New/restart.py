# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'restart.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import debugmode

class Ui_updateerror(object):
    def setupUi(self, updateerror):
        updateerror.setObjectName("updateerror")
        updateerror.resize(480, 320)
        updateerror.setAutoFillBackground(False)
        updateerror.setStyleSheet("background-color: rgb(52, 101, 164);")
        if(debugmode.debug==False):
            updateerror.setWindowFlags( Qt.Window|Qt.FramelessWindowHint)
            updateerror.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(updateerror)
        self.centralwidget.setObjectName("centralwidget")
        self.error1 = QtWidgets.QLabel(self.centralwidget)
        self.error1.setGeometry(QtCore.QRect(145, 70, 190, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.error1.setFont(font)
        self.error1.setStyleSheet("color: rgb(238, 238, 236);")
        self.error1.setObjectName("error1")
        self.error2 = QtWidgets.QLabel(self.centralwidget)
        self.error2.setGeometry(QtCore.QRect(130, 120, 220, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.error2.setFont(font)
        self.error2.setAutoFillBackground(False)
        self.error2.setStyleSheet("color: rgb(238, 238, 236);")
        self.error2.setAlignment(QtCore.Qt.AlignCenter)
        self.error2.setObjectName("error2")
        self.error3 = QtWidgets.QLabel(self.centralwidget)
        self.error3.setGeometry(QtCore.QRect(175, 170, 200, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.error3.setFont(font)
        self.error3.setStyleSheet("color: rgb(238, 238, 236);")
        self.error3.setObjectName("error3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(165, 230, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(196, 160, 0);")
        self.pushButton.setObjectName("pushButton")
        updateerror.setCentralWidget(self.centralwidget)

        self.retranslateUi(updateerror)
        QtCore.QMetaObject.connectSlotsByName(updateerror)

    def retranslateUi(self, updateerror):
        _translate = QtCore.QCoreApplication.translate
        updateerror.setWindowTitle(_translate("updateerror", "MainWindow"))
        self.error1.setText(_translate("updateerror", "An error was encountered"))
        self.error2.setText(_translate("updateerror", "While downloading an update"))
        self.error3.setText(_translate("updateerror", "Please call 514 743 1628"))
        self.pushButton.setText(_translate("updateerror", "Restart"))

