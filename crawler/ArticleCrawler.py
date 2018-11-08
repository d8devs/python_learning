import requests
from bs4 import BeautifulSoup
import time

from .Article import Article

class ArticleCrawler():
    def getArticles(self):
        url = "https://d8devs.com"

        while url != "":
            time.sleep(1)
            r = requests.get(url)
            doc = BeautifulSoup(r.text, "html.parser")

            for article in doc.select("article"):
                link = article.select_one(".wrap-entry-meta span a")['href']
                date = article.select_one(".wrap-entry-meta time").text
                title = article.select_one(".entry-title a").text

                yield Article(title, date, link)

                nextPage = doc.select_one('.nav-links .next')

                if nextPage:
                    url = nextPage['href']
                else:
                    url = ""