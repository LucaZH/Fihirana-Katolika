import json
from utils.Pagination import FihiranapPagination
from utils.HiraBoky import HiraBoky

with open('./utils/Fihirana.json', 'r', encoding='utf-8') as json_file:
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

    output_filename = f"./results/{title.lower().replace(' ', '_')}.json"

    with open(output_filename, 'w', encoding='utf-8') as json_file:
        json.dump(list_hira, json_file, ensure_ascii=False, indent=4)

    print(f"Result for {title} has been written to {output_filename}")

    list_hira.clear
