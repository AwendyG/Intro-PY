import requests
from bs4 import BeautifulSoup

url = "https://www.boredpanda.com/"
response = requests.get(url)

print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

trial = soup.find_all("article", class_="post")

for i in trial:
    print(i.get_text())