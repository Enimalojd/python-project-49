import random
import operator


def get_description():
    return 'What is the result of the expression?'


def get_question_answer():
    dig1 = random.randint(0, 50)
    dig2 = random.randint(0, 50)

    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    operator_symbol, operator_func = random.choice(list(operators.items()))

    question = f'{dig1} {operator_symbol} {dig2}'
    answer = operator_func(dig1, dig2)

    return question, str(answer)
