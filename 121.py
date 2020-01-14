# coding:utf-8

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QMouseEvent
from PyQt5 import Qt

import u2

class LoginDialog(QMainWindow, u2.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.Qt.FramelessWindowHint)  # 隐藏窗口标题栏
        self.mDragWindow = False
        self.mMousePoint = []