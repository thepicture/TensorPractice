class Field:
    def __init__(self, input_list):
        self._field = dict()
        for i in range(len(input_list)):
            for j in range(len(input_list[0])):
                self._field[i, j] = input_list[i][j]

    def append(self, x, y, value):
        """Appends a new indices to the field.
        """
        self._field[x, y] = value

    def get(self, x, y):
        """Gets the value from the field
        with the given
        two-dimensioned coordinates.

        Raises an exception if
        the given pair of coordinates
        does not exist
        in this Field.
        """
        if (x, y) not in self._field:
            raise IndexError('The position '
                             f'of the field at {x}, {y} '
                             'is undefined.')
        return self._field[x, y]
