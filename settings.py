from pathlib import Path

class Settings:

    resolution_x = 800
    resolution_y = 800

    def __init__(self):
        self.project_path = Path(__file__).parent.absolute()
        self.styles_path = self.project_path.joinpath('res').joinpath('styles')

settings = Settings()
