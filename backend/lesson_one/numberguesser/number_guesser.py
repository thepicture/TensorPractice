import math


class NumberGuesser:

    def __init__(self, inf, sup):
        """Init with the minimum and maximum values"""
        self.inf = inf
        self.sup = sup
        self.is_done = False

    def say_greater(self):
        """Notifies the guesser that the number is greater
        than the offered.

        """
        self.inf = self.get_mean_number()
        self.ask()

    def say_less(self):
        """Notifies the guesser that the number is less
               than the offered.

               """
        self.sup = self.get_mean_number()
        self.ask()

    def say_equal(self):
        """Notifies the guesser that the number does equal
               to the offered.

               """
        print(f'The number is {self.get_mean_number()}')

        self.is_done = True

    def ask(self):
        """Invokes the guesser to offer a number."""
        print(self.inf, self.sup)
        print(f'Is the number greater or equals to '
              f'{self.get_mean_number()}?')

    def get_mean_number(self):
        """Return the mean of the minimum and maximum."""
        return math.ceil((self.inf + self.sup) / 2)

    def is_guessed(self):
        """Check if the number was guessed."""
        return self.is_done
