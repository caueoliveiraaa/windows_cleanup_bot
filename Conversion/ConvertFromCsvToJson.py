from pandas import DataFrame
import pandas as pd 
import json
import os 


def get_csv_data() -> DataFrame:
    if not os.path.exists('data'):
        os.makedirs('data')
        
    if len(os.listdir('data')) > 1:
        print('Add only one csv to the folder for conversion.')
    else:
        file = os.listdir('data')[0]
        if os.path.exists(f'data\\{file}') and file.endswith('.csv'):
            return pd.read_csv(f'data\\{file}')
        raise Exception('Invalid file.')
        

def clean_data(df: DataFrame, key: str) -> dict:
    movie_data = {}
    
    for index, row in df.iterrows():
        title = row[key]
        row_dict = row.drop(key).to_dict()
        row_dict_cleaned = {
            k: v if pd.notna(v) else '' for k, v in row_dict.items()}
        
        try:
            if isinstance(row_dict_cleaned['Duration (min)'], float)\
            or isinstance(row_dict_cleaned['Duration (min)'], int):
                row_dict_cleaned['Duration (min)'] = int(
                    float(row_dict_cleaned['Duration (min)']))
                
            if isinstance(row_dict_cleaned['Year'], float)\
            or isinstance(row_dict_cleaned['Year'], int):
                row_dict_cleaned['Year'] = int(row_dict_cleaned['Year'])
        except ValueError:
            row_dict_cleaned['Duration (min)'] = 0 
            row_dict_cleaned['Year'] = 0 
            
        movie_data[title] = row_dict_cleaned
    
    return movie_data


def save_data_into_json(movie_data: json) -> None:
    if not os.path.exists('out'):
        os.makedirs('out')
    
    with open('.\\out\\movie_data.json', 'w') as json_file:
        json.dump(movie_data, json_file, indent=4)


def main() -> None:
    try:
        df = get_csv_data()
        column_for_key = 'Title'
        # NOTE use input to choose the column that will be the key
        # input_msg = 'Type in the column that will be the key for each value'
        # column_for_key = input(input_msg)
        save_data_into_json(clean_data(df, column_for_key))
    except Exception as e:
        print(f'{e.__class__} - {e}')


if __name__ == '__main__':
    main()
