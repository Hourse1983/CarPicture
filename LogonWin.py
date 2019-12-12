# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LogonWin.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LogonWin(object):
    def setupUi(self, LogonWin):
        LogonWin.setObjectName("LogonWin")
        LogonWin.resize(429, 309)
        self.verticalLayoutWidget = QtWidgets.QWidget(LogonWin)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 20, 271, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit_username = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.verticalLayout.addWidget(self.lineEdit_username)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.verticalLayout.addWidget(self.lineEdit_password)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(LogonWin)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(49, 160, 271, 87))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_logON = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_logON.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_logON.setFont(font)
        self.pushButton_logON.setAcceptDrops(False)
        self.pushButton_logON.setObjectName("pushButton_logON")
        self.verticalLayout_2.addWidget(self.pushButton_logON)
        self.pushButton_center = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_center.setFont(font)
        self.pushButton_center.setObjectName("pushButton_center")
        self.verticalLayout_2.addWidget(self.pushButton_center)
        self.pushButton_center.raise_()
        self.pushButton_logON.raise_()

        self.retranslateUi(LogonWin)
        self.pushButton_center.clicked.connect(LogonWin.close)
        QtCore.QMetaObject.connectSlotsByName(LogonWin)

    def retranslateUi(self, LogonWin):
        _translate = QtCore.QCoreApplication.translate
        LogonWin.setWindowTitle(_translate("LogonWin", "登录"))
        self.label.setText(_translate("LogonWin", "用户名（mingri）："))
        self.lineEdit_username.setPlaceholderText(_translate("LogonWin", "请输入用户名"))
        self.label_2.setText(_translate("LogonWin", "密码（666666）："))
        self.lineEdit_password.setPlaceholderText(_translate("LogonWin", "请输入密码"))
        self.pushButton_logON.setText(_translate("LogonWin", "登录"))
        self.pushButton_center.setText(_translate("LogonWin", "退出"))
