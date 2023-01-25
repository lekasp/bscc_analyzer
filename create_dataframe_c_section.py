import pandas as pd
import data_grabber

data = data_grabber.grab_data()
new_data = list()

for item in data:
    if item["short_id"] is not None:
        if item["short_id"].startswith("C"):
            new_item = {
                "transcription": item["transcription"]["original"],
                "short_id": item["short_id"],
                "label": item["label"]
            }

            if len(item["connection"]) > 0:
                if "to" in item["connection"][0]:
                    new_item["company_connection"] = item["connection"][0]["to"][0]["short_id"]
                if "what" in item["connection"][0]:
                    new_item["company_goods"] = item["connection"][0]["what"][0]["short_id"]

            new_data.append(new_item)

df = pd.DataFrame.from_records(new_data)


print(df.columns)

# Count Location occurences
#print(df["label"].value_counts())

# Count Company connections
#print(df["company_connection"].value_counts())

# Count Company connections
#print(df["company_goods"].value_counts())