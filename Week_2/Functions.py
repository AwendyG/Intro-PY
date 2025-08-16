import re
text = "My email is user@example.com or contact@domain.com and daisy.joy@gmail.com or dear-sir@gmail.com even s#care@gmail.co.ke"
#pattern = r"\b\w+[@]\w+\.[a-z]+"
pattern = r"\b[a-zA-Z0-9.-#]+[@][a-zA-Z0-9]+\.[a-z.]"
match = re.findall(pattern,text)
print(match)