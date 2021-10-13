from digitsumgetter import get_sum_of_even_digits, get_sum_of_odd_digits

if __name__ == '__main__':
    while True:
        number = input("Enter the number: ")

        if not number.isdigit():
            print(f"Type {type(number)} is not a number. Enter a valid number.")
            continue

        odd_sum = get_sum_of_odd_digits(number)
        even_sum = get_sum_of_even_digits(number)

        print(odd_sum, even_sum)
        break
