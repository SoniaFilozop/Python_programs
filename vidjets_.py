import sys

# Импортируем из PyQt5.QtWidgets классы для создания приложения и виджет
from PyQt5.QtWidgets import QApplication, QWidget

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QCheckBox
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 400, 450, 200)
        self.setWindowTitle('Арифмометр')

        self.box = QCheckBox('edit 1', self)
        self.box.toggle()
        self.box.move(20, 20)
        self.box2 = QCheckBox('edit 2', self)
        self.box2.toggle() 
        self.box2.move(20, 60)
        self.box3 = QCheckBox('edit 3', self)
        self.box3.toggle()
        self.box3.move(20, 100)
        self.box4 = QCheckBox('edit 4', self)
        self.box4.toggle()
        self.box4.move(20, 140)
        self.name_input = QLineEdit(self)
        self.name_input.move(100, 20)
        self.name_input.setText('Поле edit1')
        self.name2_input = QLineEdit(self)
        self.name2_input.move(100, 60)
        self.name2_input.setText('Поле edit2')
        self.name3_input = QLineEdit(self)
        self.name3_input.move(100, 100)
        self.name3_input.setText('Поле edit3')
        self.name4_input = QLineEdit(self)
        self.name4_input.move(100, 140)
        self.name4_input.setText('Поле edit4')
        self.box.stateChanged.connect(self.count)
        self.box2.stateChanged.connect(self.count)
        self.box3.stateChanged.connect(self.count)
        self.box4.stateChanged.connect(self.count)

        # Текст задается также, как и для кнопки

    def count(self, state):
        if self.box.sender() == self.box:
            if state == Qt.Checked:
                self.name_input.show()
            else:
                self.name_input.hide()
        elif self.box2.sender() == self.box2:
            if state == Qt.Checked:
                self.name2_input.show()
            else:
                self.name2_input.hide()
        elif self.box3.sender() == self.box3:
            if state == Qt.Checked:
                self.name3_input.show()
            else:
                self.name3_input.hide()
        else:
            if state == Qt.Checked:
                self.name4_input.show()
            else:
                self.name4_input.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
