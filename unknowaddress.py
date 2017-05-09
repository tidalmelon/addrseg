# -*- coding: utf-8 -*-

from entities import AddressTokenInf
from entities import AddTypeInf
from entities import AddressType
from entities import AddTypes


class UnknowAddress(object):

    @staticmethod
    def mergeUnknow(tokens):

        #for i in range(len(tokens)):
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token.data is not None:
                i += 1
                continue

            unknowText = ''
            start = token.start
            while True:
                unknowText += token.termText
                del tokens[i]
                if i >= len(tokens):
                    end = token.end
                    unKnowTokenInf = AddressTokenInf(start, end, unknowText)
                    item = AddTypeInf(AddressType.Unknow, 10, 0, unKnowTokenInf)
                    d = AddTypes()
                    d.put(item)
                    unKnowTokenInf.setData(d)
                    tokens.insert(i, unKnowTokenInf)
                    break
                token = tokens[i]
                if token.data is not None:
                    end = token.start

                    unKnowTokenInf = AddressTokenInf(start, end, unknowText)
                    item = AddTypeInf(AddressType.Unknow, 10, 0, unKnowTokenInf)
                    d = AddTypes()
                    d.put(item)
                    unKnowTokenInf.setData(d)
                    tokens.insert(i, unKnowTokenInf)
                    break

            i += 1
