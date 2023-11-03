import random


def get_description():
    return 'What number is missing in the progression?\n'


def get_question_answer():
    start = random.randint(1, 5)
    end = random.randint(30, 33)
    step = random.randint(2, 4)

    progression = list(range(start, end+1, step))
    random_index = random.randint(1, len(progression)-1)

    answer = progression[random_index]
    progression[random_index] = '...'
    question = ' '.join(map(str, progression))

    return question, str(answer)

