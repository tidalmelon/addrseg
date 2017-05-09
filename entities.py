# -*- coding: utf-8 -*-

import bisect


class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance


class AddressType(object):
    Country = 0
    Municipality = 1  # 直辖市
    SuffixMunicipality = 2  # 特别行政区后缀
    Province = 3  # 省
    City = 4  # 市
    County = 5  # 区
    Town = 6  # 镇
    Street = 7  # 街道
    StreetNo = 8  # 街门牌号
    No = 9  # 编号
    Symbol = 10  # 字母符号
    LandMark = 11  # 地标性建筑
    RelatedPos = 12  # 相对位置
    Crossing = 13  # 交叉路
    DetailDesc = 14  # 详细描述
    ChildFacility = 15  # 子设施
    Village = 16  # 村
    VillageNo = 17  # 村号
    BuildingNo = 18  # 楼号
    BuildingUnit = 19  #楼单元
    SuffixBuildingUnit = 20  #楼单元后缀
    SuffixBuildingNo = 21  #楼号后缀
    Start = 22  # 开始状态
    End = 23  # 结束状态
    StartSuffix = 24 
    EndSuffix = 25
    Unknow = 26
    Other = 27
    SuffixProvince = 28
    SuffixCity = 29
    SuffixCounty = 30
    District = 31
    SuffixDistrict = 32
    SuffixTown = 33
    SuffixStreet = 34
    SuffixLandMark = 35
    SuffixVillage = 36
    SuffixIndicationFacility = 37  # 指示性设施后缀
    IndicationFacility = 38  # 指示性设施
    SuffixIndicationPosition = 39  # 指示设施方位后缀
    IndicationPosition = 40  # 指示性设施方位
    Conj = 41  # 连接词

    names = ['Country', 'Municipality', 'SuffixMunicipality', 'Province', 'City', 'County', 'Town', 'Street', 'StreetNo', 'No', 'Symbol', 'LandMark', 'RelatedPos', 'Crossing', 'DetailDesc', 'ChildFacility', 'Village', 'VillageNo', 'BuildingNo', 'BuildingUnit', 'SuffixBuildingUnit', 'SuffixBuildingNo', 'Start', 'End', 'StartSuffix', 'EndSuffix', 'Unknow', 'Other', 'SuffixProvince', 'SuffixCity', 'SuffixCounty', 'District', 'SuffixDistrict', 'SuffixTown', 'SuffixStreet', 'SuffixLandMark', 'SuffixVillage', 'SuffixIndicationFacility', 'IndicationFacility', 'SuffixIndicationPosition', 'IndicationPosition', 'Conj'] 

    def getName(idx):
        return AddressType.names[idx]

    @staticmethod
    def getLen():
        return 42

class AddTypeInf(object):
    def __init__(self, pos, freq, semanticCode, parent):
        """
        param:bestPrev AddTypeInf, herself
        param:parent AddressTokenInf
        """
        self.pos = pos
        self.weight = freq
        self.code = semanticCode
        self.prob = 0
        self.parent = parent

        self.bestPre = None

    @staticmethod
    def convertFrom(addTypeInf, parent):
        ins = AddTypeInf(addTypeInf.pos, addTypeInf.freq, addTypeInf.code, parent)
        ins.prob = 0
        ins.bestPre = None
        return ins

    def __cmp__(self, other):
        return cmp(self.pos, other.pos)

    def __str__(self):
        return AddressType.names[self.pos] + ':' + str(self.weight)


class AddTypes(object):
    def __init__(self):
        self.data = []

    def put(self, item):
        self.data.append(item)

    def insert(self, item):
        bisect.insort(self.data, item)

    def findType(self, pos):
        try:
            idx = self.data.index(AddTypeInf(pos))
            return self.data[idx]
        except ValueError:
            return None

    def size(self):
        return len(self.data)

    def totalCost(self):
        return sum([e.weight for e in self.data])

    def getHead(self):
        return self.data[0]

    def __str__(self):
        res = u''
        for ati in self.data:
            res += str(ati)
        return res


class AddDicTypes(object):

    class AddTypeInf(object):

        def __init__(self, pos, freq, semanticCode):
            self.pos = pos
            # 频率
            self.freq = freq
            # 语义编码
            self.code = semanticCode

        def __cmp__(self, other):
            return cmp(self.pos, other.pos)

        def __str__(self):
            return AddressType.names[self.pos] + ':' + str(self.freq)

    def __init__(self):
        self.data = []

    def put(self, item):
        self.data.append(item)

    def insert(self, item):
        bisect.insort(self.data, item)

    def findType(self, pos):
        toFind = AddDicTypes.AddTypeInf(pos, 0, 0)
        idx = bisect.bisect_left(self.data, toFind)
        try:
            if self.data[idx] == toFind:
                return self.data[idx]
        except IndexError:
            return None
        return None

    def size(self):
        return len(self.data)

    def totalCost(self):
        return sum([e.freq for e in self.data])

    def getHead(self):
        return self.data[0]

    def __str__(self):
        buf = [str(item) for item in self.data]
        return ' '.join(buf)


class AddressTokenInf(object):
    def __init__(self, vertexFrom, vertexTo, word):
        self.start = vertexFrom
        self.end = vertexTo
        self.termText = word

        self.data = None
        self.cost = 0

        self.bestPrev = None
        self.bestTypeInf = None

    def setData(self, d):
        self.data = d
        self.cost = d.totalCost()

    def __str__(self):
        line =  u'text:' + self.termText + ' '\
               + 'start:' + str(self.start) + ' ' \
               + 'end:' + str(self.end) + ' '\
               + 'cost:' + str(self.cost) + ' '\
               + 'data:' + str(self.data)
        return line.encode('utf-8')


class AddressToken(object):
    def __init__(self, start=None, end=None, cost=None, word=None, type=None, code=None):
        self.termText = word
        self.type = type
        self.start = start
        self.end = end
        self.cost = cost
        self.code = code

    def __str__(self):

        line = 'text:' + self.termText + ' start:' + str(self.start) \
                + ' end:' + str(self.end) + ' cost:' + str(self.cost) \
                + ' pos:' + AddressType.names[self.type] + ' code:' + str(self.code)
        line = line.encode('utf-8')
        return line

