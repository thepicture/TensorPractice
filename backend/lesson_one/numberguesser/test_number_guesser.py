from unittest import TestCase

from backend.lesson_one.numberguesser.number_guesser import (
    NumberGuesser
)


class TestNumberGuesser(TestCase):
    def test_get_mean_number(self):
        """Test for correct guessing of the 73 number
        in [log2(100)] attempts.

        """

        # Arrange.
        guesser = NumberGuesser(0, 100)
        guesser.ask()
        guesser.say_greater()
        guesser.say_less()
        guesser.say_greater()
        guesser.say_greater()
        guesser.say_greater()
        guesser.say_less()
        expected = 73
        # Act.
        actual = guesser.get_mean_number()
        # Assert.
        TestCase.assertEqual(self, expected, actual)
