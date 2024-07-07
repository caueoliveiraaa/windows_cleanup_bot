import json
import os 

import pandas as pd 
from pandas import DataFrame


def create_data_folder() -> None:
    if not os.path.exists('data'):
        os.makedirs('data')


def get_csv_files(file_list: list) -> list:
    return [file for file in file_list if file.lower().endswith('.csv')]


def get_csv_data() -> DataFrame:
    create_data_folder()
    csv_files = get_csv_files(os.listdir('data'))
    
    if len(csv_files) > 1:
        print('Add only one csv to the folder for conversion.')
    else:
        file = os.listdir('data')[0]
        if os.path.exists(f"data\\{file}") and file.endswith('.csv'):
            return pd.read_csv(f'data\\{file}')
        raise Exception('Invalid file.')
        

def save_data_into_json(csv_data: json) -> None:
    if not os.path.exists('out'):
        os.makedirs('out')
    
    with open('.\\out\\csv_data.json', 'w') as json_file:
        json.dump(csv_data, json_file, indent=4)


def clean_dict(row_dict: dict) -> dict:
    return {key: value\
        if pd.notna(value) else ''\
        for key, value in row_dict.items()}


def validate_row(row_dict_cleaned: dict) -> dict:
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
        
    return row_dict_cleaned


def clean_data(df: DataFrame, column_for_key: str) -> dict:
    csv_data_converted: dict = {}
    
    for index, row in df.iterrows():
        title = row[column_for_key]
        row_dict = row.drop(column_for_key).to_dict()
        row_dict_cleaned = clean_dict(row_dict)
        csv_data_converted[title] = validate_row(row_dict_cleaned)
    
    return csv_data_converted


def main() -> None:
    # Contant representing what column will be the main key 
    # for each item in the .json file
    COLUMN_FOR_KEY: str = 'Title'
    
    try:
        df = get_csv_data()
        save_data_into_json(clean_data(df, COLUMN_FOR_KEY))
    except Exception as e:
        print(f'{e.__class__} - {e}')


if __name__ == '__main__':
    main()
