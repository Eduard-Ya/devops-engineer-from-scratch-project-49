import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# Проверяем простое ли число 
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Проверяем делители до квадратного корня из n
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2  # Проверяем только нечетные делители
    
    return True


# Генерация раундов
def generate_round():
    # Генерируем число от 1 до 100 (можно изменить диапазон)
    number = random.randint(1, 100)
    
    question = str(number)
    correct_answer = 'yes' if is_prime(number) else 'no'
    
    return question, correct_answer