# -*- coding: utf-8 -*-

import os
import codecs

class RType(object):

    PROVINCE = 0
    CITY = 1
    COUNTY = 2
    TOWN = 3
    # 目前先不支持吧，
    # 需要修改数据结构
    # 加载所有村会内存溢出
    #VILLAGE = 4

    names = ['PROVINCE', 'CITY', 'COUNTY', 'TOWN']


class TSTNode(object):

    def __init__(self, key):
        self.splitChar = key
        self.loNode = None
        self.eqNode = None
        self.hiNode = None
        self.codes = None

    def __str__(self):
        line = self.splitChar
        line += str(list(self.codes))
        return line.encode('utf-8')


class DicRegion(object):

    def __init__(self, dicdir='./data/'):

        self.rootNode = None

        fname = os.path.join(dicdir, 'province.txt')
        self.loadDict(fname)
        fname = os.path.join(dicdir, 'city.txt')
        self.loadDict(fname)
        fname = os.path.join(dicdir, 'county.txt')
        self.loadDict(fname)
        fname = os.path.join(dicdir, 'town.txt')
        self.loadDict(fname)

    def loadDict(self, fname):
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
                currentNode = self.getOrCreateNode(token)
                if not currentNode.codes:
                    # token可能相同，但code不同
                    # 兴安县， 兴安盟 token是相同的，但code不同 
                    # 重名的还很多
                    currentNode.codes = set()
                    currentNode.codes.add(code)
                else:
                    currentNode.codes.add(code)

    def getOrCreateNode(self, key):

        charIndex = 0

        if self.rootNode is None:
            self.rootNode = TSTNode(key[0])

        currentNode = self.rootNode

        while True:
            compa = ord(key[charIndex]) - ord(currentNode.splitChar)
            if compa == 0:
                charIndex += 1
                if charIndex == len(key):
                    return currentNode

                if currentNode.eqNode is None:
                    currentNode.eqNode = TSTNode(key[charIndex])

                currentNode = currentNode.eqNode
            elif compa < 0:
                if currentNode.loNode is None:
                    currentNode.loNode = TSTNode(key[charIndex])
                currentNode = currentNode.loNode
            else:
                if currentNode.hiNode is None:
                    currentNode.hiNode = TSTNode(key[charIndex])
                currentNode = currentNode.hiNode

    def getNode(self, key):
        if not key:
            return None
        size = len(key)
        if size == 0:
            return None

        charIndex = 0
        currentNode = self.rootNode

        while True:
            if not currentNode:
                return None
            compa = ord(key[charIndex]) - ord(currentNode.splitChar)

            if compa == 0:
                charIndex += 1
                if charIndex == size:
                    return currentNode
                currentNode = currentNode.eqNode
            elif compa < 0:
                currentNode = currentNode.loNode
            else:
                currentNode = currentNode.hiNode

if __name__ == '__main__':
    dic = DicRegion()
    fnode = dic.getNode(u'北京市')
    print fnode.codes
