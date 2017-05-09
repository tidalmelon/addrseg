# -*- coding: utf-8 -*-

import sys

names = [u'自治区直辖县级行政区划', u'省直辖县级行政区划', u'市辖区', u'县']

suffixs = [u'地区', u'市', u'盟']
suffixs.append(u'朝鲜族自治州')
suffixs.append(u'土家族苗族自治州')
suffixs.append(u'藏族羌族自治州')
suffixs.append(u'藏族自治州')
suffixs.append(u'彝族自治州')
suffixs.append(u'布依族苗族自治州')
suffixs.append(u'苗族侗族自治州')
suffixs.append(u'哈尼族彝族自治州')
suffixs.append(u'壮族苗族自治州')
suffixs.append(u'傣族自治州')
suffixs.append(u'白族自治州')
suffixs.append(u'傣族景颇族自治州')
suffixs.append(u'傈僳族自治州')
suffixs.append(u'藏族自治州')
suffixs.append(u'回族自治州')
suffixs.append(u'蒙古族藏族自治州')
suffixs.append(u'蒙古自治州')
suffixs.append(u'柯尔克孜自治州')
suffixs.append(u'哈萨克自治州')

def endwith(city, suffixs, code):
    for suffix in suffixs:
        if city.endswith(suffix):
            city = city.replace(suffix, '')
            key = '%s\t%s' % (city, code)
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
    city, code = arr

    if city in names:
        continue

    if endwith(city, suffixs, code):
        continue

    print 'err'
