import requests
import json
import pandas as pd

# Define the base URL for the Steam API
base_url = "https://store.steampowered.com/api/appdetails"

# Read app_ids from the CSV file
# `app_list.csv` can be manually created or generated from `request_from_steampy.py`
app_ids_df = pd.read_csv('app_list.csv')
app_ids = app_ids_df['appid'].tolist()  # Extract app_ids into a list

# Create an empty list to store the results
results = []

# Loop through each app_id and make the request
for app_id in app_ids[:100]:  # Limit to 100 app_ids
    # Create the request URL for the specific app ID
    url = f"{base_url}?appids={app_id}"

    # Make the GET request to retrieve data
    response = requests.get(url)

    # Check for a successful response
    if response.status_code == 200:
        # Parse the JSON response
        game_data = response.json()

        # Access the entire data block for the app_id
        app_data = game_data.get(str(app_id), {}).get('data', {})

        if app_data:
            # Add the app_data to the results list
            results.append(app_data)
        else:
            print(f"Game data not found for app_id {app_id}.")
    else:
        print(f"Failed to retrieve data for app_id {app_id}. Status code: {response.status_code}")
        print('Response:', response.text)

# Create a DataFrame from the results
result_df = pd.DataFrame(results)

# Write all the data to a CSV file
result_df.to_csv('steam_app_data.csv', index=False)

print(f"All data for 100 app_ids successfully written to 'steam_app_data.csv'.")