import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.pushButton.clicked.connect(self.open)

    def open(self):
        self.con = sqlite3.connect("coffee.sqlite3")
        cur = self.con.cursor()
        result = cur.execute('''SELECT * FROM Coffee''').fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
