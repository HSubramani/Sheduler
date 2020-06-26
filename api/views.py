from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from datetime import datetime
import requests
import time
def api(request,date,url):
    result='Not valid'
    pdate=datetime.now()
    year,month,day=pdate.year,pdate.month,pdate.day
    hr,min=pdate.hour,pdate.minute
    if((day==int(date[0:2]))& (month==int(date[2:4]))& (year==int(date[4:8]))& (hr==int(date[8:10]))&(min==int(date[10:]))):
        code=requests.get('https://'+url).status_code
        time.sleep(5)
        if(code==200):
            result='Valid code: '+str(code)
        else:
            result='Invalid code: '+str(code)
    return HttpResponse(result)
def ping(request):
    data={'status':'ok'}
    return JsonResponse(data)
