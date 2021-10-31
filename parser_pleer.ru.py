import random
from bs4 import BeautifulSoup
import requests
from pleer_parser import check_proxies as ch_p

URL = 'https://www.pleer.ru/fullcatalog.html/'
HEADERS = {'User-agent': 'curl/7.64.1'}


def get_html(valid_proxies, url, headers=''):
    session = requests.Session()
    proxy = random.choice(valid_proxies)
    session.proxies = {"http": proxy, "https": proxy}
    response = session.get(url=url, headers=headers)
    print(response)
    return response.text


def main_parser(html):
    """Main parser, parse web shop."""
    soup = BeautifulSoup(html, 'lxml')
    data = []
    HEADER = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/92.0.4515.159 YaBrowser/21.8.3.614 Yowser/2.5 Safari/537.36'}

    main_categories = soup.find_all('div', class_='top-menu-category')
    for category in main_categories:
        data.append(
            {
                'main_categories': category.text,
            }
        )
        with open('products_links.txt', 'r') as file:
            for url in file:
                url = url.strip()
                try:
                    response2 = get_html(ch_p.get_valid_proxies(), URL)
                    print(response2)
                except Exception as e:
                    print(e)


main_parser(get_html(ch_p.get_valid_proxies(), URL, HEADERS))
