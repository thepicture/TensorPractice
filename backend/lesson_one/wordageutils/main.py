from backend.lesson_one.wordageutils.word_by_age_getter import (
    get_word_by_age
)

from backend.lesson_one.stringcheckutils import (
    get_integer_if_valid
)

if __name__ == '__main__':
    age = get_integer_if_valid(0, 200)

    age = str(age)

    age_word = get_word_by_age(age)

    print(age, age_word)
