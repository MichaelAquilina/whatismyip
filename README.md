whatismyip
==========

Command line tool to print out your current ip address. 

Works by scraping the contents of www.whatismyip.com

Requirements:
* BeautifulSoup4
* lxml
* requests

The best way to utilise this script is to create a symbolic link in `/usr/local/bin` to the `whatismyip.py` script.

    ln -s /path/to/whatismyip/whatismyip.py /usr/local/bin/whatismyip

This will allow you to run the `whatismyip` command from anywhere.
