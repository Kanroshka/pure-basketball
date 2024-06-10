import sys
import os
import sqlite3
import subprocess
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QTextEdit, QVBoxLayout, QHBoxLayout, QWidget, QStackedWidget, QListWidget, QListWidgetItem, QFileDialog, QDialog, QCheckBox
from PyQt5.QtCore import Qt

from DataBase.head import create_db, add_command, add_argument, get_logs
 
class HomePage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        layout = QVBoxLayout()

        self.label = QLabel("Linux Tools", self)
        self.label.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(self.label)

        self.detail_button = QPushButton("Подробнее", self)
        self.detail_button.clicked.connect(self.main_window.show_detail_page)
        layout.addWidget(self.detail_button)

        self.constructor_button = QPushButton("Конструктор", self)
        self.constructor_button.clicked.connect(self.main_window.show_constructor_page)
        layout.addWidget(self.constructor_button)

        self.logs_button = QPushButton("Логи", self)
        self.logs_button.clicked.connect(self.main_window.show_logs_page)
        layout.addWidget(self.logs_button)

        self.chat_button = QPushButton("Задать вопрос в ChatGPT", self)
        self.chat_button.clicked.connect(self.main_window.show_chat_page)
        layout.addWidget(self.chat_button)

        self.setLayout(layout)
