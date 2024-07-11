import random

MAX_ROUNDS = 3


def generate_progression():
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    length = 10
    progression = [start + step * i for i in range(length)]

    missing_index = random.randint(0, length - 1)
    missing_number = progression[missing_index]
    progression[missing_index] = '..'

    question = ' '.join(map(str, progression))
    return question, missing_number


def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")

    correct_answers = 0

    while correct_answers < MAX_ROUNDS:
        question, correct_answer = generate_progression()
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
