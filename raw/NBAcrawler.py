import json
import os
import datetime
import argparse
import requests

# Set up argument parser
parser = argparse.ArgumentParser()
parser.add_argument("--endpoint")
parser.add_argument("--api_key", default="1d89f363-6868-4a8b-b17a-9344bb084c78")
parser.add_argument("--date", action='append', help="Specify dates for the API call")
args = parser.parse_args()

endpoint = args.endpoint
api_key = args.api_key
params = {}

if args.date:
    params['dates[]'] = args.date
    params['per_page'] = 100

url = f"https://api.balldontlie.io/v1/{endpoint}"
raw_path = f"C:\\Users\\Samuel\\Desktop\\NBA_API\\raw\\data\\{endpoint}"



def save_data(raw_path, data):
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S%f")
    if not os.path.exists(raw_path):
        os.makedirs(raw_path)
    path = os.path.join(raw_path, f"{now}.json")
    with open(path, "w") as open_file:
        json.dump(data, open_file)
    return True

def get_data(url, headers, params):
    res = requests.get(url, headers=headers, params=params)
    data = res.json()
    return data

params['cursor'] =0
while params['cursor']!=None:
    headers = {"Authorization": f"{api_key}"}
    x = get_data(url=url, headers=headers, params=params)
    print(x)
    y = save_data(raw_path=raw_path, data=x)
    try:
        params['cursor'] = x['meta']['next_cursor']
    except:
        break