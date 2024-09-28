

class Node:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

class Body:
    def __init__(self, length = 1, area_size = (0, 0,)):
        x_start = area_size[0]/2
        y_start = area_size[1]
        self.parts = [Node(x_start, y_start - i) for i in range(length)]

    def __len__(self):
        len(self.parts)

    # def __add__(self, other):
    #     if isinstance(other, int):
    #         self.parts.append()

    def __sub__(self, other):
        if isinstance(other, int):
            self.parts.pop()
        if not self.parts:
            del self
