import sys
import os
import sqlite3
import subprocess
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QTextEdit, QVBoxLayout, QHBoxLayout, QWidget, QStackedWidget, QListWidget, QListWidgetItem, QFileDialog, QDialog, QCheckBox
from PyQt5.QtCore import Qt

from DataBase.head import create_db, add_command, add_argument, get_logs
from home import HomePage
from detail import DetailPage
from constr import ConstructorPage
from lgs import LogsPage
from gpt import ChatPage
from DataBase.commands_data import commands_data, arguments_data

create_db()



for name, description in commands_data:
    add_command(name, description)

for command_name, argument, description in arguments_data:
    add_argument(command_name, argument, description)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Linux Tools")
        self.setGeometry(100, 100, 800, 600)

        # Стек для страниц
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Страницы
        self.home_page = HomePage(self)
        self.detail_page = DetailPage(self)
        self.constructor_page = ConstructorPage(self)
        self.logs_page = LogsPage(self)
        self.chat_page = ChatPage(self)

        # Добавление страниц в стек
        self.stacked_widget.addWidget(self.home_page)
        self.stacked_widget.addWidget(self.detail_page)
        self.stacked_widget.addWidget(self.constructor_page)
        self.stacked_widget.addWidget(self.logs_page)
        self.stacked_widget.addWidget(self.chat_page)

        # Переход на начальную страницу
        self.show_home_page()

    def show_home_page(self):
        self.stacked_widget.setCurrentWidget(self.home_page)

    def show_detail_page(self):
        self.stacked_widget.setCurrentWidget(self.detail_page)

    def show_constructor_page(self):
        self.stacked_widget.setCurrentWidget(self.constructor_page)

    def show_logs_page(self):
        self.stacked_widget.setCurrentWidget(self.logs_page)
        self.logs_page.load_logs()

    def show_chat_page(self):
        self.stacked_widget.setCurrentWidget(self.chat_page)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
