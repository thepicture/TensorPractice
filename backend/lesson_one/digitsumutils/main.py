from digitsumgetter import get_sum_of_even_digits, \
    get_sum_of_odd_digits

if __name__ == '__main__':
    while True:
        number = input('Enter the number: ')

        error_message = 'Enter a valid number.'

        if not number.isdigit():
            print(f'Type {type(number)} is not a number. {error_message}')
            continue

        if not 0 < int(number) < 10 ** 20:
            print('Number must be an integer in interval '
                  f'between 0 and 10 ** 20 exclusively. {error_message}')
            continue

        odd_sum = get_sum_of_odd_digits(number)
        even_sum = get_sum_of_even_digits(number)

        print(odd_sum, even_sum)
        break
