# -*- coding: utf-8 -*-

from entities import Singleton
from entities import AddressType


class ContextStatAddress(Singleton):

    def __init__(self):
        size = AddressType.getLen()
        #self.transProbs = [[0] * AddressType.getLen()] * AddressType.getLen()
        self.transProbs = [[0 for j in range(size)] for i in range(size)]
        self.addTrob(AddressType.Start, AddressType.Street, 10000000)
        self.addTrob(AddressType.Start, AddressType.LandMark, 1000000)
        self.addTrob(AddressType.Start, AddressType.District, 100000000)
        self.addTrob(AddressType.Start, AddressType.Village, 1000000)
        self.addTrob(AddressType.Start, AddressType.Town, 100000)
        self.addTrob(AddressType.Start, AddressType.City, 1000000)
        self.addTrob(AddressType.Start, AddressType.County, 1000000)
        self.addTrob(AddressType.Start, AddressType.Country, 1000000)
        self.addTrob(AddressType.Start, AddressType.Province, 1000000)
        self.addTrob(AddressType.Start, AddressType.Municipality, 1000000)

        self.addTrob(AddressType.Province, AddressType.City, 100000000)
        self.addTrob(AddressType.Province, AddressType.County, 1000000)
        self.addTrob(AddressType.Province, AddressType.Town, 10)
        self.addTrob(AddressType.Province, AddressType.End, 10000000)
        self.addTrob(AddressType.Province, AddressType.SuffixMunicipality, -10000000)
        self.addTrob(AddressType.Municipality, AddressType.District, 1000000)
        self.addTrob(AddressType.Municipality, AddressType.County, 10000000)
        self.addTrob(AddressType.Municipality, AddressType.Street, 10000)

        self.addTrob(AddressType.Municipality, AddressType.End, 10000)
        self.addTrob(AddressType.City, AddressType.County, 10000000)
        self.addTrob(AddressType.City, AddressType.Town, 10000000)
        self.addTrob(AddressType.City, AddressType.City, 1000000)
        self.addTrob(AddressType.City, AddressType.Street, 100000000)
        self.addTrob(AddressType.City, AddressType.District, 10000000)
        self.addTrob(AddressType.City, AddressType.LandMark, 1000000)
        self.addTrob(AddressType.City, AddressType.Country, 1000)
        self.addTrob(AddressType.City, AddressType.End, 1000)
        self.addTrob(AddressType.City, AddressType.SuffixCity, -1000000)
        self.addTrob(AddressType.City, AddressType.SuffixLandMark, -100000)
        self.addTrob(AddressType.City, AddressType.SuffixStreet, -100000)
        self.addTrob(AddressType.City, AddressType.SuffixCounty, -100000)
        self.addTrob(AddressType.County, AddressType.Village, 10000)
        self.addTrob(AddressType.County, AddressType.Town, 100000)
        self.addTrob(AddressType.County, AddressType.Province, 100)
        self.addTrob(AddressType.County, AddressType.Street, 100000000)
        self.addTrob(AddressType.County, AddressType.District, 10000000)
        self.addTrob(AddressType.County, AddressType.County, -900000000)
        self.addTrob(AddressType.County, AddressType.Other, -1000)
        self.addTrob(AddressType.County, AddressType.Unknow, -10000000)
        self.addTrob(AddressType.County, AddressType.End, 10000)
        self.addTrob(AddressType.County, AddressType.LandMark, 1000000000)
        self.addTrob(AddressType.County, AddressType.SuffixDistrict, -1000000000)
        self.addTrob(AddressType.County, AddressType.City, -1000000000)
        self.addTrob(AddressType.County, AddressType.SuffixCity, -1000000000)

        self.addTrob(AddressType.RelatedPos, AddressType.County, -1000)
        self.addTrob(AddressType.RelatedPos, AddressType.LandMark, 100000)
        self.addTrob(AddressType.RelatedPos, AddressType.End, 10)
        self.addTrob(AddressType.RelatedPos, AddressType.Municipality, 100)
        self.addTrob(AddressType.Street, AddressType.SuffixLandMark, 100)

        self.addTrob(AddressType.Town, AddressType.Village, 10000000)
        self.addTrob(AddressType.Town, AddressType.LandMark, 10000000)
        self.addTrob(AddressType.Town, AddressType.District, 10000000)
        self.addTrob(AddressType.Town, AddressType.Street, 100000000)
        self.addTrob(AddressType.Town, AddressType.SuffixLandMark, 10000000)
        self.addTrob(AddressType.Town, AddressType.End, 100)
        self.addTrob(AddressType.Town, AddressType.Town, 1)
        self.addTrob(AddressType.Town, AddressType.RelatedPos, 10000000)
        self.addTrob(AddressType.Town, AddressType.Village, 100000000)
        self.addTrob(AddressType.Town, AddressType.SuffixCounty, -100000000)
        self.addTrob(AddressType.StreetNo, AddressType.BuildingUnit, 10)
        self.addTrob(AddressType.StreetNo, AddressType.LandMark, 10000000)
        self.addTrob(AddressType.StreetNo, AddressType.BuildingNo, 100)
        self.addTrob(AddressType.StreetNo, AddressType.City, 10000)
        self.addTrob(AddressType.No, AddressType.District, 10000000)
        self.addTrob(AddressType.No, AddressType.RelatedPos, 10000)
        self.addTrob(AddressType.No, AddressType.LandMark, 10000000)
        self.addTrob(AddressType.No, AddressType.Street, 10000000)
        self.addTrob(AddressType.No, AddressType.City, -10000000)
        self.addTrob(AddressType.No, AddressType.SuffixBuildingUnit, 10000000)

        self.addTrob(AddressType.Street, AddressType.City, -1000000000)
        self.addTrob(AddressType.Street, AddressType.County, -10000000)
        self.addTrob(AddressType.Street, AddressType.Town, -1000000)
        self.addTrob(AddressType.Street, AddressType.Street, 1000000000)
        self.addTrob(AddressType.Street, AddressType.SuffixStreet, 10000)
        self.addTrob(AddressType.Street, AddressType.LandMark, 10000000)
        self.addTrob(AddressType.Street, AddressType.No, 10000)
        self.addTrob(AddressType.Street, AddressType.End, 1000000)
        self.addTrob(AddressType.Street, AddressType.City, -1000000)
        self.addTrob(AddressType.Village, AddressType.District, 1000)
        self.addTrob(AddressType.Village, AddressType.End, 100)
        self.addTrob(AddressType.Village, AddressType.Street, 100)
        self.addTrob(AddressType.Village, AddressType.LandMark, 100)
        self.addTrob(AddressType.LandMark, AddressType.No, 10000)
        self.addTrob(AddressType.LandMark, AddressType.End, 10000)
        self.addTrob(AddressType.LandMark, AddressType.Street, 10000000)
        self.addTrob(AddressType.LandMark, AddressType.StartSuffix, 10000000)
        self.addTrob(AddressType.LandMark, AddressType.RelatedPos, 100000)
        self.addTrob(AddressType.LandMark, AddressType.City, -900000000)
        self.addTrob(AddressType.LandMark, AddressType.County, -900000000)

        self.addTrob(AddressType.BuildingUnit, AddressType.District, 100000)
        self.addTrob(AddressType.BuildingUnit, AddressType.Province, 10)
        self.addTrob(AddressType.BuildingUnit, AddressType.Street, 10)
        self.addTrob(AddressType.District, AddressType.LandMark, 1000000)
        self.addTrob(AddressType.District, AddressType.City, -10000)
        self.addTrob(AddressType.District, AddressType.Village, 1000000)
        self.addTrob(AddressType.District, AddressType.Street, 1000000)
        self.addTrob(AddressType.District, AddressType.County, -1000000)
        self.addTrob(AddressType.District, AddressType.District, 1000000)
        self.addTrob(AddressType.District, AddressType.End, 1000000)
        self.addTrob(AddressType.SuffixBuildingNo, AddressType.County, 10000)
        self.addTrob(AddressType.IndicationFacility, AddressType.IndicationPosition, 10000)
        self.addTrob(AddressType.IndicationFacility, AddressType.RelatedPos, 100000000)
        self.addTrob(AddressType.IndicationPosition, AddressType.LandMark, 100000000)
        self.addTrob(AddressType.Unknow, AddressType.SuffixLandMark, 100000)
        self.addTrob(AddressType.Unknow, AddressType.Street, 100000)
        self.addTrob(AddressType.Unknow, AddressType.SuffixStreet, 100000)
        self.addTrob(AddressType.Unknow, AddressType.City, -1000000000)

        self.addTrob(AddressType.SuffixLandMark, AddressType.No, 100000)
        self.addTrob(AddressType.SuffixLandMark, AddressType.RelatedPos, 100000)
        self.addTrob(AddressType.SuffixLandMark, AddressType.County, -10000)

        self.addTrob(AddressType.County, AddressType.SuffixLandMark, -10000)
        self.addTrob(AddressType.County, AddressType.County, -10000)
        self.addTrob(AddressType.County, AddressType.SuffixCounty, -100000)
        self.addTrob(AddressType.Municipality, AddressType.SuffixCity, -100000)
        self.addTrob(AddressType.Municipality, AddressType.SuffixStreet, -100000)
        self.addTrob(AddressType.Municipality, AddressType.City, -1000000000)
        self.addTrob(AddressType.County, AddressType.SuffixStreet, -100000)
        self.addTrob(AddressType.Unknow, AddressType.Town, -100000)
        self.addTrob(AddressType.Unknow, AddressType.County, -100000)
        self.addTrob(AddressType.Other, AddressType.LandMark, 100000000)

        self.addTrob(AddressType.SuffixCity, AddressType.SuffixLandMark, -100000)
        self.addTrob(AddressType.City, AddressType.SuffixCity, -100000)
        self.addTrob(AddressType.No, AddressType.SuffixLandMark, 100000)

        self.addTrob(AddressType.SuffixDistrict, AddressType.County, -1000)
        self.addTrob(AddressType.Street, AddressType.County, -100000000)
        self.addTrob(AddressType.SuffixCity, AddressType.Street, 1000000000)
        self.addTrob(AddressType.SuffixCounty, AddressType.Town, 1000000)
        self.addTrob(AddressType.SuffixCounty, AddressType.Street, 1000000000)
        self.addTrob(AddressType.SuffixCounty, AddressType.County, -100000000)
        self.addTrob(AddressType.SuffixCounty, AddressType.City, -10000000)
        self.addTrob(AddressType.SuffixStreet, AddressType.City, -100000)
        self.addTrob(AddressType.SuffixCounty, AddressType.Village, 100000000)
        self.addTrob(AddressType.SuffixCounty, AddressType.Street, 10000000)
        self.addTrob(AddressType.SuffixCounty, AddressType.District, 100000000)
        self.addTrob(AddressType.SuffixCounty, AddressType.LandMark, 1000000000)
        self.addTrob(AddressType.SuffixTown, AddressType.Town, -100000000)
        self.addTrob(AddressType.SuffixTown, AddressType.County, -100000000)
        self.addTrob(AddressType.SuffixTown, AddressType.Village, 100000000)
        self.addTrob(AddressType.SuffixTown, AddressType.RelatedPos, -10000000)
        self.addTrob(AddressType.SuffixTown, AddressType.City, -100000)

        self.addTrob(AddressType.LandMark, AddressType.SuffixCounty, -900000000)
        self.addTrob(AddressType.LandMark, AddressType.SuffixCity, -900000000)
        self.addTrob(AddressType.SuffixLandMark, AddressType.County, -100000)
        self.addTrob(AddressType.SuffixLandMark, AddressType.Street, 10000000)
        self.addTrob(AddressType.StartSuffix, AddressType.LandMark, 20000)
        self.addTrob(AddressType.StartSuffix, AddressType.Town, -10000000)

    def addTrob(self, prev, cur, val):
        self.transProbs[prev][cur] = val

    def getContextPossibility(self, prev, cur):
        return self.transProbs[prev][cur]

    def getContextPossibility_1(self, prev, cur):
        if prev.data is None or cur.data is None:
            return 0
        maxProb = -2147483648
        for previnf in prev.data.data:
            for curinf in cur.data.data:
                prob = self.transProbs[previnf.pos][curinf.pos]
                if prob > maxProb:
                    maxProb = prob
        if maxProb == -2147483648:
            maxProb = 0
        return maxProb

    def getTransProbs(self):
        return self.transProbs














