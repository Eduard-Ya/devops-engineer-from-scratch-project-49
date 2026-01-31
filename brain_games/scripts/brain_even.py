import random
from brain_games import engine


### Проверка на четность
def is_even(number):
    return number % 2 == 0


### Генерация раундов
def generate_round():
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer


### Старт игры
def main():
    rules = "Нужно ответить 'yes', если число чётное, или 'no' — если нечётное"
    engine.run_game(rules, generate_round)


if __name__ == '__main__':
    main()