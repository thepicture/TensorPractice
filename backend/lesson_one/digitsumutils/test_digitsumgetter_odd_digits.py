from unittest import TestCase

from backend.lesson_one.digitsumutils.digitsumgetter import get_sum_of_odd_digits


class TestGetSumOfOddDigits(TestCase):
    def test_get_sum_of_odd_digits(self):
        """Test for get_sum_of_odd_digits definition."""
        # Arrange.
        number = "1234567890"
        expected = 25
        # Act.
        actual = get_sum_of_odd_digits(number)
        # Assert.
        self.assertEqual(expected, actual)
