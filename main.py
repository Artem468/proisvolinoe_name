import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication
from neui import Ui_MainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.drawf)
        self.initUI()

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def initUI(self):
        self.setWindowTitle('Рисование')
        self.coords_ = [0, 0]
        self.setMouseTracking(True)
        self.qp = QPainter()
        self.flag = False
        self.status = None

        self.show()

    def draw(self):
        r = randint(1, 100)
        self.coords_ = [randint(100, 700), randint(100, 500)]
        self.qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        self.qp.drawEllipse(self.coords_[0], self.coords_[1], r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
