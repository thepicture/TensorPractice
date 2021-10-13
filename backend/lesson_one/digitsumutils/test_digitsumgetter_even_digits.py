from unittest import TestCase

from digitsumgetter import get_sum_of_even_digits


class TestGetSumOfEvenDigits(TestCase):
    def test_get_sum_of_even_digits(self):
        """Test for get_sum_of_even_digits definition."""
        # Arrange.
        number = "1234567890"
        expected = 20
        # Act.
        actual = get_sum_of_even_digits(number)
        # Assert.
        self.assertEqual(expected, actual)
