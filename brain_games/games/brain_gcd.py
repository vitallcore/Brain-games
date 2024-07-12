from random import randint
from math import gcd
from brain_games.games.game_engine import run_game

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_question_and_answer():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question = f'{num1} {num2}'
    answer = gcd(num1, num2)
    return question, answer


def main():
    run_game(DESCRIPTION, generate_question_and_answer)
