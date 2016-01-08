'''
Created on 2016. 1. 7.

@author: jaylee
'''
from util.TypeDef import TypeDef


class Asset(object):

    def __init__(self, assetName, assetCode, assetType):
        self._assetName = assetName
        self._assetCode = assetCode
        self._assetType = assetType
        self._marketPrice = None;
    
    def getAssetName(self):
        return self._assetName
    
    def getAssetCode(self):
        return self._assetCode
    
    def setMarketPrice(self, marketPrice):
        self._marketPrice = marketPrice
    
    def getMarketPrice(self):
        return self._marketPrice
    
    def __str__(self):
        return "AssetCode: " + str(self._assetCode) + \
            "; AssetName: " + str(self._assetName) + \
            "; AssetType: " + str(self._assetType)
            
class Equity(Asset):
    
    def __init__(self, assetName, assetCode, equityType):
        self._assetName = assetName
        self._assetCode = assetCode
        self._equityType = equityType
        super(Equity, self).__init__(assetName, assetCode, 
                                     TypeDef.AssetType.EQUITY)
    
    def getEquityType(self):
        return self._equityType
    
    def __str__(self):
        return "AssetCode: " + str(self._assetCode) + \
            "; AssetName: " + str(self._assetName) + \
            "; AssetType: " + str(self._assetType) + \
            "; EquityType: " + str(self._equityType)

class Cash(Asset):
    
    def __init__(self, assetName, assetCode):
        self._assetName = assetName
        self._assetCode = assetCode
        super(Cash, self).__init__(assetName, assetCode, 
                                     TypeDef.AssetType.CASH)
    
    def __str__(self):
        return "AssetCode: " + str(self._assetCode) + \
            "; AssetName: " + str(self._assetName) + \
            "; AssetType: " + str(self._assetType)
