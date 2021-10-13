def get_integer_if_valid(a, b):
    """Return the valid integer in the interval (a, b)"""
    while True:
        number = input('Enter the number: ')

        error_message = 'Enter a valid number.'

        if not number.isdigit():
            print(f'Type {type(number)} is not a number. {error_message}')
            continue

        if not a < int(number) < b:
            print('Number must be an integer in interval '
                  f'between 0 and 10 ** 20 exclusively. {error_message}')
            continue
        return number
