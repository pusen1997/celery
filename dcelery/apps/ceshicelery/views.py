from django.http import HttpResponse
from django.shortcuts import render
from mycelery.sms.tasks import send_sms,send_sms2
from datetime import datetime,timedelta


# 异步任务
def test(request):

    send_sms.delay('send_sms')
    send_sms2.delay('send_sms2')

    return HttpResponse('OK')

# 定时任务
def beat(request):
    ctime = datetime.now()
    utc_ctime = datetime.utcfromtimestamp(ctime.timestamp())
    time_dealy = timedelta(seconds=3)
    task_time = utc_ctime + time_dealy
    result = send_sms.apply_async(['911',],eta = task_time)
    result2 = send_sms2.apply_async(['13142163063',],eta = task_time)
    print(result.id)
    print(result2.id)
    return HttpResponse('短信-定时任务发送！')