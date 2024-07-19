from random import randint
from math import gcd


def generate_question_and_answer():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question = f'{num1} {num2}'
    answer = gcd(num1, num2)
    return question, answer
