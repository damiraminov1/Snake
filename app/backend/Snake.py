from app.backend.Body import Body


class Snake:
    def __init__(self, area_size = (0, 0,)):
        self.body = Body(length=50, area_size=area_size)
        self.area_size = area_size

    def __len__(self):
        return len(self.body)

    @property
    def coords(self):
        coords = list()
        for node in self.body.parts:
            coords.append((node.x, node.y,))
        return coords
