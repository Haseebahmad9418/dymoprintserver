# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wifilist.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import debugmode
class Ui_wifilist(object):
    def setupUi(self, wifilist):
        wifilist.setObjectName("wifilist")
        wifilist.resize(480, 320)
        wifilist.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(wifilist)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.centralwidget.setObjectName("centralwidget")
        self.ssidlist = QtWidgets.QListWidget(self.centralwidget)
        self.ssidlist.setGeometry(QtCore.QRect(30, 50, 420, 260))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ssidlist.setFont(font)
        self.ssidlist.setAutoFillBackground(True)
        self.ssidlist.setStyleSheet("QListView::item { padding: 3px 5px 3px 8px; border-radius: 5px;background-color: rgb(252, 175, 62);}\n"
"QListView {border-radius: 10px}\n"
"QScrollBar:vertical { width: 40px; margin: 0px;}\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical  { height: 0px; }\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { height: 0px; }\n"
"")
        self.ssidlist.setObjectName("ssidlist")
        self.wifilist1 = QtWidgets.QLabel(self.centralwidget)
        self.wifilist1.setGeometry(QtCore.QRect(20, 20, 135, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.wifilist1.setFont(font)
        self.wifilist1.setStyleSheet("color: rgb(238, 238, 236);")
        self.wifilist1.setObjectName("wifilist1")
        self.refreshbtn = QtWidgets.QPushButton(self.centralwidget)
        self.refreshbtn.setGeometry(QtCore.QRect(160, 20, 25, 25))
        self.refreshbtn.setText("")
        self.refreshbtn.setObjectName("refreshbtn")
        picpath=debugmode.dpath+"Server/ri.png"
        self.refreshbtn.setIcon(QtGui.QIcon(picpath))
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(430, 20, 25, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.cancel.setFont(font)
        self.cancel.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.cancel.setObjectName("cancel")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(240, 20, 180, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.clear.setFont(font)
        self.clear.setStyleSheet("background-color: rgb(196, 160, 0);\n"
"")
        self.clear.setObjectName("clear")
        wifilist.setCentralWidget(self.centralwidget)
        if(debugmode.debug==False):
            wifilist.setWindowFlags(Qt.Window|Qt.FramelessWindowHint)
            wifilist.showFullScreen()

        self.retranslateUi(wifilist)
        QtCore.QMetaObject.connectSlotsByName(wifilist)

    def retranslateUi(self, wifilist):
        _translate = QtCore.QCoreApplication.translate
        wifilist.setWindowTitle(_translate("wifilist", "MainWindow"))
        self.wifilist1.setText(_translate("wifilist", "Choose a network:"))
        self.cancel.setText(_translate("wifilist", "x"))
        self.clear.setText(_translate("wifilist", "Clear Password"))

