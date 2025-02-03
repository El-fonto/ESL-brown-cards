import random
import csv
from pathlib import Path

# TODO:
# When printing, it would be nice to remember what's the rank/type of question, the name of the card, next to art and the question in a box
# Fix .csv es/b1 and es/b2
# Check if I could use 1 data structure only RANK_SYMBOL and SUIT_SYMBOL and update the class to not use the list and only use the keys of the dict


class DeckOfCards:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Jack",
        "Queen",
        "King",
    ]
    # Dictionaries to draw art
    SUIT_SYMBOL = {"Hearts": "♥", "Diamonds": "♦", "Clubs": "♣", "Spades": "♠"}
    RANK_SYMBOL = {
        "Ace": "A",
        "Two": "2",
        "Three": "3",
        "Four": "4",
        "Five": "5",
        "Six": "6",
        "Seven": "7",
        "Eight": "8",
        "Nine": "9",
        "Ten": "10",
        "Jack": "J",
        "Queen": "Q",
        "King": "K",
    }

    def __init__(self):
        # private list to populate with cards
        self.__cards = []
        self.create_deck()

    def create_deck(self):
        # tuple card
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.__cards.append((rank, suit))
        return self.__cards

    def shuffle_deck(self):
        random.shuffle(self.__cards)

    def deal_card(self):
        # end of the list card is the top of the deck
        if len(self.__cards) == 0:
            return None
        return self.__cards.pop()

    def __str__(self):
        return f"The deck has {len(self.__cards)} cards left"


def main():
    # random seed for testing purposes
    random.seed(1)
    language = get_language()
    level = get_level(language)
    questions = load_questions(language, level)
    rounds = get_rounds()
    counter = 0

    # single deck and shuffle it once for playing
    deck = DeckOfCards()
    deck.shuffle_deck()

    # Game loop
    for _ in range(rounds):
        rounds_to_go = rounds - counter
        card = deck.deal_card()

        if not card:
            print("Deck is empty!")
            break

        # unpack tuple
        rank, suit = card

        # get questions and prevent errors
        try:
            question = questions[suit][rank]
        except KeyError:
            question = f"No question was found for {rank} of {suit}"

        counter += 1
        print("\n" + get_question_type(suit) + question)
        print("\n" + get_card_art(rank, suit))
        # print(deck)

        input(f"{rounds_to_go} rounds are left\nPress Enter to continue...")

    print("Game Over! See you next time")


def get_question_type(suit):
    """match questions to print"""
    question_type = {
        "Diamonds": "Conditional question",
        "Clubs": "Mixed question",
        "Spades": "Describing a thing",
        "Hearts": "What question",
    }

    symbol = DeckOfCards.SUIT_SYMBOL[suit]

    if suit in question_type:
        return f"{symbol} {question_type[suit]} {symbol}: "
    else:
        return "?"


def get_level(language):
    # list to add more levels, if necessary
    levels = ["A2", "B1", "B2"]

    # match user's language input to continue during the game
    while True:
        if language == "en":
            level = input(f"Level {levels}: ").upper()
            if level in levels:
                return level
            else:
                print(f"======== Select a level: {levels} ========")
        if language == "es":
            level = input(f"Nivel {levels}: ").upper()
            if level in levels:
                return level
            else:
                print(f"======== Selecciona un nivel: {levels} ========")


def get_language():
    """determine printing language"""
    # list to add more laguages, if necessary
    languages = ["es", "en"]
    while True:
        language = input(f"pick a language {languages}: ")
        if language.lower() in languages:
            return language
        else:
            print("======== Not an implemented language ========")


def load_questions(language, level):
    """handle csv file and output a questions dictionary"""
    questions = {}
    filename = Path(f"questions/{language}_{level}.csv")

    try:
        with open(filename, "r") as file:
            # read the csv
            reader = csv.reader(file, delimiter="#")
            # get header row ['Spades, 'Hearts', 'Clubs', 'Diamonds']
            suits = next(reader)

            # nested dict (suit: rank) in questions dict
            for suit in suits:
                questions[suit] = {}

            # process remaining rows
            for row in reader:
                # prevent inappropriate card generation checking correct row length
                if len(row) != len(suits):
                    # message to debug properly
                    print(
                        f"Skipping invalid row: {row} (columns: {len(row)}, expected: {len(suits)})"
                    )
                    continue

                # tuple `i, cell` that comes with `index,value` using enumerate()
                for i, cell in enumerate(row):
                    suit = suits[i]

                    try:
                        # split in two parts at the ';'
                        rank, question = cell.split(";", 1)

                        # add to nested dictionary: questions[suit][rank] (key) = question (value)
                        questions[suit][rank.strip()] = question.strip()

                    except ValueError:
                        print(f"Skipping invalid entry: {cell}")
                        # continue with loop to next cell
                        continue

    except FileNotFoundError:
        print(f"Error: question file '{filename}' not found")
        return {}  # return empty dict to prevent crash

    return questions


def get_rounds():
    """Validate number of game loops"""
    while True:
        try:
            rounds = int(input("Rounds to play (1-52): "))
            if 1 <= rounds <= 52:
                return rounds
        except ValueError:
            print("Please enter a number between 1 and 52")


def get_card_art(rank, suit):
    """Generate ASCII art for a playing card"""
    # default return is '?', in case no rank or suit are in dict
    rank_symbol = DeckOfCards.RANK_SYMBOL.get(rank, "?")
    suit_symbol = DeckOfCards.SUIT_SYMBOL.get(suit, "?")

    # Define card lines
    lines = [
        "┌─────────┐",
        f"│{rank_symbol} {suit_symbol.ljust(7)}│",  # Left-aligned rank+suit
        "│         │",
        f"│    {suit_symbol}    │",  # Centered suit
        "│         │",
        f"│{rank_symbol} {suit_symbol.rjust(7)}│",  # Right-aligned rank+suit
        "└─────────┘",
    ]

    # Special case for "10" rank
    if rank == "Ten":
        lines[1] = f"│{rank_symbol}{suit_symbol.ljust(7)}│"
        lines[5] = f"│{rank_symbol}{suit_symbol.rjust(7)}│"

    return "\n".join(lines)


if __name__ == "__main__":
    main()
