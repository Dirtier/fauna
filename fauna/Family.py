from Utils import *
from fauna.Genus import Genus


class Family:
    def __init__(self, name: str):
        self.name = name
        self.list = []

    def populate(self, row: list):
        collapse(self, row, Genus)

    def add_genus(self, genus: Genus):
        self.list.append(genus)

    def print_children(self, width: int):
        for item in self.list:
            spacing = '\t' * width
            _str = f'GENUS: {item.name}'
            print(f'{spacing}{_str}')
            item.print_children(width + 1)
