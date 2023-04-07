import scrapy
import os
from scrapy.crawler import CrawlerProcess, CrawlerRunner
import html2text
from urllib.parse import urlparse
from twisted.internet import reactor
from scrapy.utils.project import get_project_settings
from multiprocessing import Process, Queue
import re

class KuzenSpider(scrapy.Spider):
    name = "kuzen"
    start_urls = [
        'https://www.kuzen.io',
        'https://corp.kuzen.io',
        'https://corp.kuzen.io/news.html'
    ]

    def parse(self, response):
        for href in response.css('a::attr(href)').getall():
            if href.startswith('http'):
                yield scrapy.Request(href, callback=self.parse_page)
            elif href[0] == "/" and href != "/":
                yield scrapy.Request(response.url + href, callback=self.parse_page)
            elif href.split('/')[0] != '':
                domain = urlparse(response.url).netloc
                yield scrapy.Request(f'https://{domain}/{href}', callback=self.parse_page)

    def parse_page(self, response):
        h = html2text.HTML2Text()
        h.ignore_links = True
        content = h.handle(response.text)
        # Save data to files
        if urlparse(response.url).netloc in ["kuzen.io", "note.com", "corp.kuzen.io"]:
            link_path = response.url.replace('http://', '').replace('https://', '').replace('/', '_')
            filename_data = os.path.join('data_crawled', link_path + ".txt")
            os.makedirs(os.path.dirname(filename_data), exist_ok=True)
            cleaned_content = re.sub(r'\!\[[^\]]*[^\)]+[^\n]*\)', '', content)
            with open(filename_data, 'w', encoding="utf-8") as data:
                data.write(cleaned_content)
            for href in response.css('a::attr(href)').getall():
                if href.startswith('http'):
                    yield scrapy.Request(href, callback=self.parse_page)

def run_spider():
    process = CrawlerProcess(get_project_settings())
    process.crawl(KuzenSpider)
    process.start()

def start_crawl():
    def f(q):
        try:
            runner = CrawlerRunner()
            deferred = runner.crawl(KuzenSpider)
            deferred.addBoth(lambda _: reactor.stop())
            reactor.run()
            q.put(None)
        except Exception as e:
            q.put(e)

    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    result = q.get()
    p.join()

    if result is not None:
        raise result