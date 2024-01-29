import requests
from bs4 import BeautifulSoup

class TononKira:
    def __init__(self, url):
        self.url = url

    def fetch_html_content(self):
        response = requests.get(self.url)
        return response.content

    def parse_html_content(self,html_content):
        return BeautifulSoup(html_content, 'html.parser')

    def extract_hira_show_content(self):
        html_content = self.fetch_html_content()
        soup = self.parse_html_content(html_content)
        hira_show_div = soup.find('div', class_='hira_show')
        if hira_show_div:
            title = hira_show_div.find('h1').get_text(strip=True)
            paragraphs = [p.get_text(strip=True) for p in hira_show_div.find_all('p')]

            return title, paragraphs

        return None