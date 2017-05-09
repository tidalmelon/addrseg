# -*- coding: utf-8 -*-

from addresstagger import AddressTagger
from dicaddress import DicAddress 
from stataddress import ContextStatAddress
from unknowgrammar import UnknowGrammar
from addrutil.util import AddrCompletion
from addrutil.dicregion import RType

#from spider.save.hbase.webpage import WebPage

dictAddress = DicAddress()
contextStatAddress = ContextStatAddress()
grammar = UnknowGrammar()
tagger = AddressTagger(dictAddress, contextStatAddress, grammar)
acom = AddrCompletion(sourcedir='./addrutil/source_data/', dicdir='./addrutil/data/')

#db = WebPage()
#
#for url, address in db.getAllAddress('com.tianyancha', 100):
#    print address
#    tokens = tagger.tag(address)
#    for token in tokens:
#        print token
#    print '*' * 20


def getrtype(rtype):
    if rtype in [1, 3]:
        return RType.PROVINCE
    if rtype in [4]:
        return RType.CITY
    if rtype == 5:
        return RType.COUNTY
    if rtype == 6:
        return RType.TOWN



#import MySQLdb
#
#con = MySQLdb.connect(host='115.28.184.100', port=5001, user='root', passwd='mysql', db='spider')
#con.set_character_set('utf8')
#
#cursor = con.cursor()
#cursor.execute('SET NAMES utf8;')
#cursor.execute('SET CHARACTER SET utf8;')
#cursor.execute('SET character_set_connection=utf8;')
#
#
#def update_addr_new(pid, state, city, address,cursor, con):
#    doc = u'"country":"中国","state":"%s","city":"%s","detail":"%s"'
#    doc = doc  % (state, city, address)
#    doc = doc.encode('utf-8')
#    #print doc
#
#    doc = MySQLdb.escape_string(doc)
#
#    #sql = 'update product_20160805 set addr_new = \'%s\' where pid = %s' % (doc, pid)
#    sql = 'update product set addr_new = \'%s\' where pid = %s' % (doc, pid)
#    print sql
#    cursor.execute(sql)
#    con.commit()
#
#
#sql = 'select pid, address from product_20160805 where address is not null limit 485030, 10'
#sql = 'select pid, address from product_20160805 where address is not null'
#sql = 'select pid, address from product where address is not null'
#
#cursor.execute(sql)
#
#records = cursor.fetchall()
#
#
#
#for pid, address in records:
#    address = address.strip()
#    address = address.decode('utf-8', 'ignore')
#    print '------------------------'
#    print pid, address
#    tokens = tagger.tag(address)
#    if not tokens:
#        continue
#
#    for token in tokens:
#        print token
#    
#    if len(tokens) <= 2:
#        continue
#    token = tokens[1]
#    rtype_1 = token.type
#    rtype = getrtype(rtype_1)
#
#    t = acom.getFullAddr(token.termText, rtype)
#    if not t:
#        state = '' 
#        city = ''
#        update_addr_new(pid, state, city, address, cursor, con)
#        continue
#
#    line = u''
#    if rtype_1 == 1:
#        state = token.termText 
#        city = token.termText
#        update_addr_new(pid, state, city, address, cursor, con)
#
#    if rtype_1 == 3:
#        state = token.termText
#        if len(tokens) > 2 and tokens[2].type == 4:
#            city = tokens[2].termText
#        else:
#            city = ''
#        update_addr_new(pid, state, city, address, cursor, con)
#
#
#    if len(t) >= 2:
#        state = t[0][2]
#        city = t[1][2]
#        update_addr_new(pid, state, city, address, cursor, con)
#
#
#
#
#
#cursor.close()
#con.close()

address = u'湘阴县金龙镇天井村'
#address = u'太原市万柏林区小王村红旗北街220号302室'
address = u'萧山区市心中路398号金茂大厦1幢1603室'
#address = u'济南历下区留创园'
address = u'工人体育场东路丙2号中国红街3号楼2层'
address = u'朝阳门外大街甲6号万通中心AB座2F3005'
address = u'后沙峪中粮祥云小镇安泰大街9号院19号楼104建设银行左边'
address = u'珠海香洲区翠前南路1号'

tokens = tagger.tag(address)
for token in tokens:
    print token
token = tokens[1]
rtype = token.type
print rtype
rtype = getrtype(rtype)


print '*' * 20
print token.termText
t = acom.getFullAddr(token.termText, rtype)
line = u''
for tup in t:
    std = '[%s:%s:%s]' % tup
    line += std
print line.encode('utf-8')

