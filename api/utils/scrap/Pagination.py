import requests
from bs4 import BeautifulSoup

class FihiranapPagination:
    def __init__(self, url):
        self.url = url
        self.response = self._get_page_content()

    def _get_page_content(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.content
        else:
            raise Exception(f"Failed to retrieve the page. Status code: {response.status_code}")

    def scrape_first_and_last_elements(self):
        soup = BeautifulSoup(self.response, 'html.parser')

        first_element_href = soup.find('ul', class_='pagination').find_all('li')[0].a['href']
        last_element_href = soup.find('ul', class_='pagination').find_all('li')[-1].a['href']

        return first_element_href, last_element_href
    
    def generate_pagination_links(self):
        first_href, last_href = self.scrape_first_and_last_elements()
        start_page = int(first_href.split('=')[-1])
        end_page = int(last_href.split('=')[-1])

        pagination_links = [f"{self.url}?page={page}" for page in range(start_page, end_page + 1)]
        return pagination_links

