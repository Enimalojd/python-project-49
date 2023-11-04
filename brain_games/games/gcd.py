import math
import random


def get_description():
    return 'Find the greatest common divisor of given numbers.'


def get_question_answer():
    dig1 = random.randint(1, 50)
    dig2 = random.randint(1, 50)

    question = f'{dig1} {dig2}'
    answer = math.gcd(dig1, dig2)

    return question, str(answer)
