from PyQt5.QtWidgets import QDialog, QLineEdit, QLabel, QPushButton


class Registration_form(QDialog):
    def __init__(self, *param):
        super().__init__()
        self.setupUI()
        self.show()

    def setupUI(self):
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Регистрация')

        self.login = QLineEdit(self)
        self.label_login = QLabel(self)
        self.login.move(70, 30)
        self.label_login.move(20, 30)
        self.label_login.setText('Логин:')
        self.label_login.resize(50, 20)
        self.login.resize(100, 20)

        self.name = QLineEdit(self)
        self.label_name = QLabel(self)
        self.name.move(70, 60)
        self.label_name.move(30, 60)
        self.label_name.setText('Имя:')
        self.label_name.resize(50, 20)
        self.name.resize(100, 20)

        self.passwd = QLineEdit(self)
        self.label_passwd = QLabel(self)
        self.passwd.move(70, 90)
        self.label_passwd.move(10, 90)
        self.label_passwd.setText('Пароль:')
        self.passwd.setEchoMode(QLineEdit.Password)
        self.label_passwd.resize(60, 20)
        self.passwd.resize(100, 20)

        self.btn_OK = QPushButton(self)
        self.btn_OK.setText('Регистрация:')
        self.btn_OK.move(30, 150)
        self.btn_OK.resize(100, 30)
        self.btn_OK.clicked.connect(self.reject)



