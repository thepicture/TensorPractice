from unittest import TestCase
from backend.lesson_two.main import main


def get_output_str():
    with open('output.txt') as file:
        return file.read()


class TestMain(TestCase):
    def test_main(self):
        # Arrange
        expected = """0 0 1 0 0 1 0 0 
0 0 0 0 0 0 0 0 
1 0 0 0 0 0 0 1 
1 0 0 0 0 0 0 1 
1 0 0 0 0 0 0 1 
0 0 0 0 0 0 0 0 
0 0 1 0 0 1 0 0 
"""

        # Act
        main('input.txt')
        actual = get_output_str()

        # Assert
        self.assertEqual(expected, actual)
