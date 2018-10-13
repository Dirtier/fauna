from Utils import *
from fauna.Phylum import Phylum
import csv


class Fauna:
    def __init__(self, file):
        self.list = []

        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)

            for row in csv_reader:
                self.populate(row)

    def populate(self, row: list):
        collapse(self, row, Phylum)

    def add_phylum(self, phylum: Phylum):
        self.list.append(phylum)

    def __str__(self):
        for item in self.list:
            print(f'PHYLUM: {item.name}')
            item.print_children(1)

