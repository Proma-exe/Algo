from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont, QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit)
from finalwin import *
from instr import *
from MegaMakson9000 import *
class SecondWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
    def initUI(self):
        self.btn_next1 = QPushButton(txt_hard1, self)
        self.btn_next2 = QPushButton(txt_hard2, self)
        self.btn_next3 = QPushButton(txt_hard3, self)
        self.n_text = QLabel(txt_n)
        self.settings_text1 = QLabel(txt_settings1)
        self.settings_text2 = QLabel(txt_settings2)
        self.settings_text3 = QLabel(txt_settings3)

        self.n_text.setFont(QFont("Times", 18, QFont.Bold))
        self.n_text.setStyleSheet("color: rgb(255,255,255)")

        self.settings_text1.setFont(QFont("Times", 16))
        self.settings_text1.setStyleSheet("color: rgb(255,255,255)")
        self.settings_text2.setFont(QFont("Times", 16))
        self.settings_text2.setStyleSheet("color: rgb(255,255,255)")
        self.settings_text3.setFont(QFont("Times", 16))
        self.settings_text3.setStyleSheet("color: rgb(255,255,255)")

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.n_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.settings_text1, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.settings_text2, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.settings_text3, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.btn_next1, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.btn_next2, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.btn_next3, alignment = Qt.AlignCenter)
        self.setLayout(self.layout_line)
    def next_click1(self):
        self.hide()
        self.fw = startgame(10)
    
    def next_click2(self):
        self.hide()
        self.fw = startgame(25)
    
    def next_click3(self):
        self.hide()
        self.fw = startgame(40)
    
    def connects(self):
        self.btn_next1.clicked.connect(self.next_click1)
        self.btn_next2.clicked.connect(self.next_click2)
        self.btn_next3.clicked.connect(self.next_click3)
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        self.setObjectName("MainWindow")
        self.setStyleSheet("#MainWindow{background-color:dark-blue}")