#! /usr/bin/python

import requests

from bs4 import BeautifulSoup


def main():
    r = requests.get('http://www.whatismyip.com')

    soup = BeautifulSoup(r.text)

    ip_address = ''
    for span in soup.find('div', 'the-ip'):
        ip_address += span.text

    print(ip_address)


if __name__ == '__main__':
    main()
