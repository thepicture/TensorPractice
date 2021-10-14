def get_word_by_age(age):
    """Return the appropriate word for the given age."""
    last_two_digits = age[-2:]
    age = int(last_two_digits)

    if age in range(10, 20) or age % 5 == 0:
        return 'лет'
    if age % 10 == 1:
        return 'год'
    if age % 10 in range(2, 5):
        return 'года'
    return 'лет'
