def parse_field(input_string_list):
    """Parses the given field
    from the given list of strings.
    """
    rows_str = input_string_list.split('\n')
    m = int(rows_str[0], 10)
    field_str = rows_str[1:]
    row_list = list()
    for row in field_str:
        column_list = list()
        for column in row.split(' '):
            column_int = int(column, 10)
            column_list.append(column_int)
        row_list.append(column_list)
    return row_list, m
