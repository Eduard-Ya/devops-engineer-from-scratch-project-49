from brain_games.engine import run_game
from brain_games.games import even


def main():
    """Start the Even game."""
    run_game(even.RULES, even.generate_round)


if __name__ == '__main__':
    main()