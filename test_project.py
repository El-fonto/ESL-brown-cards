from project import DeckOfCards, load_questions, get_question_type, get_card_art

"""Deck Functionality Tests"""


# test deck creation
def test_create_deck():
    deck = DeckOfCards()
    assert len(deck._DeckOfCards__cards) == 52


# shuffled cards should be random
def test_shuffle_deck():
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


# str method is correctly printed
def test_deck_str():
    deck = DeckOfCards()
    assert "52 cards left" in str(deck)
    deck.deal_card()
    assert "51 cards left" in str(deck)


"""Question Loading"""


def test_load_questions():
    # test with valid language and level
    questions = load_questions("en", "A2")
    assert isinstance(questions, dict)  # return value should be a dict
    assert len(questions) > 0  # dict should not be empty

    # test with invalid language (empty dict)
    questions = load_questions("invalid", "A2")
    assert questions == {}


def test_get_card_art():
    card_art = get_card_art("Ace", "Hearts")
    assert "A ♥" in card_art  # check if art contains rank and suit symbols


def test_get_question_type():
    # English question type check
    question_type_english = get_question_type("Diamonds", "en")
    assert "♦ Conditional question ♦" in question_type_english
    assert question_type_english == "♦ Conditional question ♦ : "

    # Spanish question type check
    question_type_spanish = get_question_type("Clubs", "es")
    assert question_type_spanish == "♣ Pregunta mixta ♣ : "

