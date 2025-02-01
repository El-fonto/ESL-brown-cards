import random
import csv
from pathlib import Path


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
        return f"The deck has {len(self.__cards)} cards"


def main():
    language = get_language()
    level = get_level(language)
    questions = load_questions(language, level)

    # Input validation for possible amount of rounds
    while True:
        try:
            rounds = int(input("Rounds to play (1-52): "))
            if 1 <= rounds <= 52:
                break
        except ValueError:
            print("Please enter a number between 1 and 52")

    # Game loop
    for _ in range(rounds):
        deck = DeckOfCards()
        random.seed(1)
        deck.shuffle_deck()
        card = deck.deal_card()

        if not card:
            print("Deck is empty!")
            break

        rank, suit = card
        try:
            question = questions[suit][rank]
        except KeyError:
            question = f"No question was found for {rank} of {suit}"

        print(f"Card: {rank} of {suit}")
        print(f"Question: {question}")
        input("\nPress Enter to continue...")

    print("Game Over! See you next time")


def get_level(language):
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
    languages = ["es", "en"]
    while True:
        language = input(f"pick a language {languages}: ")
        if language.lower() in languages:
            return language
        else:
            print("======== Not an implemented language ========")


def load_questions(language, level):
    # dictionary to store questions
    questions = {}
    filename = Path(f"questions/{language}_{level}.csv")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            # read the csv
            reader = csv.reader(file, delimiter="#")
            # get header row ['Spades, 'Hearts', 'Clubs', 'Diamonds']
            suits = next(reader)

            # nested dict (suit: rank) in questions dict
            for suit in suits:
                questions[suit] = {}

            # process remaining rows

            for row in reader:
                # use enumerate to
                if len(row) != len(suits):
                    print(
                        f"Skipping invalid row: {row} (columns: {len(row)}, expected: {len(suits)})"
                    )
                    continue
                for i, cell in enumerate(row):
                    suit = suits[i]

                    try:
                        # split in two parts at the ';'
                        rank, question = cell.split(";", 1)

                        # add to nested dictionary: questions[suit][rank] = question
                        questions[suit][rank.strip()] = question.strip()

                    except ValueError:
                        print(f"Skipping invalid entry: {cell}")
                        # continue with loop to next cell
                        continue

    except FileNotFoundError:
        print(f"Error: question file '{filename}' not found")
        # return empty dict to prevent crash
        return {}

    return questions


if __name__ == "__main__":
    main()
