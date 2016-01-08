'''
Created on 2016. 1. 8.

@author: Jay
'''
from engine.data.AbstractData import AbstractData
from engine.strategy.Asset import Equity, Cash
from stockInfo.models import ZzImsiSisae
from util.TypeDef import TypeDef
from util.time.Date import Date


startDate = Date.valueOf("20150509")
endDate = Date.valueOf("20150520")
equity1 = Equity("samsung", "KS005930", TypeDef.EquityType.STOCK)
equity2 = Equity("shilla", "KS008770", TypeDef.EquityType.STOCK)
cash = Cash("cash", "cashCode")
assets = {"KS005930" : equity1, "KS008770" : equity2, "cash" : cash}

data = AbstractData()
dataResults = data.getData(startDate, endDate, assets)

for x in dataResults :
    print x.code, x.currentprice, x.date

# stocks = ZzImsiSisae.objects.filter(date__gte = '20150509').filter(code__in = ['KS005930', 'KS008770'])
# 
# print stocks[len(stocks) - 1].code
# 
# for x in stocks :
#     print x.code, x.currentprice, x.date