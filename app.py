from flask import Flask, jsonify, request
import json
from fuzzywuzzy import process

app = Flask(__name__)

fihirana_files = [
    "results/hira/ankalazao_ny_tompo.json",
    "results/hira/antsao_ny_tompo.json",
    "results/hira/fihirana_dera.json",
    "results/hira/fihirana_hasina.json",
    "results/hira/fihirana_vaovao.json",
    "results/hira/karine_dera.json",
    "results/hira/vavaka_sy_hira.json",
]

hira_by_fihirana = {}

for file_path in fihirana_files:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        fihirana_name = file_path.split("/")[-1].split(".")[0]
        hira_by_fihirana[fihirana_name] = data

@app.route('/api/fihirana/all', methods=['GET'])
def get_all_fihirana():
    return jsonify(hira_by_fihirana)

@app.route('/api/fihirana/<fihirana_name>', methods=['GET'])
def get_hira_by_fihirana(fihirana_name):
    if fihirana_name in hira_by_fihirana:
        return jsonify(hira_by_fihirana[fihirana_name])
    else:
        return jsonify({"error": "Fichier non trouvé"}), 404

@app.route('/api/fihirana/search', methods=['GET'])
def search_all_hira():
    search_term = request.args.get('q', '')

    results = {}

    for fihirana_name, hira in hira_by_fihirana.items():
        matching_hira = process.extract(search_term, [hira["title"] for hira in hira], limit=5)
        matching_hira = [{"title": match[0]} for match in matching_hira if match[1] > 50]
        if matching_hira:
            results[fihirana_name] = matching_hira

    return jsonify(results)

@app.route('/api/fihirana/<fihirana_name>/search', methods=['GET'])
def search_hira_in_fihirana(fihirana_name):
    if fihirana_name in hira_by_fihirana:
        search_term = request.args.get('q', '')
        matching_hira = process.extract(search_term, [hira["title"] for hira in hira_by_fihirana[fihirana_name]], limit=5)
        matching_hira = [{"title": match[0]} for match in matching_hira if match[1] > 50]
        return jsonify(matching_hira)
    else:
        return jsonify({"error": "Hira non trouvé"}), 404


if __name__ == '__main__':
    app.run(debug=True)
