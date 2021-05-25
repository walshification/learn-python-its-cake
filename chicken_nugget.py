class TotalError(Exception):
    """Custom error if we can't math up a solution."""
    pass


def calculate_packs(total):
    """Calculates the required combination of chicken nugget packs to
    get a total number for a party.

    args:
        total (int): the total required nuggets.
    """
    count = 0
    six_packs = 0
    nine_packs = 0
    twenty_packs = 0

    for six_packs in range((total // 6) + 1):
        for nine_packs in range((total // 9) + 1):
            for twenty_packs in range((total // 20) + 1):
                count = 6 * six_packs + 9 * nine_packs + 20 * twenty_packs
                if count == total:
                    return six_packs, nine_packs, twenty_packs

    raise TotalError


def main():
    """Ask for a number of nuggets for a party, and then display the
    necessary combinations of packs to get that many.
    """
    print(
        """Nugget Program
==============================
"""
    )
    while True:
        try:
            total = input(
                "How many Nuggets do you need in your Party, [type 'q' to exit]: "
            )
            if total == "q":
                break

            total = int(total)
            six_packs, nine_packs, twenty_packs = calculate_packs(total)
        except ValueError:
            print("An Error Occurred. Make sure you enter an Integer.")

        except TotalError:
            print(f"\nNo solution for : {total} nuggets.\n")

        else:
            print(
                f"\n6-packs = {six_packs}, "
                f"9-packs = {nine_packs}, "
                f"20-packs = {twenty_packs}\n"
            )


if __name__ == "__main__":
    main()
