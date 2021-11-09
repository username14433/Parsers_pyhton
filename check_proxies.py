import random
import time

import requests
from bs4 import BeautifulSoup

URL = 'https://free-proxy-list.net/'

start_time = time.time()
def get_proxy_html(url):
    response = requests.get(url=url)
    return response.text


def parse_proxies(resp):
    """Parse web site with free proxies."""
    proxies_list = []
    soup = BeautifulSoup(resp, 'lxml')
    main_div = soup.find('div', class_='table-responsive fpl-list')
    if main_div:
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


def get_session(proxies):
    session = requests.Session()
    proxy = random.choice(proxies)
    session.proxies = {"http": "http://" + proxy, "https": "https://" + proxy}
    return session

def validate_proxy(proxies, session):
    valid_proxies = []
    for proxy in proxies:
        try:
            s = get_session(proxies)
            proxy = s.get('http://icanhazip.com/', timeout=1.5).text.strip()
            if proxy and len(proxy) <= 16 and ':' not in proxy:
                valid_proxies.append(proxy)
        except Exception as e:
            continue
    return valid_proxies
# print(validate_proxy(parse_proxies(get_proxy_html(URL)), get_session(parse_proxies(get_proxy_html(URL)))))


def call_all():
    proxies_list = parse_proxies(get_proxy_html(URL))
    valid_proxies = validate_proxy(proxies_list, get_session(proxies_list))
    print(len(valid_proxies))
    return valid_proxies
print(call_all())
