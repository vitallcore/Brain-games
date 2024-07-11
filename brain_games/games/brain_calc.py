import random
import operator

MAX_ROUNDS = 3


def generate_question():
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }

    num1 = random.randint(1, 100)
    num2 = random.randint(num1, 100)
    op_symbol = random.choice(list(operations.keys()))
    op_function = operations[op_symbol]

    question = f"{num2} {op_symbol} {num1}"
    answer = op_function(num2, num1)

    return question, answer


def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")

    correct_answers = 0

    while correct_answers < MAX_ROUNDS:
        question, correct_answer = generate_question()
        print(f"Question: {question}")

        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print(f"Please enter a valid number. Let's try again, {name}!")
            continue

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(."
                f" Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
