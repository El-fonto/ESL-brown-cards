import random


class DeckOfCards:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
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
    if level and language:
        deck = DeckOfCards()
        random.seed(1)
        deck.shuffle_deck()
        print(f"first: {deck}")
        for _ in range(52):
            card = deck.deal_card()
            print(f"{card[0]} of {card[1]}")
        print(f"second: {deck}")


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
