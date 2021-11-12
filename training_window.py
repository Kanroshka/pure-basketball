import os
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from PyQt5.QtCore import Qt, QRect

from PyQt5 import QtGui


class TrainingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setMouseTracking(True)
        self.grabMouse()

        self.setWindowTitle('Purebasket  |  Тренировки')
        self.setFixedSize(1500, 1000)
        self.move(250, 0)
        self.setWindowIcon(QtGui.QIcon('img/photo_2021-11-09_02-23-47.jpg'))

        # Название окна.
        self.partition_name = QLabel(self)
        self.partition_name.setText('Тренировки')
        self.partition_name.move(535, 0)
        self.partition_name.setStyleSheet('''
                font: bold 70px;
        ''')

        # Кнопка выхода из окна 'Тринировки'.
        self.btn_exit = QPushButton('Назад', self)
        self.btn_exit.move(1390, 40)
        self.btn_exit.resize(100, 40)
        self.btn_exit.setStyleSheet('''
                   border: 2px;
                    border-radius: 10px;
                    color: gray;
                    font: bold 20px;
               ''')

        # Начальное окошко с тренировкой.
        background_pxmp = QPixmap('img/image.jpeg')

        self.qwe = QLabel(self)
        self.qwe.move(200, 130)
        self.qwe.resize(1100, 800)
        self.qwe.setPixmap(background_pxmp.scaled(1600, 1600, Qt.KeepAspectRatio))
        self.qwe.setText('Наведите на желаемую тренировку, чтобы посмотреть ее')
        self.qwe.setWordWrap(True)
        self.qwe.setAlignment(Qt.AlignCenter)
        self.qwe.setStyleSheet('''
                color: gray;
                border: 4px solid gray;
                border-radius: 10px;
                font: bold 70px;
        ''')

        # Рисуем "главную" линию в окне.
        self.main_line = QLabel(self)
        line = QPixmap('img/1614261337_1-p-fon-chernii-odnotonnii-1.jpg')

        self.main_line.move(0, 100)
        self.main_line.resize(1500, 10)
        self.main_line.setPixmap(line)

        # Ячейки с тренировками.
        with open(f'TrainingText/title.txt', encoding='utf-8') as f:
            data = f.readlines()

        for i in range(15):
            self.practice_cell = QLabel(self)

            if i < 10:
                if i < 5:
                    self.practice_cell.move(10, 130 + i * 160)
                else:
                    self.practice_cell.move(1310, 130 + (i - 5) * 160)
                self.practice_cell.resize(180, 150)
                self.practice_cell.setAlignment(Qt.AlignCenter)
            else:
                self.practice_cell.move(30 + (i - 10) * 290, 935)
                self.practice_cell.resize(280, 65)
                self.practice_cell.setAlignment(Qt.AlignHCenter)
            self.practice_cell.setStyleSheet('''
                        border: 2px solid black;
                        border-radius: 8;
                        color: black;
                        font: bold 19px;
                    ''')
            self.practice_cell.setWordWrap(True)
            self.practice_cell.setText(f'{data[i]}')

        # Полная версия тренировки.
        self.training_list = []
        for i in range(15):
            with open(f'TrainingText/{i}.txt', encoding='utf-8') as f:
                data = ''.join(f.readlines())

            self.training = QLabel(self)
            self.training.resize(1100, 800)
            self.training.move(200, 130)
            self.training.setText(data)
            self.training.setStyleSheet('''
                     background-color: white;
                     border: 6px solid black;
                     border-radius: 10px;
                     font: bold 15px;
             ''')
            self.training.setWordWrap(True)
            self.training.setAlignment(Qt.AlignHCenter)
            self.training_list.append(self.training)
            self.training.hide()

    def closeEvent(self, e):
        os.execl(sys.executable, sys.executable, *sys.argv)

    def mouseMoveEvent(self, event):
        self.coordinate_training = []
        for i in range(15):
            if i < 10:
                if i < 5:
                    self.coordinate_training.append(QRect(10, 130 + i * 160, 180, 150))
                else:
                    self.coordinate_training.append(QRect(1310, 130 + (i - 5) * 160, 180, 150))
            else:
                self.coordinate_training.append(QRect(30 + (i - 10) * 290, 935, 280, 65))

        location_check = False
        for i in range(15):
            if event.pos() in self.coordinate_training[i]:
                location_check = True
                self.training_list[i].show()

        if not location_check:
            for i in range(15):
                self.training_list[i].hide()

    def mousePressEvent(self, event):
        coordinate_exit = QRect(1390, 40, 100, 40)

        if (event.button() == Qt.LeftButton) and event.pos() in coordinate_exit:
            self.close()
