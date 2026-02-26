from brain_games.engine import run_game
from brain_games.games import progression


# Старт игры
def main():
    run_game(progression.RULES, progression.generate_round)


if __name__ == '__main__':
    main()