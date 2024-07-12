from random import randint
from brain_games.games.game_engine import run_game

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_question_and_answer():
    number = randint(1, 100)
    question = str(number)
    answer = 'yes' if is_prime(number) else 'no'
    return question, answer


def main():
    run_game(DESCRIPTION, generate_question_and_answer)
