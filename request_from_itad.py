import requests
import json

# Your API key
api_key = 'xxxxxx'  # I masked my own API key here in case it is denied due to massive access

# Define the endpoint (with the API key in the URL)
url = f"https://api.isthereanydeal.com/games/historylow/v1?key={api_key}"

# Define the game IDs as an array (non-empty, which the API expects)
payload = [
    "01849783-6a26-7147-ab32-71804ca47e8e",  # Replace with actual game UUIDs
    "01849782-1017-7389-8de4-c97c587fd7e3"
]

# Set the request headers
headers = {
    'Content-Type': 'application/json'
}

# Make the POST request to the API
response = requests.post(url, headers=headers, json=payload)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    print(json.dumps(data, indent=4))  # Pretty print the JSON response
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    print(f"Response: {response.text}")
