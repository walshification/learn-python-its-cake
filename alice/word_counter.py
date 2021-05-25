from collections import Counter
from sys import argv


def main():
    """Read a file given from the command line, count the numbers in it,
    and print the twenty most used words in the text.
    """
    if len(argv) != 2:
        print("Usage: ./word_counter.py file.txt")

    counter = Counter()

    with open(argv[1], "r") as f:
        for line in f:
            for word in line.split():
                counter[word.lower()] += 1

    for word, count in counter.most_common()[:20]:
        print(f"{word} --- {count}")


if __name__ == "__main__":
    main()
