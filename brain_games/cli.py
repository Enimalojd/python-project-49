import prompt


def get_username():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
