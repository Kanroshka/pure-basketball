from db_work import *

from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt

from PyQt5 import QtGui


class RegistrationForm(QDialog):
    def __init__(self, *param):
        super().__init__()
        self.setupUI()
        self.releaseMouse()
        self.setMouseTracking(False)
        self.show()

    def setupUI(self):
        self.move(750, 350)
        self.setFixedSize(283, 190)
        self.setWindowTitle('Вход')
        self.setWindowIcon(QtGui.QIcon('img/photo_2021-11-09_02-23-47.jpg'))

        self.login = QLineEdit(self)
        self.login.move(7, 7)
        self.login.setPlaceholderText("Login..")
        self.login.resize(269, 40)

        self.passwd = QLineEdit(self)
        self.passwd.move(7, 54)
        self.passwd.resize(269, 40)
        self.passwd.setEchoMode(QLineEdit.Password)
        self.passwd.setPlaceholderText("Password..")

        self.passwd_and_login = [self.passwd, self.login]

        self.btn_reg = QPushButton(self)
        self.btn_reg.setText('Зарегистрироваться')
        self.btn_reg.move(7, 101)
        self.btn_reg.resize(269, 40)
        self.btn_reg.clicked.connect(self.reg)

        self.btn_auth = QPushButton(self)
        self.btn_auth.setText('Войти')
        self.btn_auth.move(7, 148)
        self.btn_auth.resize(269, 40)
        self.btn_auth.clicked.connect(self.auth)

        self.msg = QLabel(self)
        self.msg.setText('Вы успешно зарегистрированы!')
        self.msg.move(20, 80)
        self.msg.resize(244, 80)
        self.msg.setAlignment(Qt.AlignHCenter)
        self.msg.setStyleSheet('''
                background-color: white;
                border: 1px solid gray;
                
        ''')
        self.msg.hide()

        self.msg_er = QLabel(self)
        self.msg_er.setText('Проверьте введенные данные!')
        self.msg_er.move(20, 80)
        self.msg_er.resize(244, 80)
        self.msg_er.setAlignment(Qt.AlignHCenter)
        self.msg_er.setStyleSheet('''
                background-color: white;
                border: 1px solid gray;

        ''')
        self.msg_er.hide()

        self.btn_ex = QPushButton(self)
        self.btn_ex.setText('OK')
        self.btn_ex.move(124, 110)
        self.btn_ex.resize(40, 40)
        self.btn_ex.clicked.connect(self.accept)
        self.btn_ex.hide()

        self.btn_ex_msg = QPushButton(self)
        self.btn_ex_msg.setText('Повторить')
        self.btn_ex_msg.move(50, 110)
        self.btn_ex_msg.resize(200, 40)
        self.btn_ex_msg.clicked.connect(self.cls_msg)
        self.btn_ex_msg.hide()

    def check_input(self):
        for data in self.passwd_and_login:
            if len(data.text()) == 0:
                print(len(data.text()))
                return False
        return True

    def auth(self):
        chek = self.check_input()
        if not chek:
            self.msg_er.show()
            self.btn_ex_msg.show()

        else:
            login = self.login.text()
            passwd = self.passwd.text()
            check = check_auth(login, passwd)
            if check:
                self.accept()
            else:
                self.msg_er.show()
                self.btn_ex_msg.show()

    def reg(self):
        chek = self.check_input()
        if not chek:
            self.msg_er.show()
            self.btn_ex_msg.show()

        else:
            login = self.login.text()
            passwd = self.passwd.text()
            check = register(login, passwd)
            if check:
                self.msg.show()
                self.btn_ex.show()
            else:
                self.msg_er.setText('Такой пользователь уже есть!')
                self.msg_er.show()
                self.btn_ex_msg.show()

    def cls_msg(self):
        self.msg_er.setText('Проверьте введенные данные!')
        self.msg_er.hide()
        self.btn_ex_msg.hide()



