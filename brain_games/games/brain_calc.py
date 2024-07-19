from random import randint, choice


def generate_question_and_answer():
    num1 = randint(1, 100)
    num2 = randint(num1, 100)
    operation = choice(['+', '-', '*'])
    if operation == '+':
        answer = num2 + num1
    elif operation == '-':
        answer = num2 - num1
    else:
        answer = num2 * num1
    question = f'{num2} {operation} {num1}'
    return question, answer
