# -*- coding: utf-8 -*-

from entities import AddressType
from entities import AddressToken


class AddressSpan(object):
    def __init__(self, l, t):
        self.length = l
        self.type = t

    def __str__(self):
        return AddressType.names[self.type] + ':' + str(self.length)


class UnknowGrammar(object):

    class TSTNode(object):
        
        def __init__(self, splitchar):
            self.splitchar = splitchar
            self.root = None

            self.data = None
            self.loKID = None
            self.eqKID = None
            self.hiKID = None

        def __str__(self):
            return 'splitchar:' + self.splitchar

    #class Prefix(object):

    #    def __init__(self, val):
    #        self.value = val

    #    def __str__(self):
    #        if self.value == 0:
    #            return 'Match'
    #        elif self.value == 1:
    #            return 'MisMatch'
    #        elif self.value == 2:
    #            return 'MatchPrefix'
    #        return 'Invalid'

    class MatchRet(object):

        def __init__(self, e, d):
            self.end = e
            self.lhs = d

        def __str__(self):
            tmp = [str(e) for e in self.lhs]
            tmp = ' '.join(tmp)
            return str(self.end) + ':' + tmp

    def __init__(self):

        self.root = None

        # 北京市
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Municipality)
        rhs.append(AddressType.SuffixCity)
        lhs = []
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(2, AddressType.Municipality))
        self.addProduct(rhs, lhs)

        #北京市朝阳区高碑店乡高碑店
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Municipality)
        rhs.append(AddressType.County)
        rhs.append(AddressType.County)
        rhs.append(AddressType.SuffixTown)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.End)
        lhs = []
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Municipality))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(2, AddressType.Town))
        lhs.append(AddressSpan(1, AddressType.Town))
        lhs.append(AddressSpan(1, AddressType.Unknow))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        #中国江苏南京市江苏省
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Country)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.SuffixProvince)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Country))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.Unknow))
        lhs.append(AddressSpan(2, AddressType.Province))

        self.addProduct(rhs, lhs)

        # 中国江苏江阴市江苏省
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Country)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.SuffixProvince)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Country))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.Unknow))
        lhs.append(AddressSpan(2, AddressType.Province))

        self.addProduct(rhs, lhs)
        # 中国江苏苏州市吴中区江苏省
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Country)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.SuffixProvince)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Country))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.Unknow))
        lhs.append(AddressSpan(2, AddressType.Province))

        self.addProduct(rhs, lhs)
        # 中国江苏苏州市吴中区江苏省
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.County)
        rhs.append(AddressType.SuffixProvince)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(2, AddressType.Province))

        self.addProduct(rhs, lhs)
        # 河南郑州市河南省
        lhs = []
        rhs = []
        rhs.append(AddressType.SuffixIndicationFacility)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.SuffixProvince)
        lhs.append(AddressSpan(3, AddressType.Province))

        self.addProduct(rhs, lhs)

        # 河南郑州市河南省
        lhs = []
        rhs = []
        rhs.append(AddressType.Province)
        rhs.append(AddressType.SuffixProvince)
        lhs.append(AddressSpan(2, AddressType.Province))

        self.addProduct(rhs, lhs)

        # =============================以下是市部分

        # 中国江苏南京市
        lhs = []
        rhs = []

        rhs.append(AddressType.City)
        rhs.append(AddressType.SuffixCity)
        lhs.append(AddressSpan(2, AddressType.City))

        self.addProduct(rhs, lhs)
        # 中国江苏南京市
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Country)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.SuffixCity)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Country))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(2, AddressType.City))

        self.addProduct(rhs, lhs)

        # 中国江苏南京市南京市
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Country)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.City)
        rhs.append(AddressType.SuffixCity)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Country))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.Unknow))
        lhs.append(AddressSpan(2, AddressType.City))

        self.addProduct(rhs, lhs)
        # 中国江苏南京市栖霞区南京市
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Country)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.City)
        rhs.append(AddressType.SuffixCity)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Country))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.Unknow))
        lhs.append(AddressSpan(2, AddressType.City))

        self.addProduct(rhs, lhs)
        # 广东省东莞市市
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.SuffixCity)
        rhs.append(AddressType.SuffixCity)
        rhs.append(AddressType.SuffixCounty)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(2, AddressType.City))
        lhs.append(AddressSpan(2, AddressType.Other))

        self.addProduct(rhs, lhs)

        # 广东省东莞市市
        lhs = []
        rhs = []
        rhs.append(AddressType.Other)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.Street)
        lhs.append(AddressSpan(1, AddressType.Other))
        lhs.append(AddressSpan(3, AddressType.Street))

        self.addProduct(rhs, lhs)

        # 河南省郑州市
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.SuffixCity)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(2, AddressType.City))

        self.addProduct(rhs, lhs)

        # =================================以下是县区部分
        # 北京市朝阳区
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.SuffixCounty)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(2, AddressType.County))

        self.addProduct(rhs, lhs)

        # 北京市大兴区
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.County)
        rhs.append(AddressType.SuffixCounty)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(2, AddressType.County))

        self.addProduct(rhs, lhs)
        #
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Country)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.SuffixCounty)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Country))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.Unknow))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(2, AddressType.County))
        self.addProduct(rhs, lhs)
        # 中国江苏常州市江苏省常州市武进区
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Country)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.SuffixProvince)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.SuffixCounty)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Country))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.Unknow))
        lhs.append(AddressSpan(2, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.Unknow))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(2, AddressType.County))
        self.addProduct(rhs, lhs)
        # 中国江苏如东县
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Country)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.County)
        rhs.append(AddressType.SuffixCounty)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Country))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(2, AddressType.County))
        self.addProduct(rhs, lhs)
        # 中国 江苏 无锡市惠山区
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Country)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.SuffixCounty)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Country))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(2, AddressType.County))
        self.addProduct(rhs, lhs)
        # 广东省广州市白云区
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.SuffixCounty)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(2, AddressType.County))
        self.addProduct(rhs, lhs)
        # 东城区
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.County)
        rhs.append(AddressType.SuffixCounty)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(2, AddressType.County))
        self.addProduct(rhs, lhs)
        # 近郊密云县
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Other)
        rhs.append(AddressType.Town)
        rhs.append(AddressType.SuffixCounty)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Other))
        lhs.append(AddressSpan(2, AddressType.County))
        self.addProduct(rhs, lhs)

        # 中国江苏海安县海安县
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Country)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.County)
        rhs.append(AddressType.SuffixCounty)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Country))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.Unknow))
        lhs.append(AddressSpan(2, AddressType.County))
        self.addProduct(rhs, lhs)
        # 中国江苏常州市新北区江苏常州市新北区
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Country)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.SuffixCounty)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Country))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.Unknow))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(2, AddressType.County))
        self.addProduct(rhs, lhs)
        # 中国江苏无锡市惠山区无锡市惠山区
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Country)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.SuffixCounty)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Country))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.Unknow))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(2, AddressType.County))
        self.addProduct(rhs, lhs)

        # 中原区
        lhs = []
        rhs = []
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.SuffixCounty)
        lhs.append(AddressSpan(3, AddressType.County))
        self.addProduct(rhs, lhs)

        # 万江区
        lhs = []
        rhs = []
        rhs.append(AddressType.No)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.SuffixCounty)
        lhs.append(AddressSpan(3, AddressType.County))
        self.addProduct(rhs, lhs)

        # 道里区
        lhs = []
        rhs = []
        rhs.append(AddressType.SuffixStreet)
        rhs.append(AddressType.SuffixLandMark)
        rhs.append(AddressType.SuffixCounty)
        lhs.append(AddressSpan(2, AddressType.County))
        self.addProduct(rhs, lhs)
        # 河南新郑机场台商投资区建设路南侧
        lhs = []
        rhs = []
        rhs.append(AddressType.Province)
        rhs.append(AddressType.County)
        rhs.append(AddressType.LandMark)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.SuffixCounty)
        rhs.append(AddressType.Street)
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.LandMark))
        lhs.append(AddressSpan(2, AddressType.District))
        lhs.append(AddressSpan(1, AddressType.Street))
        self.addProduct(rhs, lhs)

        # 彭水县
        lhs = []
        rhs = []
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.SuffixCounty)
        lhs.append(AddressSpan(2, AddressType.County))
        self.addProduct(rhs, lhs)

        # 市区
        lhs = []
        rhs = []
        rhs.append(AddressType.SuffixCity)
        rhs.append(AddressType.SuffixCounty)
        lhs.append(AddressSpan(2, AddressType.County))
        self.addProduct(rhs, lhs)
        # 中国 江苏 南京市 雨花台区铁心桥星河工业园8号
        # 2010.5.26
        lhs = []
        rhs = []
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.SuffixCounty)
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(2, AddressType.County))
        self.addProduct(rhs, lhs)
        # 江宁区
        lhs = []
        rhs = []
        rhs.append(AddressType.County)
        rhs.append(AddressType.SuffixCounty)
        lhs.append(AddressSpan(2, AddressType.County))
        self.addProduct(rhs, lhs)

        # ========================以下是镇乡
        # 石排镇
        lhs = []
        rhs = []
        rhs.append(AddressType.City)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.SuffixBuildingNo)
        rhs.append(AddressType.SuffixTown)
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(3, AddressType.Town))
        self.addProduct(rhs, lhs)

        # 昌平镇
        lhs = []
        rhs = []
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.SuffixTown)
        lhs.append(AddressSpan(2, AddressType.Town))
        self.addProduct(rhs, lhs)

        # =================================以下是街道号等

        # 惠山经济开发区
        lhs = []
        rhs = []

        rhs.append(AddressType.County)
        rhs.append(AddressType.SuffixDistrict)
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.District))
        self.addProduct(rhs, lhs)
        # 洛社配套区
        lhs = []
        rhs = []

        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.SuffixDistrict)
        lhs.append(AddressSpan(2, AddressType.District))
        self.addProduct(rhs, lhs)

        # 玄武大道
        lhs = []
        rhs = []

        rhs.append(AddressType.County)
        rhs.append(AddressType.SuffixStreet)
        lhs.append(AddressSpan(2, AddressType.Street))
        self.addProduct(rhs, lhs)
        #
        lhs = []
        rhs = []

        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.SuffixStreet)
        lhs.append(AddressSpan(2, AddressType.Street))
        self.addProduct(rhs, lhs)

        # 2号楼
        lhs = []
        rhs = []

        rhs.append(AddressType.No)
        rhs.append(AddressType.SuffixBuildingUnit)
        lhs.append(AddressSpan(2, AddressType.BuildingUnit))
        self.addProduct(rhs, lhs)
        # 东路
        lhs = []
        rhs = []

        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.SuffixStreet)
        lhs.append(AddressSpan(2, AddressType.SuffixStreet))
        self.addProduct(rhs, lhs)
        # 六路
        lhs = []
        rhs = []

        rhs.append(AddressType.No)
        rhs.append(AddressType.SuffixStreet)
        lhs.append(AddressSpan(2, AddressType.SuffixStreet))
        self.addProduct(rhs, lhs)
        # 学院路
        lhs = []
        rhs = []

        rhs.append(AddressType.SuffixLandMark)
        rhs.append(AddressType.SuffixStreet)
        lhs.append(AddressSpan(2, AddressType.Street))
        self.addProduct(rhs, lhs)

        # 精神病医院
        lhs = []
        rhs = []

        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.SuffixLandMark)
        lhs.append(AddressSpan(2, AddressType.LandMark))
        self.addProduct(rhs, lhs)
        # 台城大厦
        lhs = []
        rhs = []

        rhs.append(AddressType.LandMark)
        rhs.append(AddressType.SuffixLandMark)
        lhs.append(AddressSpan(2, AddressType.LandMark))
        self.addProduct(rhs, lhs)
        # # 文峰大厦
        # lhs = []
        # rhs = []
        #
        # rhs.append(AddressType.County)
        # rhs.append(AddressType.SuffixLandMark)
        # lhs.append(AddressSpan(2, AddressType.LandMark))
        # self.addProduct(rhs, lhs)
        # 五公里处
        lhs = []
        rhs = []

        rhs.append(AddressType.No)
        rhs.append(AddressType.SuffixIndicationPosition)
        lhs.append(AddressSpan(2, AddressType.IndicationPosition))
        self.addProduct(rhs, lhs)
        # 四幢
        lhs = []
        rhs = []

        rhs.append(AddressType.No)
        rhs.append(AddressType.SuffixBuildingNo)
        lhs.append(AddressSpan(2, AddressType.BuildingNo))
        self.addProduct(rhs, lhs)

        # distract
        lhs = []
        rhs = []

        rhs.append(AddressType.LandMark)
        rhs.append(AddressType.DetailDesc)
        rhs.append(AddressType.SuffixDistrict)
        lhs.append(AddressSpan(3, AddressType.District))
        self.addProduct(rhs, lhs)

        # 玉村镇
        lhs = []
        rhs = []

        rhs.append(AddressType.Village)
        rhs.append(AddressType.SuffixTown)
        lhs.append(AddressSpan(2, AddressType.Town))
        self.addProduct(rhs, lhs)

        # 广东省东莞市长安镇107国道长安酒店斜对面
        lhs = []
        rhs = []

        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.Town)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.County)
        rhs.append(AddressType.SuffixLandMark)
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.Town))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(2, AddressType.LandMark))
        self.addProduct(rhs, lhs)

        # 江苏省南京市新街口洪武北路青石街24号
        lhs = []
        rhs = []

        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.Street)
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(3, AddressType.Street))
        self.addProduct(rhs, lhs)

        # 东莞市厚街镇新厚沙路新塘村路口直入出100米
        lhs = []
        rhs = []

        rhs.append(AddressType.Start)
        rhs.append(AddressType.City)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.SuffixTown)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.Street)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(2, AddressType.Town))
        lhs.append(AddressSpan(1, AddressType.Street))
        self.addProduct(rhs, lhs)

        # 重庆市渝北区两路镇龙兴街84号号码一支路五星小区对面
        lhs = []
        rhs = []

        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.SuffixTown)
        rhs.append(AddressType.Street)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(2, AddressType.Town))
        lhs.append(AddressSpan(1, AddressType.Street))
        self.addProduct(rhs, lhs)
        # 江苏省南京市高淳县开发区商贸区998号
        lhs = []
        rhs = []

        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.SuffixDistrict)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.SuffixCounty)
        rhs.append(AddressType.No)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.SuffixDistrict))
        lhs.append(AddressSpan(2, AddressType.District))
        lhs.append(AddressSpan(2, AddressType.No))
        self.addProduct(rhs, lhs)
        # 广东省东莞市厚街镇家具大道国际家具大道
        lhs = []
        rhs = []

        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.SuffixTown)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.Street)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(2, AddressType.Town))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.Street))
        self.addProduct(rhs, lhs)

        # 江苏省南京市江宁区淳化镇淳化居委会
        lhs = []
        rhs = []

        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Town)
        rhs.append(AddressType.County)
        rhs.append(AddressType.SuffixLandMark)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.End)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.Town))
        lhs.append(AddressSpan(3, AddressType.DetailDesc))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 海淀区西三环新兴桥西北角(新兴宾馆门口)
        lhs = []
        rhs = []

        rhs.append(AddressType.Start)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.LandMark)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.StartSuffix)
        rhs.append(AddressType.County)
        rhs.append(AddressType.SuffixLandMark)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.LandMark))
        lhs.append(AddressSpan(2, AddressType.RelatedPos))
        lhs.append(AddressSpan(1, AddressType.StartSuffix))
        lhs.append(AddressSpan(2, AddressType.DetailDesc))
        self.addProduct(rhs, lhs)

        # 朝阳区建国门外永安里新华保险大厦南侧(119中学西侧)
        lhs = []
        rhs = []

        rhs.append(AddressType.District)
        rhs.append(AddressType.LandMark)
        rhs.append(AddressType.County)
        rhs.append(AddressType.LandMark)
        lhs.append(AddressSpan(1, AddressType.District))
        lhs.append(AddressSpan(1, AddressType.LandMark))
        lhs.append(AddressSpan(2, AddressType.LandMark))
        self.addProduct(rhs, lhs)

        # 沙田西太隆工业区
        lhs = []
        rhs = []

        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.District)
        lhs.append(AddressSpan(3, AddressType.District))
        self.addProduct(rhs, lhs)

        # 东城区
        # lhs = []
        # rhs = []
        #
        # rhs.append(AddressType.RelatedPos)
        # rhs.append(AddressType.District)
        # lhs.append(AddressSpan(2, AddressType.County))
        # self.addProduct(rhs, lhs)

        # 东城区
        lhs = []
        rhs = []

        rhs.append(AddressType.LandMark)
        rhs.append(AddressType.SuffixStreet)
        lhs.append(AddressSpan(2, AddressType.Street))
        self.addProduct(rhs, lhs)

        # 大岭山工业区
        lhs = []
        rhs = []

        rhs.append(AddressType.District)
        rhs.append(AddressType.SuffixDistrict)
        lhs.append(AddressSpan(2, AddressType.District))
        self.addProduct(rhs, lhs)

        # 锦厦新村
        lhs = []
        rhs = []

        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.SuffixVillage)
        lhs.append(AddressSpan(2, AddressType.Village))
        self.addProduct(rhs, lhs)

        # 第二工业区
        lhs = []
        rhs = []

        rhs.append(AddressType.No)
        rhs.append(AddressType.SuffixDistrict)
        lhs.append(AddressSpan(2, AddressType.District))
        self.addProduct(rhs, lhs)

        # 花园新村
        lhs = []
        rhs = []

        rhs.append(AddressType.SuffixLandMark)
        rhs.append(AddressType.SuffixVillage)
        lhs.append(AddressSpan(2, AddressType.Village))
        self.addProduct(rhs, lhs)

        # 北京市朝阳区霞光里66号远洋新干线A座908室
        lhs = []
        rhs = []

        rhs.append(AddressType.No)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.Symbol)
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(3, AddressType.LandMark))
        lhs.append(AddressSpan(1, AddressType.Symbol))
        self.addProduct(rhs, lhs)
        # 雨花台区
        lhs = []
        rhs = []

        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.County)
        lhs.append(AddressSpan(2, AddressType.County))
        self.addProduct(rhs, lhs)

        # 新寓二村
        lhs = []
        rhs = []

        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.Village)
        lhs.append(AddressSpan(2, AddressType.Village))
        self.addProduct(rhs, lhs)

        # 港口路
        lhs = []
        rhs = []

        rhs.append(AddressType.SuffixDistrict)
        rhs.append(AddressType.SuffixStreet)
        lhs.append(AddressSpan(2, AddressType.Street))
        self.addProduct(rhs, lhs)

        # #新风中路
        # lhs = []
        # rhs = []
        #
        # rhs.append(AddressType.Unknow)
        # rhs.append(AddressType.RelatedPos)
        # lhs.append(AddressSpan(2, AddressType.Street))
        # self.addProduct(rhs, lhs)

        # 学前路
        lhs = []
        rhs = []

        rhs.append(AddressType.Street)
        rhs.append(AddressType.SuffixStreet)
        lhs.append(AddressSpan(2, AddressType.Street))
        self.addProduct(rhs, lhs)

        #
        lhs = []
        rhs = []

        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.Street)
        lhs.append(AddressSpan(2, AddressType.Street))
        self.addProduct(rhs, lhs)

        # 哈尔滨市哈平路集中区黄海路39号
        lhs = []
        rhs = []

        rhs.append(AddressType.City)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.SuffixCounty)
        rhs.append(AddressType.Street)
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(2, AddressType.District))
        lhs.append(AddressSpan(1, AddressType.Street))
        self.addProduct(rhs, lhs)

        # 广东省东莞市市区红山西路红街二巷9号
        lhs = []
        rhs = []

        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.Street)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(3, AddressType.Street))
        self.addProduct(rhs, lhs)

        # 东莞市横沥镇中山路576号
        lhs = []
        rhs = []

        rhs.append(AddressType.Start)
        rhs.append(AddressType.City)
        rhs.append(AddressType.Town)
        rhs.append(AddressType.City)
        rhs.append(AddressType.SuffixStreet)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.Town))
        lhs.append(AddressSpan(2, AddressType.Street))
        self.addProduct(rhs, lhs)

        # 东城区北锣鼓巷沙络胡同7号院(近安定门地铁A口)
        lhs = []
        rhs = []

        rhs.append(AddressType.Start)
        rhs.append(AddressType.County)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.Street)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(2, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.Street))
        self.addProduct(rhs, lhs)

        # 东城区北三环和平里东街小街桥北(美廉美东北角)
        lhs = []
        rhs = []

        rhs.append(AddressType.Start)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.SuffixLandMark)
        rhs.append(AddressType.RelatedPos)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.LandMark))
        lhs.append(AddressSpan(1, AddressType.RelatedPos))
        self.addProduct(rhs, lhs)

        # 广东省广州市白云区广园中路景泰直街东2巷2号认真英语大厦903
        lhs = []
        rhs = []

        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.Street)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(2, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.RelatedPos))
        lhs.append(AddressSpan(1, AddressType.Street))
        self.addProduct(rhs, lhs)

        # 广东省广州市从化市太平镇太平经济技术开发区
        lhs = []
        rhs = []

        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Town)
        rhs.append(AddressType.County)
        rhs.append(AddressType.District)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.Town))
        lhs.append(AddressSpan(2, AddressType.District))
        self.addProduct(rhs, lhs)

        # 广东省广州市番禺区大石街冼村城岗大街3巷10号
        lhs = []
        rhs = []

        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.Village)
        rhs.append(AddressType.SuffixLandMark)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.Street)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.Village))
        lhs.append(AddressSpan(3, AddressType.Street))
        self.addProduct(rhs, lhs)

        # 海淀区大钟寺四道口路1号(近学院南路)
        lhs = []
        rhs = []

        rhs.append(AddressType.Start)
        rhs.append(AddressType.County)
        rhs.append(AddressType.District)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.No)
        rhs.append(AddressType.StartSuffix)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.SuffixLandMark)
        rhs.append(AddressType.Street)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.District))
        lhs.append(AddressSpan(2, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(1, AddressType.StartSuffix))
        lhs.append(AddressSpan(1, AddressType.RelatedPos))
        lhs.append(AddressSpan(1, AddressType.SuffixLandMark))
        lhs.append(AddressSpan(1, AddressType.IndicationPosition))
        self.addProduct(rhs, lhs)
        # 朝阳区来广营西路88号
        lhs = []
        rhs = []

        rhs.append(AddressType.Start)
        rhs.append(AddressType.City)
        rhs.append(AddressType.SuffixCounty)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(2, AddressType.County))
        self.addProduct(rhs, lhs)

        # 道镇闸口村东莞电化集团进宝工业区
        lhs = []
        rhs = []

        rhs.append(AddressType.Start)
        rhs.append(AddressType.SuffixStreet)
        rhs.append(AddressType.SuffixTown)
        rhs.append(AddressType.Village)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(2, AddressType.Town))
        lhs.append(AddressSpan(1, AddressType.Village))
        self.addProduct(rhs, lhs)
        # 道镇闸口村东莞电化集团进宝工业区
        lhs = []
        rhs = []

        rhs.append(AddressType.Town)
        rhs.append(AddressType.Village)
        rhs.append(AddressType.City)
        rhs.append(AddressType.District)
        lhs.append(AddressSpan(1, AddressType.Town))
        lhs.append(AddressSpan(1, AddressType.Village))
        lhs.append(AddressSpan(2, AddressType.District))
        self.addProduct(rhs, lhs)
        # 江苏省南京市高淳县淳溪镇镇兴路288号
        lhs = []
        rhs = []

        rhs.append(AddressType.County)
        rhs.append(AddressType.Town)
        rhs.append(AddressType.SuffixTown)
        rhs.append(AddressType.Street)
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.Town))
        lhs.append(AddressSpan(2, AddressType.Street))
        self.addProduct(rhs, lhs)

        # 重庆市巫溪县城厢镇镇泉街
        lhs = []
        rhs = []

        rhs.append(AddressType.County)
        rhs.append(AddressType.SuffixLandMark)
        rhs.append(AddressType.Town)
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(2, AddressType.Town))
        self.addProduct(rhs, lhs)
        # 北京市密云县檀营乡二村
        # 2010.5.24
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.Town)
        rhs.append(AddressType.SuffixCounty)
        rhs.append(AddressType.Town)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(2, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.Town))
        self.addProduct(rhs, lhs)
        # 重庆市永川市双竹镇石梯坎村
        # 2010.5.24
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.County)
        rhs.append(AddressType.SuffixCity)
        rhs.append(AddressType.Town)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(2, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.Town))
        self.addProduct(rhs, lhs)

        # 重庆市合川区市合阳镇文明街97号
        # 2010.5.24
        lhs = []
        rhs = []
        rhs.append(AddressType.County)
        rhs.append(AddressType.SuffixTown)
        lhs.append(AddressSpan(2, AddressType.Town))
        self.addProduct(rhs, lhs)

        # 江苏省南京市溧水县大东门街29号3楼
        # 2010.5.24
        lhs = []
        rhs = []
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.County)
        rhs.append(AddressType.SuffixBuildingUnit)
        rhs.append(AddressType.SuffixStreet)
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(3, AddressType.Street))
        self.addProduct(rhs, lhs)
        # 河南省郑州市惠济区桥南新区金桥路2号
        # 2010.5.24
        lhs = []
        rhs = []
        rhs.append(AddressType.County)
        rhs.append(AddressType.SuffixLandMark)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.SuffixDistrict)
        rhs.append(AddressType.Street)
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(3, AddressType.District))
        lhs.append(AddressSpan(1, AddressType.Street))
        self.addProduct(rhs, lhs)

        # 渝北区龙湖花园美食街
        # 2010.5.24
        lhs = []
        rhs = []
        rhs.append(AddressType.County)
        rhs.append(AddressType.SuffixLandMark)
        lhs.append(AddressSpan(2, AddressType.LandMark))
        self.addProduct(rhs, lhs)
        # 北京市房山区韩村河镇韩村河村
        # 2010.5.24
        lhs = []
        rhs = []
        rhs.append(AddressType.County)
        rhs.append(AddressType.Village)
        rhs.append(AddressType.SuffixIndicationFacility)
        rhs.append(AddressType.SuffixTown)
        rhs.append(AddressType.Village)
        rhs.append(AddressType.Village)
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(3, AddressType.Town))
        lhs.append(AddressSpan(2, AddressType.Village))
        self.addProduct(rhs, lhs)
        # 北京市房山区韩村河镇尤家坟村
        # 2010.5.24
        lhs = []
        rhs = []
        rhs.append(AddressType.County)
        rhs.append(AddressType.Village)
        rhs.append(AddressType.SuffixIndicationFacility)
        rhs.append(AddressType.SuffixTown)
        rhs.append(AddressType.Village)
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(3, AddressType.Town))
        lhs.append(AddressSpan(1, AddressType.Village))
        self.addProduct(rhs, lhs)
        # 北京市海淀区罗庄南里3号楼
        # 2010.5.24
        lhs = []
        rhs = []
        rhs.append(AddressType.County)
        rhs.append(AddressType.County)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.SuffixLandMark)
        rhs.append(AddressType.BuildingUnit)
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(3, AddressType.LandMark))
        lhs.append(AddressSpan(1, AddressType.BuildingUnit))
        self.addProduct(rhs, lhs)
        # 道镇闸口村东莞电化集团进宝工业区
        # 2010.5.24
        lhs = []
        rhs = []
        rhs.append(AddressType.Town)
        rhs.append(AddressType.Village)
        rhs.append(AddressType.Town)
        rhs.append(AddressType.District)
        lhs.append(AddressSpan(1, AddressType.Town))
        lhs.append(AddressSpan(1, AddressType.Village))
        lhs.append(AddressSpan(2, AddressType.District))
        self.addProduct(rhs, lhs)
        # 鼓楼区草场门大街阳光广场龙江体育馆内地图
        # 2010.5.24
        lhs = []
        rhs = []
        rhs.append(AddressType.LandMark)
        rhs.append(AddressType.County)
        rhs.append(AddressType.LandMark)
        lhs.append(AddressSpan(1, AddressType.LandMark))
        lhs.append(AddressSpan(2, AddressType.LandMark))
        self.addProduct(rhs, lhs)

        # 广东省东莞市市区红山西路红街二巷9号
        # 2010.5.24
        lhs = []
        rhs = []
        rhs.append(AddressType.City)
        rhs.append(AddressType.District)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.Street)
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.District))
        lhs.append(AddressSpan(3, AddressType.Street))
        self.addProduct(rhs, lhs)
        # 广东省广州市白云区机场路新市西街17号
        # 2010.5.24
        lhs = []
        rhs = []
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Street)
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(2, AddressType.Street))
        self.addProduct(rhs, lhs)
        # 广东省广州市海珠区工业大道南金城一街29号
        # 2010.5.24
        lhs = []
        rhs = []
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.City)
        rhs.append(AddressType.Street)
        lhs.append(AddressSpan(1, AddressType.RelatedPos))
        lhs.append(AddressSpan(2, AddressType.Street))
        self.addProduct(rhs, lhs)
        # 广东省广州市海珠区泰宁村南晒场2号13B
        # 2010.5.24
        lhs = []
        rhs = []
        rhs.append(AddressType.County)
        rhs.append(AddressType.County)
        rhs.append(AddressType.SuffixVillage)
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(2, AddressType.Village))
        self.addProduct(rhs, lhs)
        # 广东省广州市天河区龙口中路3号帝景苑C栋14E房
        # 2010.5.24
        lhs = []
        rhs = []
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Street)
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(2, AddressType.Street))
        self.addProduct(rhs, lhs)
        # 海淀区学院路明光北里8号
        # 2010.5.25
        lhs = []
        rhs = []
        rhs.append(AddressType.County)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.County)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.SuffixLandMark)
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(3, AddressType.LandMark))
        self.addProduct(rhs, lhs)

        # 重庆市渝中区嘉陵江滨江路
        # 2010.5.25
        # lhs = []
        # rhs = []
        # rhs.append(AddressType.Province)
        # rhs.append(AddressType.County)
        # rhs.append(AddressType.County)
        # rhs.append(AddressType.Street)
        # lhs.append(AddressSpan(1, AddressType.Province))
        # lhs.append(AddressSpan(1, AddressType.County))
        # lhs.append(AddressSpan(2, AddressType.Street))
        # self.addProduct(rhs, lhs)
        # 重庆市沙坪坝区马家岩临江装饰城14-5号
        # 2010.5.25
        lhs = []
        rhs = []
        rhs.append(AddressType.County)
        rhs.append(AddressType.District)
        rhs.append(AddressType.County)
        rhs.append(AddressType.LandMark)
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.District))
        lhs.append(AddressSpan(2, AddressType.LandMark))
        self.addProduct(rhs, lhs)
        # 中国 江苏 无锡市滨湖区 无锡前桥洋溪大桥南（振兴仓储有限公司）
        # 2010.5.25
        lhs = []
        rhs = []
        rhs.append(AddressType.StartSuffix)
        rhs.append(AddressType.County)
        rhs.append(AddressType.LandMark)
        lhs.append(AddressSpan(1, AddressType.StartSuffix))
        lhs.append(AddressSpan(2, AddressType.LandMark))
        self.addProduct(rhs, lhs)
        # 中国 江苏 无锡市北塘区 新兴工业区
        # 2010.5.25
        lhs = []
        rhs = []
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.County)
        rhs.append(AddressType.SuffixDistrict)
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(2, AddressType.District))
        self.addProduct(rhs, lhs)
        # 中国 江苏 苏州市吴中区 吴江市盛泽和服商区D幢16号
        # 2010.5.25
        lhs = []
        rhs = []
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.County)
        rhs.append(AddressType.LandMark)
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(2, AddressType.LandMark))
        self.addProduct(rhs, lhs)
        # 东莞市东城大道方中大厦2楼
        # 2010.5.25
        lhs = []
        rhs = []
        rhs.append(AddressType.City)
        rhs.append(AddressType.Town)
        rhs.append(AddressType.SuffixStreet)
        rhs.append(AddressType.LandMark)
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(2, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.LandMark))
        self.addProduct(rhs, lhs)
        # 江苏省南京市玄武区南拘中山东路301号
        # 2010.5.25
        lhs = []
        rhs = []
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.District)
        rhs.append(AddressType.Town)
        rhs.append(AddressType.Street)
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.District))
        lhs.append(AddressSpan(2, AddressType.Street))
        self.addProduct(rhs, lhs)
        # 河南郑州市河南省郑州市南关街民乐东里38号
        # 2010.5.25
        lhs = []
        rhs = []
        rhs.append(AddressType.Street)
        rhs.append(AddressType.County)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.SuffixLandMark)
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(3, AddressType.LandMark))
        self.addProduct(rhs, lhs)
        # 广东省东莞市大岭山镇连平下高田村
        # 2010.5.26
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.Town)
        rhs.append(AddressType.County)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.Village)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.End)
        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.Town))
        lhs.append(AddressSpan(3, AddressType.Village))
        lhs.append(AddressSpan(1, AddressType.Unknow))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 东莞市东城区花园新村市场路20号
        # 2010.5.26
        lhs = []
        rhs = []
        rhs.append(AddressType.City)
        rhs.append(AddressType.Town)
        rhs.append(AddressType.SuffixCounty)
        rhs.append(AddressType.Village)
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(2, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.Village))
        self.addProduct(rhs, lhs)
        # 北京市丰台区右安门外玉林里26号楼1单元301室
        # 2010.5.26
        lhs = []
        rhs = []
        rhs.append(AddressType.County)
        rhs.append(AddressType.District)
        rhs.append(AddressType.Town)
        rhs.append(AddressType.SuffixLandMark)
        rhs.append(AddressType.BuildingUnit)
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.District))
        lhs.append(AddressSpan(2, AddressType.LandMark))
        lhs.append(AddressSpan(1, AddressType.BuildingUnit))
        self.addProduct(rhs, lhs)

        # 北京市密云县工业开发区
        # 2010.5.26
        lhs = []
        rhs = []
        rhs.append(AddressType.Province)
        rhs.append(AddressType.Town)
        rhs.append(AddressType.SuffixCounty)
        rhs.append(AddressType.SuffixDistrict)
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(2, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.SuffixDistrict))
        self.addProduct(rhs, lhs)
        # 北京市密云县密云镇白檀村
        # 2010.5.26
        lhs = []
        rhs = []
        rhs.append(AddressType.County)
        rhs.append(AddressType.Town)
        rhs.append(AddressType.SuffixTown)
        rhs.append(AddressType.Village)
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(2, AddressType.Town))
        lhs.append(AddressSpan(1, AddressType.Village))
        self.addProduct(rhs, lhs)
        # 朝阳区博大中路荣华桥东(近亦庄)
        # 2010.5.26
        lhs = []
        rhs = []
        rhs.append(AddressType.StartSuffix)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.Town)
        lhs.append(AddressSpan(1, AddressType.StartSuffix))
        lhs.append(AddressSpan(1, AddressType.RelatedPos))
        lhs.append(AddressSpan(1, AddressType.DetailDesc))
        self.addProduct(rhs, lhs)
        # 海淀区学院南路68号吉安大厦C座汇智楼111室
        # 2010.5.26
        lhs = []
        rhs = []
        rhs.append(AddressType.Street)
        rhs.append(AddressType.No)
        rhs.append(AddressType.Town)
        rhs.append(AddressType.SuffixLandMark)
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(2, AddressType.LandMark))
        self.addProduct(rhs, lhs)
        # 中国 江苏 江阴市 永康五金城大街49-51号
        # 2010.5.26
        lhs = []
        rhs = []
        rhs.append(AddressType.Province)
        rhs.append(AddressType.County)
        rhs.append(AddressType.SuffixCity)
        rhs.append(AddressType.Street)
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(2, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.Street))
        self.addProduct(rhs, lhs)
        # 巩义市站街镇粮管所内
        lhs = []
        rhs = []
        rhs.append(AddressType.County)
        rhs.append(AddressType.Town)
        rhs.append(AddressType.SuffixTown)
        rhs.append(AddressType.LandMark)
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(2, AddressType.Town))
        lhs.append(AddressSpan(1, AddressType.LandMark))
        self.addProduct(rhs, lhs)
        # 河南省郑州市管城区南五里堡村西堡103号
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.No)
        rhs.append(AddressType.SuffixLandMark)
        rhs.append(AddressType.Village)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.RelatedPos))
        lhs.append(AddressSpan(3, AddressType.Village))
        self.addProduct(rhs, lhs)
        # 鼓楼东街
        lhs = []
        rhs = []
        rhs.append(AddressType.District)
        rhs.append(AddressType.SuffixStreet)

        lhs.append(AddressSpan(1, AddressType.Street))
        self.addProduct(rhs, lhs)
        # 从化市
        lhs = []
        rhs = []
        rhs.append(AddressType.County)
        rhs.append(AddressType.SuffixCity)
        rhs.append(AddressType.Street)

        lhs.append(AddressSpan(2, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.Street))
        self.addProduct(rhs, lhs)
        # 北京西站
        lhs = []
        rhs = []
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.SuffixIndicationFacility)

        lhs.append(AddressSpan(2, AddressType.SuffixIndicationFacility))
        self.addProduct(rhs, lhs)

        # 西站
        lhs = []
        rhs = []
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.SuffixIndicationFacility)

        lhs.append(AddressSpan(2, AddressType.SuffixIndicationFacility))
        self.addProduct(rhs, lhs)

        # 北门
        lhs = []
        rhs = []
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.SuffixBuildingUnit)

        lhs.append(AddressSpan(2, AddressType.SuffixBuildingUnit))
        self.addProduct(rhs, lhs)

        # 科技大学北门
        lhs = []
        rhs = []
        rhs.append(AddressType.LandMark)
        rhs.append(AddressType.SuffixBuildingUnit)

        lhs.append(AddressSpan(2, AddressType.BuildingUnit))
        self.addProduct(rhs, lhs)
        # 一里
        lhs = []
        rhs = []
        rhs.append(AddressType.No)
        rhs.append(AddressType.SuffixLandMark)

        lhs.append(AddressSpan(2, AddressType.SuffixLandMark))
        self.addProduct(rhs, lhs)
        # 西桥
        lhs = []
        rhs = []
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.SuffixLandMark)

        lhs.append(AddressSpan(2, AddressType.SuffixLandMark))
        self.addProduct(rhs, lhs)

        # 天华园 一里
        lhs = []
        rhs = []
        rhs.append(AddressType.District)
        rhs.append(AddressType.SuffixLandMark)

        lhs.append(AddressSpan(2, AddressType.LandMark))
        self.addProduct(rhs, lhs)
        # 东方太阳城社区
        lhs = []
        rhs = []
        rhs.append(AddressType.LandMark)
        rhs.append(AddressType.SuffixDistrict)

        lhs.append(AddressSpan(2, AddressType.District))
        self.addProduct(rhs, lhs)
        # 北京市东城区南河沿大街华龙街二段c座一层
        lhs = []
        rhs = []
        rhs.append(AddressType.County)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.Street)

        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(3, AddressType.Street))
        self.addProduct(rhs, lhs)

        # 11-A
        lhs = []
        rhs = []
        rhs.append(AddressType.Street)
        rhs.append(AddressType.No)
        rhs.append(AddressType.Symbol)

        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(2, AddressType.No))
        self.addProduct(rhs, lhs)

        # 四川省大邑县甲子路５４号
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.County)
        rhs.append(AddressType.No)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.No)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(2, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 云南省昆明市红河谷商铺Ｂ－４
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.City)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.SuffixBuildingUnit)
        rhs.append(AddressType.Symbol)
        rhs.append(AddressType.No)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(3, AddressType.LandMark))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 云南省昆明市滇池路路口省人大对面
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.SuffixCity)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.SuffixStreet)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.LandMark)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(2, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(2, AddressType.RelatedPos))
        lhs.append(AddressSpan(1, AddressType.LandMark))
        lhs.append(AddressSpan(1, AddressType.RelatedPos))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 广东省广州市荔湾区西塱麦村北约５２
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.Village)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.No)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(2, AddressType.Village))
        lhs.append(AddressSpan(1, AddressType.RelatedPos))
        lhs.append(AddressSpan(1, AddressType.Unknow))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 广东省广州市白云区黄边二横路７０
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.No)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.No)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(3, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 广东省广州市越秀区下塘宝汉直街８
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.No)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(2, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 广东省广州市天河区员村路２２６
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Village)
        rhs.append(AddressType.SuffixStreet)
        rhs.append(AddressType.No)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(2, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 四川省成都市九里堤南支路２１
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.No)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(4, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 四川省新津县五津男装３１号
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.County)
        rhs.append(AddressType.No)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.No)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(2, AddressType.LandMark))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 广东省广州市天河区东圃镇大观路中海康城
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Town)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.LandMark)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.Town))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(2, AddressType.LandMark))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 四川省成都市茶店子横街１２
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.LandMark)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.No)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(2, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 云南省昆明市一二一大街１３４号云南民族学院图书馆
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.SuffixStreet)
        rhs.append(AddressType.No)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.LandMark)
        rhs.append(AddressType.SuffixIndicationFacility)
        rhs.append(AddressType.LandMark)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(4, AddressType.LandMark))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 云南省昆明市广福路五甲河公共汽车站鲁班家装旁
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.No)
        rhs.append(AddressType.SuffixIndicationFacility)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.LandMark)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(4, AddressType.LandMark))
        lhs.append(AddressSpan(1, AddressType.Unknow))
        lhs.append(AddressSpan(1, AddressType.RelatedPos))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 武汉市洪山区鲁磨路地质大学旁新成都火锅对面
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.LandMark)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.City)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.LandMark))
        lhs.append(AddressSpan(1, AddressType.RelatedPos))
        lhs.append(AddressSpan(3, AddressType.Unknow))
        lhs.append(AddressSpan(1, AddressType.RelatedPos))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 上海长宁区长宁路１２７７弄中山公寓１５栋２０２室
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Municipality)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.Town)
        rhs.append(AddressType.SuffixLandMark)
        rhs.append(AddressType.BuildingNo)
        rhs.append(AddressType.BuildingUnit)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Municipality))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(2, AddressType.LandMark))
        lhs.append(AddressSpan(1, AddressType.BuildingNo))
        lhs.append(AddressSpan(1, AddressType.BuildingUnit))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 成都市一环路西二段21号成都体院旁
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.City)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.No)
        rhs.append(AddressType.City)
        rhs.append(AddressType.SuffixLandMark)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(2, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(2, AddressType.LandMark))
        lhs.append(AddressSpan(1, AddressType.RelatedPos))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 江北区建新北路65号海关外贸大厦旁
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.No)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.LandMark)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(3, AddressType.LandMark))
        lhs.append(AddressSpan(1, AddressType.RelatedPos))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 思明区莲花北路25号(二村市场旁)
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.No)
        rhs.append(AddressType.StartSuffix)
        rhs.append(AddressType.Village)
        rhs.append(AddressType.SuffixLandMark)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(1, AddressType.StartSuffix))
        lhs.append(AddressSpan(2, AddressType.LandMark))
        lhs.append(AddressSpan(1, AddressType.RelatedPos))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 拱墅区潮王路45号东方豪园文豪阁2604
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.No)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.LandMark)
        rhs.append(AddressType.No)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(2, AddressType.LandMark))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 高新区高新技术产业开发区前进大街2699号吉林大学前卫南区北门商贸楼2楼
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.District)
        rhs.append(AddressType.District)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.No)
        rhs.append(AddressType.LandMark)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.SuffixCounty)
        rhs.append(AddressType.SuffixBuildingUnit)
        rhs.append(AddressType.SuffixLandMark)
        rhs.append(AddressType.BuildingUnit)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.District))
        lhs.append(AddressSpan(1, AddressType.District))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(1, AddressType.LandMark))
        lhs.append(AddressSpan(4, AddressType.LandMark))
        lhs.append(AddressSpan(1, AddressType.SuffixBuildingUnit))
        lhs.append(AddressSpan(1, AddressType.SuffixLandMark))
        lhs.append(AddressSpan(1, AddressType.BuildingUnit))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 文三路398号东信大厦裙房2层
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.No)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.LandMark)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.BuildingUnit)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(2, AddressType.LandMark))
        lhs.append(AddressSpan(2, AddressType.BuildingUnit))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 海曙区公园路118弄2号鼓楼步行街
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.No)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(2, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 海曙区公园路118弄2号鼓楼步行街
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.No)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.No)
        rhs.append(AddressType.LandMark)
        rhs.append(AddressType.BuildingUnit)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(3, AddressType.LandMark))
        lhs.append(AddressSpan(1, AddressType.BuildingUnit))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 市南区广西路11号(工商银行对面)
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.SuffixCity)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.SuffixCounty)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.No)
        rhs.append(AddressType.StartSuffix)
        rhs.append(AddressType.LandMark)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(3, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(1, AddressType.StartSuffix))
        lhs.append(AddressSpan(1, AddressType.LandMark))
        lhs.append(AddressSpan(1, AddressType.RelatedPos))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 市南区广西路11号(工商银行对面)
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.LandMark)
        rhs.append(AddressType.BuildingUnit)
        rhs.append(AddressType.StartSuffix)
        rhs.append(AddressType.LandMark)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.LandMark))
        lhs.append(AddressSpan(1, AddressType.BuildingUnit))
        lhs.append(AddressSpan(1, AddressType.StartSuffix))
        lhs.append(AddressSpan(2, AddressType.LandMark))
        lhs.append(AddressSpan(1, AddressType.RelatedPos))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 广东省广州市从化市广场路１０２号
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.SuffixLandMark)
        rhs.append(AddressType.SuffixStreet)
        rhs.append(AddressType.No)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(2, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 四川省成都市龙潭寺东路
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.SuffixStreet)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(4, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 广东省广州市番禺区市良路
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.SuffixCounty)
        rhs.append(AddressType.SuffixCity)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.SuffixStreet)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(2, AddressType.County))
        lhs.append(AddressSpan(3, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 云南省寻甸回族彝族自治县
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.County)
        rhs.append(AddressType.County)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(2, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 上海市普陀区陕西北路１５５８号千路公寓Ｃ座２１０２室
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Municipality)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.No)
        rhs.append(AddressType.No)
        rhs.append(AddressType.SuffixStreet)
        rhs.append(AddressType.SuffixLandMark)
        rhs.append(AddressType.Symbol)
        rhs.append(AddressType.SuffixBuildingNo)
        rhs.append(AddressType.No)
        rhs.append(AddressType.SuffixBuildingUnit)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Municipality))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(3, AddressType.LandMark))
        lhs.append(AddressSpan(2, AddressType.SuffixBuildingNo))
        lhs.append(AddressSpan(2, AddressType.SuffixBuildingUnit))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 宛平南路99弄新汇公寓2号2201室
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.No)
        rhs.append(AddressType.SuffixStreet)
        rhs.append(AddressType.LandMark)
        rhs.append(AddressType.No)
        rhs.append(AddressType.No)
        rhs.append(AddressType.SuffixBuildingUnit)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(2, AddressType.No))
        lhs.append(AddressSpan(1, AddressType.LandMark))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(2, AddressType.SuffixBuildingUnit))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 朝阳区光华路甲8号和乔丽致酒店1楼
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.No)
        rhs.append(AddressType.Conj)
        rhs.append(AddressType.LandMark)
        rhs.append(AddressType.BuildingUnit)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(2, AddressType.LandMark))
        lhs.append(AddressSpan(1, AddressType.BuildingUnit))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 东莞市寮步镇横坑三星工业区(博士科技大楼后)
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.City)
        rhs.append(AddressType.Town)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.No)
        rhs.append(AddressType.District)
        rhs.append(AddressType.StartSuffix)
        rhs.append(AddressType.LandMark)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.Town))
        lhs.append(AddressSpan(3, AddressType.District))
        lhs.append(AddressSpan(1, AddressType.StartSuffix))
        lhs.append(AddressSpan(1, AddressType.LandMark))
        lhs.append(AddressSpan(1, AddressType.RelatedPos))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 广东省东莞市莞城金牛路121号东日电脑市场一期401室
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.LandMark)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.No)
        rhs.append(AddressType.LandMark)
        rhs.append(AddressType.BuildingUnit)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(2, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(1, AddressType.LandMark))
        lhs.append(AddressSpan(1, AddressType.BuildingUnit))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 郑州市航海东路2号富田太阳城25号702
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.City)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.No)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.LandMark)
        rhs.append(AddressType.No)
        rhs.append(AddressType.No)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(2, AddressType.LandMark))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 江苏省南京市玄武区南拘中山东路301号
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.District)
        rhs.append(AddressType.Town)
        rhs.append(AddressType.SuffixStreet)
        rhs.append(AddressType.No)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(3, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 东莞市常平镇塘角埔区环城路
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.City)
        rhs.append(AddressType.Town)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.SuffixCounty)
        rhs.append(AddressType.SuffixStreet)
        rhs.append(AddressType.SuffixLandMark)
        rhs.append(AddressType.SuffixStreet)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.Town))
        lhs.append(AddressSpan(2, AddressType.County))
        lhs.append(AddressSpan(3, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 哈尔滨市进乡街附近
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.City)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.No)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(2, AddressType.RelatedPos))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 东莞市厚街镇新厚沙路新塘村路口直入出100米
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.City)
        rhs.append(AddressType.Town)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.Village)
        rhs.append(AddressType.SuffixStreet)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.IndicationPosition)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.Town))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.Village))
        lhs.append(AddressSpan(2, AddressType.RelatedPos))
        lhs.append(AddressSpan(1, AddressType.Unknow))
        lhs.append(AddressSpan(1, AddressType.IndicationPosition))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 哈尔滨市进乡街附近
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.SuffixLandMark)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.SuffixDistrict)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(3, AddressType.District))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 河南省郑州市金水区文化路北环路交叉口北50米路东北辰公寓a2508
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Province)
        rhs.append(AddressType.City)
        rhs.append(AddressType.County)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.Crossing)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.IndicationPosition)
        rhs.append(AddressType.SuffixStreet)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.RelatedPos)
        rhs.append(AddressType.LandMark)
        rhs.append(AddressType.Symbol)
        rhs.append(AddressType.No)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Province))
        lhs.append(AddressSpan(1, AddressType.City))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.Crossing))
        lhs.append(AddressSpan(1, AddressType.RelatedPos))
        lhs.append(AddressSpan(1, AddressType.IndicationPosition))
        lhs.append(AddressSpan(2, AddressType.RelatedPos))
        lhs.append(AddressSpan(2, AddressType.LandMark))
        lhs.append(AddressSpan(1, AddressType.Symbol))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

        # 重庆市九龙坡区石坪桥横街特5号1楼44号
        lhs = []
        rhs = []
        rhs.append(AddressType.Start)
        rhs.append(AddressType.Municipality)
        rhs.append(AddressType.County)
        rhs.append(AddressType.District)
        rhs.append(AddressType.Street)
        rhs.append(AddressType.Unknow)
        rhs.append(AddressType.No)
        rhs.append(AddressType.BuildingUnit)
        rhs.append(AddressType.No)
        rhs.append(AddressType.End)

        lhs.append(AddressSpan(1, AddressType.Start))
        lhs.append(AddressSpan(1, AddressType.Municipality))
        lhs.append(AddressSpan(1, AddressType.County))
        lhs.append(AddressSpan(2, AddressType.Street))
        lhs.append(AddressSpan(1, AddressType.Unknow))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(1, AddressType.BuildingUnit))
        lhs.append(AddressSpan(1, AddressType.No))
        lhs.append(AddressSpan(1, AddressType.End))
        self.addProduct(rhs, lhs)

    def addProduct(self, key, lhs):
        if self.root is None:
            self.root = UnknowGrammar.TSTNode(key[0])
        node = None
        if len(key) > 0:
            currentNode = self.root
            charIndex = 0
            while True:
                if currentNode is None:
                    break
                charComp = key[charIndex] - currentNode.splitchar
                if charComp == 0:
                    charIndex += 1
                    if charIndex == len(key):
                        node = currentNode
                        break
                    currentNode = currentNode.eqKID
                elif charComp < 0:
                    currentNode = currentNode.loKID
                else:
                    currentNode = currentNode.hiKID

            occur2 = None
            if node is not None:
                occur2 = node.data
            if occur2 is not None:
                return
            currentNode = self.getOrCreateNode(key)
            currentNode.data = lhs

    def getOrCreateNode(self, key):
        if self.root is None:
            self.root = UnknowGrammar.TSTNode(key[0])

        currentNode = self.root
        charIndex = 0
        while True:
            charComp = key[charIndex] - currentNode.splitchar
            if charComp == 0:
                charIndex += 1
                if charIndex == len(key):
                    return currentNode
                if currentNode.eqKID is None:
                    currentNode.eqKID = UnknowGrammar.TSTNode(key[charIndex])
                currentNode = currentNode.eqKID
            elif charComp < 0:
                if currentNode.loKID is None:
                    currentNode.loKID = UnknowGrammar.TSTNode(key[charIndex])
                currentNode = currentNode.loKID
            else:
                if currentNode.hiKID is None:
                    currentNode.hiKID = UnknowGrammar.TSTNode(key[charIndex])
                currentNode = currentNode.hiKID

    def replace(self, key, offset, spans):
        j = 0
        i = offset
        while i < len(key):
            span = spans[j]

            token = key[i]

            newText = ''
            newStart = token.start
            newEnd = token.end
            newType = span.type

            for k in range(span.length):
                token = key[i + k]
                newText += token.termText
                newEnd = token.end
            
            newToken = AddressToken(start=newStart, end=newEnd, word=newText, type=newType)
            
            for k in range(span.length):
                del key[i]

            key.insert(i, newToken)
            j += 1
            if j >= len(spans):
                return
            i += 1

    def matchLong(self, key, offset, matchRet):
        if not key or not self.root or offset >= len(key):
            matchRet.end = offset
            matchRet.lhs = None
            return matchRet

        ret = offset
        retPOS = None

        currentNode = self.root
        charIndex = offset
        while True:
            if currentNode is None:
                matchRet.end = ret
                matchRet.lhs = retPOS
                return matchRet
            charComp = key[charIndex].type - currentNode.splitchar
            if charComp == 0:
                charIndex += 1
                if currentNode.data is not None and charIndex > ret:
                    ret = charIndex
                    retPOS = currentNode.data
                if charIndex == len(key):
                    matchRet.end = ret
                    matchRet.lhs = retPOS
                    return matchRet
                currentNode = currentNode.eqKID
            elif charComp < 0:
                currentNode = currentNode.loKID
            else:
                currentNode = currentNode.hiKID


if __name__ == '__main__':
    grammar = UnknowGrammar()
    input = []
    input.append(AddressToken(type=AddressType.Unknow, start=0, end=0, cost=0, word=u'中', code=0))
    input.append(AddressToken(type=AddressType.SuffixTown, start=0, end=0, cost=0, word=u'中', code=0))
    input.append(AddressToken(type=AddressType.Unknow, start=0, end=0, cost=0, word=u'中', code=0))
    input.append(AddressToken(type=AddressType.No, start=0, end=0, cost=0, word=u'中', code=0))
    input.append(AddressToken(type=AddressType.SuffixStreet, start=0, end=0, cost=0, word=u'中', code=0))

    #for offset in range(len(input)):
    offset = 0
    while offset < len(input):
        matchRet = UnknowGrammar.MatchRet(0, None)
        matchRet = grammar.matchLong(input, offset, matchRet)
        if matchRet.lhs is not None:
            grammar.replace(input, offset, matchRet.lhs)
            print 'replace'
        offset += 1

    for token in input:
        print token



