from PyQt5.QtWidgets import QPushButton

from app.gui.widgets.base.WidgetBase import WidgetBase


class StartWidget(WidgetBase):
    def __init__(self):
        super().__init__()

        self.button_start = QPushButton('Start', self)
        self.button_start.clicked.connect(self._on_start)
        self.layout.addWidget(self.button_start)

    def _on_start(self):
        self.parent().stack_switch("game")
