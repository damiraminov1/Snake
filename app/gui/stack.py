from PyQt5.QtWidgets import QStackedWidget

from app.gui.widgets.WidgetGame import WidgetGame
from app.gui.widgets.WidgetStart import StartWidget


class MainStack(QStackedWidget):
    def __init__(self):

        super().__init__()

        self.widgets = {
            "start": StartWidget("start"),
            "game": WidgetGame("game"),
        }

        self.previous_widget_name = "start"

        for name_widget in self.widgets.items():
            name = name_widget[0]
            widget = name_widget[1]
            self.addWidget(widget)
            widget.name = name


    def stack_switch(self, widget_name: str):
        self.previous_widget_name = self.currentWidget().name

        target_widget = self.widgets[widget_name]
        self.setCurrentWidget(target_widget)

    def back(self):
        self.stack_switch(self.previous_widget_name)
