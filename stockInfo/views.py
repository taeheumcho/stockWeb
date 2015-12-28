# from highcharts.views import HighChartsLineView
# import json, highcharts
import code
import json
from mimetypes import MimeTypes
import pdb
from time import timezone

from _mysql import NULL
from chartit import Chart, DataPool
from django.core import serializers
from django.http.response import HttpResponseRedirect, JsonResponse, \
    HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import request
from django.views.generic.base import TemplateView
from lxml.html.builder import CODE

from .forms import stockInfoForm
from .models import StockInfo, StockSisae, ZzImsiSisae
from json.encoder import JSONEncoder
from stockInfo.models import CcImsiData, ImsiIndexData
from django.utils.safestring import mark_safe
from django.template.context import RequestContext
import operator

# Create your views here.
data = []
def stockHome(request):
#     if request.method == "POST":  
#         entity = StockInfo.objects.get(pk = request.POST['uri'])
# #         pdb.set_trace()           
# #         form = stockInfoForm(request.POST, instance = entity)
# #         if form.is_valid():
# #         info = form.save(commit = False)
# #         info.save()
# 
#         return redirect('stockInfo.views.stock_detail2', code = entity.code)
# #         else :
# #             render(request, 'stockInfo/InfoDirector.html')
#     else :
#         form = stockInfoForm()
#         
    tmpFX = CcImsiData.objects.filter(code = 'FX_USDKRW').values('date','value').order_by('date')
    closestdate_FX = tmpFX[len(tmpFX) - 1]['value']
    
    tmpKOSPI = ImsiIndexData.objects.filter(code = 'KOSPI').values('date','value').order_by('date')
    closestdate_KOSPI = tmpKOSPI[len(tmpKOSPI) - 1]['value']

    tmpKOSDAQ = ImsiIndexData.objects.filter(code = 'KOSDAQ').values('date','value').order_by('date')
    closestdate_KOSDAQ = tmpKOSDAQ[len(tmpKOSDAQ) - 1]['value']
    
    result_list = json.dumps(list(tmpKOSDAQ))
    response = JsonResponse(result_list, safe=False)
    
    return render(request, 'stockInfo/newHome.html',{'FX': closestdate_FX, 'KOSPI': closestdate_KOSPI, 'KOSDAQ': closestdate_KOSDAQ, 'ChartData': result_list})


