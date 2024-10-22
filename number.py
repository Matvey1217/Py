import random

def guess():
    number = random.randint(1, 10)
    attempts = 3

    print("Відгадай число від 1 до 10.В тебе 3 спроби.")

    for attempt in range(attempts):
        guess = int(input(f"Спроба: Введи число: "))

        if guess > number:
            print("Менше!")
        elif guess < number:
            print("Більше!")
        else:
            print("Ти вгадав!")
            return

    print(f"Ти не вгадав! Правильне число було: {number}")


guess()
