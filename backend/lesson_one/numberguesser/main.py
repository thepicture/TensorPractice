from backend.lesson_one.numberguesser.number_guesser import (
    NumberGuesser
)

if __name__ == '__main__':
    inf = 0
    sup = 100

    guesser = NumberGuesser(inf, sup)

    while True:
        guesser.ask()

        answer = input()

        if answer == 'Больше':
            guesser.say_greater()
            continue
        elif answer == 'Меньше':
            guesser.say_less()
            continue
        elif answer == 'Верно':
            guesser.say_equal()
            break
        else:
            print('Unknown command. '
                  'Please, use "Больше" or "Меньше" or "Верно" '
                  'to answer.')
