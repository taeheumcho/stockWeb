'''
Created on 2016. 1. 7.

@author: jaylee
'''

class TypeDef(object):
    
    class AssetType(enumerate):
        EQUITY = "EQUITY"
        CASH = "CASH"
        
    class EquityType(enumerate):
        INDEX = "INDEX"
        STOCK = "STOCK"
        ETF = "ETF"
    