# Write a Python program that returns top stories from http://www.technewsworld.com
# The program should retrieve the most recent top 10 stories in the form:  title, date, and URL.

# Since many third-party libraries are not supported on the CSE machines, your solution does not have
# to run on the CSE machines. However, if you use any additional libraries, they must also be available via

# Pip -> https://pip.pypa.io/en/stable/

# easy_install -> https://pypi.python.org/pypi/setuptools
# (Unofficial Binaries) -> http://www.lfd.uci.edu/~gohlke/pythonlibs/

# Tips: Beautiful soup, urllib, and urllib2 are libraries I use often for getting information from web pages.

import urllib2
from bs4 import BeautifulSoup


def main():
    url = "http://www.technewsworld.com"

    data = urllib2.urlopen(url).read()
    soup = BeautifulSoup(data, 'html.parser')
    news = soup.find_all("div", class_="story-list")

    x = 0
    article = {}
    for element in news:
        title = element.a.get_text()
        if title != '':
            article[news[x].find(class_="title").get_text()] = {}
        x += 1

    x = 0
    for element in news:
        title = element.a.get_text()
        if title != '':
            article[news[x].find(class_="title").get_text()]["link"] = url + element.a["href"]
        x += 1

    iterator = 0
    for element in news:
        title = element.a.get_text()
        if title != '':
            article[news[iterator].find(class_="title").get_text()]["date"] = news[iterator].find(class_="date").get_text()
        iterator += 1

    for item in article.keys():
        print item + ": " + "\n\t" + "link: " + article[item]["link"] + "\n\t" + "date: " + article[item]["date"] + "\n\n"


if __name__ == "__main__":
    main()
