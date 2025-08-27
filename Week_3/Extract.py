import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    print("Fetched successfully")
else:
    print("Error")

soup = BeautifulSoup(response.text, "html.parser")

# one = soup.find_all("div",class_= "quote")
# print(one)

# one = soup.find("div",class_= "tags")
#print(one)
#print(one.text)

#one = soup.find_all("div",class_= "tags")
#for i in one:
    #print(i.text)

# links = one.find_all("a",class_="tags")
# print(links)

# quotes = soup.find_all("span",class_="text")
# print(quotes.text)

tags = soup.find_all("span", class_="tag-item")
for tag in tags:
    #print(i.get_text())
    
    links = tag.find("a", class_="tag")
    print(links.text)
    print(links['href'])