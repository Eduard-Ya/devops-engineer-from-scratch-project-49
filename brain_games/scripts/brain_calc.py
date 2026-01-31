import random
from brain_games import engine


### вычисление на основе операции
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    else:
        raise ValueError(f'Unknown operation: {operation}')


### Генерация раундов
def generate_round():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operation = random.choice(['+', '-', '*'])
    
    question = f'{num1} {operation} {num2}'
    correct_answer = calculate(num1, num2, operation)
    
    return question, str(correct_answer)


### Старт игры 
def main():
    rules = 'What is the result of the expression?'
    engine.run_game(rules, generate_round)


if __name__ == '__main__':
    main()