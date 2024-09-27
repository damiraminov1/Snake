from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QGridLayout, QLabel

from app.gui.widgets.base.WidgetBase import WidgetBase
from settings import settings


class StartWidget(WidgetBase):
    def __init__(self):
        super().__init__()

        self.label = QLabel(f"{settings.app_name} 1.0")
        self.layout.addWidget(self.label, alignment=Qt.AlignCenter)

        self.button_start = QPushButton('Start', self)
        self.button_start.setFixedSize(300, 150)
        self.button_start.clicked.connect(self._on_start)

        self.layout.addWidget(self.button_start, alignment=Qt.AlignCenter)

    def _on_start(self):
        self.parent().stack_switch("game")
