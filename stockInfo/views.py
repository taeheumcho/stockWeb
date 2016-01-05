# from highcharts.views import HighChartsLineView
# import json, highcharts

import json
from django.http.response import HttpResponseRedirect, JsonResponse, \
    HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.context import RequestContext
from django.template.context_processors import request
import pdb
from stockInfo.models import CcImsiData, ImsiIndexData, ZzImsiSisae
from django.db import models

tmpFX = []
tmpKOSPI = []
tmpKOSDAQ = []
def stockHome(request):       
    tmpFX = CcImsiData.objects.filter(code = 'FX_USDKRW').values('date','value').order_by('date')
#     pdb.set_trace()
    closestdate_FX = tmpFX[len(tmpFX) - 1]['value']
    
    tmpKOSPI = ImsiIndexData.objects.filter(code = 'KOSPI').values('date','value').order_by('date')
    closestdate_KOSPI = tmpKOSPI[len(tmpKOSPI) - 1]['value']

    tmpKOSDAQ = ImsiIndexData.objects.filter(code = 'KOSDAQ').values('date','value').order_by('date')
    closestdate_KOSDAQ = tmpKOSDAQ[len(tmpKOSDAQ) - 1]['value']
    
    result_list = json.dumps(list(tmpKOSDAQ))
    response = JsonResponse(result_list, safe=False)
    
    return render(request, 'stockInfo/home.html',{'FX': closestdate_FX, 'KOSPI': closestdate_KOSPI, 'KOSDAQ': closestdate_KOSDAQ, 'ChartData': result_list})


def backTestHome(request):

    tmpSisae = ZzImsiSisae.objects.filter(code__contains='KS', currentprice__gte='100000', date = '20150708')
    return render(request, 'stockInfo/backTest.html', {'sisae': tmpSisae})   
    