import zipfile
import pandas as pd
import os

# create "data" folder
if not os.path.exists("data/"):
    os.makedirs("data/")

# extract archive.zip
with zipfile.ZipFile("archive.zip", 'r') as zip_ref:
    i = 1
    for file_name in zip_ref.namelist():
        print(f"Extracting files [{i}/22]")
        zip_ref.extract(file_name, "data/")
        i += 1

# convert csv files to json files
i = 1
for file_name in os.listdir("data/"):
    if file_name.endswith(".csv"):
        print(f"Converting csv files to json [{i}/11]")
        csv_file = os.path.join("data", file_name)
        df = pd.read_csv(csv_file)
        df['tags'] = df['tags'].str.split("|")
        df['country'] = file_name[:2]
        json_file = os.path.splitext(csv_file)[0] + ".json"
        df.to_json(json_file, orient='records')
        os.remove(csv_file)
        i += 1

print("Done.")