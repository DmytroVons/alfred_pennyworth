import concurrent.futures
import requests
from bs4 import BeautifulSoup
from loguru import logger

logger.add('rozetka_logger.log', format='{time} {message} {level}', level='DEBUG', rotation='10 MB', compression='zip')

HEADERS = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'accept': '/*/'}
FILE = 'laptops.csv'


def get_html(url):
    return requests.get(url, headers=HEADERS)


def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('a', class_='pagination__link')
    if pagination:
        return int(pagination[-1].get_text())
    else:
        return 1


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='goods-tile__inner')
    laptops = []
    for item in items:
        if item.find('div', class_='goods-tile__availability').get_text(strip=True) == 'Есть в наличии':
            laptops.append({
                'model': item.find('span', class_='goods-tile__title').get_text(strip=True),
                'link': item.find('a').get('href'),
                'price': float(
                    item.find('span', class_='goods-tile__price-value').get_text(strip=True).replace('&nbsp;',
                                                                                                     '.').replace(
                        ' ',
                        '.')),
                'pictures': item.find('img', class_='lazy_img_hover display-none').get('src')
            })
    print(laptops)
    """"You can return you laptopst sort by price or another keys with this code: sorted(laptops, key=lambda x: x['price']"""
    return laptops


def parse(model):
    url = f'https://rozetka.com.ua/notebooks/c80004/producer={model}'
    html = get_html(url)
    if html.status_code == 200:
        laptops = []
        urls = []
        pages_count = get_pages_count(html.text)
        for page in range(1, pages_count + 1):
            logger.debug(f'parsing page {page} of {pages_count}...')
            urls.append(f'https://rozetka.com.ua/notebooks/c80004/page={page};producer={model}')
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = [executor.submit(get_html, url) for url in urls]
            for _ in concurrent.futures.as_completed(results):
                laptops.extend(get_content(html.text))
        logger.debug(f'we get {len(laptops)} laptops {model}')
        return laptops
    else:
        logger.debug('something wrong with parser!')