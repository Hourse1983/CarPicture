# -*- coding: utf-8 -*-
#开发团队
#开发人员

import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from MainWin import Ui_MainWin
from LogonWin import Ui_LogonWin

class MyMainWin(Ui_MainWin):
    pass

class MyLogonWin(Ui_LogonWin):
    pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyLogonWin()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
