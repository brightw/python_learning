import requests
import re
from bs4 import BeautifulSoup
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

dytd_main_url = 'http://www.dy2018.com'
ygdy_mail_url = 'http://www.ygdy8.com'

def is_correct_href(href):
    return href is not None and href.get('href') is not None


def is_high_href(href):
    if is_correct_href(href) == False:
        return False
    
    match = re.search(r'(20\d[789]).*', href.string)
    match = match and re.search(r'.*([789]\.\d).*', href.string)
    score = float(match.group(1)) if match else 0.0

    return score >= 7.0 or href.string.find(u'\u9ad8\u5206') != -1

def print_href(href, main_url):
    print("{:>60}  <{}>".format(href.string, main_url+href.get('href')))


def list_dytd():
    resp = requests.get(dytd_main_url)
    resp.encoding = 'gb18030'
    soup = BeautifulSoup(resp.text, 'lxml')
    for href in soup.select('div .co_content222 ul li a'):
        if is_high_href(href):
            print_href(href, dytd_main_url)

def list_ygdy():
    resp = requests.get(ygdy_mail_url)
    resp.encoding = 'gb18030'
    soup = BeautifulSoup(resp.text, 'lxml')
    for href in soup.select('div .co_content8 td a'):
        if is_high_href(href):
            print_href(href, ygdy_mail_url)



def main():

    print("************************************  {}  ************************************".format(dytd_main_url))
    list_dytd()
    
    print("************************************  {}  ************************************".format(ygdy_mail_url))
    list_ygdy()

if __name__ == '__main__':
    main()