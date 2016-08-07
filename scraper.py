#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup


def main():
    html = urlopen("https://www.oreilly.co.jp/ebook/")
    bs = BeautifulSoup(html, "html.parser")

    book_table = bs.find("table", {"id": "bookTable"})

    print(book_table.thead.tr)

    for tr in book_table.tbody.findAll("tr"):
        print(tr)

if __name__ == '__main__':
    main()
