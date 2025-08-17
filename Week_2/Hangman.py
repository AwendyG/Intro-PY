import random

options = ["luxury", "lucky", "banjo", "quiz", "zipper", "too"]
x =random.choice(options)
lives = 5
guessed_letters = set()

hidden = []
for letter in x:
    hidden += ["-"]
print(hidden)

while lives > 0:
    print("word:", "".join(hidden))
    print("Lives left:", lives)

    if "-" not in hidden:
        print("Congratulations, you did it!")
        break

    while True:
        try:
            guess = input("Guess a letter to make up a word:").strip()

            #Input must be only one character
            if len(guess) != 1:
                raise ValueError ("You can only input one letter")
    
            #Input must be a letter
            if guess not in "abcdefghijklmnopqrstuvwxyz":
                raise ValueError ("You can only input a letter")
    
            #Input should not have been guessed before
            if guess in guessed_letters:
                raise ValueError ("You have already guessed this")

            break
            
        except ValueError as e:
            print("Invalid input:", e)

    guessed_letters.add(guess) #valid guess is stored here

    if guess in x:
        for i, letter in enumerate(x):
            if letter == guess:
                hidden[i] = guess
        print("Good guess!")
    else:
        lives -= 1
        print("Try again!")

if lives == 0 and "-" in hidden:
    print("Maybe next time. The word was:", x)

