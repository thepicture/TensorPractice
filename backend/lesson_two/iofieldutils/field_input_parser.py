from backend.lesson_two.fieldutils.field_string_parser import (
    parse_field
)
from backend.lesson_two.iofieldutils.list_transposer import (
    transpose
)


def parse_file(input_file='input.txt'):
    """Parses the given file to the list
    and returns it as a two-dimensioned list
    with access by indices.
    """
    with open(input_file) as input_file:
        input_string_list = input_file.read()
        row_list, generations_count = parse_field(
            input_string_list
        )

    transposed_row_list = transpose(row_list)

    return transposed_row_list, generations_count
