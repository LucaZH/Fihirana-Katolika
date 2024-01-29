import json,os

import jsonlines
from utils.Pagination import FihiranapPagination
from utils.HiraBoky import HiraBoky
from utils.TononKira import TononKira

def scrape_and_save_hira_list(json_path='./utils/Fihirana.json', output_dir='./results/list-hira'):
    with open(json_path, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)

    for hira_info in json_data:
        link = hira_info["link"]
        title = hira_info["title"]

        pagination = FihiranapPagination(link)
        pages = pagination.generate_pagination_links()

        list_hira = []
        for page in pages:
            katolika_scraper = HiraBoky(page, list_hira)
            links_info_list = katolika_scraper.scrape_links_info()

        output_filename = f"{output_dir}/{title.lower().replace(' ', '_')}.json"

        with open(output_filename, 'w', encoding='utf-8') as json_file:
            json.dump(list_hira, json_file, ensure_ascii=False, indent=4)

        print(f"Result for {title} has been written to {output_filename}")

        list_hira.clear()

def read_json_files(directory='./results/list-hira'):
    json_files = [f for f in os.listdir(directory) if f.endswith('.json')]

    for json_file in json_files:
        file_path = os.path.join(directory, json_file)
        title_boky = os.path.splitext(file_path)[0].split('/')[-1]
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            for element in json_data:
                write_hira_into_json('./results/hira',element["link"],title_boky)

def write_hira_into_json(output_dir, url, fihirana_title):
    output_filename = f"{output_dir}/{fihirana_title}"
    hira = TononKira(url)
    hira_content = hira.extract_hira_show_content()
    entry = {
        'title': hira_content[0],
        'content': hira_content[1]
    }

    if os.path.exists(output_filename):
        with open(output_filename, 'r', encoding='utf-8') as json_file:
            existing_data = json.load(json_file)
    else:
        existing_data = []

    existing_data.append(entry)

    with open(output_filename, 'w', encoding='utf-8') as json_file:
        json.dump(existing_data, json_file, ensure_ascii=False, indent=2)


read_json_files()