import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.morze = {'a': '.-',
                      'b': '-...',
                      'c': '-.-.',
                      'd': '-..',
                      'e': '.',
                      'f': '..-.',
                      'g': '--.',
                      'h': '....',
                      'i': '..',
                      'j': '.---',
                      'k': '-.-',
                      'l': '.-..',
                      'm': '--',
                      'n': '-.',
                      'o': '---',
                      'p': '.--.',
                      'q': '--.-',
                      'r': '.-.',
                      's': '...',
                      't': '-',
                      'u': '..-',
                      'v': '...-',
                      'w': '.--',
                      'x': '-..-',
                      'y': '-.--',
                      'z': '--..'}
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 400, 500, 150)
        self.setWindowTitle('Азбука Морзе')

        n = -1
        b = -1
        for i in self.morze:
            n += 1
            self.btn = QPushButton(i, self)
            self.btn.resize(30, 30)
            if n <= 15:
                self.btn.move(10 + 30 * n, 20)
            else:
                b += 1
                self.btn.move(10 + 30 * b, 50)
            self.btn.clicked.connect(self.count)
        self.name_input = QLineEdit(self)
        self.name_input.move(10, 90)

    def count(self):
        name = self.btn.sender().text()
        self.name_input.setText(self.name_input.text() + self.morze[name])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
