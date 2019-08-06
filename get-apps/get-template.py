import pandas as pd
import requests
import json

"""Function retrives json from api and writes to output file"""


def get_data(file_path):
    r = requests.get(
        'https://fantasy.premierleague.com/api/(insert api element)/')
    jsonResponse = r.json()
    with open(file_path, 'w') as outfile:
        json.dump(jsonResponse, outfile)


get_data("(insert outfile name).json")
