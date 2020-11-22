# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'printqueue.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import debugmode
class Ui_printqueue(object):
    def setupUi(self, printqueue):
        printqueue.setObjectName("printqueue")
        printqueue.resize(480, 320)
        printqueue.setAutoFillBackground(False)
        printqueue.setStyleSheet("background-color: rgb(52, 101, 164);")
        if(debugmode.debug==False):
            printqueue.setWindowFlags( Qt.Window|Qt.FramelessWindowHint)
            printqueue.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(printqueue)
        self.centralwidget.setObjectName("centralwidget")
        self.label6 = QtWidgets.QLabel(self.centralwidget)
        self.label6.setGeometry(QtCore.QRect(195, 70, 90, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label6.setFont(font)
        self.label6.setAutoFillBackground(False)
        self.label6.setStyleSheet("color: rgb(238, 238, 236);")
        self.label6.setObjectName("label6")
        self.pb3 = QtWidgets.QPushButton(self.centralwidget)
        self.pb3.setGeometry(QtCore.QRect(30, 270, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pb3.setFont(font)
        self.pb3.setStyleSheet("background-color: rgb(196, 160, 0);")
        self.pb3.setObjectName("pb3")
        self.pb4 = QtWidgets.QPushButton(self.centralwidget)
        self.pb4.setGeometry(QtCore.QRect(250, 270, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pb4.setFont(font)
        self.pb4.setStyleSheet("background-color: rgb(196, 160, 0);")
        self.pb4.setObjectName("pb4")
        self.statusfixed = QtWidgets.QLabel(self.centralwidget)
        self.statusfixed.setGeometry(QtCore.QRect(20, 95, 70, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.statusfixed.setFont(font)
        self.statusfixed.setStyleSheet("color: rgb(186, 189, 182);")
        self.statusfixed.setAlignment(QtCore.Qt.AlignCenter)
        self.statusfixed.setObjectName("statusfixed")
        self.statusupdate = QtWidgets.QLabel(self.centralwidget)
        self.statusupdate.setGeometry(QtCore.QRect(100, 95, 340, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.statusupdate.setFont(font)
        self.statusupdate.setStyleSheet("color: rgb(186, 189, 182);")
        self.statusupdate.setText("")
        self.statusupdate.setObjectName("statusupdate")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 120, 440, 140))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("QListView::item { padding: 3px 5px 3px 8px; color: rgb(238, 238, 236); border-radius: 5px}\n"
"QListView {border-radius: 10px}\n"
"QScrollBar:vertical { width: 40px; margin: 0px;}\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical  { height: 0px; }\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { height: 0px; }\n"
"")
        self.listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.listWidget.setAutoScrollMargin(16)
        self.listWidget.setMovement(QtWidgets.QListView.Static)
        self.listWidget.setFlow(QtWidgets.QListView.TopToBottom)
        self.listWidget.setObjectName("listWidget")
        self.device = QtWidgets.QLabel(self.centralwidget)
        self.device.setGeometry(QtCore.QRect(100, 10, 280, 20))
        self.device.setAutoFillBackground(False)
        self.device.setStyleSheet("color: rgb(186, 189, 182);")
        self.device.setText("")
        self.device.setAlignment(QtCore.Qt.AlignCenter)
        self.device.setObjectName("device")
        self.org = QtWidgets.QLabel(self.centralwidget)
        self.org.setGeometry(QtCore.QRect(100, 40, 280, 20))
        self.org.setStyleSheet("color: rgb(186, 189, 182);")
        self.org.setText("")
        self.org.setAlignment(QtCore.Qt.AlignCenter)
        self.org.setObjectName("org")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(25, 60, 30, 30))
        self.pushButton.setAutoFillBackground(True)
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        picpath=debugmode.dpath+"Server/gear.png"
        self.pushButton.setIcon(QtGui.QIcon(picpath))
        printqueue.setCentralWidget(self.centralwidget)

        self.retranslateUi(printqueue)
        QtCore.QMetaObject.connectSlotsByName(printqueue)

    def retranslateUi(self, printqueue):
        _translate = QtCore.QCoreApplication.translate
        printqueue.setWindowTitle(_translate("printqueue", "MainWindow"))
        self.label6.setText(_translate("printqueue", "To Print:"))
        self.pb3.setText(_translate("printqueue", "Pause"))
        self.pb4.setText(_translate("printqueue", "Clear Queue"))
        self.statusfixed.setText(_translate("printqueue", "Status:"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)

