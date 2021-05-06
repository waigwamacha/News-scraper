from urllib.request import urlopen
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        response = urlopen(self.site)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        for tag in soup.find_all('a'):
            url = tag.get('href')
            if url and 'html' in url:
                data = soup.get_text(url)
                with open("copy.txt", "w") as file:
                    tags = file.write(data)

nytimes = Scraper("https://www.nytimes.com/")
nytimes.scrape()


