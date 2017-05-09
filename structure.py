# -*- coding: utf-8 -*-

from entities import AddressTokenInf
from entities import AddTypeInf
from entities import AddressType
from entities import AddTypes


class AdjList(object):

    def __init__(self, verticesNum):
        self.verticesNum = verticesNum
        # storage: AddressTokenInf
        self.list = [[] for i in range(verticesNum)]

        # add start AddressTokenInf
        startToken = AddressTokenInf(-1, 0, '')

        # item create
        posInf = AddTypeInf(AddressType.Start, 10, 0, startToken)
        # add item to sort list
        addressData = AddTypes()
        addressData.put(posInf)
        startToken.setData(addressData)

        # add edge
        self.addEdge(startToken)

    def addEdge(self, newAdge):
        self.list[newAdge.end].append(newAdge)

    def getCost(self, frm, to):
        if frm == to:
            return 0.0
        for t in self.list[to]:
            if t.start == frm:
                return t.cost
        return float('inf')

    def __str__(self):
        tmp = []
        for r in range(self.verticesNum):
            if not self.list[r]:
                continue
            tmp.append('node:')
            tmp.append(str(r))
            tmp.append(': ')
            for c in range(self.verticesNum):
                ati = self.list[r][c]
                tmp.append(str(ati))
            tmp.append('\n')

        return ''.join(tmp)

