from random import randint


def get_description():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_answer():
    question = randint(0, 50)
    answer = 'yes' if question % 2 == 0 else 'no'
    return question, answer
