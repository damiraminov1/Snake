from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow

from app.gui.stack import MainStack
from settings import settings


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"{settings.app_name}")
        self.setMinimumSize(settings.resolution_x, settings.resolution_y)
        self.setMaximumSize(settings.resolution_x, settings.resolution_y)

        self.stack = MainStack()
        self.setCentralWidget(self.stack)

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.stack.stack_back()

    def show(self):
        self.stack.stack_switch("start")
        super().show()
