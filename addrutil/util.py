# -*- coding: utf-8 -*-

from dicregion import DicRegion
from diccode import  STDTrie 


#tree = STDTrie()
#dic = DicRegion()
#
#fnode = dic.getNode(u'北京')
#
#for code in fnode.codes:
#    t = tree.search(code)
#    for rtype, typename, e in t:
#        print rtype, typename, e.encode('utf-8')
#    print '*' * 20


# 返回结果会是一个集合
# 因此查询时还需要一个参数是  province city county town

"""
广东省
广州市
越秀区
北京街道
********************
辽宁省
大连市
西岗区
北京街道
********************
北京市
********************
"""

class AddrCompletion(object):

    def __init__(self, sourcedir='./source_data/', dicdir='./data/'):
        self.dic = DicRegion(dicdir=dicdir)
        self.tree = STDTrie(dicdir=sourcedir)

    def getFullAddr(self, addrtoken, rtype):
        node = self.dic.getNode(addrtoken)
        if not node:
            return None
        if not node.codes:
            return None
        for code in node.codes:
            t = self.tree.search(code)
            if t:
                rtype_1, rtypename, region = t[-1]
                if rtype_1 == rtype:
                    return t


if __name__ == '__main__':
    from dicregion import RType
    acom = AddrCompletion()
    t = acom.getFullAddr(u'北京', RType.TOWN)
    print t
