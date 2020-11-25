import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QDialog, QLineEdit, QFormLayout, QDialogButtonBox
from PyQt5.QtWidgets import QColorDialog, QVBoxLayout, QApplication, QWidget, QTableWidgetItem
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from random import randint
import sqlite3

all_stones = 0
id1 = 0
color = 'white'
choise_number = 0


class LoginDialog(QDialog):  # Создание формы для регистрации пользователя
    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)

        self.username = QLineEdit()
        self.con = sqlite3.connect('Nim.db')
        loginLayout = QFormLayout()
        loginLayout.addRow("Имя игрока", self.username)

        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttons.accepted.connect(self.check)
        self.buttons.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addLayout(loginLayout)
        layout.addWidget(self.buttons)
        self.setLayout(layout)

    def check(self):  # Добавление пользователя в базу данных игроков для составления рейтинга
        global id1
        if self.username:
            cursor = self.con.cursor()
            result = cursor.execute("""SELECT id FROM Gamers
                WHERE Имя = ?""", (self.username.text(),)).fetchall()
            for elem in result:
                id1 = list(elem)[0]
            if not id1:
                sql = "INSERT INTO Gamers (Имя) VALUES (?)"
                val = self.username.text()
                cursor.execute(sql, (val,))
                self.con.commit()
                self.con = sqlite3.connect('Nim.db')
                cur = self.con.cursor()
                sql = "SELECT id FROM Gamers WHERE Имя = ?"
                id2 = cur.execute(sql, (self.username.text(),)).fetchall()
                for elem in id2:
                    id1 = list(elem)[0]
                self.con.close()
            self.accept()


class Rules(QMainWindow):  # Окно с правилами игры
    def __init__(self):
        QWidget.__init__(self)
        uic.loadUi('rules.ui', self)
        self.setWindowTitle('Правила игры')


class Instruction(QMainWindow):  # Окно с инструкцией к игре
    def __init__(self):
        QWidget.__init__(self)
        uic.loadUi('instruction.ui', self)
        self.setWindowTitle('Инструкция')


class UpdateResult(QMainWindow):  # Окно с таблицой рейтинга
    def __init__(self):
        QWidget.__init__(self)
        uic.loadUi('top.ui', self)
        self.setWindowTitle('Рейтинг')
        self.con = sqlite3.connect("Nim.db")

    def show_result(self):  # Добавление данных в таблицу из базы данных
        cur = self.con.cursor()
        result = cur.execute("SELECT Имя, Победы_компьютера, Победы_игрока, Процент_побед FROM Gamers").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        result = sorted(list(result), reverse=True, key=lambda x: int(list(x)[3][:len(list(x)[3]) - 1]))
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.show()


