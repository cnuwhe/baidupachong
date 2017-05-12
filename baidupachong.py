import urllib.request
import re
from bs4 import BeautifulSoup

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


def readhomepage(homepage):
    baseurl = homepage
    webheader = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=baseurl, headers=webheader)
    page = urllib.request.urlopen(req)
    data = page.read()
    data = data.decode('UTF-8')
    return data
if __name__ == '__main__':
    homepage = readhomepage(
        "http://tieba.baidu.com/f?kw=%E5%AE%A0%E7%89%A9&fr=wwwt")
    basepage = "http://tieba.baidu.com"
    f = open('base.txt', 'w', encoding='utf-8')
    f.write(homepage)
    p1 = r'"/p/\d*" title="\S*"'
    p1 = re.compile(p1)
    res = re.findall(p1, homepage)
    for x in res:
        print(x)
    print(type(res))

