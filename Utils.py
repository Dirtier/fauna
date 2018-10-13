def collapse(self, row: list, _next):
    instance = _next(row[0])
    found = False

    for item in self.list:
        if item.name == row[0]:
            instance = item
            found = True

    if not found:
        self.list.append(instance)

    if row[0] == 'Subspecies':
        return

    instance.populate(row[1:])
