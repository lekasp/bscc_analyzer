import json
import os


def grab_data():
    walk_dir = 'data/output_1951'

    data = list()

    for root, subdirs, files in os.walk(walk_dir):
        for filename in files:
            if filename.endswith(".json"):
                file_path = os.path.join(root, filename)
                f = open(file_path, encoding='utf8')
                data.append(json.load(f))

    return data


def get_company(json_data):
    try:
        company = json_data["label"]
    except Exception:
        company = "0"
    return company
    write_to_tsv('companies.tsv', company)



def get_country(json_data):
    try:
        country = json_data["location"]["code"]
    except Exception:
        country = []
    return country


