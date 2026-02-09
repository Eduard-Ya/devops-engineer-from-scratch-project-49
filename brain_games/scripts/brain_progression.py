import random
from brain_games import engine


### Генерация арефмитической прогрессии
def generate_progression(start, step, length):
    progression = []
    for i in range(length):
        progression.append(start + i * step)
    return progression


### Генерация раундов
def generate_round():
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    length = random.randint(5, 10)  # от 5 до 10 элементов
    
    # Создаем прогрессию
    progression = generate_progression(start, step, length)
    
    # Выбираем случайную позицию для скрытого элемента
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    
    # Создаем строку вопроса с ".." вместо скрытого элемента
    question_parts = []
    for i, num in enumerate(progression):
        if i == hidden_index:
            question_parts.append('..')
        else:
            question_parts.append(str(num))
    
    question = ' '.join(question_parts)
    
    return question, str(correct_answer)


### Старт игры
def main():
    rules = "What number is missing in the progression?"
    engine.run_game(rules, generate_round)


if __name__ == '__main__':
    main()