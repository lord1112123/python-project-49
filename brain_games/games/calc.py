import random

DESCRIPTION = 'What is the result of the expression?'

def generate_game():
    random_number1 = int(random.randint(1, 100))
    random_number2 = int(random.randint(1, 100))
    operators = random.choice(['+', '-', '*'])
    question = f'{ran_num1} {operators} {ran_num2}'
    correct_answer = str(eval(question))

    return question, correct_answer
