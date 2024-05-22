import pandas as pd 
import json
import os 

file_path = 'imdb-movies-dataset.csv'

try:
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        movie_data = {}
        for index, row in df.iterrows():
            title = row['Title']
            row_dict = row.drop('Title').to_dict()
            row_dict_cleaned = {k: v if pd.notna(v) else '' for k, v in row_dict.items()}
            movie_data[title] = row_dict_cleaned
        with open('movie_data.json', 'w') as json_file:
            json.dump(movie_data, json_file, indent=4)
    else:
        print('Inform a valid path!') 
except Exception as e:
    print(e)
