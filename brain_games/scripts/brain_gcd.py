import random


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def main():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')

    for _ in range(3):
        ran_num1 = int(random.randint(1, 100))
        ran_num2 = int(random.randint(1, 100))
        question = f'{ran_num1}, {ran_num2}'
        corr_ans = gcd(ran_num1, ran_num2)
        print(f'Question: {question}')
        user_ans = int(input('Your answer: '))
        if user_ans == corr_ans:
            print('Correct!')
        else:
            print(f"'{user_ans}' is wrong answer ;(. Correct answer was '{corr_ans}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
