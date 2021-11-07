import random
from bs4 import BeautifulSoup
import requests
from pleer_parser import check_proxies as ch_p

URL = 'https://www.pleer.ru/fullcatalog.html/'
HEADERS = {'User-agent': 'curl/7.64.1'}


def get_html(valid_proxies, url, headers=None):
    if headers is None:
        headers = {}
    session = requests.Session()
    proxy = random.choice(valid_proxies)
    if "http" in url:
        session.proxies = {"http": proxy}
    else:
        session.proxies = {"https": proxy}
    response = session.get(url=url, headers=headers)
    return response.text


def get_session(valid_proxies, url, headers):
    session = requests.Session()
    proxy = random.choice(valid_proxies)
    if "http" in url:
        session.proxies = {"http": proxy}
    else:
        session.proxies = {"https": proxy}
    response2 = session.get(url=url, headers=headers)
    return response2


def main_parser(html):
    """Main parser, parse web shop."""
    HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                            ' (KHTML, like Gecko) Chrome/93.0.4577.82 YaBrowser/21.9.2.169 Yowser/2.5 Safari/537.36'}
    print("successful")
    data = []
    soup = BeautifulSoup(html, 'lxml')
    main_categories = soup.find_all('div', class_='top-menu-category')
    for category in main_categories:
        data.append(
            {
                'main_categories': category.text,
            }
        )
        print("successful")
        with open('products_links.txt', 'r') as file:
            for url in file:

                url = url.strip()
                if url:
                    print(url)
                    response2 = get_session(ch_p.parse_proxies(ch_p.get_proxy_html()), url, HEADER)
                    print(response2.text)



main_parser(get_html(ch_p.parse_proxies(ch_p.get_proxy_html()), URL, HEADERS))
