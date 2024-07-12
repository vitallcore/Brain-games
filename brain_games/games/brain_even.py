from random import randint
from brain_games.games.game_engine import run_game

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_and_answer():
    number = randint(1, 100)
    question = str(number)
    answer = 'yes' if number % 2 == 0 else 'no'
    return question, answer


def main():
    run_game(DESCRIPTION, generate_question_and_answer)
