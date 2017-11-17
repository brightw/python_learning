import requests
import re
from bs4 import BeautifulSoup
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

g_main_url = 'http://www.dy2018.com'


def is_correct_li(li):
    return li.a is not None and li.a.get('href') is not None

def is_high_li(li):
    if is_correct_li(li) == False:
        return False
    
    match = re.search(r'(20\d[789]).*', li.a.string)
    match = match and re.search(r'.*([789]\.\d).*', li.a.string)
    score = float(match.group(1)) if match else 0.0
    return score >= 7.0

def print_li(li):
    print("{}  <{}>".format(li.a.string, g_main_url+li.a.get('href')))

def main():

    resp = requests.get(g_main_url)
    resp.encoding = 'gb18030'

    #print(resp.text)
    soup = BeautifulSoup(resp.text, 'lxml')

    for li in soup.select('div .co_content222 ul li'):
        if is_high_li(li):
            print_li(li)

if __name__ == '__main__':
    main()