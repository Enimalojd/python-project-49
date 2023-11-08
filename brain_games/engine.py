import prompt


def run_game(game):
    print('Welcome to the Brain Games!')

    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.get_description())

    game_rounds = 3

    while game_rounds > 0:

        question, answer = game.get_question_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == answer:
            print('Correct!')
            game_rounds -= 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'. Let's try again, {name}!")
            break

    if game_rounds == 0:
        print(f'Congratulations, {name}!')
