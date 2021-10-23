class Field:
    def __init__(self, input_list):
        """Initializes this field with
        the given input_list's values.
        """
        self._dict = dict()
        for i in range(len(input_list)):
            for j in range(len(input_list[0])):
                self._dict[i, j] = input_list[i][j]

    def append(self, x, y, value):
        """Appends a new indices to the field.
        """
        self._dict[x, y] = value

    def get(self, x, y):
        """Gets the value from the field
        with the given
        two-dimensioned coordinates.

        Raises an exception if
        the given pair of coordinates
        does not exist
        in this Field.
        """
        if (x, y) not in self._dict:
            raise IndexError('The position '
                             f'of the field at {x}, {y} '
                             'is undefined.')
        return self._dict[x, y]

    def set(self, x, y, val):
        """Sets the value at the given position
        of this field.
        """
        self._dict[x, y] = val

    def get_width(self):
        """"Returns the width of the field.
        """
        return max(x for x, y in self._dict.keys()) + 1

    def get_height(self):
        """Returns the height of the field.
        """
        return max(y for x, y in self._dict.keys()) + 1

    def print(self):
        """Prints this field in a readable form.
        """
        for y in range(self.get_height()):
            for x in range(self.get_width()):
                print(self.get(x, y), end=' ')
            print()
