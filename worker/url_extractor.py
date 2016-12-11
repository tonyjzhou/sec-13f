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
    links = soup.findAll('a', attrs={'id': 'documentsbutton'})
    sub_dirs = [link['href'] for link in links]

    return _make_full_urls(collection_url, sub_dirs)


def extract_url_13f_xml(detail_url):
    try:
        html = urlopen(detail_url)
    except ValueError:
        return []

    # print(html.read())
    soup = BeautifulSoup(html.read(), "html.parser")
    links = soup.findAll('a', text='form13fInfoTable.xml')
    sub_dirs = [link['href'] for link in links]

    return _make_full_urls(detail_url, sub_dirs)


def _make_full_urls(url, sub_dirs):
    parse_result = urlparse(url)
    root_url = "%s://%s" % (parse_result.scheme, parse_result.netloc)
    urls = ["%s%s" % (root_url, sub_dir) for sub_dir in sub_dirs]
    # print(urls)
    return urls
