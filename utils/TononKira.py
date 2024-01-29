import requests
from bs4 import BeautifulSoup

class TononKira:
    def __init__(self, url):
        self.url = url
        self.html_content = None
        self.soup = None

    def fetch_html_content(self):
        response = requests.get(self.url)
        self.html_content = response.content

    def parse_html_content(self):
        if self.html_content:
            self.soup = BeautifulSoup(self.html_content, 'html.parser')

    def extract_hira_show_content(self):
        if self.soup:
            hira_show_div = self.soup.find('div', class_='hira_show')
            if hira_show_div:
                title = hira_show_div.find('h1').get_text(strip=True)
                paragraphs = [p.get_text(strip=True) for p in hira_show_div.find_all('p')]

                return title, paragraphs

        return None