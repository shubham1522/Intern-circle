import random

def guessing_game():
    secret = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess the number (1-100): "))
            attempts += 1

            if guess < secret:
                print("Too low!")
            elif guess > secret:
                print("Too high!")
            else:
                print(f"Correct! Attempts: {attempts}")
                break

        except ValueError:
            print("Enter a valid number.")

def word_counter():
    filename = input("Enter file name: ")

    try:
        with open(filename, "r") as file:
            text = file.read().lower()

        words = text.split()

        freq = {}

        for word in words:
            word = word.strip(".,!?")
            freq[word] = freq.get(word, 0) + 1

        print("\nTotal Words:", len(words))
        print("\nTop Frequencies:")

        for word, count in sorted(freq.items()):
            print(word, ":", count)

    except FileNotFoundError:
        print("File not found.")

while True:
    print("\n===== MENU =====")
    print("1. Number Guessing Game")
    print("2. Word Counter")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        guessing_game()
    elif choice == "2":
        word_counter()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")