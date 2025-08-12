# Conditional statements

# make decisions; True, False
# if, else

age = int(input("How old are you?"))

# if age is above 18, you are an adult
# if below 18, you are minor

if age <= 10:
    print("You are a  baby")
elif age >10 and age <= 18:
    print("You are a teen,pray alittle")
elif age > 18 and age <= 25:
    print("Dear young adult,start Praying")
else:
    print("You are an adult, pray without ceasing")