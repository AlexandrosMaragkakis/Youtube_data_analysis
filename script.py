import pymongo
import json
import os


client = pymongo.MongoClient("localhost", 27017)

db = client["my_db"]
collection_cat = db['youtube_categories']
collection_vids = db['videos_data']

# Iterate through the json files in the "data" directory
for filename in os.listdir("data/"):
    print(f'Inserting {filename}...')
    filename = 'data/' + filename
    with open(filename, 'r') as f:
        data = json.load(f)
    if 'category' in filename:

        collection_cat.insert_many(data["items"])
        
    else:
        # Insert the json documents into the collection
        
        collection_vids.insert_many(data)