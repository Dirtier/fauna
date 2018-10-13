from fauna.Subspecies import Subspecies


class Species:
    def __init__(self, name: str):
        self.name = name
        self.list = []

    def populate(self, row: list):
        if row[0]:
            self.list.append(Subspecies(row[0]))

    def add_subspecies(self, subspecies: Subspecies):
        self.list.append(subspecies)

    def print_children(self, width: int):
        for item in self.list:
            spacing = '\t' * width
            _str = f'SUBSPECIES: {item.name}'
            print(f'{spacing}{_str}')
