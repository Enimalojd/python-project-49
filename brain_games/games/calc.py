import random


def get_description():
    return 'What is the result of the expression?\n'


def get_question_answer():
    dig1 = random.randint(0, 50)
    dig2 = random.randint(0, 50)

    operators = ['+', '-', '*',]
    operator = random.choice(operators)

    question = f'{dig1} {operator} {dig2}'
    answer = eval(question)

    return question, str(answer)
