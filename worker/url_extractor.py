#!/usr/bin/env python3
from urllib.parse import urlparse
from urllib.request import urlopen

from bs4 import BeautifulSoup


def extract_detail_urls(collection_url):
    try:
        html = urlopen(collection_url)
    except ValueError:
        return []

    # print(html.read())
    soup = BeautifulSoup(html.read(), "html.parser")
    links = soup.findAll('a', {'id': 'documentsbutton'})

    parse_result = urlparse(collection_url)
    root_url = "%s://%s" % (parse_result.scheme, parse_result.netloc)
    urls = ["%s%s" % (root_url, link['href']) for link in links]
    # print(urls)
    return urls
