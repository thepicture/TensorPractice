from backend.lesson_two.fieldutils.field import Field
from backend.lesson_two.iofieldutils.field_input_parser import (
    parse_file
)

MAX_WIDTH = 20
MAX_HEIGHT = 20
MESSAGE_TEMPLATE = 'Field %s length must be less than %s, ' \
                   'current is %s'

if __name__ == '__main__':
    field_list, generations_count = parse_file('input.txt')
    field = Field(field_list)

    for generation in range(generations_count):
        generation_history = dict()
        print('Generation %s:' % (generation + 1))
        print('Before:')
        field.print()
        for x in range(field.get_width()):
            for y in range(field.get_height()):
                count_of_neighbors = 0

                for neighbor_x in range(x - 1, x + 2):
                    for neighbor_y in range(y - 1, y + 2):
                        if neighbor_x < 0 or neighbor_y < 0:
                            continue
                        if neighbor_x >= field.get_width() or \
                                neighbor_y >= field.get_height():
                            continue
                        if neighbor_x == x and neighbor_y == y:
                            continue
                        count_of_neighbors += field.get(
                            neighbor_x,
                            neighbor_y
                        )
                if not field.get(x, y):
                    if count_of_neighbors == 3:
                        generation_history[x, y] = 1
                    else:
                        generation_history[x, y] = 0
                elif count_of_neighbors not in range(2, 4):
                    generation_history[x, y] = 0
        for history_x, history_y in generation_history:
            field.set(history_x, history_y,
                      generation_history[history_x,
                                         history_y])
        print('After: ')
        field.print()
