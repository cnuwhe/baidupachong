import urllib.request
if __name__ == '__main__':
    baseurl = "http://tieba.baidu.com/f?ie=utf-8&kw=%E9%98%BF%E5%BE%B7%E8%8E%B1%E5%BE%B7%E5%A4%A7%E5%AD%A6&fr=search&red_tag=i3356703565"
    webheader = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req=urllib.request.Request(url=baseurl,headers=webheader)
    page=urllib.request.urlopen(req)
    data=page.read()
    data=data.decode('UTF-8')
    f=open('base.txt','w')
    f.write(data)
