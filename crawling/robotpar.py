#coding=utf-8
from urllib import robotparser

def  get_robots_parser(url):
    rp = robotparser.RobotFileParser()
    rp.set_url(url)
    rp.read()
    return rp


def  check_download(url, user_agent='wswp'):    
    rp = get_robots_parser(url)
    return rp.can_fetch(user_agent, url)

    
'''
url = 'http://example.python-scraping.com'
user_agent = 'BadCrawler'
print( rp.can_fetch(user_agent, url))

user_agent = 'GoodCrawler'
print( rp.can_fetch(user_agent, url))
'http://example.python-scraping.com/robots.txt'
'''