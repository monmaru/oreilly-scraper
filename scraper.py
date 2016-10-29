#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv


def scrape():
    # noinspection PyBroadException
    try:
        html = urlopen('https://www.oreilly.co.jp/ebook/')
        bs = BeautifulSoup(html, 'html.parser')
        table = bs.find('table', {'id': 'bookTable'})
        body = [parse_tr(tr) for tr in table.tbody.findAll('tr')]

        with open('eBooks.csv', 'w', encoding='utf-8') as f:
            w = csv.writer(f)
            w.writerow(['ISBN', 'タイトル', '価格', '発行月', 'フォーマット'])
            w.writerows(body)
    except:
        import traceback
        traceback.print_exc()


def parse_tr(tr):
    isbn = tr.find('td', {'class': 'isbn'}).string
    title = tr.find('td', {'class': 'title'}).find('a').string
    price = tr.find('td', {'class': 'price'}).string
    month = tr.find('td', {'class': None}).string
    form = ' | '.join([img.attrs['title'] for img in tr.findAll('img')])
    return [isbn, title, price, month, form]

if __name__ == '__main__':
    scrape()
