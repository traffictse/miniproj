import requests
import json

# # Official code examples from https://api-docs.igdb.com/#getting-started
# from requests import post
# response = post('https://api.igdb.com/v4/games', **{'headers': {'Client-ID': 'Client ID', 'Authorization': 'Bearer access_token'},'data': 'fields age_ratings,aggregated_rating,aggregated_rating_count,alternative_names,artworks,bundles,category,checksum,collection,collections,cover,created_at,dlcs,expanded_games,expansions,external_games,first_release_date,follows,forks,franchise,franchises,game_engines,game_localizations,game_modes,genres,hypes,involved_companies,keywords,language_supports,multiplayer_modes,name,parent_game,platforms,player_perspectives,ports,rating,rating_count,release_dates,remakes,remasters,screenshots,similar_games,slug,standalone_expansions,status,storyline,summary,tags,themes,total_rating,total_rating_count,updated_at,url,version_parent,version_title,videos,websites;'})
# print ("response: %s" % str(response.json()))

# Define the URL and headers
url = 'https://api.igdb.com/v4/games'
headers = {
    'Client-ID': 'tagbrp3661efpnk00us7rz1dwp1ftj',  # Replace with your actual Client ID
    'Authorization': 'Bearer q8c7r6815ouxowmexkuvbnxp2ww0ff'  # Replace with your actual access token
}

# Define the body of the request (IGDB uses a special query format)
body = 'fields *; limit 100;'  # Example to retrieve all fields for 10 games

# Make the POST request
response = requests.post(url, headers=headers, data=body)

# Check for successful response and print the data
if response.status_code == 200:
    # Pretty-print the JSON response
    response_data = response.json()
    # print(json.dumps(response_data, indent=4))

    # Write the JSON data to a file
    with open('igdb_response.json', 'w') as f:
        json.dump(response_data, f, indent=4)

    print("Data successfully written to 'igdb_response.json'")
else:
    print('Failed to retrieve data. Status code:', response.status_code)
    print('Response:', response.text)