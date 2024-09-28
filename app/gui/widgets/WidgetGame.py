import cairo
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

    def draw(self, context: cairo.Context) -> None:
        context.set_source_rgb(0, 0, 0)
        context.set_line_width(20)
        context.move_to(self.height() / 2, self.width())
        context.line_to(self.height() / 2, self.width() - 50)
        context.stroke()
