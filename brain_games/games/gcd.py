import secrets

RULES = 'Find the greatest common divisor of given numbers.'


# Алгоритм Евклида
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Генерация раундов
def generate_round():
    num1 = secrets.randbelow(100) + 1
    num2 = secrets.randbelow(100) + 1
    
    question = f'{num1} {num2}'
    correct_answer = gcd(num1, num2)
    
    return question, str(correct_answer)