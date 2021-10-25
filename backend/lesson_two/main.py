from functools import wraps

from backend.lesson_two.fieldutils import neighbor_counter
from backend.lesson_two.fieldutils.field import Field
from backend.lesson_two.iofieldutils import field_saver
from backend.lesson_two.iofieldutils.field_input_parser import (
    parse_file
)

MAX_WIDTH = 20
MAX_HEIGHT = 20
RECTANGLES_ARE_ALLOWED = True
LIFE_CHANGE_ALL_AT_ONCE = True
MESSAGE_TEMPLATE = 'Field %s length must be less than %s, ' \
                   'current is %s'

assert RECTANGLES_ARE_ALLOWED
assert LIFE_CHANGE_ALL_AT_ONCE


def main(input_file):
    """The game "Life" main start point.
    """
    input_file = input_file

    field_list, generations_count = parse_file(input_file)
    field = Field(field_list)

    if field.get_width() >= 20:
        print_size_error(field, 'column')
        return
    if field.get_height() >= 20:
        print_size_error(field, 'row')
        return

    assert field.get_width() < 20
    assert field.get_height() < 20

    for generation in range(generations_count):
        calculate_generation(field, generation, generations_count)


def print_size_error(field, object_):
    """Prints the errors
    with the given object as a reason.
    """
    print(MESSAGE_TEMPLATE
          % (object_,
             MAX_WIDTH,
             field.get_width())
          )


def generation_logger(func):
    """Prints each generation's view after and
    before changing in the console.

    Has sense only if functions change a field
    such that print of the field
    will change.
    """

    @wraps(func)
    def wrapper(field, generation, *_):
        print('Generation %s:' % (generation + 1))
        print('Before:')
        field.print()
        func(field, generation, *_)
        print('After: ')
        field.print()

    return wrapper


@generation_logger
def calculate_generation(field, generation, generations_count):
    """Calculates the current system state
    for the given step.
    """
    generation_history = dict()

    is_last_generation = generations_count - generation < 2

    if is_last_generation:
        field_saver.save_field(field)
    for x in range(field.get_width()):
        loop_for_y_and_update(field, generation_history, x)

    update_field_with_history(field, generation_history)


def update_field_with_history(field, generation_history):
    """Updates the field's history."""
    for history_x, history_y in generation_history:
        field.set(
            history_x, history_y,
            generation_history[
                history_x, history_y,
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
        field, x, y)

    generation_dict = check_generation_conditions(
        field, x, y,
        count_of_neighbors)

    generation_history.update(generation_dict)


def check_generation_conditions(field, x,
                                y, count_of_neighbors) -> dict:
    """Checks if the given conditions are right:

    If the cell is a zero, then if it contains three neighbors,
    then give a life to the cell.

    Else if the cell contains from two to three neighbors,
    then pass, otherwise the cell will be dead."""
    generation_history = dict()

    if not field.get(x, y):
        update_if_3_neighbors(
            count_of_neighbors, generation_history,
            x, y)
    else:
        if (x, y) in generation_history:
            print(True)
        generation_history[x, y] = int(count_of_neighbors in range(2, 4))

    return generation_history


def update_if_3_neighbors(
        count_of_neighbors, generation_history,
        x, y):
    """Writes the history if
    the cell has exactly three neighbors.
    """
    if (x, y) in generation_history:
        print(True)
    generation_history[x, y] = int(count_of_neighbors == 3)


if __name__ == '__main__':
    main('input.txt')
