import requests
from bs4 import BeautifulSoup

r = requests.get("http://d8devs.com")

doc = BeautifulSoup(r.text, "html.parser")


for paragpText in doc.find_all("p"):
    print(paragpText.attrs)
    print(paragpText.text)

for article in doc.select(".post"):
    title = article.select_one(".entry-title").text.strip('\n')
    date = article.select_one(".entry-date").text.strip('\n')

    text = "Title:{} / Date: {}".format(title, date)
    print(text)


