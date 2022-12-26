from django.http import HttpResponse
from mycelery.sms.tasks import send_sms,send_sms2
# Create your views here.


def test(request):

    # 异步任务
    send_sms.delay('111')
    send_sms2.delay('222')

    # 定时任务

    return HttpResponse('定时任务完成！')