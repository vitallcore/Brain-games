import random


def is_even(n):
    return n % 2 == 0


def game_even():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers_count = 0

    while correct_answers_count < 3:
        number = random.randint(1, 32)
        print(f"Question: {number}")
        answer = input("Your answer: ").strip().lower()

        if is_even(number):
            correct_answer = "yes"
        else:
            correct_answer = "no"

        if answer == correct_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    game_even()
