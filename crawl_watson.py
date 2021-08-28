import requests
from bs4 import BeautifulSoup

url = 'https://www.watson.ch'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

articles = soup.find_all('h2')

for article in articles:
    article_index = articles.index(article)
    print('article no.:', article_index, 'article title:', article.get_text(strip=True))