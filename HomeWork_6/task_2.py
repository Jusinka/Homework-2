import json
import datetime

def open_data():
    with open('acdc.json') as f:
        data_json = json.load(f)
        duration = 0
        for track in data_json["album"]["tracks"]["track"]:
            duration += int(track['duration'])
    return duration

def convert_time(secs):
    convert = (datetime.timedelta(seconds=secs))
    return convert

seconds = open_data()
result = convert_time(seconds)

print(result)
