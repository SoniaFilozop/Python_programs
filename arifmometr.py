import sys

# Импортируем из PyQt5.QtWidgets классы для создания приложения и виджет
from PyQt5.QtWidgets import QApplication, QWidget

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber, QTextEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 400, 450, 100)
        self.setWindowTitle('Арифмометр')

        self.btn = QPushButton('+', self)
        self.btn.resize(40, 40)
        self.btn.move(105, 10)
        self.btn1 = QPushButton('-', self)
        self.btn1.resize(40, 40)
        self.btn1.move(145, 10)
        self.btn2 = QPushButton('*', self)
        self.btn2.resize(40, 40)
        self.btn2.move(185, 10)
        self.name_input = QLineEdit(self)
        self.name_input.resize(90, 40)
        self.name_input.move(10, 10)
        self.name2_input = QLineEdit(self)
        self.name2_input.resize(90, 40)
        self.name2_input.move(230, 10)
        self.label = QLabel(self)
        self.label.setText("=")
        self.label.move(320, 20)
        self.plain = QLineEdit(self)
        self.plain.setFrame(False)
        self.plain.setReadOnly(True)
        self.plain.resize(90, 40)
        self.plain.move(330, 10)
        self.btn.clicked.connect(self.count)
        self.btn1.clicked.connect(self.count)
        self.btn2.clicked.connect(self.count)
        # Текст задается также, как и для кнопки

    def count(self):
        name = self.name_input.text()
        name1 = self.name2_input.text()
        oper = self.btn.sender().text()
        if oper == '+':
            self.plain.setText(str(int(name) + int(name1)))
        elif oper == '-':
            self.plain.setText(str(int(name) - int(name1)))
        else:
            self.plain.setText(str(int(name) * int(name1)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
