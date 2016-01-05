from django import forms

from stockInfo.models import ZzImsiSisae

from .models import StockInfo


class stockInfoForm(forms.ModelForm):
    
    class Meta:
        model = StockInfo
        fields = ('code',)

class stockSisaeForm(forms.ModelForm):
    class Meta:
        model = ZzImsiSisae
        fields = ('code','date','currentprice',)
        
class assetSelection(forms.ModelForm):
    class Meta:
        model = ZzImsiSisae
        fields = ('code',)