import requests
import pandas as pd
from time import sleep
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm  # Import tqdm for progress bar

# # Official code examples from https://api-docs.igdb.com/#getting-started
# from requests import post
# response = post('https://api.igdb.com/v4/games', **{'headers': {'Client-ID': 'Client ID', 'Authorization': 'Bearer access_token'},'data': 'fields age_ratings,aggregated_rating,aggregated_rating_count,alternative_names,artworks,bundles,category,checksum,collection,collections,cover,created_at,dlcs,expanded_games,expansions,external_games,first_release_date,follows,forks,franchise,franchises,game_engines,game_localizations,game_modes,genres,hypes,involved_companies,keywords,language_supports,multiplayer_modes,name,parent_game,platforms,player_perspectives,ports,rating,rating_count,release_dates,remakes,remasters,screenshots,similar_games,slug,standalone_expansions,status,storyline,summary,tags,themes,total_rating,total_rating_count,updated_at,url,version_parent,version_title,videos,websites;'})
# print ("response: %s" % str(response.json()))

# Define the URL and headers
url = "https://api.igdb.com/v4/games"
headers = {
    "Client-ID": "tagbrp3661efpnk00us7rz1dwp1ftj",  # Replace with your actual Client ID
    "Authorization": "Bearer q8c7r6815ouxowmexkuvbnxp2ww0ff",  # Replace with your actual access token
}

app_df = pd.read_json("apps_clean.json")
print(app_df.shape)
print(app_df.columns)
print(app_df.head(10))

# Drop duplicate appid rows, keeping only the first occurrence
app_df_unique = app_df.drop_duplicates(subset="appid")
# Convert the DataFrame to a dictionary with 'appid' as keys
app_dict = app_df_unique.set_index("appid").to_dict(orient="index")

# Print a sample of the dictionary to verify
print(list(app_dict.items())[:10])  # Prints the first 10 items as a sample

data = pd.read_csv("clean_regular_price_half_time.csv")
id_list = data["gameID"].tolist()
# id_list = [1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034]

data_list = []


# Function to make a single API request
def fetch_game_data(game_name):
    body = f"fields id,name,rating; where name={game_name};"
    response = requests.post(url, headers=headers, data=body)
    if response.status_code == 200 and response.json():
        return response.json()[0]  # Return the data for this game
    else:
        print(
            f"Failed to retrieve data for NAME {game_name}. Status code:",
            response.status_code,
        )
        return None


# List to store the data
data_list = []

# Use ThreadPoolExecutor for parallel requests
with ThreadPoolExecutor(max_workers=4) as executor:
    future_to_id = {
        executor.submit(fetch_game_data, app_dict[game_id]): app_dict[game_id]
        for game_id in id_list
    }
    for future in as_completed(future_to_id):
        result = future.result()
        if result:
            data_list.append(result)
        sleep(0.25)  # Small delay to keep the request rate within limits

# Save data to CSV
if data_list:
    df = pd.DataFrame(data_list)
    df.to_csv("igdb_data.csv", index=False)
    print("Data successfully written to 'igdb_data.csv'")
else:
    print("No data retrieved.")
