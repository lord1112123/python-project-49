import random


def arif_progress(a, d, k):
    progress = [a + i * d for i in range(k)]
    return progress


def hide_element(progress, index):
    hide_value = progress[index]
    progress_hide = progress[:]
    progress_hide[index] = ".."
    return progress_hide, hide_value


def main():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')

    for _ in range(3):
        ran_num1 = int(random.randint(1, 10))
        ran_num2 = int(random.randint(1, 10))
        ran_num3 = int(random.randint(5, 10))
        hide_index = random.randint(0, ran_num3 - 1)
        progress = arif_progress(ran_num1, ran_num2, ran_num3)
        question, corr_ans = hide_element(progress, hide_index)
        question_str = ' '.join(map(str, question))
        print(f'Question: {question_str}')
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
