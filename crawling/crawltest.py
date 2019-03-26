import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError
import re
import itertools
import robotpar


def download(url, num_retries=2, user_agent="wswp", charset='utf-8'):
    print("Downloading:", url)
    request = urllib.request.Request(url)
    if not user_agent:
        request.add_header("User-agent", user_agent)

    try:
        req = urllib.request.urlopen(request)
        cs = req.headers.get_content_charset()
        if not cs:
            cs = charset
        html = req.read().decode(cs)
    except (URLError, HTTPError, ContentTooShortError) as e:
        print("Download error:", e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, "code") and 500 <= e.code < 600:
                return download(url, num_retries - 1)
    return html


#下载比较多列表的数据
def crawl_site(url, max_errors=5):
    num_errors = 0
    for page in itertools.count(1):
        pg_url = '{}{}'.format(url, page)
        html = download(pg_url)
        if html is None:
            num_errors += 1
            if num_errors == max_errors:
                break
        else:
            pass
            #print(html)


def link_crawler(start_url, link_regex, robots_url=None, user_agent='wswp'):
    if not robots_url:
        robots_url = '{}/robots.txt'.format(start_url)
    crawl_queue = [start_url]
    while crawl_queue:
        url = crawl_queue.pop()

        if robotpar.check_download(url):
            html = download(url)
        if html is None:
            continue
        for link in get_links(html):
            crawl_queue.append(link)


def get_links(html):
    webpage_regex = re.compile("""<link[^>]+href=["'](.*?)["']""",
                               re.IGNORECASE)
    urls = webpage_regex.findall(html)

    return urls


if __name__ == "__main__":
    link_crawler("http://www.baidu.com", '/(index/view)')
