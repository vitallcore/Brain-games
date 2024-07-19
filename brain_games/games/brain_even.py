from random import randint


def generate_question_and_answer():
    number = randint(1, 100)
    question = str(number)
    answer = 'yes' if number % 2 == 0 else 'no'
    return question, answer
