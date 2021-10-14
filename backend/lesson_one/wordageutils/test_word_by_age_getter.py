from unittest import TestCase

from backend.lesson_one.wordageutils.word_by_age_getter import (
    get_word_by_age
)


class TestGetWordByAge(TestCase):
    def test_get_word_by_age(self):
        """Test for age which equals to 11."""
        # Arrange.
        expected = 'лет'
        # Act.
        actual = get_word_by_age(str(11))
        # Assert.
        self.assertEqual(expected, actual)
