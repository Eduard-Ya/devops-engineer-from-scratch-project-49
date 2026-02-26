from brain_games.engine import run_game
from brain_games.games import gcd


# Старт игры
def main():
    run_game(gcd.RULES, gcd.generate_round)

if __name__ == '__main__':
    main()