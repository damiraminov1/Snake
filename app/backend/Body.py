

class BodyPart:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __del__(self):
        pass

class Body:
    def __init__(self, length = 1):
        self.parts = [BodyPart() for _ in range(length)]

    def __len__(self):
        len(self.parts)

    def __add__(self, other):
        if isinstance(other, int):
            self.parts.append(BodyPart())

    def __sub__(self, other):
        if isinstance(other, int):
            self.parts.pop()
        if not self.parts:
            del self
