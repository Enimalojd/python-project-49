import random


def get_description():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    case = [i for i in range(n + 1)]
    case[1] = 0
    i = 2

    while i < n ** 0.5:
        if case[i] != 0:
            j = i ** 2
            while j <= n:
                case[j] = 0
                j += i
        i += 1

    case = [i for i in case if case[i] != 0]
    return True if n in case else False


def get_question_answer():
    question = random.randint(1, 3500)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer
