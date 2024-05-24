import random


def main():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')

    for _ in range(3):
        ran_num1 = int(random.randint(1, 100))
        ran_num2 = int(random.randint(1, 100))
        operators = random.choice(['+', '-', '*'])
        question = f'{ran_num1} {operators} {ran_num2}'
        corr_ans = str(eval(question))
        print(f'Question: {question}')
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
