

def calculator():
    while True:
        print("\n--- Basic Calculator ---")

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        operator = input("Enter operation (+, -, *, /): ")

        if operator == "+":
            print("Result:", num1 + num2)

        elif operator == "-":
            print("Result:", num1 - num2)

        elif operator == "*":
            print("Result:", num1 * num2)

        elif operator == "/":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                print("Result:", num1 / num2)

        else:
            print("Invalid operator!")

        break


def unit_converter():
    while True:
        print("\n--- Unit Converter ---")
        print("1. Kilometers to Miles")
        print("2. Celsius to Fahrenheit")
        print("3. Back")

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                km = float(input("Enter kilometers: "))
                miles = km * 0.621371
                print(f"{km} km = {miles:.2f} miles")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "2":
            try:
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = (celsius * 9 / 5) + 32
                print(f"{celsius}°C = {fahrenheit:.2f}°F")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            break

        else:
            print("Invalid choice. Try again.")


def currency_converter():
    while True:
        print("\n--- Currency Converter ---")
        print("1. USD to INR")
        print("2. INR to USD")
        print("3. Back")

        choice = input("Choose an option: ")

        # Example learning rate — update when needed
        usd_to_inr = 90.0

        if choice == "1":
            try:
                usd = float(input("Enter USD amount: "))
                print(f"${usd:.2f} = ₹{usd * usd_to_inr:.2f}")
            except ValueError:
                print("Please enter a valid amount.")

        elif choice == "2":
            try:
                inr = float(input("Enter INR amount: "))
                print(f"₹{inr:.2f} = ${inr / usd_to_inr:.2f}")
            except ValueError:
                print("Please enter a valid amount.")

        elif choice == "3":
            break

        else:
            print("Invalid choice. Try again.")


def main():
    while True:
        print("\n==============================")
        print(" Calculator & Unit Converter")
        print("==============================")
        print("1. Basic Calculator")
        print("2. Unit Converter")
        print("3. Currency Converter")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            calculator()

        elif choice == "2":
            unit_converter()

        elif choice == "3":
            currency_converter()

        elif choice == "4":
            print("Thanks for using the program!")
            break

        else:
            print("Invalid choice. Please select 1-4.")


main()