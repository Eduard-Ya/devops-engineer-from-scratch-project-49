import random

RULES = 'Find the greatest common divisor of given numbers.'


# Алгоритм Евклида
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Генерация раундов
def generate_round():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    
    question = f'{num1} {num2}'
    correct_answer = gcd(num1, num2)
    
    return question, str(correct_answer)