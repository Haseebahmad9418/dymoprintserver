# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_server(object):
    def setupUi(self, server):
        server.setObjectName("server")
        server.resize(480, 320)
        server.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.centralwidget = QtWidgets.QWidget(server)
        self.centralwidget.setObjectName("centralwidget")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(80, 30, 320, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label3.setFont(font)
        self.label3.setStyleSheet("color: rgb(238, 238, 236);")
        self.label3.setScaledContents(True)
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
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
        server.setCentralWidget(self.centralwidget)

        self.retranslateUi(server)
        QtCore.QMetaObject.connectSlotsByName(server)

    def retranslateUi(self, server):
        _translate = QtCore.QCoreApplication.translate
        server.setWindowTitle(_translate("server", "MainWindow"))
        self.label3.setText(_translate("server", "Sorry, Server is not responding"))
        self.pb2.setText(_translate("server", "Try Again"))

