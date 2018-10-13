from Utils import collapse


class Subspecies:
    def __init__(self, name: str):
        self.name = name

    def populate(self, row: list):
        return

    def print(self, width: int):
        spacing = '\t' * width
        _str = f'SUBSPECIES: {self.name}'
        print(f'{spacing}{_str}')