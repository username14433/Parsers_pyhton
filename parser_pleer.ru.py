import random
from bs4 import BeautifulSoup
import requests
from pleer_parser import check_proxies as ch_p

URL = 'https://www.pleer.ru/fullcatalog.html/'
HEADERS = {'User-agent': 'curl/7.64.1'}


def get_session(valid_proxies):
    session = requests.Session()
    if valid_proxies != []:
        proxy = random.choice(valid_proxies)
        if len(proxy) != 0:
            session.proxies = {"http": proxy, "https": proxy}
            return session
        else:
            raise Exception



def get_html(url, headers):
    response = requests.get(url=url, headers=headers)
    return response.text




def main_parser(html, valid_proxies, session):
    """Main parser, parse web shop."""
    soup = BeautifulSoup(html, 'lxml')
    data = []
    HEADER = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 YaBrowser/21.8.3.614 Yowser/2.5 Safari/537.36'}

    main_categories = soup.find_all('div', class_='top-menu-category')
    for category in main_categories:
        data.append(
            {
                'main_categories': category.text,
            }
        )

    all_uls = soup.find_all('ul', class_='top-menu-catalog')
    for ul in all_uls:

        with open('products_links.txt', 'r') as file:
                for url in file:
                    if "\"" in url.strip():
                        continue
                    else:
                        response2 = get_session(ch_p.get_valid_proxies()).get(url=url)
                        print(response2)

main_parser(get_html(URL, HEADERS), ch_p.get_valid_proxies(), get_session(ch_p.get_valid_proxies()))
