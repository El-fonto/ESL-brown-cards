import random


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
    level = get_level()
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
        level
        language

        deck = DeckOfCards()
        random.seed(1)
        deck.shuffle_deck()
        print(f"first: {deck}")

        card = deck.deal_card()
        print(f"{card[0]} of {card[1]}")


def get_level():
    levels = ["A2", "B1", "B2"]
    while True:
        level = input("Level: ")
        if level.upper() in levels:
            return level
        else:
            print(f"======== Select: {levels} ========")


def get_language():
    languages = ["Spanish", "English"]
    while True:
        language = input(f"pick a language {languages}: ")
        if language.title() in languages:
            return language
        else:
            print("======== Not an implemented language ========")


if __name__ == "__main__":
    main()
