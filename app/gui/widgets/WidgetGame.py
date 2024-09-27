from PyQt5.QtCore import Qt

from app.gui.widgets.base.WidgetBase import WidgetBase
from app.gui.widgets.base.WidgetCairo import WidgetCairo
from settings import settings


class WidgetGame(WidgetBase):
    def __init__(self, name):
        super().__init__(name)

        cairo = WidgetCairo()
        cairo.setMaximumSize(settings.resolution_y, settings.resolution_x)
        cairo.setMinimumSize(settings.resolution_y, settings.resolution_x)
        cairo.draw = self.draw
        self.layout.addWidget(cairo, alignment=Qt.AlignHCenter | Qt.AlignVCenter)

    @staticmethod
    def draw(context):
        x, y, x1, y1 = 0.1, 0.5, 0.4, 0.9
        x2, y2, x3, y3 = 0.6, 0.1, 0.9, 0.5
        context.scale(200, 200)
        context.set_line_width(0.04)
        context.move_to(x, y)
        context.curve_to(x1, y1, x2, y2, x3, y3)
        context.stroke()
        context.set_source_rgba(1, 0.2, 0.2, 0.6)
        context.set_line_width(0.02)
        context.move_to(x, y)
        context.line_to(x1, y1)
        context.move_to(x2, y2)
        context.line_to(x3, y3)
        context.stroke()
