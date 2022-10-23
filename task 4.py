#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PySide2 import QtWidgets
from PySide2.QtWidgets import QFileDialog, QWidget, QVBoxLayout, QTextEdit, QHBoxLayout, QPushButton, QApplication


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task 4")
        self.setGeometry(100, 100, 100, 100)
        self.text = QTextEdit()
        self.initializeUI()

    def initializeUI(self):
        vbox = QVBoxLayout()
        grid = QHBoxLayout()
        vbox.addLayout(grid)
        btn1 = QPushButton("Save")
        btn1.clicked.connect(self.save)
        btn2 = QPushButton("Open")
        btn2.clicked.connect(self.open)
        grid.addWidget(btn1)
        grid.addWidget(btn2)
        vbox.addWidget(self.text)
        self.setLayout(vbox)

    def save(self):
        filename, _ = QFileDialog.getSaveFileName(
            self,
            'Save File As',
            '',
            "Text Files (*.txt)"
        )
        if filename:
            text = self.text.toPlainText()
            with open(filename, 'w', encoding="utf-8") as f:
                f.write(text)

    def open(self):
        self.text.clear()
        name = QFileDialog.getOpenFileName()
        with open(name[0], 'r', encoding="utf-8") as f:
            data = f.read()
        self.text.setText(str(data))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
