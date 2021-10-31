import random
import requests
from bs4 import BeautifulSoup

URL = 'http://www.w3.org/TR/html4/strict.dtd'


def get_proxy_html():
    URL1 = 'https://openproxy.space/ru/list/890-w2mSkt'
    response = requests.get(url=URL1)
    return response.text


def parse_proxies(resp):
    """Parse web site with free proxies."""
    proxies_list = []
    soup = BeautifulSoup(resp, 'lxml')
    main_div = soup.find('div', class_='list-code http')
    table = main_div.find('table').text
    all_tr = table.find_all('tr')
    for tr in all_tr:
        proxy = tr.find('td').text
        print(proxy)

parse_proxies(get_proxy_html())
# def get_session(proxies):
#     session = requests.Session()
#     proxy = random.choice(proxies)
#     session.proxies = {"http": proxy, "https": proxy}
#     return session
#
#
# def validate_proxy(proxies, session):
#     valid_proxies = []
#     for proxy in proxies:
#         s = get_session(proxies)
#         try:
#             proxy = s.get("http://icanhazip.com", timeout=1.5).text.strip()
#             print(proxy)
#             if proxy and len(proxy) < 16:
#                 valid_proxies.append(proxy)
#         except Exception as e:
#             continue
#         if valid_proxies:
#             return valid_proxies
#
#
# def get_valid_proxies():
#     proxies_list = parse_proxies(get_proxy_html())
#     valid_proxies = validate_proxy(proxies_list, get_session(proxies_list))
#     return valid_proxies
# get_valid_proxies()