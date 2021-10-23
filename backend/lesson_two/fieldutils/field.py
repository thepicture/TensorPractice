class Field:
    def __init__(self):
        self._field = dict()

    def append(self, x, y, value):
        self._field[x, y] = value

    def get(self, x, y):
        if (x, y) not in self._field:
            raise IndexError('The position '
                             f'of the field at {x}, {y} '
                             'is undefined.')
        return self._field[x, y]


if __name__ == '__main__':
    field = Field()
    field.append(2, 3, 5)
    print(field.get(2, 3))
    print(field.get(4, 6))
