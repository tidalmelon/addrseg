#!/usr/bin/env python
# coding=utf-8

import codecs

fname = 'county_city.csv'
with codecs.open(fname, encoding='gbk') as f:
    while True:
        line = f.readline()
        if not line:
            break
        line = line.strip()
        line = line.replace('"', '')
        arr = line.split(',')
        print arr[1].encode('utf-8')
