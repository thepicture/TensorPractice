from functools import wraps

from backend.lesson_two.fieldutils import neighbor_counter
from backend.lesson_two.fieldutils.field import Field
from backend.lesson_two.iofieldutils import field_saver
from backend.lesson_two.iofieldutils.field_input_parser import (
    parse_file
)

MAX_WIDTH = 20
MAX_HEIGHT = 20
MESSAGE_TEMPLATE = 'Field %s length must be less than %s, ' \
                   'current is %s'

assert MAX_WIDTH == MAX_HEIGHT


def main():
    """The game "Life" main start point.
    """
    input_file = 'input.txt'

    field_list, generations_count = parse_file(input_file)
    field = Field(field_list)

    if field.get_width() >= 20:
        print(MESSAGE_TEMPLATE % ('column',
                                  MAX_WIDTH,
                                  field.get_width(),
                                  )
              )
        return
    if field.get_height() >= 20:
        print(MESSAGE_TEMPLATE % ('row',
                                  MAX_HEIGHT,
                                  field.get_height()),
              )
        return

    for generation in range(generations_count):
        calculate_generation(field, generation)


def generation_logger(func):
    """Logs generations in after and
    before states in the console.
    """

    @wraps(func)
    def wrapper(field, generation, **kwargs):
        print('Generation %s:' % (generation + 1))
        print('Before:')
        field.print()
        func(field, generation, **kwargs)
        print('After: ')
        field.print()

    return wrapper


@generation_logger
def calculate_generation(field, generation):
    """Calculates the current system state
    for the given step.
    """
    generation_history = dict()
    field_saver.save_field(field)
    for x in range(field.get_width()):
        loop_for_y_and_update(field, generation_history, x)
    for history_x, history_y in generation_history:
        field.set(history_x,
                  history_y,
                  generation_history[
                      history_x, history_y
                  ],
                  )


def loop_for_y_and_update(field, generation_history, x):
    """Loops the generation state for y-axis and
    updates life cycle.
    """
    for y in range(field.get_height()):
        update_field(field, generation_history, x, y)


def update_field(field, generation_history, x, y):
    """Counts the members and
    then updates the history
    of the current generation.
    """
    count_of_neighbors = neighbor_counter.get_count_of_neighbors(
        field,
        x, y,
    )
    generation_history.update(check_generation_conditions(
        field, x,
        y, count_of_neighbors,
    ))


def check_generation_conditions(field, x,
                                y, count_of_neighbors,
                                ):
    """Checks if the given conditions are right:

    If the cell is a zero, then if it contains three neighbors,
    then give a life to the cell.

    Else if the cell contains from two to three neighbors,
    then pass, otherwise the cell will be dead."""
    generation_history = dict()

    if not field.get(x, y):
        update_if_3_neighbors(count_of_neighbors, generation_history,
                              x, y,
                              )
    elif count_of_neighbors in range(2, 4):
        generation_history[x, y] = 1
    else:
        generation_history[x, y] = 0

    return generation_history


def update_if_3_neighbors(count_of_neighbors, generation_history,
                          x, y,
                          ):
    """Writes the history if
    the cell has exactly three neighbors.
    """
    if count_of_neighbors == 3:
        generation_history[x, y] = 1
    else:
        generation_history[x, y] = 0


if __name__ == '__main__':
    main()
