from app.gui.widgets.base.WidgetBase import WidgetBase
from app.gui.widgets.base.WidgetCairo import WidgetCairo


class WidgetGame(WidgetBase):
    def __init__(self, name):
        super().__init__(name)

        cairo = WidgetCairo()
        self.layout.addWidget(cairo)
