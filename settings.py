from pathlib import Path

class Settings:

    def __init__(self):
        self.project_path = Path(__file__).parent.absolute()
        self.styles_path = self.project_path.joinpath('res').joinpath('styles')

settings = Settings()
