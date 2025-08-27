import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

response = requests.get(url)

#print(response.text[:500])
#print(response.status_code)

#if response.status_code == 200:
    #print("fetched succesfully")
#else:
    #print("Error")

soup = BeautifulSoup(response.text, "html.parser")
#headlines=soup.find_all("h2")

#for h in headlines[:10]:
    #print(h.text)
    #print(h.get_text())

sample = soup.find("div", class_="sc-9d830f2a-1 dOyfhs")
    
print(sample.get_text())

sample = soup.find_all("div", class_="sc-9d830f2a-1 dOyfhs")
    
for div in sample:
    print(div.get_text())