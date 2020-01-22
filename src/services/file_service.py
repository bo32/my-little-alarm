import pathlib

class FileService:

    def __init__(self):
        pass

    @staticmethod
    def file_exists(filepath):
        return pathlib.Path(filepath).exists()