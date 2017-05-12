import os
import datetime


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
    yesterday = getyesterday()
    print(yesterday)
    keywords = readkeywords('keywords.txt')
    print(keywords)
