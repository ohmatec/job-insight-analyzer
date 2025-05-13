import requests

url = "https://jsearch.p.rapidapi.com/search"

querystring = {"query":"developer jobs in chicago","page":"1","num_pages":"1","country":"us","date_posted":"all"}

headers = {
	"x-rapidapi-key": "a3df78911amshccfd2390c5d23a1p13e2f7jsn16471e49c65a",
	"x-rapidapi-host": "jsearch.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())