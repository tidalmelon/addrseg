# -*- coding=utf-8 -*-

import urlparse



def reverseUrl(url):
    """
    examples:

    http://bar.foo.com:8983/to/index.html?a=b
    com.foo.bar:http:8983/to/index.html?a=b
    
    https://www.google.com.hk:8080/home/search;12432?newwi.1.9.serpuc#1234
    hk.com.google.www:https:8080/home/search;12432?newwi.1.9.serpuc#1234
    """
    reverse_url = ''
    url = urlparse.urlsplit(url)

    reverse_host = '.'.join(url.hostname.split('.')[::-1])
    reverse_url += reverse_host

    reverse_url += ':'
    reverse_url += url.scheme

    if url.port:
        reverse_url += ':'
        reverse_url += str(url.port)

    if url.path:
        reverse_url += url.path

    if url.query:
        reverse_url += '?'
        reverse_url += url.query

    if url.fragment:
        reverse_url += '#'
        reverse_url += url.fragment

    return reverse_url


if __name__ == '__main__':
    url = 'http://www.tianyancha.com/company/2313776032'
    url = 'http://www.11467.com/foshan/co/444200.htm'
    print reverseUrl(url)



