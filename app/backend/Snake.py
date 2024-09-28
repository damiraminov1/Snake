from app.backend.Body import Body


class Snake:
    def __init__(self):
        self.body = Body()

    def __len__(self):
        return len(self.body)
