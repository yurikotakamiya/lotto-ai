from db import connection, insert_winning_pairs
import requests
import json

from sys import argv
from datetime import datetime

def get_date(date_string):
    date_object = datetime.strptime(date_string[0:10], '%Y-%m-%d')
    return date_object.strftime('%d-%b-%y')

def get_numbers(numbers_string):
    numbers = numbers_string.split(' ')
    number_array = [int(num) for num in numbers]
    return ', '.join([str(num) for num in number_array])

def fetch_numbers(lotto_type, latest_only):
    if lotto_type == 'megamillion':
        url = 'https://data.ny.gov/resource/5xaw-6ayf.json'
        r = requests.get(url)
        json_object = json.loads(r.content)

        if latest_only.lower() == 'true':
            date = get_date(json_object[0]['draw_date'])
            numbers = get_numbers(json_object[0]['winning_numbers']) + ', ' + json_object[0]['mega_ball']
            multiplier = json_object[0]['multiplier']
            multiplier = str(int(multiplier)) if multiplier else '1'
            string = f"'{date}', {numbers}, {multiplier}"
            insert_winning_pairs(lotto_type, string)

        else:
            for row in json_object:
                date = get_date(row['draw_date'])
                numbers = get_numbers(row['winning_numbers'])  + ', ' + row['mega_ball']
                multiplier = str(int(row['multiplier']))                
                multiplier = str(int(multiplier)) if multiplier else '1'
                string = f"'{date}', {numbers}, {multiplier}"
                insert_winning_pairs(lotto_type, string)
            
    elif lotto_type == 'powerball':
        url = 'https://data.ny.gov/resource/d6yy-54nr.json'
        r = requests.get(url)
        json_object = json.loads(r.content)
        if latest_only.lower() == 'true':
            date = get_date(json_object[0]['draw_date'])
            numbers = get_numbers(json_object[0]['winning_numbers'])
            multiplier = json_object[0]['multiplier']
            multiplier = str(int(multiplier)) if multiplier else '1'
            string = f"'{date}', {numbers}, {multiplier}"
            insert_winning_pairs(lotto_type, string)

        else:
            for row in json_object:
                date = get_date(row['draw_date'])
                numbers = get_numbers(row['winning_numbers'])
                multiplier = ''
                if 'multiplier' in row:
                    multiplier = row['multiplier']
                else:
                    multiplier = '1'
                string = f"'{date}', {numbers}, {multiplier}"
                insert_winning_pairs(lotto_type, string)
                
    connection.commit()

fetch_numbers(argv[1], argv[2])