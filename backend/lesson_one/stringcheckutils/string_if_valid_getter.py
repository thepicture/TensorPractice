def get_integer_if_valid(a, b):
    """Return the valid integer in the interval (a, b)."""
    while True:
        number = input('Enter the number: ')

        error_message = 'Enter a valid number.'

        if not number.isdigit():
            print(f'Type {type(number)} is not a number. {error_message}')
            continue

        if not a <= int(number) <= b:
            print('Number must be an integer in the interval '
                  f'between {a} and {b} inclusively. {error_message}')
            continue
        return number
