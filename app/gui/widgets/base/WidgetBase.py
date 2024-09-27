from PyQt5.QtWidgets import QWidget, QVBoxLayout


class WidgetBase(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Snake - Simple offline game')
        self.setMinimumSize(500, 500)
        self.setMaximumSize(500, 500)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.name = None
