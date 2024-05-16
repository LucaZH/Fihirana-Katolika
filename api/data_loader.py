import json
import os

def load_data():
    fihirana_files = [
        "data/hira/ankalazao_ny_tompo.json",
        "data/hira/antsao_ny_tompo.json",
        "data/hira/fihirana_dera.json",
        "data/hira/fihirana_hasina.json",
        "data/hira/fihirana_vaovao.json",
        "data/hira/karine_dera.json",
        "data/hira/vavaka_sy_hira.json",
    ]

    hira_by_fihirana = {}

    for file_path in fihirana_files:
        if not os.path.exists(file_path):
            print(f"Warning: File {file_path} does not exist.")
            continue

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                fihirana_name = file_path.split("/")[-1].split(".")[0]
                hira_by_fihirana[fihirana_name] = data
        except json.JSONDecodeError:
            print(f"Warning: File {file_path} is not a valid JSON file.")

    return hira_by_fihirana