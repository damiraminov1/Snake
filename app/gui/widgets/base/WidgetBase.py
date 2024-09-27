from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from settings import settings


class WidgetBase(QWidget):
    def __init__(self, name):
        super().__init__()
        self.setMinimumSize(settings.resolution_x, settings.resolution_y)
        self.setMaximumSize(settings.resolution_x, settings.resolution_y)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.name = name

        self.load_css()

    def load_css(self):
        file = QtCore.QFile(str(settings.styles_path.joinpath("widgets").joinpath(f"{self.name}.css")))
        file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
        stream = QtCore.QTextStream(file)
        self.setStyleSheet(stream.readAll())
