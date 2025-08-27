import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_banks_in_Kenya"

response = requests.get(url)

soup =BeautifulSoup(response.text, "html.parser")

main = soup.find("div", class_="mw-content-ltr mw-parser-output")
# print(main)

items = main.find("ul")
# print(items)

links = items.find_all("li")

for link in links:
    print(link.text)