import cairo
from PyQt5.QtCore import Qt

from app.backend.Snake import Snake
from app.gui.widgets.base.WidgetBase import WidgetBase
from app.gui.widgets.base.WidgetCairo import WidgetCairo
from settings import settings


class WidgetGame(WidgetBase):
    def __init__(self, name):
        super().__init__(name)

        self.snake = None

        cairo = WidgetCairo()
        cairo.setMaximumSize(settings.resolution_y, settings.resolution_x)
        cairo.setMinimumSize(settings.resolution_y, settings.resolution_x)
        cairo.draw = self.draw
        self.layout.addWidget(cairo, alignment=Qt.AlignHCenter | Qt.AlignVCenter)
        self.snake = Snake(area_size=(self.height(), self.width(),))

    def draw(self, context: cairo.Context) -> None:
        if self.snake is not None:
            context.set_source_rgb(0, 0, 0)
            context.set_line_width(20)

            start_coords = self.snake.coords[0]
            context.move_to(*start_coords)

            for coords in self.snake.coords[1:]:
                context.line_to(*coords)
                context.stroke()
                context.move_to(*coords)
