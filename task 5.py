#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PySide2.QtWidgets import QWidget, QApplication, QPushButton, QButtonGroup, QGridLayout, QLabel
from PySide2.QtCore import Qt

"""
Напишите программу, в которой имеется несколько объединенных в группу радиокнопок. Если какая-нибудь кнопка включается, 
то в метке должна отображаться соответствующая ей информация. Обычных кнопок в окне быть не должно.
"""
members = {
    'BTS': 'also known as the Bangtan Boys,\n '
           'is a South Korean boy band formed in\n '
           '2010 and debuting in 2013 under Big Hit Entertainment.\n '
           'Consisting of members: Kim Namjoon, Kim Seokjin, Min Yoongi, Jeong Hoseok,\n'
           'Park Jimin, Kim Taehyung, Jeon Jungkook',
    'Taehyung': '30.12.1995',
    'Jungkook': '1.09.1997',
    'Jimin': '12.10.1995',
    'Jin': '4.12.1992',
    'Hoseok': '12.02.1994',
    'Namjoon': '12.09.1994',
    'Yoongi': '9.03.1993'
}


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BTS")
        self.setGeometry(470, 390, 470, 390)
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.radio_button_1 = QPushButton('BTS')
        self.radio_button_1.setCheckable(True)
        self.radio_button_2 = QPushButton('Taehyung')
        self.radio_button_2.setCheckable(True)
        self.radio_button_3 = QPushButton('Jungkook')
        self.radio_button_3.setCheckable(True)
        self.radio_button_4 = QPushButton('Jimin')
        self.radio_button_4.setCheckable(True)
        self.radio_button_5 = QPushButton('Jin')
        self.radio_button_5.setCheckable(True)
        self.radio_button_6 = QPushButton('Hoseok')
        self.radio_button_6.setCheckable(True)
        self.radio_button_7 = QPushButton('Namjoon')
        self.radio_button_7.setCheckable(True)
        self.radio_button_8 = QPushButton('Yoongi')
        self.radio_button_8.setCheckable(True)

        self.button_group = QButtonGroup()
        self.button_group.addButton(self.radio_button_1)
        self.button_group.addButton(self.radio_button_2)
        self.button_group.addButton(self.radio_button_3)
        self.button_group.addButton(self.radio_button_4)
        self.button_group.addButton(self.radio_button_5)
        self.button_group.addButton(self.radio_button_6)
        self.button_group.addButton(self.radio_button_7)
        self.button_group.addButton(self.radio_button_8)
        self.button_group.buttonClicked.connect(self._radiobutton_clk)
        self.grid_layot()
        self.show()


    def grid_layot(self):
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.radio_button_1, 1, 0)
        grid.addWidget(self.radio_button_2, 2, 0)
        grid.addWidget(self.radio_button_3, 3, 0)
        grid.addWidget(self.radio_button_4, 4, 0)
        grid.addWidget(self.radio_button_5, 5, 0)
        grid.addWidget(self.radio_button_6, 6, 0)
        grid.addWidget(self.radio_button_7, 7, 0)
        grid.addWidget(self.radio_button_8, 8, 0)
        grid.addWidget(self.label, 2, 2)
        self.setLayout(grid)

    def _radiobutton_clk(self, button):
        self.label.setText(members[button.text()])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setObjectName("MainWindow")
    window.setStyleSheet("#MainWindow{background-color:purple}")
    window.show()
    sys.exit(app.exec_())
