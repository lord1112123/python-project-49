import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def generate_game():
    random_number1 = int(random.randint(1, 100))
    random_number2 = int(random.randint(1, 100))
    question = f'{random_number1}, {random_number2}'
    correct_answer = str(gcd(random_number1, random_number2))
    return question, correct_answer
