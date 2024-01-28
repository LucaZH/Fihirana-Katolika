import json
from utils.Pagination import FihiranapPagination
from utils.HiraBoky import HiraBoky

url_dera = "https://katolika.org/fihirana/boky/show/4"
pagination = FihiranapPagination(url_dera)
pages = pagination.generate_pagination_links()
list_hira = []

for page in pages:
    katolika_scraper = HiraBoky(page, list_hira)
    links_info_list = katolika_scraper.scrape_links_info()

output = "./results/dera.json"
with open(output, 'w', encoding='utf-8') as json_file:
    json.dump(list_hira, json_file, ensure_ascii=False, indent=4)