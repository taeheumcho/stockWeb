'''
Created on 2016. 1. 7.

@author: jaylee
'''

class ProcessInfo(object):
    
    def __init__(self, 
                 trainStartDate, trainEndDate,
                 testStartDate, testEndDate,
                 timeLeg, calendar, rebalancFreq):
        
        self._trainStartDate = trainStartDate
        self._trainEndDate = trainEndDate
        self._testStartDate = testStartDate
        self._testEndDate = testEndDate
        self._calendar = calendar
        self._rebalanceFreq = rebalancFreq
        self._timeLeg = timeLeg
        
    def getTrainStartDate(self):
        return self._trainStartDate
    
    def getTrainEndDate(self):
        return self._trainEndDate
    
    def getTestStartDate(self):
        return self._testStartDate
    
    def getTestEndDate(self):
        return self._testEndDate
        
    def getCalendar(self):
        return self._calendar
    
    def getRebalanceFreq(self):
        return self._rebalanceFreq
    
    def getTimeLeg(self):
        return self._timeLeg