class MyWidget(QMainWindow):  # Основное окно игры
    def __init__(self):
        self.k = 0
        self.x = 0
        self.y = 0
        self.x1 = 0
        self.y1 = 0
        self.move = 0
        super().__init__()
        self.initUi()

    def initUi(self):
        uic.loadUi('project_3.ui', self)
        self.setWindowTitle('Игра Баше')
        self.con = sqlite3.connect('Nim.db')
        self.do_paint = False
        self.rules = Rules()
        self.result = UpdateResult()
        self.instruction = Instruction()
        self.pushButton.clicked.connect(self.color_changes)
        self.pushButton_2.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.paint)
        self.pushButton_3.clicked.connect(self.ShowRules)
        self.pushButton_4.clicked.connect(self.result.show_result)
        self.pushButton_5.clicked.connect(self.instruction.show)

    def run(self):  # Определение количества камней и порядка хода
        global all_stones
        count = self.spinBox.value()
        self.label_3.setText(str(count))
        all_stones = int(self.label_3.text())
        if all_stones >= 20:
            self.k = 1
        elif (all_stones >= 3) and (all_stones < 20):
            self.k = 2
        elif all_stones < 3:
            self.k = 3
        if self.comboBox.currentText() == 'Второй':
            self.label_8.setText('Ход компьютера')
            if all_stones == 1:
                n = 0
                if int(self.label_3.text()) != 0:
                    n += 1
                    comp = 1
                    self.rename(comp)
                    self.listWidget.addItem('Компьютер взял - ' + str(comp))
                    self.winner_comp()
            elif all_stones == 2:
                n = 0
                if int(self.label_3.text()) != 0:
                    n += 1
                    comp = randint(1, 2)
                    while comp > int(self.label_3.text()):
                        comp = randint(1, 2)
                    self.rename(comp)
                    self.listWidget.addItem('Компьютер взял - ' + str(comp))
                    if int(self.label_3.text()) == 0:
                        self.winner_comp()
            elif all_stones < 20:
                n = 0
                if int(self.label_3.text()) != 0:
                    n += 1
                    comp = randint(1, 3)
                    while comp > int(self.label_3.text()):
                        comp = randint(1, 3)
                    self.rename(comp)
                    self.listWidget.addItem('Компьютер взял - ' + str(comp))
                    if int(self.label_3.text()) == 0:
                        self.winner_comp()
            elif all_stones >= 20:
                n = 0
                if int(self.label_3.text()) != 0:
                    n += 1
                    comp = randint(1, 5)
                    while comp > int(self.label_3.text()):
                        comp = randint(1, 5)
                    self.rename(comp)
                    self.listWidget.addItem('Компьютер взял - ' + str(comp))
        self.label_8.setText('Ваш ход')

    def rename(self, comp):  # Изменение количества камней
        self.label_3.setText(str(int(self.label_3.text()) - comp))

    def ShowRules(self):  # Показать правила
        self.rules.show()

    def color_changes(self):  # Изменение цвета камней
        global color
        color1 = QColorDialog.getColor()
        if color1.isValid():
            color = color1.name()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.drawing(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def drawing(self, qp):  # Рисование камней
        global all_stones
        global color
        a = 0
        if self.k == 1:  # Если общее количество камней 20 или больше
            for i in range(5):
                qp.setBrush(QColor(color))
                qp.drawEllipse(80 + a, 360, 80, 80)
                a += 120
        elif self.k == 2:  # Если общее количество камней меньше 20 и больше или равно 3
            for i in range(3):
                qp.setBrush(QColor(color))
                qp.drawEllipse(80 + a, 360, 80, 80)
                a += 120
        elif self.k == 3:  # Если общее количество камней меньше 3
            for i in range(all_stones):
                qp.setBrush(QColor(color))
                qp.drawEllipse(80 + a, 360, 80, 80)
                a += 120
        if a != 0:
            self.label_5.setText('Сколько камней взять?')

    def choice(self):  # Выбор количества забираемых игроком камней
        global all_stones
        global choise_number
        if all_stones == 1:
            if (93 <= self.x <= 147 and 360 <= self.y <= 440) or (80 <= self.x <= 160 and 373 <= self.y <= 427):
                choise_number = 1
                if self.comboBox.currentText() == 'Первый':
                    self.play_i()
                else:
                    self.play_c()
        if all_stones == 2:
            if (93 <= self.x <= 147 and 360 <= self.y <= 440) or (80 <= self.x <= 160 and 373 <= self.y <= 427):
                choise_number = 1
                if self.comboBox.currentText() == 'Первый':
                    self.play_i()
                else:
                    self.play_c()
            elif (93 + 120 <= self.x <= 147 + 120 and 360 <= self.y <= 410 + 30) or (
                    80 + 120 <= self.x <= 160 + 120 and 343 + 30 <= self.y <= 397 + 30):
                choise_number = 2
                if self.comboBox.currentText() == 'Первый':
                    self.play_i()
                else:
                    self.play_c()
        elif all_stones < 20:
            if (93 <= self.x <= 147 and 330 + 30 <= self.y <= 410 + 30) or (
                    80 <= self.x <= 160 and 343 + 30 <= self.y <= 397 + 30):
                choise_number = 1
                if self.comboBox.currentText() == 'Первый':
                    self.play_i()
                else:
                    self.play_c()
            elif (93 + 120 <= self.x <= 147 + 120 and 330 + 30 <= self.y <= 410 + 30) or (
                    80 + 120 <= self.x <= 160 + 120 and 343 + 30 <= self.y <= 397 + 30):
                choise_number = 2
                if self.comboBox.currentText() == 'Первый':
                    self.play_i()
                else:
                    self.play_c()
            elif (93 + 240 <= self.x <= 147 + 240 and 330 + 30 <= self.y <= 410 + 30) or (
                    80 + 240 <= self.x <= 160 + 240 and 343 + 30 <= self.y <= 397 + 30):
                choise_number = 3
                if self.comboBox.currentText() == 'Первый':
                    self.play_i()
                else:
                    self.play_c()
        elif all_stones >= 20:
            if (93 <= self.x <= 147 and 330 + 30 <= self.y <= 410 + 30) or (
                    80 <= self.x <= 160 and 343 + 30 <= self.y <= 397 + 30):
                choise_number = 1
                if self.comboBox.currentText() == 'Первый':
                    self.play_i()
                else:
                    self.play_c()
            elif (93 + 120 <= self.x <= 147 + 120 and 330 + 30 <= self.y <= 410 + 30) or (
                    80 + 120 <= self.x <= 160 + 120 and 343 + 30 <= self.y <= 397 + 30):
                choise_number = 2
                if self.comboBox.currentText() == 'Первый':
                    self.play_i()
                else:
                    self.play_c()
            elif (93 + 240 <= self.x <= 147 + 240 and 330 + 30 <= self.y <= 410 + 30) or (
                    80 + 240 <= self.x <= 160 + 240 and 343 + 30 <= self.y <= 397 + 30):
                choise_number = 3
                if self.comboBox.currentText() == 'Первый':
                    self.play_i()
                else:
                    self.play_c()
            elif (93 + 360 <= self.x <= 147 + 360 and 330 + 30 <= self.y <= 410 + 30) or (
                    80 + 360 <= self.x <= 160 + 360 and 343 + 30 <= self.y <= 397 + 30):
                choise_number = 4
                if self.comboBox.currentText() == 'Первый':
                    self.play_i()
                else:
                    self.play_c()
            elif (93 + 480 <= self.x <= 147 + 480 and 330 + 30 <= self.y <= 410 + 30) or (
                    80 + 480 <= self.x <= 160 + 480 and 343 + 30 <= self.y <= 397 + 30):
                choise_number = 5
                if self.comboBox.currentText() == 'Первый':
                    self.play_i()
                else:
                    self.play_c()

    def play_i(self):  # Если игрок ходит первым
        global all_stones
        global choise_number
        n = 0
        if 3 <= all_stones < 20:
            if choise_number <= 3 and choise_number <= int(self.label_3.text()):
                self.rename(choise_number)
                self.listWidget.addItem('Игрок взял - ' + str(choise_number))
                if int(self.label_3.text()) != 0:
                    self.label_8.setText('Ход компьютера')
                    n += 1
                    comp = randint(1, 3)
                    while comp > int(self.label_3.text()):
                        comp = randint(1, 3)
                    self.rename(comp)
                    self.listWidget.addItem('Компьютер взял - ' + str(comp))
                if int(self.label_3.text()) == 0:
                    if n == 1:
                        self.winner_comp()
                    else:
                        self.winner_i()
                else:
                    self.label_8.setText('Ваш ход')
        elif all_stones >= 20:
            if choise_number <= 5 and choise_number <= int(self.label_3.text()):
                self.rename(choise_number)
                self.listWidget.addItem('Игрок взял - ' + str(choise_number))
                if int(self.label_3.text()) != 0:
                    self.label_8.setText('Ход компьютера')
                    n += 1
                    comp = randint(1, 5)
                    while comp > int(self.label_3.text()):
                        comp = randint(1, 5)
                    self.rename(comp)
                    self.listWidget.addItem('Компьютер взял - ' + str(comp))
                if int(self.label_3.text()) == 0:
                    if n == 1:
                        self.winner_comp()
                    else:
                        self.winner_i()
                else:
                    self.label_8.setText('Ваш ход')
        elif all_stones == 2:
            if choise_number <= all_stones and choise_number <= int(self.label_3.text()):
                self.rename(choise_number)
                self.listWidget.addItem('Игрок взял - ' + str(choise_number))
                if int(self.label_3.text()) != 0:
                    self.label_8.setText('Ход компьютера')
                    n += 1
                    comp = randint(1, 3)
                    while comp > int(self.label_3.text()):
                        comp = randint(1, 2)
                    self.rename(comp)
                    self.listWidget.addItem('Компьютер взял - ' + str(comp))
                if int(self.label_3.text()) == 0:
                    if n == 1:
                        self.winner_comp()
                    else:
                        self.winner_i()
                else:
                    self.label_8.setText('Ваш ход')
        elif all_stones == 1:
            if choise_number <= all_stones and choise_number <= int(self.label_3.text()):
                self.rename(choise_number)
                self.listWidget.addItem('Игрок взял - ' + str(choise_number))
                if int(self.label_3.text()) != 0:
                    self.label_8.setText('Ход компьютера')
                    n += 1
                    comp = 1
                    self.rename(comp)
                    self.listWidget.addItem('Компьютер взял - ' + str(comp))
                if int(self.label_3.text()) == 0:
                    if n == 1:
                        self.winner_comp()
                    else:
                        self.winner_i()
                else:
                    self.label_8.setText('Ваш ход')

    def play_c(self):  # Если игрок ходит вторым
        global all_stones
        global choise_number
        n = 0
        if 3 <= all_stones < 20:
            if int(self.label_3.text()) != 0:
                self.label_8.setText('Ваш ход')
                if choise_number <= 3 and choise_number <= int(self.label_3.text()):
                    self.rename(choise_number)
                    self.listWidget.addItem('Игрок взял - ' + str(choise_number))
                    if int(self.label_3.text()) != 0:
                        self.label_8.setText('Ход компьютера')
                        n += 1
                        comp = randint(1, 3)
                        while comp > int(self.label_3.text()):
                            comp = randint(1, 3)
                        self.rename(comp)
                        self.listWidget.addItem('Компьютер взял - ' + str(comp))
                if int(self.label_3.text()) == 0:
                    if n == 1:
                        self.winner_comp()
                    else:
                        self.winner_i()
                else:
                    self.label_8.setText('Ваш ход')
        elif all_stones >= 20:
            if int(self.label_3.text()) != 0:
                self.label_8.setText('Ваш ход')
                if choise_number <= 3 and choise_number <= int(self.label_3.text()):
                    self.rename(choise_number)
                    self.listWidget.addItem('Игрок взял - ' + str(choise_number))
                    if int(self.label_3.text()) != 0:
                        self.label_8.setText('Ход компьютера')
                        n += 1
                        comp = randint(1, 5)
                        while comp > int(self.label_3.text()):
                            comp = randint(1, 5)
                        self.rename(comp)
                        self.listWidget.addItem('Компьютер взял - ' + str(comp))
                if int(self.label_3.text()) == 0:
                    if n == 1:
                        self.winner_comp()
                    else:
                        self.winner_i()
                else:
                    self.label_8.setText('Ваш ход')
        elif all_stones == 2:
            if int(self.label_3.text()) != 0:
                self.label_8.setText('Ваш ход')
                if choise_number <= all_stones and choise_number <= int(self.label_3.text()):
                    self.rename(choise_number)
                    self.listWidget.addItem('Игрок взял - ' + str(choise_number))
                    if int(self.label_3.text()) != 0:
                        self.label_8.setText('Ход компьютера')
                        n += 1
                        comp = randint(1, 3)
                        while comp > int(self.label_3.text()):
                            comp = randint(1, 2)
                        self.rename(comp)
                        self.listWidget.addItem('Компьютер взял - ' + str(comp))
                if int(self.label_3.text()) == 0:
                    if n == 1:
                        self.winner_comp()
                    else:
                        self.winner_i()
                else:
                    self.label_8.setText('Ваш ход')
        elif all_stones == 1:
            if int(self.label_3.text()) != 0:
                self.label_8.setText('Ваш ход')
                if choise_number <= all_stones and choise_number <= int(self.label_3.text()):
                    self.rename(choise_number)
                    self.listWidget.addItem('Игрок взял - ' + str(choise_number))
                    if int(self.label_3.text()) != 0:
                        self.label_8.setText('Ход компьютера')
                        n += 1
                        comp = 1
                        self.rename(comp)
                        self.listWidget.addItem('Компьютер взял - ' + str(comp))
                    if int(self.label_3.text()) == 0:
                        if n == 1:
                            self.winner_comp()
                        else:
                            self.winner_i()
                    else:
                        self.label_8.setText('Ваш ход')

    def mousePressEvent(self, event):  # Определение координат щелчка левой кнопки мыши
        self.x = event.x()
        self.y = event.y()
        if event.button() == Qt.LeftButton:
            self.choice()
        self.update()

    def winner_i(self):  # Фиксирование победителя в базе данных, если выиграл игрок
        global id1
        cursor = self.con.cursor()
        s = "SELECT Победы_игрока FROM Gamers WHERE id = ?"
        number = cursor.execute(s, (id1,)).fetchall()  # Получим количество побед игрока из базы данных
        win = 0
        for elem in number:
            win = list(elem)[0]
        if not win:
            win = 0
        s = "SELECT Победы_компьютера FROM Gamers WHERE id = ?"
        number2 = cursor.execute(s, (id1,)).fetchall()  # Получим количество побед компьютера из базы данных
        lose = 0
        for elem in number2:
            lose = list(elem)[0]
        if not lose:
            lose = 0
        sql = "UPDATE Gamers SET Победы_игрока = ? WHERE id = ?"
        cursor.execute(sql, ((win + 1), id1))  # Изменим количество побед игрока в базе данных
        sql = "UPDATE Gamers SET Процент_побед = ? WHERE id = ?"
        if lose != 0:
            cursor.execute(sql, (
                (str(100 * (win + 1) // (win + 1 + lose)) + '%'), id1))  # Изменим процент побед игрока в базе данных
        else:
            cursor.execute(sql, ('100%', id1))
        self.con.commit()
        self.label_4.setText('Игрок выиграл!')

    def winner_comp(self):  # Фиксирование победителя в базе данных, если выиграл компьютер
        cursor = self.con.cursor()
        s = "SELECT Победы_компьютера FROM Gamers WHERE id = ?"
        number = cursor.execute(s, (id1,)).fetchall()  # Получим количество побед компьютера из базы данных
        lose = 0
        for elem in number:
            lose = list(elem)[0]
        if not lose:
            lose = 0
        s = "SELECT Победы_игрока FROM Gamers WHERE id = ?"
        number2 = cursor.execute(s, (id1,)).fetchall()  # Получим количество побед игрока из базы данных
        win = 0
        for elem in number2:
            win = list(elem)[0]
        if not win:
            win = 0
        sql = "UPDATE Gamers SET Победы_компьютера = ? WHERE id = ?"
        cursor.execute(sql, ((lose + 1), id1))  # Изменим количество побед компьютера в базе данных
        sql = "UPDATE Gamers SET Процент_побед = ? WHERE id = ?"
        if win != 0:
            cursor.execute(sql, (
                (str(100 * win // (lose + win + 1)) + '%'), id1))  # Изменим процент побед игрока в базе данных
        else:
            cursor.execute(sql, ('0%', id1))
        self.con.commit()
        self.label_4.setText('Компьютер выиграл!')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginDialog()
    if not login.exec_():
        sys.exit(-1)
    else:
        ex = MyWidget()
        ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
