# -*- coding: utf-8 -*-

"""
load address name dic

"""

import os
import codecs

from entities import Singleton
from entities import AddDicTypes
from entities import AddressType

class DicAddress(Singleton):

    class TSTNode(object):
    
        def __init__(self, key):
            self.loKID = None
            self.eqKID = None
            self.hiKID = None
    
            self.data = None
            self.splitchar = key
    
        def __str__(self):
            return 'splitchar:' + self.splitchar


    class MatchRet(object):
        
        def __init__(self, end, posInf):
            self.end = end
            self.posInf = posInf  #AddDicTypes
    
        def __str__(self):
            return 'endPosition:' + str(self.end) + ' posInf:' + str(self.posInf)

    def __init__(self, dicDir='dic/'):
        self.dicDir = dicDir
        self.root = None
        self.numset = set(u"零○一二两三四五六七八九十廿壹贰叁肆伍陆柒捌玖百千万亿拾佰仟百千"
                          u"万亿拾佰仟甲乙丙丁M1234567890附第期")

        self.load('country.txt', AddressType.Country, 10000)
        self.load('province.txt', AddressType.Province, 10000)
        self.load('city.txt', AddressType.City, 10000)
        self.load('county.txt', AddressType.County, 1000)
        self.load('street.txt', AddressType.Street, 10000000)
        self.load('relatedPos.txt', AddressType.RelatedPos, 100)
        self.load('landmark.txt', AddressType.LandMark, 100000)
        self.load('town.txt', AddressType.Town, 1000)
        self.load('district.txt', AddressType.District, 1000000)
        self.load('village.txt', AddressType.Village, 10000)
        self.load('SuffixLandMark.txt', AddressType.SuffixLandMark, 100000)
        self.load('SuffixDistrict.txt', AddressType.SuffixDistrict, 100000)
        self.load('SuffixBuildingUnit.txt', AddressType.SuffixBuildingUnit, 1000)

        self.addWord(u'其他国家或地区', 100000000000, AddressType.Country, 100)	
        self.addWord(u'北京市', 110000000000, AddressType.Municipality, 200000)
        self.addWord(u'北京', 110000000000, AddressType.Municipality, 200000)
        self.addWord(u'上海市', 310000000000, AddressType.Municipality, 200000)
        self.addWord(u'上海', 310000000000, AddressType.Municipality, 200000)
        self.addWord(u'天津市', 120000000000, AddressType.Municipality, 200000)
        self.addWord(u'天津', 120000000000, AddressType.Municipality, 200000)
        self.addWord(u'重庆市', 500000000000, AddressType.Municipality, 200000)
        self.addWord(u'重庆', 500000000000, AddressType.Municipality, 200000)		
        self.addWord(u'郑州市', 410100000000, AddressType.City, 10000000)	
        self.addWord(u'南京市', 320100000000, AddressType.City, 10000000)	
        self.addWord(u'九龙坡', 500107000000, AddressType.County, 10000000)	
        self.addWord(u'九龙坡区', 500107000000, AddressType.County, 10000000)	
        self.addWord(u'中山区', 210202000000, AddressType.County, 10000000)	
        
        self.addWord(u'交叉口', 0, AddressType.Crossing, 100)
        self.addWord(u'交界处', 0, AddressType.Crossing, 100)
        self.addWord(u'十字路口', 0, AddressType.Crossing, 100)
        
        self.addWord(u'近郊', 0, AddressType.Other, 100000)
        
        self.addWord(u'（', 0, AddressType.StartSuffix, 1300000)
        self.addWord(u'(u', 0, AddressType.StartSuffix, 1300000)
        self.addWord(u'大街', 0, AddressType.SuffixStreet, 1300000)
        self.addWord(u'弄', 0, AddressType.SuffixStreet, 1300000)
        self.addWord(u'环', 0, AddressType.SuffixStreet, 1300000)
        self.addWord(u'段', 0, AddressType.SuffixStreet, 1300000)
        self.addWord(u'胡同', 0, AddressType.SuffixStreet, 1300000)
        self.addWord(u'公路', 0, AddressType.SuffixStreet, 1200000)
        self.addWord(u'路', 0, AddressType.SuffixStreet, 1200000)		
        self.addWord(u'大道', 0, AddressType.SuffixStreet, 200)
        self.addWord(u'道', 0, AddressType.SuffixStreet, 200)
        self.addWord(u'街', 0, AddressType.SuffixStreet, 200)
        self.addWord(u'巷', 0, AddressType.SuffixStreet, 200)
        self.addWord(u'国道', 0, AddressType.SuffixStreet, 200)
        self.addWord(u'路口', 0, AddressType.SuffixStreet, 200)
        self.addWord(u'条', 0, AddressType.SuffixStreet, 200)
        
        self.addWord(u'省', 0, AddressType.SuffixProvince, 10)
        self.addWord(u'自治区', 0, AddressType.SuffixProvince, 10)
        self.addWord(u'特别行政区', 0, AddressType.SuffixMunicipality, 10)
        self.addWord(u'市', 0, AddressType.SuffixCity, 10)
        self.addWord(u'依族苗族自治州', 0, AddressType.SuffixCity, 10)
        self.addWord(u'自治州', 0, AddressType.SuffixCity, 100)
        self.addWord(u'藏族自治州', 0, AddressType.SuffixCity, 100)
        self.addWord(u'土家族苗族自治州', 0, AddressType.SuffixCity, 100)
        self.addWord(u'朝鲜族自治州', 0, AddressType.SuffixCity, 100)
        self.addWord(u'盟', 0, AddressType.SuffixCity, 100)
        
        self.addWord(u'回族区', 0, AddressType.SuffixCounty, 100)
        self.addWord(u'区', 0, AddressType.SuffixCounty, 100)
        self.addWord(u'县', 0, AddressType.SuffixCounty, 100)
        self.addWord(u'自治旗', 0, AddressType.SuffixCounty, 100)
        self.addWord(u'自治县', 0, AddressType.SuffixCounty, 100)
        self.addWord(u'回族自治县', 0, AddressType.SuffixCounty, 100)
        self.addWord(u'土家族自治县', 0, AddressType.SuffixCounty, 100)
        
        self.addWord(u'镇', 0, AddressType.SuffixTown, 10000)
        self.addWord(u'乡', 0, AddressType.SuffixTown, 10000)
        
        self.addWord(u'庄', 0, AddressType.SuffixVillage, 100)
        self.addWord(u'新村', 0, AddressType.SuffixVillage, 1000000000)	
        self.addWord(u'村', 0, AddressType.SuffixVillage, 1000)
        
        self.addWord(u'栋', 0, AddressType.SuffixBuildingNo, 200)
        self.addWord(u'亭', 0, AddressType.SuffixBuildingNo, 200)
        self.addWord(u'组', 0, AddressType.SuffixBuildingNo, 200)
        self.addWord(u'档', 0, AddressType.SuffixBuildingNo, 200)
        self.addWord(u'卡', 0, AddressType.SuffixBuildingNo, 200)
        
        self.addWord(u'号', 0, AddressType.SuffixBuildingNo, 200)
        self.addWord(u'号楼', 0, AddressType.SuffixBuildingNo, 200)
        self.addWord(u'幢', 0, AddressType.SuffixBuildingNo, 200)		
        self.addWord(u'排', 0, AddressType.SuffixBuildingNo, 200)
        self.addWord(u'栋', 0, AddressType.SuffixBuildingNo, 200)
        self.addWord(u'座', 0, AddressType.SuffixBuildingNo, 1000)
        self.addWord(u'号', 0, AddressType.SuffixBuildingNo, 200)
        self.addWord(u'房', 0, AddressType.SuffixBuildingNo, 200)
        self.addWord(u'期', 0, AddressType.SuffixBuildingNo, 200)
        self.addWord(u'临时', 0, AddressType.SuffixBuildingNo, 200)		
        
        self.addWord(u'院', 0, AddressType.SuffixIndicationFacility, 200)
        self.addWord(u'大院', 0, AddressType.SuffixIndicationFacility, 200)
        self.addWord(u'路口', 0, AddressType.SuffixIndicationFacility, 100)
        self.addWord(u'站', 0, AddressType.SuffixIndicationFacility, 100)
        self.addWord(u'库', 0, AddressType.SuffixIndicationFacility, 100)
        self.addWord(u'地铁', 0, AddressType.SuffixIndicationFacility, 100)
        self.addWord(u'大桥', 0, AddressType.SuffixIndicationFacility, 100)
        self.addWord(u'桥', 0, AddressType.SuffixIndicationFacility, 100)
        self.addWord(u'河', 0, AddressType.SuffixIndicationFacility, 100)
        self.addWord(u'公里', 0, AddressType.SuffixIndicationPosition, 100)
        self.addWord(u'米', 0, AddressType.SuffixIndicationPosition, 100)
        self.addWord(u'市辖区', 0, AddressType.Other, 900000000)	
        self.addWord(u'和', 0, AddressType.Conj, 10)
        self.addWord(u'附近', 0, AddressType.RelatedPos, 100)

    def load(self, dic, address_type, freq):
        fname = os.path.join(self.dicDir, dic)
        with codecs.open(fname, encoding='gbk', errors='ignore') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                line = line.strip()
                if not line:
                    continue
                arr = line.split(':')

                key = arr[0]
                code = int(arr[1]) if len(arr) >= 2 else 0
                self.addWord(key, code, address_type, freq)

    def addWord(self, key, code, address_type, freq):
        if self.root is None:
            self.root = DicAddress.TSTNode(key[0])

        pi = AddDicTypes.AddTypeInf(address_type, freq, code)
        node = None
        currentNode = self.root
        charIndex = 0
        while True:
            if currentNode is None:
                break
            charComp = ord(key[charIndex]) - ord(currentNode.splitchar)
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
            occur2.insert(pi)
            return

        currentNode = self.getOrCreateNode(key)

        occur3 = currentNode.data
        if occur3 is not None:
            occur3.insert(pi)
        else:
            occur = AddDicTypes()
            occur.put(pi)
            currentNode.data = occur

    def getOrCreateNode(self, key):
        
        if self.root is None:
            self.root = DicAddress.TSTNode(key[0])

        currentNode = self.root
        charIndex = 0
        while True:
            charComp = ord(key[charIndex]) - ord(currentNode.splitchar)
            if charComp == 0:
                charIndex += 1
                if charIndex == len(key):
                    return currentNode
                if currentNode.eqKID is None:
                    currentNode.eqKID = DicAddress.TSTNode(key[charIndex])
                currentNode = currentNode.eqKID
            elif charComp < 0:
                if currentNode.loKID is None:
                    currentNode.loKID = DicAddress.TSTNode(key[charIndex])
                currentNode = currentNode.loKID
            else:
                if currentNode.hiKID is None:
                    currentNode.hiKID = DicAddress.TSTNode(key[charIndex])
                currentNode = currentNode.hiKID

    def matchNum(self, start, sen):
        i = start
        count = len(sen)
        while i < count:
            c = sen[i]
            #if (c >= u'0' and c <= u'9') or (c >= u'０' and c <= u'９') or c == u'-' or c == u'－':
            if c.isdigit() or c == u'-' or c == u'－':
                i += 1
            else:
                break
    
        if start < i < count:
            end = sen[i]
            if end in [u'号', u'#', u'＃']:
                i += 1
    
        return i

    def matchEnglish(self, start, key):
        i = start
        count = len(key)
        std = u'ＱＷＥＲＴＹＵＩＯＰＡＳＤＦＧＨＪＫＬＺＸＣＶＢＮＭ号'
        while i < count:
            c = key[i]
            if 'a' <= c <= 'z' or 'A' <= c <= 'Z' or c in std:
                i += 1
            else:
                break
        return i

    def matchChineseNum(self, start, sen):
        i = start
        count = len(sen)
        while i < count:
            c = sen[i]
            if c in self.numset:
                i += 1
            else:
                break
        if start < i < count:
            if sen[i] == u'号':
                i += 1
        return i

    def matchAll(self, key, offset):
        matchRets = []
        if not key or not self.root or offset >= len(key):
            return matchRets

        ret = offset
        retPOS = None
        retWeight = 0

        ret = self.matchNum(offset, key)
        if ret > offset:
            retPOS = AddressType.No
            retWeight = 100
            
            posInf = AddDicTypes.AddTypeInf(retPOS, retWeight, 0)
            addressData = AddDicTypes()
            addressData.put(posInf)
            matchRet = DicAddress.MatchRet(ret, addressData)
            matchRets.append(matchRet)

        retChineseNum = self.matchChineseNum(offset, key)
        if retChineseNum > ret:
            ret = retChineseNum
            retPOS = AddressType.No
            retWeight = 100
            posInf = AddDicTypes.AddTypeInf(retPOS, retWeight, 0)
            addressData = AddDicTypes()
            addressData.put(posInf)
            matchRet = DicAddress.MatchRet(ret, addressData)
            matchRets.append(matchRet)

        retEnglishNum = self.matchEnglish(offset, key)
        if retEnglishNum > ret:
            ret = retEnglishNum
            retPOS = AddressType.Symbol
            retWeight = 100
            posInf = AddDicTypes.AddTypeInf(retPOS, retWeight, 0)
            addressData = AddDicTypes()
            addressData.put(posInf)
            matchRet = DicAddress.MatchRet(ret, addressData)
            matchRets.append(matchRet)

        currentNode = self.root
        charIndex = offset

        while True:
            if currentNode is None:
                return matchRets
            charComp = ord(key[charIndex]) - ord(currentNode.splitchar)

            if charComp == 0:
                charIndex += 1
                if currentNode.data is not None:
                    ret = charIndex
                    matchRet = DicAddress.MatchRet(ret, currentNode.data)
                    matchRets.append(matchRet)

                if charIndex == len(key):
                    return matchRets
                currentNode = currentNode.eqKID
            elif charComp < 0:
                currentNode = currentNode.loKID
            else:
                currentNode = currentNode.hiKID


if __name__ == '__main__':
    dic = DicAddress()

    word = u'朝阳北京'
    offset = 0

    matchRets = dic.matchAll(word, offset)
    for m in matchRets:
        print word, ' matchRet:', m
