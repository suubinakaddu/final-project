import random

word_themes = {
    "Animals": ["dog" , "pony", "dshark", "zebra", "rhino"],
    "Fruits":["mango", "stawberry", "peach", "lime", "grape"],
    "Sports":["football","volleyball", "hockey", "boxing", "wrestling"],
    "Countries":["uganda", "korea", "canada", "england", "spain"],
    
}

difficulty_levels = {
    "Easy": {"length": 3, "attempts": 8},
    "Medium": {"length": 5, "attempts": 6},
    "Hard": {"length": 8, "attempts": 5},
}


def print_instructions():
    print("Welcome to themed wordle!")
    print("Instructions:")
    print("1. Choose a Theme")
    print("2. Choose a difficulty level (Easy, Medium, Hard).")
    print("3. Guess the word within the allowed attempts.")
    print("4. Feedback will be given")
    print("   - 'Green': Correct letter in the correct position.")
    print("   - 'Yellow': Correct letter in the wrong  position.")
    print("   - 'Gray': Letter not in the word\n")


def display_themes():
    print("Available Themes:")
    for i, theme in enumerate(word_themes.keys(), 1):
        print(f"{i}. {theme}")
    print()

# Validates theme
def choose_theme():
    while True:
        display_themes()
        choice= input("Choose a theme by entering the number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(word_themes):
            theme = list(word_themes.keys())[int(choice) - 1]
            print(f"You selected the theme: {theme}\n")
            return theme
        else:
            print("Invalid choice. Please try again.\n")
          

# Displays difficulty
def choose_difficulty():
    print("Difficulty levels")
    for level in difficulty_levels:
        print(f"- {level}")
    print()

    while True:
        choice=input("Choose a difficulty level (Easy, Medium, Hard): ").capitalize()
        if choice in difficulty_levels:
            print(f"You selected: {choice} difficulty\n")
            return choice
        else:
            print("Invalid choice Please try again.\n")

# Filters words based on difficulty
def get_filtered_words(theme,difficulty):
    word_list= word_themes[theme]
    word_length=difficulty_levels[difficulty]["length"]
    return[word for word in word_list if len(word) == word_length]

# Get feedback from guesses
def get_feedback(word,guess):
    feedback = []
    for i in range(len(word)):
        if guess[i] == word[i]:
            feedback.append("Green")
        elif guess[i] in word:
            feedback.append("Yellow")
        else:
            feedback.append("Gray")
    return feedback

# Main game loop
def play_game():
    print_instructions()
    theme=choose_theme()
    difficulty = choose_difficulty()

    # Filter words based on difficulty
    filtered_words= get_filtered_words(theme, difficulty)
    if not filtered_words:
        print(f"No words available for {theme} at {difficulty} difficulty. Please restart the game.\n")
        return
    word=random.choice(filtered_words)
    attempts=difficulty_levels[difficulty]["attempts"]
   

    print(f"The word has {len(word)} letters. You have {attempts} attempts. Start guessing!\n")

    for attempt in range(attempts):
        guess = input(f"Attempt {attempt + 1}/{attempts}: ").lower()

        if len(guess) != len(word):
            print(f"Your guess must be {len(word)} letters long. Try again\n")
            continue

        if guess == word:
            print("Congratulations! You guessed the word correctly!\n")
            break

        feedback = get_feedback(word, guess)
        print(f"Feedback: {' '.join(feedback)}\n")
    else:
        print(f"Out of attempts! The correct answers were: {word}\n")

# Run the game
if __name__=="__main__":
    play_game()
  
