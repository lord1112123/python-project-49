import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def even_or_add(number):
    return number % 2 == 0


def generate_game():
    random_number = random.randint(1, 100)
    question = random_number
    correct_answer = 'yes' if even_or_add(random_number) else 'no'
    return question, correct_answer
