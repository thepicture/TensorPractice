MESSAGE_TEMPLATE = 'Field %s length must be less than 20, ' \
                   'current is %s'

with open('input.txt') as input_file:
    input_list = input_file.read()
    rows_str = input_list.split('\n')
    if len(rows_str) > 20:
        print(MESSAGE_TEMPLATE % ('row', len(rows_str)))
    m = int(rows_str[0])
    field_str = rows_str[1:]
    row_list = list()
    for row in field_str:
        column_list = list()
        for column in row.split(' '):
            column_int = int(column)
            column_list.append(column_int)
        if len(column_list) > 20:
            print(MESSAGE_TEMPLATE % ('column', len(rows_str)))
        row_list.append(column_list)
        x = len(row_list)
        y = len(row_list[0])
    for generation in range(0, m):
        history_of_generation = dict()
        for i in range(x):
            for j in range(y):
                neighbors_list = [
                    (i, j + 1),
                    (i, j - 1),
                    (i + 1, j),
                    (i + 1, j + 1),
                    (i + 1, j - 1),
                    (i - 1, j),
                    (i - 1, j + 1),
                    (i - 1, j - 1),
                ]
                print(row_list[i][j], end=' ')
                neighbor_count = 0
                for neighbor_x, neighbor_y in neighbors_list:
                    if neighbor_x < 0 or \
                            neighbor_y < 0 or \
                            neighbor_x >= x or \
                            neighbor_y >= y:
                        continue
                    if row_list[neighbor_x][neighbor_y]:
                        neighbor_count += 1
                if not row_list[i][j]:
                    if neighbor_count == 3:
                        history_of_generation[i, j] = 1
                elif neighbor_count not in range(2, 4):
                    history_of_generation[i, j] = 0
            print()
        print('^ generation', generation + 1)
        for (history_x, history_y), state in history_of_generation.items():
            row_list[history_x][history_y] = state
    with open('output.txt', mode='w') as output_file:
        for i in range(x):
            for j in range(y):
                output_file.write(f'{row_list[i][j]} ')
            output_file.write('\n')
