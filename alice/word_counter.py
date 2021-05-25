from collections import Counter
from sys import argv


def count_words(file_name):
    """Counts the words of a file. Returns a dictionary of the words
    found along with their counts.
    """
    counter = Counter()
    with open(file_name, "r") as f:
        for line in f:
            for word in line.split():
                counter[word.lower()] += 1

    return counter


def main():
    """Read a file given from the command line, count the numbers in it,
    and print the twenty most used words in the text.
    """
    if len(argv) != 2:
        print("Usage: ./word_counter.py file.txt")

    counter = count_words(argv[1])

    for word, count in counter.most_common()[:20]:
        print(f"{word} --- {count}")


if __name__ == "__main__":
    main()
