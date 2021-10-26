class FieldPrinter:
    @staticmethod
    def print(field):
        """Prints the given field in a readable form."""
        for y in range(field.get_height()):
            for x in range(field.get_width()):
                print(field.get(x, y), end=' ')
            print()
