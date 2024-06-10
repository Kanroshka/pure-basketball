import sys
import os
import sqlite3
import subprocess
import time
# import openai
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QTextEdit, QVBoxLayout, QHBoxLayout, QWidget, QStackedWidget, QListWidget, QListWidgetItem, QFileDialog, QDialog, QCheckBox
from PyQt5.QtCore import Qt

class ChatPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        layout = QVBoxLayout()

        self.question_input = QLineEdit(self)
        layout.addWidget(self.question_input)

        self.ask_button = QPushButton("Спросить", self)
        self.ask_button.clicked.connect(self.ask_chatgpt)
        layout.addWidget(self.ask_button)

        self.answer_text = QTextEdit(self)
        self.answer_text.setReadOnly(True)
        layout.addWidget(self.answer_text)

        self.back_button = QPushButton("Назад", self)
        self.back_button.clicked.connect(self.main_window.show_home_page)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def ask_chatgpt(self):
        question = self.question_input.text()
        response = openai.Completion.create(
            engine="davinci",
            prompt=question,
            max_tokens=150
        )
        answer = response.choices[0].text.strip()
        self.answer_text.setText(answer)
