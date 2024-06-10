from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QTextEdit, QVBoxLayout, QHBoxLayout, QWidget, QStackedWidget, QListWidget, QListWidgetItem, QFileDialog, QDialog, QCheckBox
from PyQt5.QtCore import Qt
import sys
import os
import sqlite3
import subprocess
import time

from DataBase.head import create_db, add_command, add_argument, get_logs, read_log

DB_NAME = "commands.db"
LOGS_DIR = "logs"


class LogsPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        layout = QVBoxLayout()

        self.logs_list = QListWidget(self)
        layout.addWidget(self.logs_list)

        self.view_button = QPushButton("Просмотр", self)
        self.view_button.clicked.connect(self.view_log)
        layout.addWidget(self.view_button)

        self.back_button = QPushButton("Назад", self)
        self.back_button.clicked.connect(self.main_window.show_home_page)
        layout.addWidget(self.back_button)

        self.setLayout(layout)
        self.load_logs()

    def load_logs(self):
        logs = get_logs()
        self.logs_list.clear()
        for log in logs:
            self.logs_list.addItem(log)

    def view_log(self):
        selected_log = self.logs_list.currentItem().text()
        log_content = read_log(os.path.join(LOGS_DIR, selected_log))
        log_dialog = LogDialog(log_content)
        log_dialog.exec_()

class LogDialog(QDialog):
    def __init__(self, content):
        super().__init__()
        self.setWindowTitle("Лог")
        self.setGeometry(100, 100, 600, 400)
        layout = QVBoxLayout()
        self.log_text = QTextEdit(self)
        self.log_text.setReadOnly(True)
        self.log_text.setText(content)
        layout.addWidget(self.log_text)
        self.setLayout(layout)
