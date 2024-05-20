"""
Author: Moraa Chrispus Obare
A simple word program game that allow a user to guesse the word prompted by the program
"""
#we begin by declaring the name, and storing the name in the variable secret
#We save the new word and we as well get the legnth of the real word to help us identify if the guessed word is correct or not
#The word must be exactly the same as the number of letter provided
secret = "chris"
lnew = ["_"] * len(secret)  # use a list to hold the current state of the guessed word

while True:
    guesse = input(f"Please guess what the word is and your hint is {''.join(lnew)} ")
    
    if len(guesse) != len(secret):
        print(f"Sorry, the guess must have the same number of letters as the secret word. Your hint is {''.join(lnew)}\n")
        continue
    
    for i in range(len(secret)):
        if guesse[i] == secret[i]:
            lnew[i] = guesse[i]
    
    # This part updates lnew if the guessed letter is in the secret word but not in the correct position.
    for i in range(len(secret)):
        if guesse[i] in secret and guesse[i] != secret[i]:
            for j in range(len(secret)):
                if guesse[i] == secret[j] and lnew[j] == "_":
                    lnew[j] = guesse[i]
                    break  # Ensure only the first occurrence is replaced to avoid overwriting correct guesses
    
    if ''.join(lnew) == secret:
        break 

print(f"Your word is {''.join(lnew)}")

