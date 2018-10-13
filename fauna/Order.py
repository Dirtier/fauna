from Utils import *
from fauna.Family import Family


class Order:
    def __init__(self, name: str):
        self.name = name
        self.list = []

    def populate(self, row: list):
        collapse(self, row, Family)

    def add_family(self, family: Family):
        self.list.append(family)

    def print_children(self, width: int):
        for item in self.list:
            spacing = '\t' * width
            _str = f'FAMILY: {item.name}'
            print(f'{spacing}{_str}')
            item.print_children(width + 1)
