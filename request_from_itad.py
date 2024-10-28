import requests
import json

# Define the endpoint (with the API key in the URL)
url = "https://api.isthereanydeal.com/games/history/v2?"
headers = {
    'Client-ID': '8a6bc0f7309571f4',  # Replace with your actual Client ID
    'Authorization': 'Bearer 84a44a2357e9a7c7149c05fdce31bc3645688a2e'  # Replace with your actual access token
}

# Define the game IDs as an array (non-empty, which the API expects)
payload = {, "US", [65,35], ""}

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
