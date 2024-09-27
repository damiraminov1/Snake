from PyQt5.QtWidgets import QMainWindow

from app.gui.stack import MainStack
from settings import settings


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Snake - Simple Python Game')
        self.setMinimumSize(settings.resolution_x, settings.resolution_y)
        self.setMaximumSize(settings.resolution_x, settings.resolution_y)

        self.stack = MainStack()
        self.setCentralWidget(self.stack)

    def show(self):
        self.stack.stack_switch("start")
        super().show()
