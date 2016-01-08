'''
Created on 2016. 1. 7.

@author: jaylee
'''
from engine.data.AbstractData import AbstractData

class AbstractStrategy(object):
    
    def __init__(self):
        '''
        '''
        self._assets = None
        self._params = None
        self._function = None
        
    def setAssets(self, assets):
        self._assets = assets
        
    def train(self, trainingStartDate, trainingEndDate):
        '''
        '''
        
    def weights(self, legDate):
        '''
        Return weights
        '''
                
        weights = {}
        for asset in self._assets.keys() :
             weights[asset] = 1
    
        return weights
        
