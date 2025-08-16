#Regular Expressions
#regex is a specialized languange within python for defining search patterns
#It has it's on syntax and some special symbols like \d, [], ^
#We can say it is filter that scans through data to find sequences that match the criteria given.
# Flexible - it can handle anything from simple text to conditional and grouped matches

#import re

#re.search() - Find the first match
import re
text = "I have 2 cats and 4 dogs"
match = re.search(r"\d", text)
matched = re.search(r"\w+", text)
print(match.group())
print(matched.group())

#we add .group because when using regex it stores details of the match. We use it to pull out the exact matched text.

#re.findall() n- Find all the matches

numbers = re.findall(r"\d", text)
words = re.findall(r"\w+", text)
strictly_words = re.findall(r"[A-Za-z]+", text)
print(numbers)
print(words)
print(strictly_words)

#re.match() - Check if it starts with a match

quote = "Kindness wins all the time"
print(re.match(r"Kindness", quote))
print(re.match(r"all", quote))

#re.split() - Cut text into pieces or clean up your data.

names = "Mary; Joy, Victor Salman; Atieno and Annex"
print(re.split(r"[,; ]+|and", names))

#re.sub = used to substitute

raw = "Cooking is very difficult"
better = re.sub(r"very", "sometimes", raw)
print(better)

#re.complile - compiles a patters for reuse
#re.fullmatch - match the entire string
#re.subn - works like sub but also tells you how many subs were made

#metacharacters

#matches any single character
text = "aa, ab, aaab, acb, dab"
pattern = r"[a.b]"
match = re.findall(pattern,text)
print(match)

#+ #matches one or more

#? #matches zero or one

#matches 0 or more repetitions of the preceding character
text = "aa, ab, aaab, acb, dab"
pattern = r"[a*b]"
match = re.findall(pattern,text)
print(match)

#CHARACTER CLASSES
text = "alpha, beta, omega, pi"
print(re.findall(r"[abc]", text))

#matches lower case
text = "Regex is fUn"
print(re.findall(r"[a-z]", text))

#matches digits
text = "They have 2 dogs, 5 fish and only 1 cat"
pattern = r"[0-9]"
numbers = re.findall(pattern, text)
print(numbers)

#ANCHORS
# ^ caret, $ Dollarsign

text = "I am good friend"
pattern = r"^I"
print(re.findall(pattern, text))

text = "pi, beta, omega, alpha"
pattern = r"[abc]$"
print(re.findall(pattern, text))

#word boundary \b - position sequence - it looks for non word characters
text = "fan fantastic fandom fanciful infant fanbase"

pattern = r"\bfan\b"

match = re.findall(pattern, text)

print(match)

#\B - not a word boundary, looks for words within words, or word characters.

text = "fan fantastic fandom fanciful infant fanbase"

pattern = r"\Bfan\B"

match = re.findall(pattern, text)

print(match)

#find all words that start with py

text = "We are learning python and python is fun pyooo pywi"
pattern = r"\bpy\w*"
match = re.findall(pattern, text)
print(match)

#find all words that have letters o or e in them.

text = "Hello, world! I love python"

pattern = r"\w*[oe]\w*\b"

match = re.findall(pattern,text)

print(match)

#find all 4 digit numbers

text = "2020 was a hard year but I got a new phone number 072084992762."

pattern = r"\d{4}"

match = re.findall(pattern, text)

print(match)

#Grouping
text = "phone number is (254) 456-7890"
pattern = r"(\(\d{3}\))\s\d{3}-(\d{4})"
match = re.search(pattern,text)

#print(match.group(0))
#print(match.group(1))
#print(match.group(2))

text = "My email is user@example.com or contact@domain.com and daisy.joy@gmail.com or dear-sir@gmail.com even s#care@gmail.co.ke"
#pattern = r"\b\w+[@]\w+\.[a-z]+"
pattern = r"\b[a-zA-Z0-9.-#]+[@][a-zA-Z0-9]+\.[a-z.]"
match = re.findall(pattern,text)
print(match)