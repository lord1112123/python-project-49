import math
import random


def is_prime(number):
    if number <= 1:
        return False
    number_sqrt = int(math.sqrt(number))
    divisors = range(2, (number_sqrt + 1))

    for element in divisors:
        if number % element == 0:
            return False
    return True


def main():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for _ in range(3):
        random_number = random.randint(1, 100)
        corr_ans = 'yes' if is_prime(random_number) else 'no'

        print(f'Question: {random_number}')
        user_ans = input('Your answer: ')

        if user_ans.lower() == corr_ans:
            print('Correct!')
        else:
            print(f"'{user_ans}' is wrong answer ;(. Correct answer was '{corr_ans}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
