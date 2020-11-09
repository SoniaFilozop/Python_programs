import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from random import randrange


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle('Кнопка')
        self.btn = QPushButton('Нажми меня', self)
        self.btn.resize(150, 60)
        self.btn.move(180, 220)

    def mouseMoveEvent(self, event):
        if ((event.x() >= self.btn.x() - self.btn.width()) and (event.x() <= self.btn.x() + self.btn.width())) and ((
                event.y() >= self.btn.y() - self.btn.height()) and (event.y() <= self.btn.y() + self.btn.height())):
            u = randrange(500)
            d = randrange(500)
            while (u + self.btn.width() >= 500) or (d + self.btn.height() >= 500):
                u = randrange(500)
                d = randrange(500)
            self.btn.move(u, d)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
