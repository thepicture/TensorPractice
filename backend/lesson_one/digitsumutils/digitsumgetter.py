def get_sum_of_even_digits(number):
    """Return the sum of even digits in the given number."""
    accumulator = 0

    for digit in number:
        if int(digit) % 2 == 0:
            accumulator += int(digit)

    return accumulator


def get_sum_of_odd_digits(number):
    """Return the sum of odd digits in the given number."""
    accumulator = 0

    for digit in number:
        if int(digit) % 2 != 0:
            accumulator += int(digit)

    return accumulator
