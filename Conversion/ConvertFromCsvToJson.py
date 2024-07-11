import json
import os

import pandas as pd
from pandas import DataFrame


def create_data_folder() -> None:
    if not os.path.exists('data'):
        os.makedirs('data')


def get_csv_files(file_list: list) -> list:
    return [file for file in file_list
            if file.lower().endswith('.csv')]


def get_csv_data() -> DataFrame:
    create_data_folder()
    csv_files = get_csv_files(os.listdir('data'))

    if len(csv_files) > 1:
        print('Add only one csv to the folder for conversion.')
    else:
        return validate_csv_data()


def validate_csv_data() -> DataFrame:
    file = os.listdir('data')[0]

    if os.path.exists(f"data\\{file}") and file.endswith('.csv'):
        return pd.read_csv(f'data\\{file}')

    raise Exception('Invalid CSV file.')


def validate_row(row_dict: dict) -> dict:
    """
    Validate years and duration because some come enmpty
    """

    try:
        cols = ['Duration (min)', 'Year']
        row_dict = validate_numbers(row_dict, cols)
    except ValueError:
        row_dict['Duration (min)'] = 0
        row_dict['Year'] = 0

    return row_dict


def validate_numbers(row_dict: dict, cols: list) -> dict:
    for col in cols:
        if isinstance(row_dict[col], (float, int)):
            row_dict[col] = int(float(row_dict[col]))

    return row_dict


def clean_data(df: DataFrame) -> dict:
    csv_data_converted: dict = {}
    for index, row in df.iterrows():
        csv_data_converted[index] = clean_dict(
            validate_row(row.to_dict())
        )

    return csv_data_converted


def clean_dict(row_dict: dict) -> dict:
    dict_ = {}
    for key, value in row_dict.items():
        if not pd.isna(value):
            dict_[key.lower()] = value
        else:
            dict_[key.lower()] = ''

    return dict_


def save_data_into_json(csv_data: json) -> None:
    if not os.path.exists('out'):
        os.makedirs('out')

    with open('.\\out\\csv_data.json', 'w') as json_file:
        json.dump(csv_data, json_file, indent=4)


def main() -> None:
    try:
        dataframe = get_csv_data()
        save_data_into_json(clean_data(dataframe))
    except Exception as e:
        print(f'{e.__class__} - {e}')


if __name__ == '__main__':
    main()
