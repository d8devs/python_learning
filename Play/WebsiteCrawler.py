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
        articles = []

        while url != "":
            time.sleep(1)
            r = requests.get(url)
            doc = BeautifulSoup(r.text, "html.parser")

            for article in doc.select("article"):
                link = article.select_one(".wrap-entry-meta span a")['href']
                date = article.select_one(".wrap-entry-meta time").text
                title = article.select_one(".entry-title a").text

                newArticle = Article(title, date, link)
                articles.append(newArticle)

                nextPage = doc.select_one('.nav-links .next')

                if nextPage:
                    url = nextPage['href']
                else:
                    url = ""
        return articles



webpageCrawler = WebpageCrawler()
articles = webpageCrawler.getArticles()

for article in articles:
    row = "Article : {} {} - {}".format(article.title, article.date, article.link)
    print(row)


