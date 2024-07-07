import random

MAX_ROUNDS = 3


def generate_question():
    num = random.randint(1, 100)
    question = f"{num}"
    answer = "yes" if num % 2 == 0 else "no"
    return question, answer


def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0

    while correct_answers < MAX_ROUNDS:
        question, correct_answer = generate_question()
        print(f"Question: {question}")

        user_answer = input("Your answer: ").strip().lower()

        if user_answer not in {"yes", "no"}:
            print(f"Please enter 'yes' or 'no'. Let's try again, {name}!")
            continue

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
