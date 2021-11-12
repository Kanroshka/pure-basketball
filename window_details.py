import os
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QWidget, QPushButton
from PyQt5.QtCore import Qt, QRect

from PyQt5 import QtGui


class WindowDetails(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setMouseTracking(True)
        self.grabMouse()

        self.setFixedSize(1000, 800)
        self.move(500, 100)
        self.setWindowTitle('Purebasket')
        self.setStyleSheet('''background-color: black;''')
        self.setWindowIcon(QtGui.QIcon('img/photo_2021-11-09_02-23-47.jpg'))


        # Иконка приложения.
        self.pixmap = QPixmap('img/photo_2021-11-09_01-57-58.jpg')
        self.image = QLabel(self)
        self.image.move(280, 50)
        self.image.resize(400, 230)
        self.image.setPixmap(self.pixmap.scaled(400, 230, Qt.KeepAspectRatio))
        self.image.setStyleSheet('''
                    border: 2px  white;
                    border-radius: 10px;''')

        # Текст окна "Подробнее".
        with open('TrainingText/details.txt', encoding='utf-8') as f:
            data = ''.join(f.readlines())
        self.information = QLabel(self)
        self.information.setText(data)
        self.information.resize(595, 500)
        self.information.move(190, 290)
        self.information.setStyleSheet('''
                       color: white;
                       font: bold 18px;
                  ''')
        self.information.setAlignment(Qt.AlignHCenter)
        self.information.setWordWrap(True)

        # Кнопка выхода из окна 'Подробнее'.
        self.btn_exit = QPushButton('Назад', self)
        self.btn_exit.move(450, 700)
        self.btn_exit.resize(100, 40)
        self.btn_exit.setStyleSheet('''
                    border: 2px;
                     border-radius: 10px;
                     color: white;
                     font: bold 20px;
                ''')


    def mousePressEvent(self, event):
        coordinate_exit = QRect(450, 700, 100, 40)

        if (event.button() == Qt.LeftButton) and event.pos() in coordinate_exit:
            self.close()


    def closeEvent(self, e):
        os.execl(sys.executable, sys.executable, *sys.argv)
