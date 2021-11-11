import requests
from bs4 import BeautifulSoup


def parser():
    url = 'https://ria.ru/basketball/'

    links = []
    news = []
    link_img = []
    news_text_final = []
    times = []

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    tables = soup.find_all('a', {'class': 'list-item__title color-font-hover-only'}, limit=8)
    time = soup.find_all('div', {'class': 'list-item__date'}, limit=8)
    img = soup.find_all('img', {'class': 'responsive_img m-list-img'}, 'src', limit=8)

    for data in img:
        link_img.append(data.get('src'))
    for data in tables:
        links.append(data.get('href'))
    for data in tables:
        news.append(data.text)
    for data in time:
        times.append(data.text)

    news_with_links = (list(zip(news, links)))

    for url1 in links:
        r = requests.get(url1)
        soup = BeautifulSoup(r.text, "lxml")
        tables = soup.find('div', {'class': 'article__body js-mediator-article mia-analytics'})

        news_text = []
        for i in tables:
            news_text.append(f'{i.text}\n')
        news_text_final.append(news_text)

    return news_with_links, link_img, news_text_final, times
