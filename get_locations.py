import csv
import json
import os
import pandas


def grab_data():
    walk_dir = 'output/output_1951'
    data = list()

    for root, subdirs, files in os.walk(walk_dir):
        for filename in files:
            if filename.endswith(".json"):
                file_path = os.path.join(root, filename)
                f = open(file_path, encoding='utf8')
                file_data = json.load(f)
                # print("append: ", file_data)
                data.append(file_data)
    return data


def get_first_location(json_data):
    empty_loc = {"inferred": "No Location", "id": "00000", "lat": "0", "lng": "0", "country": {"code": "XX"}}
    try:
        locations = json_data["location"]
        if len(locations) > 0:
            if "id" not in locations[0]:
                return {"inferred": "Unknown Location", "id": "00001", "lat": "1", "lng": "1", "country": {"code": "XX"}}

            return locations[0]
        else:
            return empty_loc
    except Exception:
        return empty_loc

def write_to_tsv(filename, records):
    with open(filename, 'w', newline='') as tsvfile:
        writer = csv.writer(tsvfile, delimiter='\t', lineterminator='\n')
        for record in records:
            writer.writerow(record)

def get_locations_with_count():
    locations = {}
    data_list = grab_data()
    for data_point in data_list:
        #print(data_point)
        loc = get_first_location(data_point)

        if loc["id"] not in locations:
            locations[loc["id"]] = loc
            locations[loc["id"]]["number_of_companies"] = 1
        else:
            locations[loc["id"]]["number_of_companies"] += 1

    loc_list = list()
    for loc in locations:
        loc_list.append([loc,
                         locations[loc]["inferred"],
                         locations[loc]["lat"],
                         locations[loc]["lng"],
                         locations[loc]["country"]["code"],
                         locations[loc]["number_of_companies"]
                         ])
    write_to_tsv('data/locations.tsv', loc_list)


get_locations_with_count()
