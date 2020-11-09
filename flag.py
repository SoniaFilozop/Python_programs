import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QRadioButton
from PyQt5.QtCore import Qt


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('flag.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)
        self.radio.buttonClicked.connect(self.run2)
        self.radio2.buttonClicked.connect(self.run2)
        self.radio3.buttonClicked.connect(self.run2)
        self.color = {self.radio: 'синий', self.radio2: 'синий', self.radio3: 'синй'}

        # Обратите внимание: имя элемента такое же как в QTDesigner

    def run(self):
        self.label_4.setText('Цвета: {}, {} и {}'.format(*self.color.values()))
        self.label_4.resize(self.label_4.sizeHint())

    def run2(self, button):
        self.color[self.sender()] = button.text()

        # Имя элемента совпадает с objectName в QTDesigner


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())