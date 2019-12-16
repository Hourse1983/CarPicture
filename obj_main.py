# -*- coding: utf-8 -*-
#开发团队
#开发人员
import os
import sys

from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

from MainWin import Ui_MainWin
from LogonWin import Ui_LogonWin
from retbmm import ReTbmm

class MyMainWin(QtWidgets.QWidget,Ui_MainWin):
    def __init__(self):
        super(MyMainWin, self).__init__()
        self.setupUi(self)
        self.cdir = os.getcwd()
        self.root = QTreeWidgetItem(self.treeWidget)
        self.root.setText(0,'V8 Vantage 2018')
        self.pushButton.clicked.connect(self.OnClick_Start)

    def OnClick_Start(self):
        #关闭爬虫按键
        self.pushButton.setVisible(False)
        #建立爬虫类对象
        ui = ReTbmm()
        #调用爬虫类函数爬取数据
        ui.Retbmm()
        self.pushButton.setVisible(True)
        self.path =self.cdir + '/mrsoft'
        dirs = os.listdir(self.path)
        #循环文件名称
        for dir in dirs:
            #添加文件名称到树形结构
            QTreeWidgetItem(self.root).setText(0,dir)
        self.treeWidget.clicked.connect(self.onTreeClicked)

    def onTreeClicked(self,Qmodelidx):
        items = self.treeWidget.currentItem()
        if items.text(0) == 'V8 Vantage 2018':
            self.root.takeChildren()
            self.path = self.cdir + '/mrsoft'
            dirs = os.listdir(self.path)
            for dir in dirs:
                QTreeWidgetItem(self.root).setText(0,dir)
            self.treeWidget.clicked.connect(self.onTreeClicked)
        else:
            while self.gridLayout.count():
                item = self.gridLayout.takeAt(0)
                widget = item.widget()
                widget.deleteLater()
            filenames = []
            for filename in os.listdir(self.cdir +'/mrsoft/'+items.text(0)):
                filenames.append(filename)
            i = -1
            for n in range(len(filenames)):
                x = n%3
                if x ==0:
                    i += 1
                self.widget = QWidget()
                self.widget.setGeometry(QtCore.QRect(0,0,250,200))
                self.widget.setObjectName("Widget" + str(n))
                self.lable = QLabel(self.widget)
                self.lable.setGeometry(QtCore.QRect(0,0,250,200))
                self.lable.setPixmap(QPixmap(self.path + '/'+items.text(0) + '/' + filenames[n]))
                self.lable.setScaledContents(True)
                self.lable.setObjectName("label"+str(n))
                self.commandLinkButton = QCommandLinkButton(self.widget)
                self.commandLinkButton.setGeometry(QtCore.QRect(0,0,111,41))
                self.commandLinkButton.setObjectName("label"+str(n))
                self.commandLinkButton.setText(filenames[n])
                self.commandLinkButton.clicked.connect(lambda: self.wichbtn(self.path + '/' +items.text(0) +'/'))
                self.gridLayout.addWidget(self.widget,i,x)
            self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
            self.scrollAreaWidgetContents_2.setMinimumWidth(800)
            self.scrollAreaWidgetContents_2.setMinimumHeight(i*200)

    def wichbtn(self,tppath):
         sender = self.gridLayout.sender()
         img = Image.open(tppath + sender.text())
         img.show()




class MyLogonWin(QtWidgets.QWidget,Ui_LogonWin):
    def __init__(self):
        super(MyLogonWin, self).__init__()
        self.setupUi(self)
        self.pushButton_logON.clicked.connect(self.OnClick_Logon)

    def OnClick_Logon(self):
        if self.lineEdit_username.text() =="mingri":
            if self.lineEdit_password.text() =="666666":
                self.close()
            else:
                self.lineEdit_password.setText("密码错误")
        else:
            self.lineEdit_username.setText("请输入正确的用户名")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MyMainWin()
    ui.show()
    sys.exit(app.exec_())
