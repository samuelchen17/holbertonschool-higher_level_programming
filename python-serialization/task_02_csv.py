"""this module contains functions related to serialization and deserialization"""

import csv, json


def convert_csv_to_json(csv_filename):
    data = []

    try:
        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                data.append(row)

        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f)

        return True
    except Exception:
        return False
