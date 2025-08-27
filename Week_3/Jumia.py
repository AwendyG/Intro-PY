import re
import csv
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.jumia.co.ke/mlp-top-sellers/"

response = requests.get(url)

#print(response.status_code) - confirmed that the requst was succefull

soup = BeautifulSoup(response.text, 'html.parser')

product_names = []
product_name = soup.find_all("h3", class_="name")
for product in product_name:
    text = product.get_text(" ", strip=True)
    product_names.append(text)

discount_list = []
discounts = soup.find_all("div", class_="bdg _dsct _sm")
for discount in discounts:
    discount_list.append(discount.get_text(strip=True))

    star_list = []    
    stars = soup.find_all("div", class_="stars _s")
    for star in stars:
        text = star.get_text(" ", strip = True)
        star_list.append(text)

review_list = []
number_of_reviews = soup.find_all("div", class_="rev")
for rev in number_of_reviews:
    text = rev.get_text(strip=True)  # Get the full text
    match = re.search(r"\((\d+)\)", text)  # Look for digits inside ()
    if match:
        reviews = match.group(1)  # Extract number only
        review_list.append(reviews)
    else:
        review_list.append(None)

#Combine into a DataFrame
data = {
    "Product Name": product_names,
    "Discount": discount_list,
    "Stars": star_list,
    "Reviews": review_list
}

df = pd.DataFrame(data)

print(df)  # ✅ check first few rows
df.to_csv("jumia_top_sellers.csv", index=False)
