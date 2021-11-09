from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel
from PyQt5.QtCore import QRect, Qt

from PyQt5 import QtGui

from parser import parser

from urllib import request


class NewsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setMouseTracking(True)
        self.grabMouse()

        self.setFixedSize(1500, 1000)
        # self.adjustSize()
        self.setWindowTitle('Purebasket  |  Новости')
        self.setWindowIcon(QtGui.QIcon('img/photo_2021-11-09_02-23-47.jpg'))


        # Название окна.
        self.partition_name = QLabel(self)
        self.partition_name.setText('Новости')
        self.partition_name.move(595, 0)
        self.partition_name.setStyleSheet('''
                font: bold 70px;
        ''')

        # Кнопка выхода из приложения.
        self.btn_exit = QPushButton('Выход', self)
        self.btn_exit.move(1320, 40)
        self.btn_exit.resize(100, 40)

        # Запрашиваем новости с сайта "РИА НОВОСТИ".
        brief_news_text, img, news_text, time_list = parser()

        # Делаем задний фон новостей.
        background_pxmp = QPixmap('img/image.jpeg')
        for i in range(8):
            self.background = QLabel(self)
            if i < 4:
                self.background.move(15, 145 + i * 210)
                self.background.resize(740, 195)
            else:
                self.background.move(765, 145 + (i - 4) * 210)
                self.background.resize(722, 195)
            self.background.setPixmap(background_pxmp)

        # Рисуем "главную" линию в окне.
        self.main_line = QLabel(self)
        line = QPixmap('img/1614261337_1-p-fon-chernii-odnotonnii-1.jpg')

        self.main_line.move(0, 100)
        self.main_line.resize(1500, 20)
        self.main_line.setPixmap(line)

        # Рисуем горизонтальные линии.
        for i in range(16):
            self.lines = QLabel(self)
            if i < 8:
                if i < 4:
                    self.lines.move(15, 145 + 210 * i)
                else:
                    self.lines.move(15, 338 + 210 * (i - 4))
                self.lines.resize(740, 2)

            else:
                if i < 12:
                    self.lines.move(765, 145 + 210 * (i - 8))
                else:
                    self.lines.move(765, 338 + 210 * (i - 12))
                self.lines.resize(722, 2)
            self.lines.setPixmap(line)

        # Рисуем вертикальные линии.
        for i in range(16):
            self.lines = QLabel(self)
            if i < 8:
                if i < 4:
                    self.lines.move(15, 145 + 210 * i)
                else:
                    self.lines.move(755, 145 + 210 * (i - 4))
            else:
                if i < 12:
                    self.lines.move(765, 145 + 210 * (i - 8))
                else:
                    self.lines.move(1487, 145 + 210 * (i - 12))
            self.lines.resize(2, 195)
            self.lines.setPixmap(line)

        # Краткий текст новости.
        for i in range(8):
            self.news = QLabel(f'{brief_news_text[i][0]}', self)
            if i < 4:
                self.news.move(340, 110 + i * 210)
                self.news.resize(410, 180)
            else:
                self.news.move(1090, 110 + (i - 4) * 210)
                self.news.resize(405, 180)
            self.news.setWordWrap(True)
            self.news.setStyleSheet("""
                    font: bold 23px;
            """)

        # Изображение, сопровождающая новость.
        for i in range(8):
            data = request.urlopen(img[i]).read()
            pixmam = QPixmap()
            pixmam.loadFromData(data)

            self.image_news = QLabel(self)
            if i < 4:
                self.image_news.move(20, 150 + 210 * i)
            else:
                self.image_news.move(770, 150 + 210 * (i - 4))
            self.image_news.setPixmap(pixmam.scaled(300, 200, Qt.KeepAspectRatio))
            self.image_news.setStyleSheet('''
                    border: 6px solid black;
                    border-radius: 10px;
            ''')

        # Дата выпуска новости.
        for i in range(8):
            self.time = QLabel(self)
            if i < 4:
                self.time.move(340, 315 + i * 210)
            else:
                self.time.move(1090, 315 + (i - 4) * 210)
            self.time.setText(time_list[i])
            self.time.setStyleSheet("""
                    font: bold 16px;
            """)

        # Состояние новости (просмотрено или нет).
        self.condition_list = []
        for i in range(8):
            self.condition = QLabel(self)
            if i < 4:
                self.condition.move(600, 315 + i * 210)
            else:
                self.condition.move(1350, 315 + (i - 4) * 210)
            self.condition.setText('Просмотрено!')
            self.condition.setStyleSheet("""
                               font: bold 16px;
                       """)
            self.condition_list.append(self.condition)
            self.condition.hide()

        # Полная версия новости.
        self.read_more_about_the_news_list = []
        for i in range(8):
            self.read_more_about_the_news = QLabel(self)
            self.read_more_about_the_news.resize(1000, 900)
            self.read_more_about_the_news.move(250, 90)
            self.read_more_about_the_news.setText(''.join(news_text[i]))
            self.read_more_about_the_news.setStyleSheet('''
                    background-color: white;
                    border: 6px solid black;
                    border-radius: 15px;
                    font: bold 20px;
            ''')
            self.read_more_about_the_news.setWordWrap(True)
            self.read_more_about_the_news.setAlignment(Qt.AlignCenter)
            self.read_more_about_the_news_list.append(self.read_more_about_the_news)
            self.read_more_about_the_news.hide()


    def mousePressEvent(self, event):
        coordinate_exit = QRect(1320, 50, 100, 40)

        if (event.button() == Qt.LeftButton) and event.pos() in coordinate_exit:
            self.close()

    def mouseMoveEvent(self, event):
        self.coordinate_news = []
        self.coordinate_news.append(QRect(20, 150, 300, 200))
        self.coordinate_news.append(QRect(20, 360, 300, 200))
        self.coordinate_news.append(QRect(20, 570, 300, 200))
        self.coordinate_news.append(QRect(20, 780, 300, 200))
        self.coordinate_news.append(QRect(770, 150, 300, 200))
        self.coordinate_news.append(QRect(770, 360, 300, 200))
        self.coordinate_news.append(QRect(770, 570, 300, 200))
        self.coordinate_news.append(QRect(770, 780, 300, 200))

        location_check = False
        for i in range(8):
            if event.pos() in self.coordinate_news[i]:
                location_check = True
                self.condition_list[i].show()
                self.read_more_about_the_news_list[i].show()

        if not location_check:
            for i in range(8):
                self.read_more_about_the_news_list[i].hide()
