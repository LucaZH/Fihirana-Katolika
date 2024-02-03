from bs4 import BeautifulSoup
import requests

class HiraBoky:
    def __init__(self, url, hira_list):
        self.url = url
        self.response = self._get_page_content()
        self.boky_show = self._get_boky_show()
        self.hira_list = hira_list

    def _get_page_content(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.content
        else:
            raise Exception(f"Failed to retrieve the page. Status code: {response.status_code}")

    def _get_boky_show(self):
        soup = BeautifulSoup(self.response, 'html.parser')
        return soup.find('div', class_='boky_show')

    def scrape_links_info(self):
        links_divs = self.boky_show.find_all('div', class_='row striped mb-3 p-2')

        for links_div in links_divs:
            page_div = links_div.find('div', class_='col-1').get_text(strip=True)

            link_elements = links_div.find_all('a')

            for link_element in link_elements:
                link_text = link_element.get_text(strip=True)
                link_href = link_element['href']
                self.hira_list.append({"page": page_div, "title": link_text, "link": link_href})