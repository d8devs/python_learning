import requests
from bs4 import BeautifulSoup
import time

class Article():
    def __init__(self, title, date, link):
        self.title = title
        self.date = date
        self.link = link


class WebpageCrawler():
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


webpageCrawler = WebpageCrawler()
articles = webpageCrawler.getArticles()

counter = 0
for article in articles:
    if counter == 5:
        break

    counter = counter + 1
    row = "Article : {} {} - {}".format(article.title, article.date, article.link)
    print(row)


