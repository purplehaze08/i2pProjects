import random
WORDS = ("cut", "purple", "haze", "king", "crimson")
word = random.choice(WORDS)

print("This word has:", len(word), "letters.")
print("You will have ten opportunities to guess letters and you shall enter the secret word after",\
      "you've used all ten opportunities.")
userGuess = input("Guess a word:")
userGuess = userGuess.lower()
userGuessTaken = 0

if userGuess == word:
    print("You got it!")
else:
    print("The guessing process starts now.")

while userGuess != word:
    guessLetter = input("Guess a letter")
    if len(guessLetter) > 1:
        print("Guess a letter not a word")
    elif guessLetter in word:
        print("Yes that letter is in the word")
        userGuessTaken = userGuessTaken + 1
        print("You have:", 10 - int(userGuessTaken), "opportunities left")
    else:
        print("The secret word does not contain that letter")
        print("You have:", 10 - int(userGuessTaken), "opportunities left")
    if userGuessTaken == 10:
        userGuessFinal = input("What do you think the secret word is?")
        if userGuessFinal == word:
            print("Well done!")
        elif userGuessFinal != word:
            print("You failed!")
            break








