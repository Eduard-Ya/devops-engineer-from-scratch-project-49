import secrets

RULES = 'What number is missing in the progression?'


# Генерация арефмитической прогрессии
def generate_progression(start, step, length):
    progression = []
    for i in range(length):
        progression.append(start + i * step)
    return progression


# Генерация раундов
def generate_round():
    start = secrets.randbelow(20) + 1 
    step = secrets.randbelow(10) + 1
    length = secrets.randbelow(6) + 5  # от 5 до 10 элементов
    
    # Создаем прогрессию
    progression = generate_progression(start, step, length)
    
    # Выбираем случайную позицию для скрытого элемента
    hidden_index = secrets.randbelow(length)
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