"""
Author: Chrispus Obare
A program that prompts a user for a word and checks if she you have it right@:
Everytime the user guesses the number of time are displayed at the end

"""
secret = "chris"
guess_count = 0  # Initialize the guess counter
hint = ["_"] * len(secret)  # Initialize the hint with underscores

while True:
    guesse = input("Please guess the word: ")
    guess_count += 1  # Increment the guess counter
    
    if len(guesse) != len(secret):
        print(f"Sorry, the guess must have the same number of letters as the secret word.")
        continue
    
    new_hint = hint.copy()  # Start with the current hint

    # First pass: Check for correct positions (uppercase)
    for i in range(len(secret)):
        if guesse[i] == secret[i]:
            new_hint[i] = guesse[i].upper()
    
    # Second pass: Check for correct letters in wrong positions (lowercase)
    for i in range(len(secret)):
        if guesse[i] != secret[i] and guesse[i] in secret:
            for j in range(len(secret)):
                if guesse[i] == secret[j] and new_hint[j] == "_" and guesse[j] != secret[j]:
                    new_hint[i] = guesse[i].lower()
                    break

    hint = new_hint  # Update the hint with the new values

    # Print the current hint
    print(f"Hint: {''.join(hint)}")
    
    # Check if the word is fully guessed
    if ''.join(hint).upper() == secret.upper():
        break

print(f"Congratulations! Your word is {''.join(hint)}")
print(f"It took you {guess_count} guesses to find the word.")
