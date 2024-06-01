import math
import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    number_sqrt = int(math.sqrt(number))
    divisors = range(2, (number_sqrt + 1))

    for element in divisors:
        if number % element == 0:
            return False
    return True


def generate_game():
    random_number = random.randint(1, 100)
    question = random_number
    correct_answer = 'yes' if is_prime(random_number) else 'no'
    return question, correct_answer
