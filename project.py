import random
import csv
from pathlib import Path
import os


class DeckOfCards:
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

    # lists to make cards
    SUITS = list(SUIT_SYMBOL.keys())
    RANKS = list(RANK_SYMBOL.keys())

    def __init__(self):
        # private list to populate with cards
        self.__cards = []
        self.create_deck()

    def create_deck(self):
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
    print("""

          =================
          CLI talking Cards
          =================

          """)

    language = get_language()
    clear_terminal()
    show_rules(language)

    level = get_level(language)
    clear_terminal()

    questions = load_questions(language, level)
    rounds = get_rounds(language)
    round_counter = 1

    deck = DeckOfCards()
    deck.shuffle_deck()

    # Game loop
    for _ in range(rounds):
        rounds_to_go = rounds - round_counter
        # updates to show correct number of rounds left
        round_counter += 1

        card = deck.deal_card()

        if not card:
            print("Deck is empty!")
            break

        rank, suit = card

        try:
            question = questions[suit][rank]
        except KeyError:
            question = f"No question was found for {rank} of {suit}"

        print("\n" + show_question_type(suit, language) + question)
        print(get_card_art(rank, suit))

        if language == "en":
            input(f"Rounds left: {rounds_to_go}\nPress Enter to continue...")
            clear_terminal()

        elif language == "es":
            input(f"Nos quedan {rounds_to_go} rondas\nPresiona Enter para continuar...")
            clear_terminal()

    if language == "en":
        print("Game Over! See you next time")

    elif language == "es":
        print("¡Fin del juego! Nos vemos la próxima")


def show_rules(language):
    if language == "en":
        rules = input("Do you want to see the rules? (Y/N): ").upper()
        if rules == "Y":
            print(
                """
            Welcome to the Talking Cards game!

            How to play:

            1.  A card is drawn from a shuffled deck.
            2.  You answer the question that matches the card. There are four types of questions:
                - ♠ Spades: Describe something.
                - ♥ Hearts: Answer a question about 'What'.
                - ♣ Clubs: Answer a mixed question.
                - ♦ Diamonds: Answer a question about 'If'.
            3.  Keep talking until you feel ready for the next question.
            4.  Repeat steps 1-3 until the game ends.

            Have fun and improve your speaking skills!
            """
            )

    elif language == "es":
        rules = input("¿Quieres ver las reglas? (S/N): ").upper()
        if rules == "S":
            print(
                """
            ¡Bienvenido al juego de Cartas para platicar!

            Cómo jugar:

            1. Se saca una carta de una baraja revuelta.
            2. Respondes la pregunta según la categoría de la carta. Hay cuatro tipos de preguntas:
                - ♠ Picas: Describe algo.
                - ♥ Corazones: Responde una pregunta sobre 'Qué'.
                - ♣ Tréboles: Responde una pregunta mixta.
                - ♦ Diamantes: Responde una pregunta condicional: 'Si...'.
            3. Habla hasta que ambos jugadores se sientan satisfechos y pasen la siguiente pregunta.
            4. Repite los pasos 1-3 hasta que termine el juego.

            ¡Diviértete y mejora tus habilidades para hablar!
            """
            )


def clear_terminal():
    os.system("clear")


def show_question_type(suit, language):
    en_question_type = {
        "Diamonds": "Conditional question",
        "Clubs": "Mixed question",
        "Spades": "Describing question",
        "Hearts": "What question",
    }

    es_question_type = {
        "Diamonds": "Pregunta condicional",
        "Clubs": "Pregunta mixta",
        "Spades": "Pregunta descriptiva",
        "Hearts": "Pregunta con qué",
    }

    symbol = DeckOfCards.SUIT_SYMBOL[suit]

    if language == "en" and suit in en_question_type:
        return f"{symbol} {en_question_type[suit]} {symbol} : "
    elif language == "es" and suit in es_question_type:
        return f"{symbol} {es_question_type[suit]} {symbol} : "
    else:
        return "?"


def get_level(language):
    levels = ["A2", "B1", "B2"]

    # match user's language input to continue during the game
    while True:
        if language == "en":
            level = input(f"Level {levels}: ").upper().strip()
            if level in levels:
                return level
            else:
                print(f"======== Select a level: {levels} ========")
        if language == "es":
            level = input(f"Nivel {levels}: ").upper().strip()
            if level in levels:
                return level
            else:
                print(f"======== Selecciona un nivel: {levels} ========")


def get_language():
    """Determine printing language"""
    languages = ["es", "en"]
    while True:
        language = input(f"pick a language {languages}: ").lower().strip()
        if language in languages:
            return language
        else:
            print("======== Not an implemented language ========")


def load_questions(language: str, level: str) -> dict:
    questions = {}
    filename = Path(f"questions/{language}_{level}.csv")

    try:
        with open(filename, "r") as file:
            reader = csv.reader(file, delimiter="#")
            # get header row ['Spades, 'Hearts', 'Clubs', 'Diamonds']
            suits = next(reader)

            # nested dict (suit: rank) in questions dict
            for suit in suits:
                questions[suit] = {}

            for row in reader:
                if len(row) != len(suits):
                    print(
                        f"Skipping invalid row: {row} (columns: {len(row)}, expected: {len(suits)})"
                    )
                    continue

                for i, cell in enumerate(row):
                    suit = suits[i]

                    try:
                        rank, question = cell.split(";", 1)

                        # add to nested dictionary: questions[suit][rank] (key) = question (value)
                        questions[suit][rank.strip()] = question.strip()

                    except ValueError:
                        print(f"Skipping invalid entry: {cell}")
                        continue

    except FileNotFoundError:
        print(f"Error: question file '{filename}' not found")
        return {}  # return empty dict to prevent crash

    return questions


def get_rounds(language):
    """Validate number of game loops"""
    while True:
        try:
            if language == "en":
                rounds = int(input("How many rounds are we playing? (1-52): "))
                if 1 <= rounds <= 52:
                    return rounds
            elif language == "es":
                rounds = int(input("¿Cuántas rondas vamos a jugar? (1-52): "))
                if 1 <= rounds <= 52:
                    return rounds
        except ValueError:
            print("Please enter a number (1-52) | Selecciona un número (1-52)")


def get_card_art(rank, suit):
    """ASCII art playing card"""
    rank_symbol = DeckOfCards.RANK_SYMBOL.get(rank, "?")
    suit_symbol = DeckOfCards.SUIT_SYMBOL.get(suit, "?")

    lines = [
        "┌─────────┐",
        f"│{rank_symbol} {suit_symbol.ljust(7)}│",  # left-aligned rank+suit
        "│         │",
        f"│    {suit_symbol}    │",  # centered suit
        "│         │",
        f"│{rank_symbol} {suit_symbol.rjust(6)} │",  # right-aligned rank+suit
        "└─────────┘",
    ]

    # special case for "10" rank
    if rank == "Ten":
        lines[1] = f"│{rank_symbol}{suit_symbol.ljust(7)}│"
        lines[5] = f"│{rank_symbol}{suit_symbol.rjust(6)} │"

    return "\n".join(lines)


if __name__ == "__main__":
    main()
