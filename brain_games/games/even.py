from random import randint
import prompt


def even_game():
    count = 3
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".\n')

    def is_even(x):
        if x % 2 == 0:
            return 1
        else:
            return 0

    while count > 0:
        dig = randint(0, 50)
        print(f"Question: {dig}")
        answer = prompt.string("Your answer: ")
        correct_answer = 'yes' if is_even(dig) else 'no'

        if answer == correct_answer:
            count -= 1
            print("Correct!\n")
        else:
            print(f"'{answer}' is the wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'. "
                  f"Let's try again, {name}!")
            break

    if count == 0:
        print(f'Congratulations, {name}!')

