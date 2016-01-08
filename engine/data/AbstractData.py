'''
Created on 2016. 1. 8.

@author: Jay
'''
import copy
from optparse import Values

from engine.strategy.Asset import Equity, Cash, Asset
from stockInfo.models import ZzImsiSisae, ImsiIndexData
from util.TypeDef import TypeDef


class AbstractData(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    
    def getMarketPrice(self, processDate, assets):
        
        newAssets = {}        
        for assetkey in assets.keys() :
            marketPrice = 0
            asset = assets[assetkey]
            newAssets[assetkey] = copy.copy(asset)         
            if (type(asset) is Equity) :
                #EQUITY
                equityType = asset.getEquityType()
                if (equityType is TypeDef.EquityType.STOCK) :
                    #STOCK
                    marketPrice = ZzImsiSisae.objects.filter(date = processDate).\
                        filter(code = asset.getAssetCode()).\
                        values('currentprice')
                    
                elif (equityType is TypeDef.EquityType.ETF) :
                    #ETF
                    asset.getAssetCode()
                
                newAssets[assetkey].setMarketPrice(marketPrice[0]['currentprice'])
            elif (type(asset) is Cash):
                #CASH
                print "CASH"
        
        return newAssets
        
    def getData(self, startDate, endDate, assets):
        assetCodesOfStocks = []
        assetCodesOfETFs = []
        assetCodesOfIndices = []
        for assetkey in assets.keys() :
            asset = assets[assetkey]
            if (type(asset) is Equity) :
                #EQUITY
                equityType = asset.getEquityType()
                if (equityType is TypeDef.EquityType.STOCK) :
                    #STOCK
                    assetCodesOfStocks.append(asset.getAssetCode())
                elif (equityType is TypeDef.EquityType.ETF) :
                    #ETF
                    assetCodesOfETFs.append(asset.getAssetCode())
                elif (equityType is TypeDef.EquityType.INDEX) :
                    #INDEX
                    assetCodesOfIndices.append(asset.getAssetCode())
            else :
                #NOT EQUITY
                print "NOT EQUITY"
                
        stockDatas = ZzImsiSisae.objects.filter(date__gte = startDate).\
                filter(date__lte = endDate).\
                filter(code__in = assetCodesOfStocks)
                
        
        indexDatas = ImsiIndexData.objects.filter(date__gte = startDate).\
                filter(date__lte = endDate).\
                filter(code__in = assetCodesOfIndices)
                
        return stockDatas