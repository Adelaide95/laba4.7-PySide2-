#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PySide2.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QLineEdit, QVBoxLayout

"""
Напишите программу, состоящую из семи кнопок, цвета которых соответствуют цветам радуги. 
При нажатии на ту или иную кнопку в текстовое поле должен вставляться код цвета, а в метку – название цвета.
Коды цветов в шестнадцатеричной кодировке: #ff0000 – красный, #ff7d00 – оранжевый, #ffff00 – желтый, #00ff00 – зеленый, 
#007dff – голубой, #0000ff – синий, #7d00ff – фиолетовый.
"""


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 150, 250)
        self.setWindowTitle("Task2")
        self.text_edit = QLineEdit(self)
        self.label = QLabel(self)
        self.button1 = QPushButton(self)
        self.button2 = QPushButton(self)
        self.button3 = QPushButton(self)
        self.button4 = QPushButton(self)
        self.button5 = QPushButton(self)
        self.button6 = QPushButton(self)
        self.button7 = QPushButton(self)
        self.initializeUI()

    def initializeUI(self):
        self.label.resize(80, 10)
        self.text_edit.resize(60, 20)

        self.button1.setStyleSheet("background-color: red;")
        self.button1.clicked.connect(self.red)

        self.button2.setStyleSheet("background-color: orange;")
        self.button2.clicked.connect(self.orange)

        self.button3.setStyleSheet("background-color: yellow;")
        self.button3.clicked.connect(self.yellow)

        self.button4.setStyleSheet("background-color: green;")
        self.button4.clicked.connect(self.green)

        self.button5.setStyleSheet("background-color: #007dff;")
        self.button5.clicked.connect(self.cuan)

        self.button6.setStyleSheet("background-color: #0000ff;")
        self.button6.clicked.connect(self.blue)

        self.button7.setStyleSheet("background-color: #7d00ff;")
        self.button7.clicked.connect(self.purple)

    def vertical_box(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.text_edit)
        vbox.addWidget(self.button1)
        vbox.addWidget(self.button2)
        vbox.addWidget(self.button3)
        vbox.addWidget(self.button4)
        vbox.addWidget(self.button5)
        vbox.addWidget(self.button6)
        vbox.addWidget(self.button7)
        self.setLayout(vbox)

    def red(self):
        self.label.setText("Красный")
        self.text_edit.setText("#ff0000")

    def orange(self):
        self.label.setText("Оранжевый")
        self.text_edit.setText("#ff7d00")

    def yellow(self):
        self.label.setText("Желтый")
        self.text_edit.setText("#ffff00")

    def green(self):
        self.label.setText("Зеленый")
        self.text_edit.setText("#00ff00")

    def cuan(self):
        self.label.setText("Голубой")
        self.text_edit.setText("#007dff")

    def blue(self):
        self.label.setText("Синий")
        self.text_edit.setText("#0000ff")

    def purple(self):
        self.label.setText("Фиолетовый")
        self.text_edit.setText("#7d00ff")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.vertical_box()
    window.show()
    sys.exit(app.exec_())
