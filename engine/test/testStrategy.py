'''
Created on 2016. 1. 7.

@author: jaylee
'''


from engine.strategy.Asset import Asset, Equity, Cash
from engine.strategy.Engine import AbstractEngine
from engine.strategy.ProcessInfo import ProcessInfo
from engine.strategy.Strategy import AbstractStrategy
from util.TypeDef import TypeDef
from util.time.Date import Date
from util.time.calendar.SouthKoreaCalendar import SouthKoreaCalendar


#Assets
equity1 = Equity("samsung", "KS005930", TypeDef.EquityType.STOCK)
equity2 = Equity("shilla", "KS008770", TypeDef.EquityType.STOCK)
cash = Cash("cash", "cashCode")

assets = {"KS005930" : equity1, "KS008770" : equity2, "cash" : cash}

#assets = [equity1, equity2]#, cash]

#Strategy
strategy = AbstractStrategy()

#ProcessInfo
trainStartDate = Date.valueOf("20150101")
trainEndDate = Date.valueOf("20150430")
testStartDate = Date.valueOf("20150510")
testEndDate = Date.valueOf("20150515")
timeLeg = 5;
calendar = SouthKoreaCalendar.getCalendar(1)
processInfo = ProcessInfo(trainStartDate, trainEndDate,
                          testStartDate, testEndDate,
                          timeLeg, calendar, None)

#ENGINE
engine = AbstractEngine(assets, strategy, processInfo)
portfolios = engine.generate()
for pfokey in portfolios.keys() :
    print portfolios[pfokey]    
    
#     numOfAssets = portfolio.getNumOfAssets()
#     print portfolio.getDate()
#     for index in range(0, numOfAssets) :
#         print str(portfolio.getAsset(index)) + "; weight: " + str(portfolio.getWeight(index))
        
        
    
