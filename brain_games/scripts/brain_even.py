from brain_games.engine import run_game
from brain_games.games import even


# Старт игры
def main():
    run_game(even.RULES, even.generate_round)


if __name__ == '__main__':
    main()