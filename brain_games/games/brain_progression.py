from random import randint


def generate_question_and_answer():
    start = randint(1, 10)
    step = randint(1, 10)
    length = 10
    progression = [start + i * step for i in range(length)]
    missing_index = randint(0, length - 1)
    answer = progression[missing_index]
    progression[missing_index] = '..'
    question = ' '.join(map(str, progression))
    return question, answer
