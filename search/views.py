#coding:utf8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from database.models import StockInfo
from .models import StockHistoryInfo
from django.db.models import Q

# Create your views here.
stockinfo = 'abc'

def main(req):
	stockinfo = req.POST['stockinfo']	
	return render(req,'search.html')

def refresh_5s(req):
	try:
		x = StockInfo.objects.get(Q(StockID=stockinfo)|Q(StockName=stockinfo))
	except StockInfo.DoesNotExist:
		pass
	else:
		return render(req,'refresh_5s.html',{'CurrentPrice':x.CurrentPrice})

def refresh_1min(req):
	x = StockHistoryInfo.objects.filter(Q(StockID=stockinfo)|Q())	#here need datatime
	return render(req,'refresh_1min.html',{'history_info':x})

def update_realtime(stockid,currentprice):
	try:
		x = StockInfo.objects.get(Q(StockID=stockinfo)|Q(StockName=stockinfo))
	except StockInfo.DoesNotExist:
		pass
	else:
		return render(req,'refresh_5s.html',{'CurrentPrice':x.CurrentPrice})
	x = StockInfo.objects.get(StockID=stockid)
	x.CurrentPrice = currentid
	x.save()

def insert_history(stockid,historytime,highestvalue,lowestvalue):
	x = StockHistoryInfo(StockID=stockid,HistoryTime=historytime,Highest_value=highestvalue,Lowest_value=lowestvalue)
	x.save()

