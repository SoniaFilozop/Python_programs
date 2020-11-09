import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Nim.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.run1)

    def run(self):
        kolvo = self.spinBox.value()
        self.lcdNumber.display(kolvo)

    def run1(self):
        vsat = int(self.lineEdit.text())
        m = 0
        if vsat <= 3 and vsat <= self.lcdNumber.value():
            self.lcdNumber.display(int(self.lcdNumber.value()) - vsat)
            self.listWidget.addItem('Игрок взял - ' + str(vsat))
            if self.lcdNumber.value() != 0:
                m += 1
                comp = randint(1, 3)
                while comp > self.lcdNumber.value():
                    comp = randint(1, 3)
                self.lcdNumber.display(self.lcdNumber.value() - comp)
                self.listWidget.addItem('Компьютер взял - ' + str(comp))
            if self.lcdNumber.value() == 0:
                if m == 1:
                    self.label_3.setText('Компьютер выиграл!')
                else:
                    self.label_3.setText('Игрок выиграл!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
