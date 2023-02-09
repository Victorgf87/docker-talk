import requests
api_url = "https://swapi.dev/api/planets/1/"
response = requests.get(api_url)
print(response.json());
