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
        # tuple card: Hearts,Diamonds, Clubs, and Spades in that order, from lowest to highest rank

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
    deck = DeckOfCards()
    random.seed(1)
    deck.shuffle_deck()
    print(f"first: {deck}")
    for _ in range(52):
        card = deck.deal_card()
        print(f"{card[0]} of {card[1]}")
    print(f"second: {deck}")


if __name__ == "__main__":
    main()
