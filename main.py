from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont, QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit)
from secondwin import *
from instr import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
    def initUI(self):
        self.btn_next = QPushButton(txt_text, self)
        self.hello_text = QLabel(txt_hello)
        self.lore = QLabel(txt_lore)

        self.pixmap = QPixmap("image/cosmos.jpg")
        self.cartoon = QLabel(self)
        self.cartoon.setPixmap(self.pixmap)

        self.hello_text.setFont(QFont("Times", 18, QFont.Bold))
        self.hello_text.setStyleSheet("color: rgb(255,255,255)")
        self.lore.setFont(QFont("Times", 14))
        self.lore.setStyleSheet("color: rgb(255,255,255)")

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.lore, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.cartoon, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)             
        self.setLayout(self.layout_line)
    def next_click(self):
        self.sw = SecondWin()
        self.hide()
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

app = QApplication([])
mw = MainWin()
mw.setObjectName("MainWindow")
mw.setStyleSheet("#MainWindow{background-color:dark-blue}")
app.exec_()