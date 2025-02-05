import pytest
from ..project import DeckOfCards


# test deck creation
def test_deck_initialization():
    deck = DeckOfCards()
    assert len(deck._DeckOfCards__cards) == 52


# shuffled cards should be random
def test_shuffle():
    deck1 = DeckOfCards()
    deck2 = DeckOfCards()
    deck2.shuffle_deck()
    assert deck1._DeckOfCards__cards != deck2._DeckOfCards__cards


def test_deal_card():
    deck = DeckOfCards()
    initial_count = len(deck._DeckOfCards__cards)
    card = deck.deal_card()
    # card was dealt
    assert len(deck._DeckOfCards__cards) == initial_count - 1
    # card is not empty
    assert card is not None
    # card is tuple
    assert isinstance(card, tuple)


# when empty it should return None
def test_empty_deck():
    deck = DeckOfCards()
    for _ in range(52):
        deck.deal_card()
    assert deck.deal_card() is None
