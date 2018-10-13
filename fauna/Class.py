from Utils import *
from fauna.Order import Order


class Class:
    def __init__(self, name: str):
        self.name = name
        self.list = []

    def populate(self, row: list):
        collapse(self, row, Order)

    def add_order(self, order: Order):
        self.list.append(order)

    def print_children(self, width: int):
        for item in self.list:
            spacing = '\t' * width
            _str = f'ORDER: {item.name}'
            print(f'{spacing}{_str}')
            item.print_children(width + 1)
