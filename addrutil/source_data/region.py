# -*- coding: utf-8 -*-

import urllib2
from lxml import etree
import re
from six.moves.urllib.parse import urljoin
import Queue
import codecs
import os

"""
http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2014/index.html
http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2014/11.html
http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2014/11/1101.html
http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2014/11/01/110101.html
http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2014/11/01/01/110101001.html

http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2014/61.html
http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2014/61/6101.html
http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2014/61/01/610102.html
http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2014/61/01/02/610102001.html
"""
pat_prov = re.compile('http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2014/\d+.html')
pat_city = re.compile('http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2014/\d+/\d+.html')
pat_county = re.compile('http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2014/\d+/\d+/\d+.html')
pat_town = re.compile('http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2014/\d+/\d+/\d+/\d+.html')

f_prov = codecs.open('province.txt', mode='wb', encoding='utf-8')
f_city = codecs.open('city.txt', mode='wb', encoding='utf-8')
f_county = codecs.open('county.txt', mode='wb', encoding='utf-8')
f_town = codecs.open('town.txt', mode='wb', encoding='utf-8')
f_vill = codecs.open('village.txt', mode='wb', encoding='utf-8')

que = Queue.Queue()
seed = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2014/index.html'
que.put([seed, 0])


def getHtml(url):
    request = urllib2.Request(url)
    request.add_header(
        'User-Agent',
        'Mozilla/5.0 (Windows NT 6.1; rv:19.0) Gecko/20100101 Firefox/19.0')
    #doc = urllib2.urlopen(request, timeout=45).read().decode('gbk')
    doc = urllib2.urlopen(request, timeout=45).read().decode('gbk', 'ignore')
    return doc


while que.qsize() > 0:
    url, count = que.get()
    if count >= 3:
        print 'retry three time', url, count
        continue
    try:
        doc = getHtml(url)
        dom = etree.HTML(doc)

        if url == seed:
            es = dom.xpath("//table[@class='provincetable']/tr[@class='provincetr']/td/a") 
            for e in es:
                prov = e.xpath('./text()')[0]
                rlink = e.xpath('./@href')[0]

                code = rlink.split('.', 1)[0]
                num_0 = 12 - len(code)
                code = code + '0' * num_0

                key = '%s\t%s' % (prov, code)
                print key.encode('utf-8')
                f_prov.write(key + os.linesep)

                link = urljoin(url, rlink)
                que.put([link, 0])
            continue

        if pat_prov.match(url):
            es = dom.xpath("//tr[@class='citytr']") 
            for e in es:
                code = e.xpath('./td[1]//text()')[0]
                city = e.xpath('./td[2]//text()')[0]

                key = '%s\t%s' % (city, code)
                print key.encode('utf-8')
                f_city.write(key + os.linesep)
                
                rlink = e.xpath('./td[2]/a/@href')[0]
                link = urljoin(url, rlink)
                que.put([link, 0])
            continue

        if pat_city.match(url):
            es = dom.xpath("//tr[@class='countytr']") 
            for e in es:
                code = e.xpath('./td[1]//text()')[0]
                county = e.xpath('./td[2]//text()')[0]

                key = '%s\t%s' % (county, code)
                print key.encode('utf-8')
                f_county.write(key + os.linesep)
                
                try:
                    rlink = e.xpath('./td[2]/a/@href')[0]
                    link = urljoin(url, rlink)
                    que.put([link, 0])
                except IndexError:
                    pass
            continue

        if pat_county.match(url):
            es = dom.xpath("//tr[@class='towntr']") 
            for e in es:
                code = e.xpath('./td[1]//text()')[0]
                town = e.xpath('./td[2]//text()')[0]

                key = '%s\t%s' % (town, code)
                print key.encode('utf-8')
                f_town.write(key + os.linesep)
                
                try:
                    rlink = e.xpath('./td[2]/a/@href')[0]
                    link = urljoin(url, rlink)
                    que.put([link, 0])
                except IndexError:
                    pass
            continue

        if pat_town.match(url):
            es = dom.xpath("//tr[@class='villagetr']") 
            for e in es:
                code = e.xpath('./td[1]//text()')[0]
                village = e.xpath('./td[3]//text()')[0]

                key = '%s\t%s' % (village, code)
                print key.encode('utf-8')
                f_vill.write(key + os.linesep)
                
            continue
    except:
        print 'err, que again'
        count += 1
        que.put([url, count])
