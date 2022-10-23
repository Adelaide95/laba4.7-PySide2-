#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PySide2.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton, QVBoxLayout
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()  # вызываем конструктор базового класса
        self.line_edit1 = QLineEdit(self)
        self.line_edit2 = QLineEdit(self)
        self.button1 = QPushButton('+', self)
        self.button2 = QPushButton('-', self)
        self.button3 = QPushButton('*', self)
        self.button4 = QPushButton('/', self)
        self.label = QLabel(self)
        self.initializeUI()


    def initializeUI(self):
        self.setGeometry(400, 200, 220, 250)
        self.setWindowTitle("Калькулятор")
        vbox = QVBoxLayout()
        vbox.addWidget(self.line_edit1)
        vbox.addWidget(self.line_edit2)
        vbox.addWidget(self.button1)
        vbox.addWidget(self.button2)
        vbox.addWidget(self.button3)
        vbox.addWidget(self.button4)
        vbox.addWidget(self.label)
        self.setLayout(vbox)


        self.button1.clicked.connect(self.Calculator)
        self.button2.clicked.connect(self.Calculator)
        self.button3.clicked.connect(self.Calculator)
        self.button4.clicked.connect(self.Calculator)
        self.show()

    def Calculator(self):
        try:
            if float(self.line_edit1.text()) and float(self.line_edit2.text()):
                n1 = float(self.line_edit1.text())
                n2 = float(self.line_edit2.text())
        except ValueError:
            self.label.setText("Введите числа")

        sender = self.sender()
        if sender.text() == "+":
            self.label.setText(str(n1 + n2))
        elif sender.text() == "-":
            self.label.setText(str(n1 - n2))
        elif sender.text() == "*":
            self.label.setText(str(n1 * n2))
        elif sender.text() == "/":
            self.label.setText(str(n1 / n2))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setObjectName("MainWindow")
    window.setStyleSheet("#MainWindow{background-color:purple}")
    sys.exit(app.exec_())