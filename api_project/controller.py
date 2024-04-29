
import requests as re

url = "https://www.boredapi.com/api/activity"

response = re.get(url)

if response.ok:
    print(response.text)
else:
    print(f"There was an error: {response.status_code}")