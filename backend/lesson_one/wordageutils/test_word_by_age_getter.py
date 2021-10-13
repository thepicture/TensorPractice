from unittest import TestCase

from backend.lesson_one.wordageutils.word_by_age_getter import (
    get_word_by_age
)


class TestGetWordByAge(TestCase):
    def test_get_word_by_age(self):
        """Test for test_get_word_by_age."""
        # Arrange.
        expected = 'лет'
        # Act.
        actual = get_word_by_age(str(11))
        # Assert.
        self.assertEqual(expected, actual)
