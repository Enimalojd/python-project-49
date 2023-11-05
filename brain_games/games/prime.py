import random


def get_description():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_answer():
    end = random.randint(50, 3500)
    case = [i for i in range(end + 1)]
    case[1] = 0
    i = 2

    while i < end ** 0.5:
        if case[i] != 0:
            j = i ** 2
            while j <= end:
                case[j] = 0
                j += i
        i += 1

    case = [i for i in case if case[i] != 0]

    question = random.randint(1, end)
    answer = 'yes' if question in case else 'no'
    return question, answer
