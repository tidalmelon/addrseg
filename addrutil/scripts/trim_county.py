# -*- coding: utf-8 -*-

import sys

names = [u'市辖区', u'县']
names.append(u'城区')
names.append(u'矿区')
names.append(u'南郊区')
names.append(u'郊区')
names.append(u'中沙群岛的岛礁及其海域')

suffixs = []
suffixs.append(u'群岛')
suffixs.append(u'行政委员会')
suffixs.append(u'回族自治县')
suffixs.append(u'满族蒙古族自治县')
suffixs.append(u'满族自治县')
suffixs.append(u'新区')
suffixs.append(u'矿区')
suffixs.append(u'区')
suffixs.append(u'县')
suffixs.append(u'市')
# 这里还有很多

def endwith(county, suffixs, code):
    for suffix in suffixs:
        if county.endswith(suffix):
            county = county.replace(suffix, '')
            key = '%s\t%s' % (county, code)
            print key.encode('utf-8')
            return True
    return False

for line in sys.stdin:
    line = line.strip()
    print line
    line = line.decode('utf-8')
    arr = line.split()
    if len(arr) != 2:
        print 'err'
        sys.exit()
    county, code = arr

    if county in names:
        continue

    if endwith(county, suffixs, code):
        continue

    if county.endswith(u'旗'):
        continue

    print 'err'
