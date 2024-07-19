#!/usr/bin/env python3

from brain_games.game_engine import run_game
from brain_games.games.brain_gcd import generate_question_and_answer

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def main():
    run_game(DESCRIPTION, generate_question_and_answer)


if __name__ == "__main__":
    main()
