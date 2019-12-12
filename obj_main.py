# -*- coding: utf-8 -*-
#开发团队
#开发人员

import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from MainWin import Ui_MainWin
from LogonWin import Ui_LogonWin

class MyMainWin(QtWidgets.QWidget,Ui_MainWin):
    def __init__(self):
        super(MyMainWin, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.OnClick_Start)

    def OnClick_Start(self):
        self.close()


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
    ui = MyLogonWin()
    ui.show()
    sys.exit(app.exec_())
