import os
import sys

from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QDialog
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtGui

from news_window import NewsWindow
from registration_form import RegistrationForm
from training_window import TrainingWindow
from window_details import WindowDetails


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(1000, 800)
        self.move(500, 100)
        self.setWindowTitle('Purebasket')

        # Иконка приложения.
        self.pixmap = QPixmap('img/photo_2021-11-09_01-57-58.jpg')
        self.image = QLabel(self)
        self.image.move(280, 50)
        self.image.resize(400, 230)
        self.image.setPixmap(self.pixmap.scaled(400, 230, Qt.KeepAspectRatio))
        self.image.setStyleSheet('''
                    border: 2px  white;
                    border-radius: 10px;''')

        # Кнопка переключение на тренировку.
        self.btn_training = QPushButton('Тренировка', self)
        self.btn_training.move(425, 550)
        self.btn_training.resize(150, 150)
        self.btn_training.setStyleSheet('''
                   border: 2px solid white;
                    border-radius: 10px;
                    background-color: black;
                    color: white;
                    font: bold 20px;
               ''')

        # Информация о кнопке "Тренировка".
        self.training_information = QLabel(self)
        self.training_information.setText('***') #Дописать!
        self.training_information.resize(410, 200)
        self.training_information.move(260, 270)
        self.training_information.setStyleSheet('''
                    color: white;
                    font: bold 15px;
               ''')
        self.training_information.setWordWrap(True)
        self.training_information.hide()

        # Кнопка переключение на новости
        self.btn_news = QPushButton('Новости', self)
        self.btn_news.move(210, 550)
        self.btn_news.resize(150, 150)
        self.btn_news.setStyleSheet('''
                    border: 2px solid white;
                    border-radius: 10px;
                    background-color: black;
                    color: white;
                    font: bold 20px;
               ''')

        # Информация о кнопке "Новости".
        self.news_information = QLabel(self)
        self.news_information.setText('***') #Дописать!
        self.news_information.resize(410, 200)
        self.news_information.move(260, 270)
        self.news_information.setWordWrap(True)
        self.news_information.setStyleSheet('''
                    color: white;
                    font: bold 15px;
               ''')
        self.news_information.hide()

        # Кнопка переключение на подробности.
        self.btn_more = QPushButton('Подробнее', self)
        self.btn_more.move(640, 550)
        self.btn_more.resize(150, 150)
        self.btn_more.setStyleSheet('''
                   border: 2px solid white;
                    border-radius: 10px;
                    background-color: black;
                    color: white;
                    font: bold 20px;
               ''')

        # Информация о кнопке "Подробнее".
        self.more_information = QLabel(self)
        self.more_information.setText('***') #Дописать!
        self.more_information.resize(410, 200)
        self.more_information.move(260, 270)
        self.more_information.setWordWrap(True)
        self.more_information.setStyleSheet('''
                    color: white;
                    font: bold 15px;
               ''')
        self.more_information.hide()

        # Окно ожидание.
        self.qwe = QLabel(self)
        self.qwe.setText('Привет! В дан dassasasdasdasdasdaasdasdsadad') #Дописать!
        self.qwe.resize(410, 200)
        self.qwe.move(10, 370)
        self.qwe.hide()

        self.setMouseTracking(True)
        self.grabMouse()

    def mouseMoveEvent(self, event):
        self.training_coordinates = QRect(425, 550, 150, 150)
        self.news_coordinates = QRect(210, 550, 150, 150)
        self.more_coordinates = QRect(640, 550, 150, 150)

        if event.pos() in self.training_coordinates:
            self.news_information.hide()
            self.more_information.hide()
            self.training_information.show()
        elif event.pos() in self.news_coordinates:
            self.training_information.hide()
            self.more_information.hide()
            self.news_information.show()
        elif event.pos() in self.more_coordinates:
            self.training_information.hide()
            self.news_information.hide()
            self.more_information.show()
        else:
            self.training_information.hide()
            self.news_information.hide()
            self.more_information.hide()

    def mousePressEvent(self, event):
        if (event.button() == Qt.LeftButton) and event.pos() in self.news_coordinates:
            try:
                self.news_window = NewsWindow()
            except:
                os.execl(sys.executable, sys.executable, *sys.argv)
            self.close()

        elif (event.button() == Qt.LeftButton) and event.pos() in self.training_coordinates:
            self.register()

        elif (event.button() == Qt.LeftButton) and event.pos() in self.more_coordinates:
            self.close()
            self.window_details = WindowDetails()

    def register(self):
        reg_form = RegistrationForm()
        result = reg_form.exec()
        if result == QDialog.Accepted:
            self.close()
            self.training_window = TrainingWindow()
        else:
            os.execl(sys.executable, sys.executable, *sys.argv)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    ex.setObjectName("Menu")
    # Установить фон главного меню.
    ex.setStyleSheet('''background-color: black;''')
    # Установить иконку приложения.
    ex.setWindowIcon(QtGui.QIcon('img/photo_2021-11-09_02-23-47.jpg'))
    sys.excepthook = except_hook
    sys.exit(app.exec())
