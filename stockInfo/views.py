# from highcharts.views import HighChartsLineView
# import json, highcharts

import json
from django.http.response import HttpResponseRedirect, JsonResponse, \
    HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.context import RequestContext
from django.template.context_processors import request, csrf
import pdb
from stockInfo.models import CcImsiData, ImsiIndexData, ZzImsiSisae
from django.db import models
from stockInfo.forms import DateRangeForm
from pytz import timezone
from IPython.core.debugger import Pdb
import datetime

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
#     pdb.set_trace()
    if request.method == "POST":
        pdb.set_trace()
        date_range = request.POST['date_range']
        start_date_string = date_range.split(' - ')[0]
        end_date_string = date_range.split(' - ')[1]
        print(start_date_string)
        f = DateRangeForm(request.POST)
        pdb.set_trace()
        if f.is_valid():
            c = f.save(commit = False)
            c.end_date = timezone.now()
            c.save()
            pdb.set_trace()
    else:
        tmpSisae = ZzImsiSisae.objects.filter(code__contains='KS', currentprice__gte='100000', date = '20150708')
        return render(request, 'stockInfo/backTest.html', {'sisae': tmpSisae}) 


    tmpSisae = ZzImsiSisae.objects.filter(code__contains='KS', currentprice__gte='100000', date = '20150708')
    return render(request, 'stockInfo/backTest.html', {'sisae': tmpSisae, 'form': f})   
    
def results(request):
    
    training_range = request.POST["training"]
    training_start_date_string = training_range.split(' - ')[0]
    training_end_date_string = training_range.split(' - ')[1]
    
    test_range = request.POST['test']
    test_start_date_string = test_range.split(' - ')[0]
    test_end_date_string = test_range.split(' - ')[1]
    
    training_start_date = datetime.datetime.strptime(training_start_date_string,"%b %d, %Y").strftime("%Y%m%d")
    training_end_date = datetime.datetime.strptime(training_end_date_string,"%b %d, %Y").strftime("%Y%m%d")
    test_start_date = datetime.datetime.strptime(test_start_date_string,"%b %d, %Y").strftime("%Y%m%d")
    test_end_date = datetime.datetime.strptime(test_end_date_string,"%b %d, %Y").strftime("%Y%m%d")
        
    asset_list_string = request.POST['assets']
    
    training_period = [training_start_date, training_end_date]
    test_period = [test_start_date, test_end_date]
    asset_list = asset_list_string.split('|')
    strategy_Num = request.POST['strategy']
    timeLag = request.POST['timelag']
    
    return render(request, 'stockInfo/strategyResults.html', {'train':training_period, 'test':test_period, 'assets':asset_list, 'strategy':strategy_Num, 'timeLag':timeLag})

