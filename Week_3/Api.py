import requests

#get the api key as guided in the documentation
api_key = "****an api key**"
lat = 1.29
lon = 32.82

#get the url or link for the site.
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

response = requests.get(url) #request the data

print(response.status_code) #Confirm whether the request was successfull if successfull you should get the outpu 200

data = response.json()

coordinates = data['coord']


