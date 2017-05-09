# -*- coding: utf-8 -*-
import codecs
import os

from dicregion import RType

"""
输入code找出完整的行政区划
"""

class TrieNode(object):

    def __init__(self):
        self.region = None 
        self.dic = {}

    def __str__(self):
        return self.region.encode('utf-8')


class STDTrie(object):

    def __init__(self, dicdir='./source_data/'):
        self.root = TrieNode()

        fname = os.path.join(dicdir, 'province.txt')
        self.loaddict(fname)

        fname = os.path.join(dicdir, 'city.txt')
        self.loaddict(fname)

        fname = os.path.join(dicdir, 'county.txt')
        self.loaddict(fname)

        fname = os.path.join(dicdir, 'town.txt')
        self.loaddict(fname)
        
        #fname = os.path.join(dicdir, 'village.txt')
        #self.loaddict(fname)

    def loaddict(self, fname):
        with codecs.open(fname, encoding='utf-8', errors='ignore') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                line = line.strip()
                arr = line.split()
                if len(arr) != 2:
                    continue

                token, code = arr[0], arr[1]
                self.add(code, token)

    def add(self, code, region):
        if len(code) != 12:
            return

        p = code[0: 2]
        c = code[2: 4]
        ct = code[4: 6]
        t = code[6: 9]
        v = code[9: 12]
        seq = [p, c, ct, t, v]
        seq = [e for e in seq if int(e) != 0]

        current = self.root
        for key in seq:
            nextNode = current.dic.get(key)
            if not nextNode:
                nextNode = TrieNode()
                current.dic[key] = nextNode
            current = nextNode
        current.region = region

    def search(self, code):
        if len(code) != 12:
            return

        p = code[0: 2]
        c = code[2: 4]
        ct = code[4: 6]
        t = code[6: 9]
        v = code[9: 12]
        seq = [p, c, ct, t, v]
        seq = [e for e in seq if int(e) != 0]

        current = self.root
        t = []
        #for key in seq:
        for rtype, key in enumerate(seq):
            current = current.dic.get(key)
            if current:
                t.append((rtype, RType.names[rtype], current.region))
        return t


if __name__ == '__main__':

    tree = STDTrie()

    #tree.add('360000000000', u'江西省')
    #tree.add('360100000000', u'南昌市')
    #tree.add('360102000000', u'东湖区')
    #tree.add('360102001000', u'公园街道办事处')
    #tree.add('360102001001', u'上营坊社区居委会')

    #t = tree.search('360102001001')
    #for e in t:
    #    print e.encode('utf-8')
    #print '*' * 20

    #t = tree.search('360102001000')
    #for e in t:
    #    print e.encode('utf-8')
    #print '*' * 20

    #t = tree.search('360102000000')
    #for e in t:
    #    print e.encode('utf-8')
    #print '*' * 20

    #t = tree.search('360100000000')
    #for e in t:
    #    print e.encode('utf-8')
    #print '*' * 20

    #t = tree.search('360000000000')
    #for e in t:
    #    print e.encode('utf-8')
    #print '*' * 20

    t = tree.search('110000000000')
    for e in t:
        print e.encode('utf-8')
    print '*' * 20

