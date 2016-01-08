'''
Created on 2016. 1. 7.

@author: jaylee
'''

class Portfolio(object):
    
    def __init__(self, date, assets, weights):
        self._date = date
        self._assets = assets        
        self._weights = weights
        self._numOfAsset = len(assets)
        
    def getDate(self):
        return self._date
    
    def getAsset(self, assetCode):
        return self._assets[assetCode]
    
    def getWeight(self, assetCode):
        return self._weights[assetCode]
    
    def getMarketPrice(self, assetCode):
        return self._assets[assetCode].getMarketPrice()
    
    def getNumOfAssets(self):
        return self._numOfAsset
    
    def __str__(self):
        
        resultStr = str(self._date) 
        for assetkey in self._assets.keys() : 
            resultStr = resultStr + ": " + str(self.getAsset(assetkey)) +\
                "; weight: " +  str(self.getWeight(assetkey)) +\
                "; marketPrice: " + str(self.getMarketPrice(assetkey))               
            
        return resultStr
        