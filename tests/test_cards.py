from ..project import DeckOfCards


def test_deck_initialization():
    deck = DeckOfCards()
    assert len(deck.__cards) == 52


def test_shuffle():
    deck1 = DeckOfCards()
    deck2 = DeckOfCards()
    deck2.shuffle_deck()
    assert deck1.__cards != deck2.__cards


def test_deal_card():
    deck = DeckOfCards()
    initial_count = len(deck.__cards)
    card = deck.deal_card()
    # card was dealt
    assert len(deck.__cards) == initial_count - 1
    # card is not empty
    assert card is not None
    # card is tuple
    assert isinstance(card, tuple)


def test_empty_deck():
    deck = DeckOfCards()
    for _ in range(52):
        deck.deal_card()
    assert deck.deal_card() is None
