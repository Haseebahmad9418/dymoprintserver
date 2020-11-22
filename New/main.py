#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 21:05:18 2020

@author: haseeb
"""

import sys
import os
import subprocess
import shutil
import time
import requests
import json
import urllib.request
from threading import Thread
import threading
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QPushButton, QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt , QTimer
from multiprocessing import Process
from subprocess import check_output

from wifilist import Ui_wifilist
from wifipassword import Ui_wifipassword
from wifitryagain import Ui_wifitryagain
from networktryagain import Ui_networktryagain
from checkingupdates import Ui_checkingupdates
from downloadupdates import Ui_downloadupdates
from printingpause import Ui_printingpause
from restart import Ui_updateerror
from restart1 import Ui_updateerror1
from updateready import Ui_readyupdate
from logo import Ui_logo
from authcode import Ui_MainWindow
from authtryagain import Ui_authtryagain
from printqueue import Ui_printqueue
from settings import Ui_settings
from server import Ui_server
import zip
import debugmode

qpath=debugmode.dpath+"queue/"
sign=True
dev=None
organize=None
global m,n,b
m=0
n=0
b=0

class splash(QtWidgets.QMainWindow, Ui_logo):  #Class to acces Main.py GUI

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        super(Ui_logo, self).__init__()
        self.setupUi(self)

class wifilisting(QtWidgets.QMainWindow, Ui_wifilist):  #Class to acces Main.py GUI
    refresh = pyqtSignal()
    switch_cancel = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        super(Ui_wifilist, self).__init__()
        self.setupUi(self)
        self.refreshbtn.clicked.connect(lambda: self.refreshlist())
        self.ssidlist.clicked.connect(self.clicked)
        self.clear.clicked.connect(lambda: self.clearlist())
        self.cancel.clicked.connect(lambda: self.cancelwifi())
        global b
        if(b==0):
            self.cancel.setEnabled(False)
        else:
            self.cancel.setEnabled(True)
        
    def clearlist(self):
        print("list cleared")
        config = (
            'ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\n'
            'update_config=0\n'
            'country=PK\n')
        with open("/etc/wpa_supplicant/wpa_supplicant.conf","w+") as wifi:
            wifi.write(config)
            wifi.close()
        #self.switch_clear.emit()
        pass
    def cancelwifi(self):
        print("Cancel pressed")
        self.switch_cancel.emit()
        pass
    def clicked(self,item):
        global selectedssid
        item=self.ssidlist.currentItem()
        selectedssid=item.text()
        print(item.text())
        self.refresh.emit()
        pass

    def refreshlist(self):
        try:
           scanoutput = check_output(["iwlist", "wlan0", "scan"])
           ss=scanoutput.decode("utf-8")
           self.ssidlist.clear()
           ssid=[]
           for line in ss.split("\n"):
               if "ESSID" in line:
                   ssid = line.split('"')[1]
                   print(ssid)
                   item=QtWidgets.QListWidgetItem(ssid,self.ssidlist)
                   item.setTextAlignment(QtCore.Qt.AlignCenter)
                   #self.ssidlist.addItem(item)
        except:
            pass
class wifipw(QtWidgets.QMainWindow, Ui_wifipassword):  #Class to acces Main.py GUI
    switch_wpdone = QtCore.pyqtSignal()
    switch_cancelpw = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        super(Ui_wifipassword, self).__init__()
        self.setupUi(self)
        global selectedssid
        self.wifiname.setText(selectedssid)
        self.codedone.clicked.connect(lambda: self.connectwifi())
        self.frame_numeric.setGeometry(QtCore.QRect(0, 85, 480, 235))
        #self.frame.setGeometry(QtCore.QRect(0, 0, 480, 320))
        clickable(self.wificode).connect(self.presstxt_password)
        self.btn1.clicked.connect(lambda: self.txtUpdate('1'))
        self.btn2.clicked.connect(lambda: self.txtUpdate('2'))
        self.btn3.clicked.connect(lambda: self.txtUpdate('3'))
        self.btn4.clicked.connect(lambda: self.txtUpdate('4'))
        self.btn5.clicked.connect(lambda: self.txtUpdate('5'))
        self.btn6.clicked.connect(lambda: self.txtUpdate('6'))
        self.btn7.clicked.connect(lambda: self.txtUpdate('7'))
        self.btn8.clicked.connect(lambda: self.txtUpdate('8'))
        self.btn9.clicked.connect(lambda: self.txtUpdate('9'))
        self.btn0.clicked.connect(lambda: self.txtUpdate('0'))
        self.btndash.clicked.connect(lambda: self.txtUpdate('-'))
        self.btnq.clicked.connect(lambda: self.txtUpdate('q'))
        self.btnw.clicked.connect(lambda: self.txtUpdate('w'))
        self.btne.clicked.connect(lambda: self.txtUpdate('e'))
        self.btnr.clicked.connect(lambda: self.txtUpdate('r'))
        self.btnt.clicked.connect(lambda: self.txtUpdate('t'))
        self.btny.clicked.connect(lambda: self.txtUpdate('y'))
        self.btnu.clicked.connect(lambda: self.txtUpdate('u'))
        self.btni.clicked.connect(lambda: self.txtUpdate('i'))
        self.btno.clicked.connect(lambda: self.txtUpdate('o'))
        self.btnp.clicked.connect(lambda: self.txtUpdate('p'))
        self.btnsqopen.clicked.connect(lambda: self.txtUpdate('['))
        self.btna.clicked.connect(lambda: self.txtUpdate('a'))
        self.btns.clicked.connect(lambda: self.txtUpdate('s'))
        self.btnd.clicked.connect(lambda: self.txtUpdate('d'))
        self.btnf.clicked.connect(lambda: self.txtUpdate('f'))
        self.btng.clicked.connect(lambda: self.txtUpdate('g'))
        self.btnh.clicked.connect(lambda: self.txtUpdate('h'))
        self.btnj.clicked.connect(lambda: self.txtUpdate('j'))
        self.btnk.clicked.connect(lambda: self.txtUpdate('k'))
        self.btnl.clicked.connect(lambda: self.txtUpdate('l'))
        self.btnz.clicked.connect(lambda: self.txtUpdate('z'))
        self.btnx.clicked.connect(lambda: self.txtUpdate('x'))
        self.btnc.clicked.connect(lambda: self.txtUpdate('c'))
        self.btnv.clicked.connect(lambda: self.txtUpdate('v'))
        self.btnb.clicked.connect(lambda: self.txtUpdate('b'))
        self.btnn.clicked.connect(lambda: self.txtUpdate('n'))
        self.btnm.clicked.connect(lambda: self.txtUpdate('m'))
        self.btncoma.clicked.connect(lambda: self.txtUpdate(','))
        self.btndot.clicked.connect(lambda: self.txtUpdate('.'))
        self.btnspace.clicked.connect(lambda: self.txtUpdate(' '))
        self.btninvopen.clicked.connect(lambda: self.txtUpdate('`'))
        self.btnequal.clicked.connect(lambda: self.txtUpdate('='))
        self.btnspclose.clicked.connect(lambda: self.txtUpdate(']'))
        self.btnbslash.clicked.connect(lambda: self.txtUpdate('\\'))
        self.btnscolon.clicked.connect(lambda: self.txtUpdate(';'))
        self.btninvclose.clicked.connect(lambda: self.txtUpdate('\''))
        self.btnfslash.clicked.connect(lambda: self.txtUpdate('/'))
        self.btncaps.clicked.connect(lambda: self.presscaps())
        self.btnEnter.clicked.connect(lambda: self.pressEnter())
        self.btnDelete.clicked.connect(lambda: self.txtdelete())
        self.btnex.clicked.connect(lambda: self.txtUpdate('!'))
        self.btnat.clicked.connect(lambda: self.txtUpdate('@'))
        self.btnhash.clicked.connect(lambda: self.txtUpdate('#'))
        self.btndollar.clicked.connect(lambda: self.txtUpdate('$'))                        
        self.btnpercent.clicked.connect(lambda: self.txtUpdate('%'))
        self.btncarat.clicked.connect(lambda: self.txtUpdate('^'))
        self.btnand.clicked.connect(lambda: self.txtUpdate('&'))
        self.btnasteric.clicked.connect(lambda: self.txtUpdate('*'))
        self.btnpbopen.clicked.connect(lambda: self.txtUpdate('('))
        self.btnpbclose.clicked.connect(lambda: self.txtUpdate(')'))
        self.btnuscore.clicked.connect(lambda: self.txtUpdate('_'))
        self.btnQ.clicked.connect(lambda: self.txtUpdate('Q'))
        self.btnW.clicked.connect(lambda: self.txtUpdate('W'))
        self.btnE.clicked.connect(lambda: self.txtUpdate('E'))
        self.btnR.clicked.connect(lambda: self.txtUpdate('R'))
        self.btnT.clicked.connect(lambda: self.txtUpdate('T'))
        self.btnY.clicked.connect(lambda: self.txtUpdate('Y'))
        self.btnU.clicked.connect(lambda: self.txtUpdate('U'))
        self.btnI.clicked.connect(lambda: self.txtUpdate('I'))
        self.btnO.clicked.connect(lambda: self.txtUpdate('O'))
        self.btnP.clicked.connect(lambda: self.txtUpdate('P'))
        self.btncrlopen.clicked.connect(lambda: self.txtUpdate('{'))
        self.btnA.clicked.connect(lambda: self.txtUpdate('A'))
        self.btnS.clicked.connect(lambda: self.txtUpdate('S'))
        self.btnD.clicked.connect(lambda: self.txtUpdate('D'))
        self.btnF.clicked.connect(lambda: self.txtUpdate('F'))
        self.btnG.clicked.connect(lambda: self.txtUpdate('G'))
        self.btnH.clicked.connect(lambda: self.txtUpdate('H'))
        self.btnJ.clicked.connect(lambda: self.txtUpdate('J'))
        self.btnK.clicked.connect(lambda: self.txtUpdate('K'))
        self.btnL.clicked.connect(lambda: self.txtUpdate('L'))
        self.btnDelete2.clicked.connect(lambda: self.txtdelete())
        self.btnZ.clicked.connect(lambda: self.txtUpdate('Z'))
        self.btnX.clicked.connect(lambda: self.txtUpdate('X'))
        self.btnC.clicked.connect(lambda: self.txtUpdate('C'))
        self.btnV.clicked.connect(lambda: self.txtUpdate('V'))
        self.btnB.clicked.connect(lambda: self.txtUpdate('B'))
        self.btnN.clicked.connect(lambda: self.txtUpdate('N'))
        self.btnM.clicked.connect(lambda: self.txtUpdate('M'))
        self.btnabopen.clicked.connect(lambda: self.txtUpdate('<'))
        self.btnabclose.clicked.connect(lambda: self.txtUpdate('>'))
        self.btnEnter2.clicked.connect(lambda:self.pressEnter())
        self.btncaps2.clicked.connect(lambda: self.presscaps2())
        self.btnspace2.clicked.connect(lambda: self.txtUpdate(' '))
        self.btntilta.clicked.connect(lambda: self.txtUpdate('~'))
        self.btnplus.clicked.connect(lambda: self.txtUpdate('+'))
        self.btncrlclose.clicked.connect(lambda: self.txtUpdate('}'))
        self.btnpipe.clicked.connect(lambda: self.txtUpdate('|'))
        self.btncolon.clicked.connect(lambda: self.txtUpdate(':'))
        self.btndqoutes.clicked.connect(lambda: self.txtUpdate('"'))
        self.btnqm.clicked.connect(lambda: self.txtUpdate('?'))
        self.cancel.clicked.connect(lambda: self.cancelpw())
        
    def cancelpw(self):
        self.switch_cancelpw.emit()
        pass
    def presscaps(self):
        self.frame_5.setGeometry(QtCore.QRect(0, 15, 480, 220))
        self.frame_3.setGeometry(QtCore.QRect(485, 15, 480, 220))

    def presscaps2(self):
        self.frame_3.setGeometry(QtCore.QRect(0, 15, 480, 220))
        self.frame_5.setGeometry(QtCore.QRect(485, 15, 480, 220))

    def presstxt_password(self):
        print('password box cliecked')
        self.frame_numeric.setGeometry(QtCore.QRect(0, 85, 480, 235))

    def pressEnter(self):
        print('pressing enter')
        #self.frame_numeric.setGeometry(QtCore.QRect(115, 110, 250, 200))
        mesg = '{}'.format(self.txtKeyboard.text())
        self.wificode.setText(mesg)
        self.connectwifi()

    def txtUpdate(self, txt):
        cur=self.wificode.cursorPosition()
        print("current position "+str(cur))
        lent = len(self.txtKeyboard.text())
        if len(self.txtKeyboard.text()) == 0:
            self.txtKeyboard.setText('{}'.format(txt))
            self.wificode.setText('{}'.format(txt))
        else:
            v = self.txtKeyboard.text()
            ele1=""
            ele2=""
            for element in range(0, cur): 
                ele1=ele1+v[element]
            for element in range(cur, lent): 
                ele2=ele2+v[element]
            print(ele1)
            print("\n"+ele2)
            self.txtKeyboard.setText('{}{}{}'.format(ele1, txt, ele2))
            mesg = '{}'.format(self.txtKeyboard.text())
            self.wificode.setText(mesg)
            self.wificode.setCursorPosition(cur+1)

#         lent = len(self.txtKeyboard.text())
#         if len(self.txtKeyboard.text()) == 0:
#             self.txtKeyboard.setText('{}'.format(txt))
#             self.wificode.setText('{}'.format(txt))
# 
#         else:
#             v = self.txtKeyboard.text()
#             self.txtKeyboard.setText('{}{}'.format(v, txt))
#             mesg = '{}'.format(self.txtKeyboard.text())
#             #self.txtPassword.setText(mesg)
#             self.wificode.setText(mesg)

    def txtdelete(self):
        vr = self.txtKeyboard.text()
        lent=len(vr)
        vrnew = ''
        ele1=""
        ele2=""
        if(lent==0):
            print("box empty")
            pass
        else:
            cur=self.wificode.cursorPosition()
            print("current position "+ str(cur))
            for element in range(0, int(cur)):
                ele1=ele1+vr[element]
            for element in range(cur,lent):
                    ele2=ele2+vr[element]
            lr_length = len(ele1) - 1
            i = 0;
            for element in ele1:
                if i == lr_length:
                    pass
                else:
                    vrnew = '{}{}'.format(vrnew, element)
                i += 1
            print(vrnew)
            mesg='{}{}'.format(vrnew,ele2)
            self.txtKeyboard.setText(mesg)
            self.wificode.setText(mesg)
            self.wificode.setCursorPosition(cur-1)
        
#         vr = self.txtKeyboard.text()
#         vrnew = ''
#         lr_length = len(vr) - 1
#         i = 0;
#         for str in vr:
#             if i == lr_length:
#                 pass
#             else:
#                 vrnew = '{}{}'.format(vrnew, str)
#             i += 1
#         print(vrnew)
#         self.txtKeyboard.setText(vrnew)
#         mesg = '{}'.format(self.txtKeyboard.text())
#         self.wificode.setText(mesg)

    def connectivity(self):
        try:
            urllib.request.urlopen("https://www.google.com/",timeout=2)
            return True
        except:
            pass
            return False

    def connectwifi(self):
        global m,sign
        global selectedssid
        sign=True
        m=0
        self.frame_3.setGeometry(QtCore.QRect(0, 485, 480, 220))
        self.frame_5.setGeometry(QtCore.QRect(485, 15, 480, 220))
        finalmsg="Connecting to "+str(selectedssid)
        self.msg.setText(finalmsg)
        self.frame.setGeometry(QtCore.QRect(50, 70, 380, 150))
        self.frame_3.hide()
        self.frame_5.hide()
        self.frame.show()
        app.processEvents()
        print(selectedssid)
        pw=self.wificode.text()
        print(pw)
        data=selectedssid+"; "+pw+"; "
        wififile=debugmode.dpath+"pidata/wifi.txt"
        wfile=os.path.isfile(wififile)
        if(wfile==False):
            file1=open(wififile,'w+')
            file1.write(data)
            file1.close()
        else:
            file1=open(wififile,'w+')
            file1.write(data)
            file1.close()
#         config = (
#         '\nnetwork={{\n' +
#         '\tssid="{}"\n' +
#         '\tpsk="{}"\n' + '}}').format(selectedssid, pw)
#         with open("/etc/wpa_supplicant/wpa_supplicant.conf") as f:
#             if config in f.read():
#                 print("Already in file\n"+config)
#             else:
#                 with open("/etc/wpa_supplicant/wpa_supplicant.conf", "a+") as wifi:
#                     wifi.write(config)
#                     wifi.close()
#             f.close()
        config = (
        'ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\n'
        'update_config=0\n'
        'country=PK\n'
        '\nnetwork={{\n' +
        '\tssid="{}"\n' +
        '\tpsk="{}"\n' + '}}').format(selectedssid, pw)
        print("File1 before adding credentials")
        with open("/etc/wpa_supplicant/wpa_supplicant.conf","r+") as wifi:
            data=wifi.read()
            wifi.close()
        print(data)
        with open("/etc/wpa_supplicant/wpa_supplicant.conf","w+") as wifi:
            wifi.write(config)
            wifi.close() 
        print("File2 After adding credentials")
        with open("/etc/wpa_supplicant/wpa_supplicant.conf","r+") as wifi:
            data=wifi.read()
            wifi.close()
        print(data)
        #os.system("sudo wpa_cli -i wlan0 reconfigure")
        proc=subprocess.Popen(["sudo wpa_cli -i wlan0 reconfigure"],stdout=subprocess.PIPE,shell=True)
        (out,err)=proc.communicate()
        try:
            print("reconfigure  out:",out)
        except:
            print("error:",err)
        loop= QtCore.QEventLoop()
        QTimer.singleShot(1000, loop.quit)
        loop.exec_()
        for n in range(0,30):
            loop= QtCore.QEventLoop()
            QTimer.singleShot(1000, loop.quit)
            loop.exec_()
            i=self.connectivity()
            if i==True:
                print(n)
                break
            else:
                n+=1
        if(n==0):
            os.system("sudo wpa_cli -i wlan0 reconfigure")
            loop= QtCore.QEventLoop()
            QTimer.singleShot(1000, loop.quit)
            loop.exec_()
            for n in range(0,30):
                loop= QtCore.QEventLoop()
                QTimer.singleShot(1000, loop.quit)
                loop.exec_()
                i=self.connectivity()
                if i==True:
                    print(n)
                    break
                else:
                    n+=1 
        print("loop finished")
        time.sleep(1)
        if(i==False):
            self.msg.setText("No access! Removing Credentials!")
            gifpath=debugmode.dpath+"Server/circle spinner.gif"
            self.gif1 = QMovie(gifpath)
            self.gif.setMovie(self.gif1)
            self.gif1.start()
            app.processEvents()
            print("no coneection")
#             fin=open("/etc/wpa_supplicant/wpa_supplicant.conf","rt")
#             data = fin.read()
#             data = data.replace(config, "")
#             fin.close()
#             fin=open("/etc/wpa_supplicant/wpa_supplicant.conf","wt")
#             fin.write(data)
#             fin.close()
            config = (
            'ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\n'
            'update_config=0\n'
            'country=PK\n')
            with open("/etc/wpa_supplicant/wpa_supplicant.conf","w+") as wifi:
                wifi.write(config)
                wifi.close()
            os.system("sudo wpa_cli -i wlan0 reconfigure")
            time.sleep(10)
        self.switch_wpdone.emit()
        pass


class Main(QtWidgets.QMainWindow, Ui_MainWindow):  #Class to acces Main.py GUI
    switch_done = QtCore.pyqtSignal()
    switch_x = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.pb1.clicked.connect(lambda: self.pressdone())
        self.frame_numeric.setGeometry(QtCore.QRect(115, 110, 250, 200))
        self.frame.setGeometry(QtCore.QRect(0, 0, 480, 320))
        clickable(self.txtPassword).connect(self.presstxt_password)
        self.btn1.clicked.connect(lambda: self.txtUpdateN('1'))
        self.btn2.clicked.connect(lambda: self.txtUpdateN('2'))
        self.btn3.clicked.connect(lambda: self.txtUpdateN('3'))
        self.btn4.clicked.connect(lambda: self.txtUpdateN('4'))
        self.btn5.clicked.connect(lambda: self.txtUpdateN('5'))
        self.btn6.clicked.connect(lambda: self.txtUpdateN('6'))
        self.btn7.clicked.connect(lambda: self.txtUpdateN('7'))
        self.btn8.clicked.connect(lambda: self.txtUpdateN('8'))
        self.btn9.clicked.connect(lambda: self.txtUpdateN('9'))
        self.btn0.clicked.connect(lambda: self.txtUpdateN('0'))
        self.btnx.clicked.connect(lambda: self.pressx())
        self.btnEnter.clicked.connect(lambda: self.pressEnterN())
        self.btnDelete.clicked.connect(lambda: self.pressdeleteN())
        global b
        if(b==0):
            self.btnx.setEnabled(False)
        else:
            self.btnx.setEnabled(True)

    def presstxt_password(self):
        print('password box clicked')
        self.frame_numeric.setGeometry(QtCore.QRect(115, 110, 250, 200))

    def pressEnterN(self):
        print('pressing enter')
        self.frame_numeric.setGeometry(QtCore.QRect(115, 110, 250, 200))
        mesg = '{}'.format(self.txtKeyboard.text())
        self.txtPassword.setText(mesg)
        self.pressdone()

    def pressx(self):
        print('X')
        self.switch_x.emit()
        pass

    def pressdeleteN(self):
        self.txtdeleteN()
        print('Delete')
        pass

    def txtUpdateN(self, txt):
        cur=self.txtPassword.cursorPosition()
        print("current position "+str(cur))
        lent = len(self.txtKeyboard.text())
        if len(self.txtKeyboard.text()) == 0:
            self.txtKeyboard.setText('{}'.format(txt))
            self.txtPassword.setText('{}'.format(txt))

        else:
            v = self.txtKeyboard.text()
            ele1=""
            ele2=""
            for element in range(0, cur): 
                ele1=ele1+v[element]
            for element in range(cur, lent): 
                ele2=ele2+v[element]
            print(ele1)
            print("\n"+ele2)
            self.txtKeyboard.setText('{}{}{}'.format(ele1, txt, ele2))
            mesg = '{}'.format(self.txtKeyboard.text())
            self.txtPassword.setText(mesg)
            self.txtPassword.setCursorPosition(cur+1)


    def txtdeleteN(self):
        vr = self.txtKeyboard.text()
        lent=len(vr)
        vrnew = ''
        ele1=""
        ele2=""
        if(lent==0):
            print("box empty")
            pass
        else:
            cur=self.txtPassword.cursorPosition()
            print("current position "+ str(cur))
            for element in range(0, int(cur)):
                ele1=ele1+vr[element]
            for element in range(cur,lent):
                    ele2=ele2+vr[element]
            lr_length = len(ele1) - 1
            i = 0;
            for element in ele1:
                if i == lr_length:
                    pass
                else:
                    vrnew = '{}{}'.format(vrnew, element)
                i += 1
            print(vrnew)
            mesg='{}{}'.format(vrnew,ele2)
            self.txtKeyboard.setText(mesg)
            self.txtPassword.setText(mesg)
            self.txtPassword.setCursorPosition(cur-1)

    def pressdone(self):
        print('Done press')
        global m,sign
        sign=True
        m=0
        self.switch_done.emit()
        pass

class networkerror(QtWidgets.QMainWindow,Ui_networktryagain ):  #Class to acces Main.py GUI
    switch_ntryagain = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        super(Ui_networktryagain, self).__init__()
        self.setupUi(self)
        self.networktabutton.clicked.connect(lambda:self.tryagain())

    def tryagain(self):
        self.switch_ntryagain.emit()
        pass

class chkupdate(QtWidgets.QMainWindow, Ui_checkingupdates):  #Class to acces Main.py GUI

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        super(Ui_checkingupdates, self).__init__()
        self.setupUi(self)

class dwnupdate(QtWidgets.QMainWindow, Ui_downloadupdates):  #Class to acces Main.py GUI

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        super(Ui_downloadupdates, self).__init__()
        self.setupUi(self)

class updateready(QtWidgets.QMainWindow, Ui_readyupdate):  #Class to acces Main.py GUI

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        super(Ui_readyupdate, self).__init__()
        self.setupUi(self)

class updaterestart(QtWidgets.QMainWindow,Ui_updateerror):  #Class to acces Main.py GUI
    switch_restartupdate = QtCore.pyqtSignal()
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        super(Ui_updateerror, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.uprestart())
    def uprestart(self):
        os.system("sudo reboot")


class authtryagain(QtWidgets.QMainWindow, Ui_authtryagain):  #Class to acces Main.py GUI
    switch_tryagain = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        super(Ui_authtryagain, self).__init__()
        self.setupUi(self)
        self.pb2.clicked.connect(lambda: self.auth())

    def auth(self):
        print('auth press')
        self.switch_tryagain.emit()
        pass

class server(QtWidgets.QMainWindow, Ui_server):  #Class to acces Main.py GUI
    switch_tryagain1 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        super(Ui_server, self).__init__()
        self.setupUi(self)
        self.pb2.clicked.connect(lambda: self.auth1())

    def auth1(self):
        print('auth press')
        self.switch_tryagain1.emit()
        pass

class CloneThread(QThread):
#    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self):
        QThread.__init__(self)


    def pause_signal(self):
        global sign
        sign=False



    def run(self):
        global sign
        global qpath
        while sign:
            pass
            print("in function")
            #cmd="lp \"/home/pi/queue/"
            cmd="lp -d dymo \""+qpath
            enteries=[]
            enteries = os.listdir(qpath)
            print(enteries)
            for entry in enteries:
                print(entry)
                fcmd=cmd+entry+"\""
                os.system(fcmd)
                time.sleep(2)
                try:
                    os.remove((qpath+entry))
                    enteries.remove(entry)
                except:
                    pass
                print("for loop")
                print(enteries)
                while sign:
                    proc=subprocess.Popen(['lpstat -R -pdymo'],stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
                    (out,err)=proc.communicate()
                    ar=str(out.decode('utf-8'))
                    if ar[16:20] =="idle":
                        print("Ready to print\n")
                        break
                    if sign==False:
                        enteries.clear()
                        print("Exiting While loop 2")
                        break
                if sign==False:
                    print("Exiting for loop")
                    enteries.clear()
                    print(enteries)
                    break

class printqueue(QtWidgets.QMainWindow, Ui_printqueue):  #Class to acces Main.py GUI
    switch_pause = QtCore.pyqtSignal()
    switch_clearqueue = QtCore.pyqtSignal()
    switch_setting = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        super(Ui_printqueue, self).__init__()
        self.setupUi(self)
        self.CT=CloneThread()
        self.CT.start()
        self.queuelistupdate()
        self.pb3.clicked.connect(lambda: self.pause())
        self.pb4.clicked.connect(lambda: self.clearqueue())
        self.pushButton.clicked.connect(lambda: self.setting())
    def setting(self):
        self.CT.pause_signal()
        global m
        m=1
        self.switch_setting.emit()
        pass
    def pause(self):
        print('Pause Pressed')
        global m
        m=1
        self.CT.pause_signal()
        self.switch_pause.emit()
        pass

    def clearqueue(self):
        print('Clear Queue Pressed')
        items=[]
        global sign
        sign=False
        time.sleep(1)
        items = os.listdir(qpath)
        for item in items:
            os.remove(qpath+item)
        self.queuelistupdate()
        sign=True
        self.switch_clearqueue.emit()
        pass
    def queuelistupdate(self):
        f = os.listdir(debugmode.dpath+"queue/")
        print("updating list")
        self.listWidget.clear()
        for i in f:
            item=QtWidgets.QListWidgetItem(i,self.listWidget)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.listWidget.update()
        t=threading.Timer(1.0, self.queuelistupdate)
        t.start()
        global m,sign
        print("value of m: "+str(m)+str(sign))
        if(m==1):
            t.cancel()
        
class printpause(QtWidgets.QMainWindow, Ui_printingpause):
    switch_continue = QtCore.pyqtSignal()
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        super(Ui_printingpause, self).__init__()
        self.setupUi(self)
        self.pb3.clicked.connect(lambda: self.resumeprinting())
        

    def resumeprinting(self):
        global m,sign
        m=0
        sign= True
        print("resume pressed: ")
        self.switch_continue.emit()
        pass

class settings(QtWidgets.QMainWindow, Ui_settings):
    switch_setwifi = QtCore.pyqtSignal()
    switch_setkiosk = QtCore.pyqtSignal()
    switch_setqueue = QtCore.pyqtSignal()
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        super(Ui_settings, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.settingswifi())
        self.pushButton_3.clicked.connect(lambda: self.settingskiosk())
        self.pushButton_2.clicked.connect(lambda: self.settingsqueue())
        

    def settingswifi(self):
        global b
        b=1
        self.switch_setwifi.emit()
        pass
    def settingskiosk(self):
        global b
        b=1
        self.switch_setkiosk.emit()
        pass
    def settingsqueue(self):
        global m,sign
        m=0
        sign=True
        self.switch_setqueue.emit()
        pass

class CloneThread1(QThread):
    #signal = pyqtSignal('PyQt_PyObject')
    finish1 = pyqtSignal()
    finish3 = pyqtSignal()

    def __init__(self):
        QThread.__init__(self)
    def run(self):
        c=zip.Checkingupdates()
        if(c==True):
            self.finish1.emit()
        else:
            self.finish3.emit()

class CloneThread2(QThread):
    finish2 = pyqtSignal()

    def __init__(self):
        QThread.__init__(self)
    def run(self):
        zip.downloadingupdates()
        print("finishing")
        self.finish2.emit()
        
        
class Controller:   # Controller class which controlls all the functions
    def __init__(self):
        print("In controller class")
        self.ct1=CloneThread1()
        self.ct2=CloneThread2()
#         self._splash = splash()
#         self._wifilisting = wifilisting()
#         self._wifipw = wifipw()
#         self._restart=restart()
        self._Main = Main()
#         self._networkerror =networkerror()
        self._chkupdate =chkupdate()
#         self._dwnupdate = dwnupdate()
#         self._updateready = updateready()
#         self._updaterestart=updaterestart()
#         self._authtryagain = authtryagain()
#         self._printqueue = printqueue()
#         self._printpause=printpause()
        pass
        
    def show_splash_page(self):
        self._splash = splash()
        self._splash.show()
        loop= QtCore.QEventLoop()
        QTimer.singleShot(6000, loop.quit)
        loop.exec_()
        a=self.conectivity()
        if(a==True):
            b=self.checkkioskfile()
            print(b)
            global n
            if(n==1):
                print("let server")
                self.show_server_page()
            else:
                if(b==True):
                    #self.show_server_page()
                    self.show_chkupdate_page()
                elif(b==False):
                    print(b)
                    self.show_Main_page()
        else:
            self.show_wifilisting_page()
        pass
    
    def conectivity(self):
        try:
            urllib.request.urlopen("https://www.google.com/",timeout=2)
            return True
        except:
            pass
            return False

    def checkkioskfile(self):
        kioskfile=debugmode.dpath+"pidata/kiosk.txt"
        kfile=os.path.isfile(kioskfile)
        if(kfile==True):
            print("file found")
            kfilesize=os.path.getsize(debugmode.dpath+"pidata/kiosk.txt")
            if(kfilesize>0):
                global dev,organize
                try:
                    rip=check_output(['hostname', '-I'])
                    file= open(kioskfile,'r')
                    for line in file:
                        feilds=line.split("; ")
                        lekid=int(feilds[0])
                    URL = "https://us-central1-high5-test.cloudfunctions.net/httpRequests/registerPi"
                    pload=json.dumps({"pin": lekid,"ip":str(rip) ,"port": 5000})#"pin": lekid,
                    headerJson={"Content-Type": "application/json;charset=UTF-8",
                    "Accept": "*/*",
                    "Host": "us-central1-high5-test.cloudfunctions.net",
                    "Connection": "keep-alive",
                    "User-Agent": "PieServer/001"}
                    r=requests.post(URL,data=pload, headers= headerJson)
                    data=json.loads(r.content)
                    print(data)
                except Exception as err:
                    print("Current error:",err)
                    b=self.conectivity()
                    if(b==False):
                        self.show_networktryagain_page()
                try:
                    if(int(data["success"])):
                        print("try")
                        kid=int(data["kiosk_id"])
                        dev=data["kiosk_name"]
                        organize=data["org_name"]
                        return True
                except:
                    print("server")
                    global n
                    n=1
                    print("n = "+str(n))
        else:
            print("false")
            return False
        
    def show_wifilisting_page(self):
        self._wifilisting = wifilisting()
        self._wifilisting.refresh.connect(self.show_wifipw_page)
        self._wifilisting.switch_cancel.connect(self.show_settings_page)
        self._wifilisting.show()
        try:
            self._splash.close()
        except:
            pass
        
        try:
            self._networkerror.close()
        except:
            pass
        try:
            self._wifipw.close()
        except:
            pass
        try:
            self._settings.close()
        except:
            pass
        loop= QtCore.QEventLoop()
        QTimer.singleShot(1000, loop.quit)
        loop.exec_()
        self._wifilisting.refreshlist()
        
        

    def show_wifipw_page(self):
        self._wifipw = wifipw()
        self._wifipw.switch_wpdone.connect(self.checkconnectivity)
        self._wifipw.switch_cancelpw.connect(self.show_wifilisting_page)
        self._wifipw.show()
        self._wifilisting.close()
        
    def checkconnectivity(self):
        internet=self.conectivity()
        if(internet== True):
            b=self.checkkioskfile()
            print(b)
            if(b==True):
                self.show_chkupdate_page()
            else:
                self.show_Main_page()
        else:
            self.show_wifilisting_page()
            
    def show_Main_page(self):
        self._Main = Main()
        self._Main.switch_done.connect(self.checkkioskcode)
        self._Main.switch_x.connect(self.show_settings_page)
        self._Main.show()
        kioskfile=debugmode.dpath+"pidata/kiosk.txt"
        with open(kioskfile,'r+') as file1:
            data=file1.read()
            file1.close()
        self._Main.txtPassword.setText(data.split("; ")[0])
        self._Main.txtKeyboard.setText(data.split("; ")[0])
        #self._wifipw.close()
        
        try:
            self._authtryagain.close()
        except:
            pass
        try:
            self._wifipw.close()
        except:
            pass
        try:
            self._splash.close()
        except:
            pass
        try:
            self._settings.close()
        except:
            pass
        try:
            self._server.close()
        except:
            pass

    def checkkioskcode(self):
        global dev,organize
        try:
            rip=check_output(['hostname', '-I'])
            kicode=self._Main.txtPassword.text()
            if(len(kicode)==0):
                lekid=123
                print(lekid)
            else:
                lekid=self._Main.txtPassword.text()
                print(lekid)
            URL = "https://us-central1-high5-test.cloudfunctions.net/httpRequests/registerPi"
            pload=json.dumps({"pin": int(lekid),"ip":str(rip) ,"port": 5000})#"pin": int(lekid),
            headerJson={"Content-Type": "application/json;charset=UTF-8",
            "Accept": "*/*",
            "Host": "us-central1-high5-test.cloudfunctions.net",
            "Connection": "keep-alive",
            "User-Agent": "PieServer/001"}
            r=requests.post(URL,data=pload, headers= headerJson)
            data=json.loads(r.content)
        except Exception as err:
            print("Current error:",err)
        b=self.conectivity()
        if(b==False):
            self.show_networktryagain_page()
        else:
            try:
                if(int(data["success"])):
                    kid=int(data["kiosk_id"])
                    dev=data["kiosk_name"]
                    organize=data["org_name"]
                    kioskfile=debugmode.dpath+"pidata/kiosk.txt"
                    with open(kioskfile,'w+') as file1:
                        file1.write(lekid+"; ")
                        file1.close()
                    self.show_chkupdate_page()
                else:
                    self.show_authtryagain_page()
            except:
                self.show_server_page()
        
    def show_networktryagain_page(self):
        self._networkerror =networkerror()
        self._networkerror.switch_ntryagain.connect(self.show_wifilisting_page)
        self._networkerror.show()
        self._Main.close()

    def show_chkupdate_page(self):
        self._chkupdate =chkupdate()
        self.ct1.finish1.connect(self.show_dwnupdate_page)
        self.ct1.finish3.connect(self.show_printqueue_page)
        self._chkupdate.show()
        self._Main.close()
        try:
            self._splash.close()
        except:
            pass
        try:
            self._wifipw.close()
        except:
            pass
        self.ct1.start()
        print("check thread started")
        
    def show_dwnupdate_page(self):
        self._dwnupdate = dwnupdate()
        self.ct2.finish2.connect(self.show_updateready_page)
        self._dwnupdate.show()
        print("closing check thread")
        self._chkupdate.close()
        self.ct2.start()
        print("dwn thread started")
        

    def show_updateready_page(self):
        self._updateready = updateready()
        self._updateready.show()
        self._dwnupdate.close()
        loop= QtCore.QEventLoop()
        QTimer.singleShot(2000, loop.quit)
        loop.exec_()
        os.system("sudo reboot")
        pass

    def show_updaterestart_page(self):
        self._updaterestart=updaterestart()
        self._updaterestart.show()
        self._updateready.close()
        
    def show_authtryagain_page(self):
        self._authtryagain = authtryagain()
        self._authtryagain.switch_tryagain.connect(self.show_Main_page)
        self._authtryagain.show()
        self._Main.close()
        pass
    
    def show_server_page(self):
        self._server = server()
        self._server.switch_tryagain1.connect(self.show_Main_page)
        self._server.show()
        try:
            self._Main.close()
        except:
            pass
        try:
            self._splash.close()
        except:
            pass
        pass

    def show_printqueue_page(self):
        try:
            self._printqueue.close()
        except:
            pass
        global dev,organize
        self._printqueue = printqueue()
        self._printqueue.device.setText("Device: "+dev)
        self._printqueue.org.setText("Organization: "+organize)
        self._printqueue.switch_pause.connect(self.show_printingpause_page)
        self._printqueue.switch_setting.connect(self.show_settings_page)
        self._printqueue.show()
        try:
            self._printpause.close()
        except:
            pass
        try:
            self._dwnupdate.close()
        except:
            pass
        try:
            self._chkupdate.close()
        except:
            pass
        try:
            self._settings.close()
        except:
            pass
    def show_settings_page(self):
        self._settings=settings()
        print("here in settings")
        self._settings.switch_setwifi.connect(self.show_wifilisting_page)
        self._settings.switch_setkiosk.connect(self.show_Main_page)
        self._settings.switch_setqueue.connect(self.show_printqueue_page)
        self._settings.show()
        self._printqueue.close()
        try:
            self._wifilisting.close()
        except:
            pass
        try:
            self._Main.close()
        except:
            pass

    def show_printingpause_page(self):
        global dev,organize
        self._printpause=printpause()
        self._printpause.device.setText("Device: "+dev)
        self._printpause.org.setText("Organization: "+organize)
        self._printpause.switch_continue.connect(self.show_printqueue_page)
        self._printpause.show()
        self._printqueue.close()

import resources
def clickable(widget):
    class Filter(QObject):
        clicked = pyqtSignal()

        def eventFilter(self, obj, event):
            if obj == widget and event.type() == QEvent.MouseButtonRelease and obj.rect().contains(event.pos()):
                self.clicked.emit()
                return True
            else:
                return False
    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked

if __name__ == "__main__":
    import sys
    print("Main")
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    print("Calling splash")
    controller.show_splash_page()
    sys.exit(app.exec_())

