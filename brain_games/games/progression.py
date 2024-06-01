import random

DESCRIPTION = 'What number is missing in the progression?'

def arif_progress(a, d, k):
    progress = [a + i * d for i in range(k)]
    return progress


def hide_element(progress, index):
    hide_value = progress[index]
    progress_hide = progress[:]
    progress_hide[index] = ".."
    return progress_hide, hide_value


def generate_game():
    number1 = int(random.randint(1, 10))
    number2 = int(random.randint(1, 10))
    number3 = int(random.randint(5, 10))
    hide_index = random.randint(0, number3 - 1)
    progress = arif_progress(number1, number2, number3)
    question, correct_answer = hide_element(progress, hide_index)
    question_str = ' '.join(map(str, question))