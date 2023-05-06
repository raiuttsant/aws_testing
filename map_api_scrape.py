import requests
import json
import time
from datetime import date
import pandas as pd

from google.colab import drive
drive.mount('/content/drive')

api_key = "AIzaSyByJNT-YmrM7D2lvfrhMdIxTPUtWdS0nM8"
search_query = "south indian restaurants near wembley central station"
region = "london"

df = pd.DataFrame(columns=["place_id","name","rating","user_ratings_total","formatted_address"])

pagetoken = ""
while True:
  url_3 = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=" +  search_query + "&key=" + api_key + "&pagetoken=" + pagetoken + "&region=" + region
  payload={}
  headers = {}
  response = requests.request("GET", url_3, headers=headers, data=payload)
  json_object = json.loads(response.text)
  for result in json_object["results"]:
    # print(result['name'])
    # print(result['rating'])
    # print(result['user_ratings_total'])
    # print(result['formatted_address'])
    # print("\n")
    name = result['name']
    place_id = result['place_id']
    rating = result['rating']
    user_ratings_total = result['user_ratings_total']
    formatted_address = result['formatted_address']
    df = df.append({'place_id': place_id, 'name': name, 'rating': rating, 'user_ratings_total': user_ratings_total, 'formatted_address': formatted_address}, ignore_index=True)
  try:
    pagetoken = json_object["next_page_token"]
    # print(pagetoken)
    time.sleep(2)
  except:
    break
# filering results
df = df[(df['rating'] >= 3.5) & (df['user_ratings_total'] >= 100)].sort_values(by = ['rating', 'user_ratings_total'], ascending=[False,False])
print(df)

split_search_query = search_query.split()
csv_file_name = 'output'
for tk in split_search_query:
  csv_file_name += '_'
  csv_file_name += tk

today = date.today()
df.to_csv(r'/content/drive/MyDrive/maps_search_project/' + csv_file_name + '_' + today.strftime("%d_%m_%Y") + '.csv', index=False)

# df.to_csv(r'/content/drive/MyDrive/map_output_' + search_query + '_' + date.today() + '.csv', index=False)
