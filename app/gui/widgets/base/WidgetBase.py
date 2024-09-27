from PyQt5.QtWidgets import QWidget, QVBoxLayout

from settings import settings


class WidgetBase(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Snake - Simple offline game')
        self.setMinimumSize(settings.resolution_x, settings.resolution_y)
        self.setMaximumSize(settings.resolution_x, settings.resolution_y)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.name = None
