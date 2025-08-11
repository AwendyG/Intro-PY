#i=0

#while i < 5:
#print("i is", i)
# i=i+1

#else:
  #print("i is greater than or equal to 5")   

number = 7
guess = None

while guess != number:

    guess = input("Guess again: ")
    guess = int(guess)

print("You did it!")