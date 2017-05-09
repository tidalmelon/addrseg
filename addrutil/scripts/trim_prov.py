# -*- coding: utf-8 -*-

import sys

suffixs = [u'壮族自治区', u'回族自治区', u'维吾尔自治区', u'省', u'市', u'自治区']

for line in sys.stdin:
    line = line.strip()
    print line
    line = line.decode('utf-8')
    arr = line.split()
    if len(arr) != 2:
        print 'err'
        sys.exit()
    prov, code = arr
    for suffix in suffixs:
        if prov.endswith(suffix):
            prov = prov.replace(suffix, '')
            key = '%s %s' % (prov, code)
            print key.encode('utf-8')
