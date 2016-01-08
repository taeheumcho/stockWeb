'''
Created on 2016. 1. 7.

@author: jaylee
'''
from util.time.BusinessDayConvention import BusinessDayConvention
from engine.strategy.Portfolio import Portfolio
from engine.data.AbstractData import AbstractData

class AbstractEngine(object):
    
    def __init__(self, assets, strategy, processInfo):
        self._assets = assets
        self._strategy = strategy
        self._processInfo = processInfo
        self._strategy.setAssets(assets)
            
    def generate(self):
        calendar = self._processInfo.getCalendar()        
        testStartDate = calendar.adjustDate(self._processInfo.getTestStartDate(),
                                        BusinessDayConvention.FOLLOWING)
        testEndDate = calendar.adjustDate(self._processInfo.getTestEndDate(),
                                      BusinessDayConvention.FOLLOWING)
        trainStartDate = calendar.adjustDate(self._processInfo.getTrainStartDate(),
                                        BusinessDayConvention.FOLLOWING)
        trainEndDate = calendar.adjustDate(self._processInfo.getTrainEndDate(),
                                        BusinessDayConvention.FOLLOWING)
        legDate = calendar.adjustDate(testStartDate.plusDays(-self._processInfo.getTimeLeg()),
                                        BusinessDayConvention.FOLLOWING)
        processDate = testStartDate
        
        portfolios = {}
        while processDate.diff(testEndDate) <= 0 :
            #MarketPrice
            processAssets = AbstractData().getMarketPrice(processDate, self._assets);            
            #Train
            self._strategy.train(trainStartDate, trainEndDate)
            #Test            
            weights = self._strategy.weights(legDate)
            
            #Portfolio
            portfolios[processDate] = Portfolio(processDate, processAssets, weights)
                        
            trainStartDate = calendar.adjustDate(trainStartDate.plusDays(1),
                                              BusinessDayConvention.FOLLOWING)
            trainEndDate = calendar.adjustDate(trainEndDate.plusDays(1),
                                              BusinessDayConvention.FOLLOWING)
            legDate = calendar.adjustDate(legDate.plusDays(1),
                                              BusinessDayConvention.FOLLOWING)
            processDate = calendar.adjustDate(processDate.plusDays(1),
                                              BusinessDayConvention.FOLLOWING)
            #print trainStartDate, trainEndDate, legDate, processDate
        return portfolios
        