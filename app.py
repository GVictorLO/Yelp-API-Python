import requests
import config

url = "https://api.yelp.com/v3/businesses/search"
headers = {
    "Authorization": "Bearer " + config.api_key
}
params = {
    "term": "restaurants",
    "location": "NYC",
}
response = requests.get(url, headers=headers, params=params)
result = response.json()
businesses = result["businesses"]

restaurants = [business["name"]
               for business in businesses if business["rating"] >= 4.0]

print(restaurants)
