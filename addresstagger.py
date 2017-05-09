# -*- coding: utf-8 -*-

from structure import AdjList
from entities import AddressTokenInf
from entities import AddTypes
from entities import AddTypeInf
from entities import AddressType
from entities import AddressToken
from unknowaddress import UnknowAddress
from unknowgrammar import UnknowGrammar


class AddressTagger(object):
    def __init__(self, dictAddress, contextStatAddress, grammar):

        self.dicAddress = dictAddress
        self.contextStatAddress = contextStatAddress
        self.grammar = grammar

        self.minValue = -2147483648 / 2

    def getAdjList(self, addressStr):

        #存放匹配的节点信息
        start = 0
        atomCount = len(addressStr)

        #初始化dictionary中词组成的图
        g = AdjList(atomCount + 2)

        #开始分词
        while True:
            matchRet = self.dicAddress.matchAll(addressStr, start)
            if len(matchRet) > 0:
                for ret in matchRet:
                    termText = addressStr[start: ret.end]
                    tokenInf = AddressTokenInf(start, ret.end, termText)

                    addDicData = AddTypes()

                    for ati in ret.posInf.data:
                        addDicData.put(AddTypeInf.convertFrom(ati, tokenInf))

                    tokenInf.setData(addDicData)
                    g.addEdge(tokenInf)
                start += 1
            else:
                edge = AddressTokenInf(start, start + 1, addressStr[start: start + 1])
                g.addEdge(edge)
                start += 1
            if start > atomCount:
                break
        return g

    def tag(self, addressStr):
        g = self.getAdjList(addressStr)
        atomCount = len(addressStr)
        endToken = AddressTokenInf(atomCount, atomCount + 1, '')
        posInf = AddTypeInf(AddressType.End, 10, 0, endToken)

        addressData = AddTypes()
        addressData.put(posInf)
        endToken.setData(addressData)
        g.addEdge(endToken)

        tokens = self.maxProb(g, endToken)
        matchRet = UnknowGrammar.MatchRet(0, None)
        offset = 0
        while True:
            matchRet = self.grammar.matchLong(tokens, offset, matchRet)

            if matchRet.lhs is not None:
                self.grammar.replace(tokens, offset, matchRet.lhs)
                offset = 0
            else:
                offset += 1
                if offset > len(tokens):
                    break
        return tokens

    def maxProb(self, g, endToken):

        for i in range(1, g.verticesNum):
            tt = g.list[i]
            for t in tt:
                self.getPrev(g, t)

        ret = []
        i = endToken
        while i:
            ret.append(i)
            i = i.bestPrev

        ret.reverse()
        UnknowAddress.mergeUnknow(ret)

        self.hmm(ret, endToken)

        lst = []
        codess = 0
        for tokenInf in ret:
            start = tokenInf.start
            end = tokenInf.end
            code = tokenInf.bestTypeInf.code if tokenInf.bestTypeInf is not None else 0
            typ = tokenInf.bestTypeInf.pos if tokenInf.bestTypeInf is not None else 0
            termText = tokenInf.termText
            addressToken = AddressToken(start=start,
                                        end=end,
                                        word=termText,
                                        type=typ,
                                        code=code)
            if codess > 0 and not self.getCode(codess, addressToken.code):
                codess = 0
            elif addressToken.code > 0:
                codess = addressToken.code

            lst.append(addressToken)

        return lst

    def getCode(self, Code, nextcode):
        min_ = Code - nextcode if Code > nextcode else nextcode - Code
        longth = str(min_)
        currentCode = str(Code)
        sCode = str(nextcode)

        if '0' == sCode or '0' == currentCode:
            return True

        if len(longth) > 10:
            return False

        try:
            idx1 = currentCode.index('000')
        except:
            idx1 = -1

        try:
            idx2 = sCode.index('000')
        except:
            idx2 = -1

        if idx1 < 13 - len(longth) or idx2 < 13 - len(longth):
            return True
        else:
            return False

    def getPrev(self, g, ati):

        maxFee = self.minValue
        maxId = None

        for t in g.list[ati.start]:
            currentCost = t.cost
            currentCost += self.contextStatAddress.getContextPossibility_1(t, ati)
            if currentCost > maxFee:
                maxId = t
                maxFee = currentCost

        if maxFee != self.minValue:
            ati.cost += maxFee
        else:
            ati.cost = maxFee

        ati.bestPrev = maxId

    def hmm(self, ret, endToken):
        code = 0
        for ati in ret[0].data.data:
            ati.prob = 1

        for stage in range(1, len(ret)):
            nextInf = ret[stage]
            if nextInf.data is None:
                continue
            for nextTypeInf in nextInf.data.data:

                preInf = ret[stage - 1]
                if preInf.data is None:
                    continue
                
                for preTypeInf in preInf.data.data:
                    trans = self.contextStatAddress.getContextPossibility(preTypeInf.pos, nextTypeInf.pos)
                    prob = preTypeInf.prob

                    if preTypeInf.code > 0 and nextTypeInf.code > 0 and self.getCode(preTypeInf.code, nextTypeInf.code):
                        trans = 800000000
                        code = nextTypeInf.code

                    if preTypeInf.code == 0 and code > 0 and nextTypeInf.code > 0 and self.getCode(code,
                                                                                                   nextTypeInf.code):
                        trans = 800000000
                        code = nextTypeInf.code

                    prob = prob + trans + nextTypeInf.weight
                    if nextTypeInf.prob <= prob:
                        nextTypeInf.prob = prob
                        nextTypeInf.bestPre = preTypeInf

                    elif nextTypeInf.bestPre is None:
                        nextTypeInf.bestPre = preTypeInf

        if endToken.data.getHead() is not None:
            i = endToken.data.getHead()
            while i is not None:
                i.parent.bestTypeInf = i
                i = i.bestPre
