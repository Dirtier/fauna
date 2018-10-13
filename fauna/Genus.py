from Utils import *
from fauna.Species import Species


class Genus:
    def __init__(self, name: str):
        self.name = name
        self.list = []

    def populate(self, row: list):
        collapse(self, row, Species)

    def add_species(self, species: Species):
        self.list.append(species)

    def print_children(self, width: int):
        for item in self.list:
            spacing = '\t' * width
            _str = f'SPECIES: {item.name}'
            print(f'{spacing}{_str}')
            item.print_children(width + 1)
