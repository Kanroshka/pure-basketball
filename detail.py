import sys
import os
import sqlite3
import subprocess
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QTextEdit, QVBoxLayout, QHBoxLayout, QWidget, QStackedWidget, QListWidget, QListWidgetItem, QFileDialog, QDialog, QCheckBox
from PyQt5.QtCore import Qt

class DetailPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        layout = QVBoxLayout()

        self.label = QLabel("Подробнее о приложении", self)
        self.label.setStyleSheet("font-size: 18px;")
        layout.addWidget(self.label)

        self.description = QLabel("Это приложение позволяет искать команды Linux и составлять сложные запросы из нескольких команд.", self)
        layout.addWidget(self.description)

        self.back_button = QPushButton("Назад", self)
        self.back_button.clicked.connect(self.main_window.show_home_page)
        layout.addWidget(self.back_button)

        self.setLayout(layout)