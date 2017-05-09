# -*- coding: utf-8 -*-
#import unittest

from entities import AddDicTypes
import random

#class TestAddDicTypesFunctions(unittest.TestCase):
#
#    def setUp(self):
#        self.sortlist = AddDicTypes()
#        
#        ati = AddDicTypes.AddTypeInf(1, 100, 0)

arr = range(10)
random.shuffle(arr)
print 'affter shuffle:', arr

adts = AddDicTypes()

for pos in arr:
    ati = AddDicTypes.AddTypeInf(pos, pos+1, pos+2)
    adts.insert(ati)

print 'after sortlist:'
for ati in adts.data:
    print ati

print str(adts)

print adts.findType(6)

print adts.findType(40)




