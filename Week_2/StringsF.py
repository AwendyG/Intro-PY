name = "Joy"
Hobby = "travelling"

print(f"My name is {name} and I love {Hobby}")

txt = "Live out loud"

print("out" in txt)
print ("love" not in txt)

#Read mode

file = open(r"C:\Users\Pc\OneDrive\Desktop\Intro to programming\Week_2\quotes.txt", "r")

content = file.read()

print(content)

file.close()

#with statement; closes the file immdiately and is the the safest option

with open(r"C:\Users\Pc\OneDrive\Desktop\Intro to programming\Week_2\quotes.txt", "r") as file:

    content = file.read()
    print(content)

with open(r"C:\Users\Pc\OneDrive\Desktop\Intro to programming\Week_2\quotes.txt", "r") as file:

    content = file.readline()

    contents = file.readlines()

    print(content)

    print(contents[0])

    print(contents[2]) 

#Append Mode

with open(r"C:\Users\Pc\OneDrive\Desktop\Intro to programming\Week_2\quotes.txt", "a") as file:
    
    file.write("\nLife is for the living")

#Write mode

with open(r"C:\Users\Pc\OneDrive\Desktop\Intro to programming\Week_2\trial.txt", "w") as file:

    file.write("Hello world")

#Write a program that takes a sentence and then prints the number of words in that sentence.

text = input("Type in a random sentence:")
