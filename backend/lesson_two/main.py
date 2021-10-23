from backend.lesson_two.fieldutils.field import Field
from backend.lesson_two.iofieldutils.field_input_parser import (
    parse_file
)

MAX_WIDTH = 20
MAX_HEIGHT = 20
MESSAGE_TEMPLATE = 'Field %s length must be less than %s, ' \
                   'current is %s'
#
# with open('input.txt') as input_file:
#     input_list = input_file.read()
#     rows_str = input_list.split('\n')
#     if len(rows_str) > MAX_WIDTH:
#         print(MESSAGE_TEMPLATE % ('row', MAX_WIDTH,
#                                   len(rows_str)))
#     m = int(rows_str[0])
#     field_str = rows_str[1:]
#     prev_row_list = list()
#     for row in field_str:
#         column_list = list()
#         for column in row.split(' '):
#             column_int = int(column)
#             column_list.append(column_int)
#         if len(column_list) > MAX_HEIGHT:
#             print(MESSAGE_TEMPLATE % ('column',
#                                       MAX_HEIGHT,
#                                       len(rows_str)))
#         prev_row_list.append(column_list)
#     print(prev_row_list)
#     width = len(prev_row_list[0])
#     height = len(prev_row_list)
#     for generation in range(0, m):
#         next_row_list = prev_row_list.copy()
#         for i in range(height):
#             for j in range(width):
#                 print(prev_row_list[i][j], end=' ')
#                 neighbors_list = [
#                     (i, j + 1),
#                     (i, j - 1),
#                     (i + 1, j),
#                     (i + 1, j + 1),
#                     (i + 1, j - 1),
#                     (i - 1, j),
#                     (i - 1, j + 1),
#                     (i - 1, j - 1),
#                 ]
#                 neighbor_count = 0
#                 for neighbor_y, neighbor_x in neighbors_list:
#                     if neighbor_x < 0 or \
#                             neighbor_x >= height or \
#                             neighbor_y < 0 or \
#                             neighbor_y >= width:
#                         continue
#                     if prev_row_list[neighbor_y][neighbor_x]:
#                         neighbor_count += 1
#                 # print('neighbor_count:', neighbor_count, 'for ', i, j)
#                 if not prev_row_list[i][j]:
#                     if neighbor_count == 3:
#                         next_row_list[i][j] = 1
#                 elif neighbor_count not in range(2, 4):
#                     next_row_list[i][j] = 0
#             print()
#         print('^ generation', generation + 1)
#         prev_row_list = next_row_list.copy()
#     with open('output.txt', mode='w') as output_file:
#         for i in range(height):
#             for j in range(width):
#                 output_file.write(f'{next_row_list[i][j]} ')
#             output_file.write('\n')

if __name__ == '__main__':
    field_list, generations_count = parse_file('input.txt')
    field = Field(field_list)
    for x in range(field.get_width()):
        for y in range(field.get_height()):
            print(field.get(x, y), end=' ')
        print()
