def save_field(field, filename='output.txt'):
    """Writes the last generation to
    the output file
    with the given file name from
    the given field.
    """
    with open(filename, 'w+') as file_output:
        for y in range(field.get_height()):
            for x in range(field.get_width()):
                file_output.write(f'{field.get(x, y)} ')
            file_output.write('\n')
