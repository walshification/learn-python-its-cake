def get_numerical_input(message, number_type=float, prompt=">> "):
    """Get input from the user with a message and prompt.

    args:
        message (str): a message to be displayed before the prompt.
        number_type (int|float) [optional]: the type to cast the input
            to. Default float.
        prompt (str) [optional]: the sympbols to deplay there the user
            should type. Default ">> ".
    """
    print(message)
    while True:
        try:
            result = number_type(input(prompt))
        except ValueError:
            print("\nMust be a number value.\n")
        else:
            print("")
            break

    return result


def main():
    """Take as inputs the total bill price, the number of diners, and
    the tip percentage, and caluclates the cost per person.
    """
    total = get_numerical_input("How much is the bill?", prompt=">> $")

    people = get_numerical_input("How many people?", number_type=int)

    tip_percentage = get_numerical_input(
        "What percentage do you want to tip?", prompt=">> %"
    ) / 100

    print("Calculating Payment...")
    per_person = round(total / people, 2)
    tip = round(per_person * tip_percentage, 2)
    per_person_with_tip = round(per_person + tip, 2)

    print(f"Each person pays ${per_person:.2f} for the bill.")
    print(f"Each person pays ${tip:.2f} for the tip.")
    print(f"Which means each person pays a total of ${per_person_with_tip:.2f}.")


if __name__ == "__main__":
    main()
