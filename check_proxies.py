import random
import requests
from bs4 import BeautifulSoup

URL = 'http://www.w3.org/TR/html4/strict.dtd'


def get_proxy_html():
    URL1 = 'https://free-proxy-list.net/'
    response = requests.get(url=URL1)
    return response.text


def parse_proxies(resp):
    """Parse web site with free proxies."""
    proxies_list = []
    soup = BeautifulSoup(resp, 'lxml')
    main_div = soup.find('div', class_='table-responsive fpl-list')
    table = main_div.find('table', class_='table table-striped table-bordered')
    all_trs = table.find_all('tr')
    for tr in all_trs:
        if tr:
            try:
                all_tds = tr.find_all('td')
                proxy = all_tds[0].text.strip()
                port = all_tds[1].text.strip()
                proxy_and_host = f"{proxy}:{port}"
                proxies_list.append(proxy_and_host)
            except IndexError:
                continue
    return proxies_list



# def get_session(proxies):
#     session = requests.Session()
#     proxy = random.choice(proxies)
#     session.proxies = {"http": proxy, "https": proxy}
#     return session
#
#
# def validate_proxy(proxies, session):
#     valid_proxies = []
#     for proxy in range(10):
#         s = get_session(proxies)
#         try:
#             proxy = s.get("http://icanhazip.com", timeout=1.5).text.strip()
#             print(proxy)
#             if proxy:
#                 valid_proxies.append(proxy)
#         except Exception as e:
#             continue
#         return valid_proxies
#
# def get_valid_proxies():
#     proxies_list = parse_proxies(get_proxy_html())
#     valid_proxies = validate_proxy(proxies_list, get_session(proxies_list))
#     print(valid_proxies)
# get_valid_proxies()