import crawler

articles = crawler.ArticleCrawler().getArticles()

for article in articles:
    print(article)