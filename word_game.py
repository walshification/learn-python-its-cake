"""
Create a word game that takes in a txt file to learn words and assigns
each word a point value based on how many times it appears.

The game takes input from the players on how many rounds to play.

A round ends when a player completes a word or creates an impossible
word.

The player that did not complete the word is awarded the word's points.

After a word is used, the word is removed from the game's dictionary.

After all the rounds are played, the winner is displayed and the game
asks if players would like to play again.

If another game is played, all words and word values removed from the
previous game are put back in.
"""
from alice.word_counter import count_words


class Player:
    """Object to help keep track of player state."""

    def __init__(self, name):
        """Constructs the player.

        args:
            name (str): the name of the player.
        """
        self.name = name
        self.score = 0


class WordGame:
    """Object to manage game state."""

    def __init__(self, dictionary_source):
        """Sets up a new game."""
        self.players = [Player("Player 1"), Player("Player 2")]
        self.rounds_total = 0
        self.word_count_map = self.populate_dictionary(dictionary_source)
        self._game_dictionary = None

    @property
    def game_dictionary(self):
        """Property to access the dictionary for the currently running
        game.
        """
        if self._game_dictionary is None:
            self._game_dictionary = self.word_count_map.copy()
        return self._game_dictionary

    def populate_dictionary(self, source):
        """Tally up the words from the source dictionary or reuse a
        previously created dictionary.
        """
        print("Loading Words...")
        word_count_map = count_words(source)
        print("Loading Complete!!!")
        return word_count_map

    def play(self):
        """Start a game!"""
        print("Game Starting...")
        play = True
        while play:
            rounds_total = self.get_rounds()

            for i in range(1, rounds_total + 1):
                print(f"Round {i}")
                print(
                    f"\n{self.players[0].name}: {self.players[0].score}     "
                    f"{self.players[1].name}: {self.players[1].score}\n"
                )
                self.play_round(i)

            print("\nRound Limit Reached\n")
            print(
                f"{self.players[0].name}: {self.players[0].score}     "
                f"{self.players[1].name}: {self.players[1].score}\n"
            )
            if self.players[0].score > self.players[1].score:
                print(f"{self.players[0].name} WINS!!!")
            elif self.players[1].score > self.players[0].score:
                print(f"{self.players[1].name} WINS!!!")
            else:
                print("There was a TIE!!!")
            print("")

            play_again = input(
                "Type \"q\" to quit or \"<any key>\" to play again: "
            ) != "q"

            if not play_again:
                print("\nThank You for Playing!!!")
                break
            self.reset()

    def get_rounds(self):
        """Ask the players how many rounds they want to play and return the
        input.

        returns: (int)
        """
        total = 0
        while True:
            try:
                total = int(
                    input(
                        "\nChoose Game Length, how many Rounds? "
                        "[enter a number larger than 0]: "
                    )
                )
                assert total > 0
            except ValueError:
                print("An Error Occured, make sure you enter an Integer.")
            except AssertionError:
                print("Please enter a number greater than 0.")
            else:
                break

        return total

    def play_round(self, current_player):
        """Play a round."""
        current_word = ""
        while True:
            current_player = (current_player + 1) % 2
            letter = input(
                f"\n{self.players[current_player].name} Please enter a letter: "
            )
            current_word += letter
            other_player = (current_player + 1) % 2
            if self.not_a_word(current_word) or current_word in self.game_dictionary:
                self.players[other_player].score += self.game_dictionary[current_word]

                print("\n" + ("!#YAH#!" * 10))
                print("")
                print(f"                Winning Word = \"{current_word}\"")
                print("")
                print(
                    f"    {self.players[other_player].name} just won that Round!!! "
                    f"({self.game_dictionary[current_word]} points)"
                )
                print("")
                print("!#YAH#!" * 10)
                del self.game_dictionary[current_word]
                break

    def not_a_word(self, fragment):
        """Checks if a word fragment is a valid potential word."""
        for word in self.game_dictionary.keys():
            if len(fragment) < len(word) and fragment == word[:len(fragment)]:
                return False
        return True

    def reset(self):
        """Return the game to its starting state."""
        self.players = [Player("Player 1"), Player("Player 2")]
        self.rounds_total = 0
        self._game_dictionary = None


def main():
    """Would you like to play a game?"""
    print(
        """
The Word Game
==============================
"""
    )
    game = WordGame("alice/alice.txt")

    game.play()


if __name__ == "__main__":
    main()
