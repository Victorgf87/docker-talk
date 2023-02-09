from datetime import datetime
import requests

minute = datetime.now().minute

api_url = f'https://swapi.dev/api/planets/{minute}/'
response = requests.get(api_url)

print(response.json())
