import pandas as pd
import data_grabber

data = data_grabber.grab_data()
new_data = list()

for item in data:
    if item["short_id"] is not None:
        if item["short_id"].startswith("A") or item["short_id"].startswith("B"):
            new_item = {
                "transcription": item["transcription"]["original"],
                "short_id": item["short_id"],
                "label": item["label"]
            }

            if "corrected" in item["transcription"]:
                new_item["transcription"] = item["transcription"]["corrected"]

            if len(item["location"]) > 0:
                if "country" in item["location"][0]:
                    new_item["country_code"] = item["location"][0]["country"]["code"]
                    new_item["location_name"] = item["location"][0]["inferred"]
                else:
                    new_item["country_code"] = "YY"
                    new_item["location_name"] = item["location"][0]["transcription"]
            else:
                new_item["country_code"] = "XX"
                new_item["location_name"] = "Unknown"

            if len(item["connection"]) > 0:
                if "to" in item["connection"][0]:
                    new_item["company_connection"] = item["connection"][0]["to"][0]["short_id"]
                if "what" in item["connection"][0]:
                    new_item["company_goods"] = item["connection"][0]["what"][0]["short_id"]

            new_data.append(new_item)

df = pd.DataFrame.from_records(new_data)

# Count Country codes
print(df["country_code"].value_counts())

# Count Location occurences
print(df["location_name"].value_counts())

# Count Company connections
print(df["company_connection"].value_counts())

# Count Company connections
print(df["company_goods"].value_counts())