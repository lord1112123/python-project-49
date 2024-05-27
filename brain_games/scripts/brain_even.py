import random


def even_or_add(number):
    return number % 2 == 0


def main():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(3):
        random_number = random.randint(1, 100)
        corr_ans = 'yes' if even_or_add(random_number) else 'no'

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
