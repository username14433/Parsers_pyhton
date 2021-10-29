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
    main_table = soup.find('table', class_='table table-striped table-bordered').find_all('tr')
    for tr in main_table:
        trs = tr.find('td')
        if trs:
            proxies_list.append(trs.text)
    return proxies_list


def get_session(proxies):
    session = requests.Session()
    proxy = random.choice(proxies)
    session.proxies = {"http": proxy, "https": proxy}
    return session


def validate_proxy(proxies, session):
    valid_proxies = []
    for i in range(30):
        s = get_session(proxies)
        try:
            proxy = s.get("http://icanhazip.com", timeout=1.5).text.strip()
            if proxy and len(proxy) < 70:
                valid_proxies.append(proxy)
        except Exception as e:
            continue
        return valid_proxies


def get_valid_proxies():
    proxies_list = parse_proxies(get_proxy_html())
    valid_proxies = validate_proxy(proxies_list, get_session(proxies_list))
    return valid_proxies
