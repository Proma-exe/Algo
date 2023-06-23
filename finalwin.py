from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont, QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit)
from instr import *
class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
    def initUI(self):
        self.btn_next = QPushButton(txt_final, self)
        self.win_text = QLabel(txt_win)
        self.r_text1 = QLabel(txt_r1)
        self.r_text2 = QLabel(txt_r2)
        self.authors_text = QLabel(txt_authors)

        self.win_text.setFont(QFont("Times", 18, QFont.Bold))
        self.win_text.setStyleSheet("color: rgb(255,255,255)")

        self.r_text1.setFont(QFont("Times", 16))
        self.r_text1.setStyleSheet("color: rgb(255,255,255)")
        self.r_text2.setFont(QFont("Times", 16))
        self.r_text2.setStyleSheet("color: rgb(255,255,255)")
        self.authors_text.setFont(QFont("Times", 16, QFont.Bold))
        self.authors_text.setStyleSheet("color: rgb(255,255,255)")

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.win_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.r_text1, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.r_text2, alignment = Qt.AlignCenter)  
        self.layout_line.addWidget(self.authors_text, alignment = Qt.AlignRight)
        self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)            
        self.setLayout(self.layout_line)
    def next_click(self):
        self.hide()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        self.setObjectName("MainWindow")
        self.setStyleSheet("#MainWindow{background-color:dark-blue}")
