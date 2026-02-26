import prompt
from brain_games.cli import welcome_user


# Запуск игры с задаными правилами
def run_game(rules, generate_round):
    name = welcome_user()
    print(rules)

    rounds_count = 3
    for _ in range(rounds_count):
        question, correct_answer = generate_round()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer.lower() == correct_answer:
            print('Correct!')
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')