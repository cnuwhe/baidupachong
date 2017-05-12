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
    data = str(data, encoding='utf-8')
    # 爬虫没写好，内容被注释掉了。。。。。去注释
    data = data.replace('<!--', '')
    data = data.replace('-->', '')
    bytes(data, encoding='utf-8')
    return data


def readtitle(homepage):
    contents = []
    soup = BeautifulSoup(homepage, "html.parser")
    f = open('base2.txt', 'w', encoding='utf-8')
    p1 = soup.find_all('div', "t_con cleafix")
    for child in p1:
        try:
            ttitle = child.find("a")
            if(ttitle['title'] != "点击隐藏本贴"):
                res = ttitle['title'] + "|" + ttitle['href'] + "|"
                # f.write(ttitle['title'])
                # f.write("|")
                # f.write(ttitle['href'])
                tlastre = child.find(
                    "span", "threadlist_reply_date pull_right j_reply_data")
                res = res + tlastre.get_text().lstrip()
                # f.write(tlastre.get_text().lstrip())
                # f.write('\n-----------------------------------\n')
                contents.append(res)
        except Exception as e:
            print(e)
    return contents
if __name__ == '__main__':
    homepage = readhomepage(
        "http://tieba.baidu.com/f?kw=%E9%98%BF%E5%BE%B7%E8%8E%B1%E5%BE%B7%E5%A4%A7%E5%AD%A6&fr=wwwt")
    basepage = "http://tieba.baidu.com"
    titles = readtitle(homepage)
    for each in titles:
        print(each)
