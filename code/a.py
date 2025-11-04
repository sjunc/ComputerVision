from PyQt5.QtWidgets import *
import sys
import winsound


class BeepSound(QMainWindow):
    def __init_(self):
        super().__init__()
        self.setWindowTitle("삑소리 내기")
        self.setGeometry(200,200,500,100)
        