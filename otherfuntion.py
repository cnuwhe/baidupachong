import os
import datetime
import urllib.request
from bs4 import BeautifulSoup

def getyesterday():
    now = datetime.datetime.now()
    yesterday = now - datetime.timedelta(days=1)
    yesterday = yesterday.strftime('%m-%d')
    return yesterday


def readkeywords(filename):
    keywords = []
    try:
        fileread = open(filename, 'r')
        for line in fileread.readlines():
            line = line.strip("\n")
            keywords.append(line)
    except:
        print("error no such file")
    return keywords

if __name__ == '__main__':
    split='/p/5090575182'
    basepage = "http://tieba.baidu.com"
    baseurl = basepage+split
    webheader = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=baseurl, headers=webheader)
    page = urllib.request.urlopen(req)
    data = page.read()
    data = str(data, encoding='utf-8')
    bytes(data, encoding='utf-8')
    soup = BeautifulSoup(data, "html.parser")
    p1 = soup.find_all('div', "l_post j_l_post l_post_bright  ")
    print(p1)
    for child in p1:
        tail=child.find('div','core_reply_tail ')
        res=tail.find_all('span')
        for each in res:
            print(each)

