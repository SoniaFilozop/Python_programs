import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('text_redactor.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.run2)
        self.pushButton_3.clicked.connect(self.run1)

    def run(self):
        self.file = open(self.lineEdit.text(), "w")
        self.file.write(self.textEdit.toPlainText())
        self.file.close()

    def run1(self):
        self.file = open(self.lineEdit.text(), "w")
        self.file.write(self.textEdit.toPlainText())
        self.file.close()

    def run2(self):
        self.file = open(self.lineEdit.text(), "rt")
        self.textEdit.setText(self.file.read())
        self.file.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
