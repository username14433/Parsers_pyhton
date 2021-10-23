# -*- coding: utf-8 -*-
import random
from bs4 import BeautifulSoup
import requests
from pleer_parser import check_proxies as ch_p

URL = 'https://www.pleer.ru/fullcatalog.html/'
HEADERS = {'User-agent': 'curl/7.64.1'}



def get_session(valid_proxies):
    session = requests.Session()
    proxy = random.choice(valid_proxies)
    if len(proxy) != 0 and proxy != None:
        session.proxies = {"https": proxy}
    return session




def main_parser(html, valid_proxies, session):
    """Main parser, parse web shop."""
    response = get_session(ch_p)
    data = []
    HEADER = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 YaBrowser/21.8.3.614 Yowser/2.5 Safari/537.36'}
    soup = BeautifulSoup(html, 'lxml')
    main_categories = soup.find_all('div', class_='top-menu-category')
    for category in main_categories:
        data.append(
            {
                'main_categories': category.text,
            }
        )

    all_uls = soup.find_all('ul', class_='top-menu-catalog')
    for ul in all_uls:
        all_items = ul.find_all('li')

        with open('../products_links.txt', 'r') as file:

            for url in file:
                response2 = get_session(ch_p.get_valid_proxies()).get(url=url)


main_parser(get_session(ch_p.get_valid_proxies()).get(url=URL), ch_p.get_valid_proxies(), get_session(ch_p.get_valid_proxies()))
