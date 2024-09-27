import cairo

from PyQt5.QtGui import QImage, QPainter

from app.gui.widgets.base.WidgetBase import WidgetBase


class WidgetCairo(WidgetBase):
    def __init__(self):
        super().__init__(self)

    def draw(self, context):
        pass
        # Draw something on the surface

    def paintEvent(self, event):
        # Create a PyCairo surface
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.width(), self.height())

        context = cairo.Context(surface)

        self.draw(context)

        # Convert the PyCairo surface to a QImage
        image = QImage(surface.get_data(), surface.get_width(), surface.get_height(), QImage.Format_ARGB32)

        # Create a QPainter and draw the image on the widget
        painter = QPainter(self)
        painter.drawImage(0, 0, image)
