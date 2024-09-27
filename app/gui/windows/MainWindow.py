from PyQt5.QtWidgets import QMainWindow

from app.gui.stack import MainStack


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Snake - Simple Python Game')
        self.setMinimumSize(1000, 1000)
        self.setMaximumSize(1000, 1000)

        self.stack = MainStack()
        self.setCentralWidget(self.stack)

    def show(self):
        self.stack.stack_switch("start")
        super().show()
