import prompt


def run_game(game):
    print('Welcome to the Brain Games!')

    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.get_description())

    game_rounds = 3

    for round_number in range(0, game_rounds):
        question, answer = game.get_question_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if answer != user_answer:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{answer}'. Let's try again, {name}!")
            return
        print('Correct!')

    print(f'Congratulations, {name}!')
