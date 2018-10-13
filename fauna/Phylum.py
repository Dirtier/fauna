from Utils import *
from fauna.Class import Class


class Phylum:
    def __init__(self, name: str):
        self.name = name
        self.list = []

    def populate(self, row: list):
        collapse(self, row, Class)

    def add_class(self, _class: Class):
        self.list.append(_class)

    def print_children(self, width: int):
        for item in self.list:
            spacing = '\t' * width
            _str = f'CLASS: {item.name}'
            print(f'{spacing}{_str}')
            item.print_children(width + 1)
