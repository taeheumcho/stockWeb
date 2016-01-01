'''
Created on 2015. 11. 15.

@author: user
'''
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.stockHome, name='stockHome'),
    url(r'^backtest/$', views.backTestHome, name='backtest'),
#     url(r'^(?P<code>\w+)/$', views.stock_detail, name = 'stock_detail'),
#     url(r'^(?P<code>\w+)/$', views.stock_detail2, name = 'detail_imsi'),
#     url(r'^(?P<code>\w+)/$', views.ahomorgetta.stock_detail_class, name = 'chartdetailwithclass'),
#     url(r'^json/(?P<code>\w+)/$', views.stock_data_json, name = 'stock_data_json'),
#     url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name = 'post_detail'),
#     url(r'^post/new/$', views.post_new, name = 'post_new'),
#     url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit')
]