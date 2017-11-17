import requests
from bs4 import BeautifulSoup
import sys

reload(sys)
sys.setdefaultencoding('utf-8')



def main():

    main_url = 'http://www.dy2018.com'
    resp = requests.get(main_url)
    resp.encoding = 'gb18030'

    print(resp.text)
    soup = BeautifulSoup(resp.text, 'lxml')
    ##for child in soup.body.children:
    ##    print(child)

    for li in soup.select('li'):
        if li.a is not None:
            li_string = li.a.string
            print("li.a attr", li.a.attrs['title'])
            print(li_string)


if __name__ == '__main__'
    main()