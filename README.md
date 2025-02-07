# CLI Talking Cards for Language Lessons

#### Video Demo: https://youtu.be/kW6PL2qC5f8

A command-line implementation of the ESL speaking activity *Talking Cards*, designed to facilitate language learning conversations in both online and in-person settings. This program digitizes and streamlines the original card-based activity [created by Michael J. Brown](http://iteslj.org/Lessons/Brown-TalkingCards.html), making it more accessible for language tutors and students by combining question banks, cards and presentation in one place.
## Overview

*Talking Cards* is an interactive language language practicing tool that combines cards with questions to encourage natural conversation practice. The program supports both English Language Learners (ELL) and Spanish Language Learners (SLL), offering questions tailored to different proficiency levels (A2, B1, B2) according to the Common European Framework of Reference (CEFR).

## Key Features

- Bilingual support (English/Spanish).
- Selectable levels (A2-B1-B2).
- ASCII art card visualization.
- Customizable number of rounds.

## Technical implementation

### Project Structure

The main program (`project.py`) consists of several components:

#### DeckOfCards Class

* Manages a standard 52-card deck with suits and ranks.
  - Uses a dictionary for suit/rank symbols to enable easy visual differentiation.
* Deck creation, shuffling and card dealing.
* Access to see cards remaining.

#### Question Management

* Questions are stored in CSV files: (`questions/[language]_[level].csv`).
* Files are organized by language and CEFR level.
  * Each file uses `#` as a delimiter to allow commas `,` inside the questions.
  * Suits act as column headers and ranks as lines.
  * Cell format: `[rank];[question]` for each entry.

#### Game Flow Control

The initial setup is managed through a series of user inputs.

* Language selection (English/Spanish).
  * Bilingual interface messages determined by the initial selection.
* Skippable rules in terminal.
* Level selection (A2-B1-B2).
* Round selection (1-52).
* Card dealing and question presentation, with visual reminders of the question type and rounds left.

### Design Decisions

1. **Card Representation**

A class was chosen because it meets the criteria of the real world object:
  * Cards are tuples (rank, suit) for easy access to its parts without mutability.
  * Separate symbol dictionaries for flexible card display formatting.
  * Visual representation in ASCII art for better visual feedback in terminal environment.

2.**CSV Format choice**

  * Files can be easily editable with Excel, Google Sheets or other spreadsheet programs.
  * File size is really small.
  * Data has already a tabular format.

3.**Error Handling**

  * Input is validated for language, level and round selections inside each function.
  * Invalid CSV entries are skipped and debug information is logged.
    * If a file is not properly formatted is easy to see which category would be incomplete.
  * Missing question files and empty deck are handled to prevent program crashes.

4.**Modifications from the Original Game**

  * The point system was removed to focus on conversational fluency rather than performance.
  * Added round number selection for session flexibility.
  * Implemented proficiency level selection and bilingual support for broader applicability.

5.**Interactive Openning Screen**

To enhance user experience, the program incorporates an interactive opening screen that provides:

*   **Language Selection:** Users can choose their preferred language (English or Spanish) for the game interface and questions.
*   **Optional Rules Display:**  A prompt allows users to view the game rules if needed, with an option to skip for those already familiar with the game.
*   **Clear Navigation:**  The opening screen guides users through the initial setup process, making it easy to start a new game.

6.**Discarded features**

  * A timer was considered, but not implemented because it didn't fully aligned with the goal of achieving conversational fluency.

## Testing

The project includes unit tests to ensure the reliability and functionality of the core functions. The tests cover:

* Deck creation, shuffling, and dealing.
* Loading questions from CSV files.
* Correct display of card art and question types.

The tests are written using the `pytest` framework and can be run with the command `pytest`.


### Game instructions

The objective of the game is to get the students used to answer general questions, and as a consequence to gain conversational confidence. It is perfect for a no-prep speaking class.

A player draws a card and answer the corresponding question in four categories. Each suit corresponds to a specific question type:

- ♠ **Spades** (Descriptive questions)
- ♥ **Hearts** (What questions)
- ♣ **Clubs** (Mixed questions)
- ♦ **Diamonds** (Conditional questions)

After both players feel satisfied with their respective answers to the question, the one running the program can move to the next question.

### Usage
1. Run the program: `python project.py`.
2. Select language: "en" or "es".
3. Choose CEFR level: "A2", "B1", or "B2".
4. Enter desired number of rounds (1-52).
5. Press Enter after each question to proceed.


### Dependencies

The program uses only Python standard library modules:

- `random`: for deck shuffling.
- `csv`: for question files process.
- `pathlib`: for file accessing.

### Future enhancements

Potential areas for expansion could be:

* Additional language support.
* More CEFR levels (A1, C1, C2).
* Multiple questions set per level.
* Stopwatch to time each question
* Question evaluation (thumbs up 👍🏽 or thumbs down 👎🏽)
* Session statistics at the end of game, especially after tracking time.
