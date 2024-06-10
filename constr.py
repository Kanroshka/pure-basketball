import sys
import os
import sqlite3
import subprocess
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QTextEdit, QVBoxLayout, QHBoxLayout, QWidget, QStackedWidget, QListWidget, QListWidgetItem, QFileDialog, QDialog, QCheckBox
from PyQt5.QtCore import Qt
from DataBase.head import search_commands, get_arguments, log_command
class ConstructorPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        layout = QVBoxLayout()

        # Верхняя панель с кнопкой Назад и выбором директории
        top_layout = QHBoxLayout()
        
        self.back_button = QPushButton("Назад", self)
        self.back_button.clicked.connect(self.main_window.show_home_page)
        top_layout.addWidget(self.back_button)
        
        self.directory_input = QLineEdit(self)
        self.directory_input.setPlaceholderText("Рабочая директория")
        top_layout.addWidget(self.directory_input)

        self.browse_button = QPushButton("Выбрать", self)
        self.browse_button.clicked.connect(self.browse_directory)
        top_layout.addWidget(self.browse_button)

        layout.addLayout(top_layout)

        # Панель поиска и результатов
        search_layout = QHBoxLayout()

        self.search_input = QLineEdit(self)
        search_layout.addWidget(self.search_input)

        self.search_button = QPushButton("Поиск", self)
        self.search_button.clicked.connect(self.search_commands)
        search_layout.addWidget(self.search_button)

        layout.addLayout(search_layout)

        # Панель с результатами поиска команд и описанием команды
        result_layout = QHBoxLayout()

        self.results_list = QListWidget(self)
        self.results_list.setFixedWidth(200)
        result_layout.addWidget(self.results_list)

        self.command_description = QLabel("", self)
        self.command_description.setWordWrap(True)
        result_layout.addWidget(self.command_description)

        layout.addLayout(result_layout)

        # Панель для выбранных команд
        self.chain_input = QTextEdit(self)
        self.chain_input.setFixedHeight(100)
        layout.addWidget(self.chain_input)

        # Панель для аргументов и кнопки добавления команды
        args_layout = QVBoxLayout()

        self.arguments_layout = QVBoxLayout()
        args_layout.addLayout(self.arguments_layout)

        self.add_button = QPushButton("Добавить", self)
        self.add_button.clicked.connect(self.add_command_to_chain)
        args_layout.addWidget(self.add_button)

        layout.addLayout(args_layout)

        # Кнопка для выполнения команд
        self.run_button = QPushButton("Продолжить", self)
        self.run_button.clicked.connect(self.run_commands)
        layout.addWidget(self.run_button)

        self.setLayout(layout)

    def search_commands(self):
        keyword = self.search_input.text()
        results = search_commands(keyword)
        self.results_list.clear()
        for name, description in results:
            item = QListWidgetItem(name)
            item.setToolTip(description)
            self.results_list.addItem(item)

        if results:
            self.results_list.itemClicked.connect(self.display_command_description)

    def display_command_description(self, item):
        command = item.text()
        description = item.toolTip()
        self.command_description.setText(description)
        self.command_input = QLineEdit(command)
        arguments = get_arguments(command)
        
        # Очистка предыдущих аргументов
        for i in reversed(range(self.arguments_layout.count())): 
            self.arguments_layout.itemAt(i).widget().setParent(None)

        self.checkboxes = []
        for arg, desc in arguments:
            arg_layout = QHBoxLayout()
            checkbox = QCheckBox(arg, self)
            arg_layout.addWidget(checkbox, 0, Qt.AlignLeft)
            arg_label = QLabel(desc, self)
            arg_layout.addWidget(arg_label, 0, Qt.AlignLeft)
            self.arguments_layout.addLayout(arg_layout)
            self.checkboxes.append(checkbox)

    def add_command_to_chain(self):
        command = self.command_input.text()
        selected_args = [cb.text() for cb in self.checkboxes if cb.isChecked()]
        argument_string = ' '.join(selected_args)
        self.chain_input.append(f"{command} {argument_string}")

    def browse_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Выбрать директорию")
        if directory:
            self.directory_input.setText(directory)

    def run_commands(self):
        commands_chain = self.chain_input.toPlainText().strip().split('\n')
        directory = self.directory_input.text()
        bash_file_path = os.path.join(directory, "commands.sh")

        with open(bash_file_path, 'w') as bash_file:
            for command in commands_chain:
                bash_file.write(command + '\n')

        os.chmod(bash_file_path, 0o755)

        try:
            result = subprocess.run(bash_file_path, shell=True, cwd=directory, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output = result.stdout if result.stdout else result.stderr
        except Exception as e:
            output = str(e)

        result_dialog = ResultDialog(output)
        result_dialog.exec_()

        log_command("\n".join(commands_chain), output)
        self.main_window.show_logs_page()


class ResultDialog(QDialog):
    def __init__(self, content):
        super().__init__()
        self.setWindowTitle("Результат выполнения команды")
        self.setGeometry(100, 100, 600, 400)
        layout = QVBoxLayout()
        self.result_text = QTextEdit(self)
        self.result_text.setReadOnly(True)
        self.result_text.setText(content)
        layout.addWidget(self.result_text)
        self.setLayout(layout)
