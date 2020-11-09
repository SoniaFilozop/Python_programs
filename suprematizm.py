import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPainter, QColor, QPolygon
from random import randint
from PyQt5.QtCore import Qt, QPoint


class Example(QWidget):
    def __init__(self):
        self.colors = ['green', 'red', 'purple', 'blue', 'yellow', 'black']
        self.k = 0
        super().__init__()
        self.setMouseTracking(True)
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle('Координаты')

    def mouseMoveEvent(self, event):
        self.x1 = event.x()
        self.y1 = event.y()

    def mousePressEvent(self, event):
        self.x = event.x()
        self.y = event.y()
        if event.button() == Qt.LeftButton:
            self.k = 1
        elif event.button() == Qt.RightButton:
            self.k = -1
        self.update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.k = 2
            self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawing(qp)
        qp.end()

    def drawing(self, qp):
        if self.k == 1:
            qp.setBrush(QColor(self.colors[randint(0, 5)]))
            m = randint(1, 100)
            qp.drawRect(self.x, self.y, m, m)
            ex.show()

        elif self.k == -1:

            qp.setBrush(QColor(self.colors[randint(0, 5)]))
            a = randint(1, 100)
            qp.drawEllipse(self.x, self.y, a, a)

        elif self.k == 2:
            qp.setBrush(QColor(self.colors[randint(0, 5)]))
            points = QPolygon([QPoint(self.x1,
                                      self.y1 - self.y1 // 2),
                               QPoint((self.x1 + self.x1 // 2), (self.y1 + self.y1 // 2)),
                               QPoint((self.x1 - self.x1 // 2), (self.y1 + self.y1 // 2))])
            qp.drawPolygon(points)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
