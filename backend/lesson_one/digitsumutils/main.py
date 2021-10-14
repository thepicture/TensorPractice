from backend.lesson_one.stringcheckutils.string_if_valid_getter import (
    get_integer_if_valid
)

from digitsumgetter import get_sum_of_even_digits, \
    get_sum_of_odd_digits

if __name__ == '__main__':
    a = 0
    b = 10 ** 20

    number = get_integer_if_valid(a, b)

    odd_sum = get_sum_of_odd_digits(number)
    even_sum = get_sum_of_even_digits(number)

    print(odd_sum, even_sum)
