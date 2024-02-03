from flask import Flask, request
from data_loader import load_data
from fuzzywuzzy import process
import json

app = Flask(__name__)
hira_by_fihirana = load_data()

@app.route('/api/fihirana/', methods=['GET'])
def get_all_fihirana():
    if not hira_by_fihirana:
        return {"status": "failure", "message": "No fihirana found"}, 404

    return {"status": "success", "data": hira_by_fihirana}, 200

@app.route('/api/<fihirana_name>/', methods=['GET'])
def get_or_search_hira_by_fihirana(fihirana_name):
    if fihirana_name in hira_by_fihirana:
        search_term = request.args.get('search', None)
        if search_term:
            matching_hira = process.extract(search_term, [hira["title"] for hira in hira_by_fihirana[fihirana_name]], limit=5)
            matching_hira = [{"title": match[0]} for match in matching_hira if match[1] > 50]
            if not matching_hira:
                return {"status": "failure", "message": "No matching hira found"}, 404
            return {"status": "success", "data": matching_hira}, 200
        else:
            return {"status": "success", "data": hira_by_fihirana[fihirana_name]}, 200
    else:
        return {"status": "failure", "message": f"No fihirana found with name {fihirana_name}"}, 404

@app.route('/api/hira/', methods=['GET'])
def search_all_hira():
    search_term = request.args.get('search', '')
    data = {}
    for fihirana_name, hira in hira_by_fihirana.items():
        matching_hira = process.extract(search_term, [hira["title"] for hira in hira], limit=5)
        matching_hira = [{"title": match[0]} for match in matching_hira if match[1] > 50]
        if matching_hira:
            data[fihirana_name] = matching_hira

    if not data:
        return {"status": "failure", "message": "No matching hira found"}, 404

    return {"status": "success", "data": data}, 200

@app.route('/api/<fihirana_name>/hira', methods=['GET'])
def get_hira(fihirana_name):
    _hira = []
    if fihirana_name in hira_by_fihirana:
        get_hira_term = request.args.get('title', '')

        for hira in hira_by_fihirana[fihirana_name]:
            if get_hira_term == hira['title']:
                _hira.append(hira)
        if len(_hira)==0:
            return {"status": "failure", "message": "Hira not found"}, 404
        else:
            return {"status": "success", "data": _hira[0]}, 200
    else:
        return {"status": "failure", "message": "Fihirana not found"}, 404
    
if __name__ == '__main__':
    app.run(debug=True)
