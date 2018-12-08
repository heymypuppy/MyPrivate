from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
import json
import re
import random
import os
import time
import requests

from login import sql
from login import models

# Create your views here.

#login function
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        phone = request.POST.get('login_id',None)
        pwd = request.POST.get('login_pwd',None)
        data = sql.veri_logininfo(phone,pwd)
        if data:

            request.session['username'] = phone
            request.session['is_login'] = True
            # return render(request, 'shop_brand.html',{'username':request.session['username']})
            return redirect("/index")
        else:
            if not models.UserInfo.objects.filter(tel=str(phone)):
                return render(request, 'login.html', {'orig_phone': phone, 'wro_acct': "账号错误,请重新输入", 'wro_pwd': "密码错误,请重新输入"})
            elif not models.UserInfo.objects.filter(tel=str(phone),pwd=str(pwd)):
                return render(request, 'login.html', {'orig_phone': phone, 'wro_pwd': '密码错误,请重新输入'})


#register function

def register_get_veri(request):
    phone_pat = re.compile('^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')

    if request.method == 'GET':
        return render(request,'register.html')
    elif request.method == 'POST':
        phone = request.POST.get('rphone',None)
        riPho = re.search(phone_pat,str(phone))

        if not riPho:
            return render(request,'register.html',{'error_msg':'手机号码格式错误','phone_num':phone})
        else:
            data = models.UserInfo.objects.filter(tel=str(phone))
            if data :
                return render(request,'register.html',{'error_msg':'手机号码已经存在','phone_num':phone})
            else:
                veri = random.randint(1000, 10000)

                pid = os.fork()
                if pid == 0:
                    time.sleep(180)
                    sql.del_veri(veri)
                    return render(request,'register.html',{'error_msg':'','phone_num':phone,'send_already':'验证码已发送,请注意查收',"able":'true'})

                else:
                    send_messag_example(phone,veri)
                    sql.add_veri(phone,veri)
                    return render(request,'register.html',{'error_msg':'','phone_num':phone,'send_already':'验证码已发送,请注意查收',"able":'true'})

#手机号码已存在的提示
#veri_send_API
def send_messag_example(phone,veri):
    data = {
        "uid": "Eu4zQDTyD4Kp",
        # "pas": "228hmbmc",
        "pas": "b9ta27yx",
        "cid": "d9Z7uIKCYqhQ",
        "type": "json"
    }
    data['mob'] = str(phone)
    data['p1'] = str(veri)
    resp = requests.post(("http://api.weimi.cc/2/sms/send.html"),data,timeout=3 , verify=False);
    result =  json.loads( resp.content )


#hand ur register msg
def hand_regst_msg(request):
    phone = request.POST.get('rePhone', None)
    veri = request.POST.get('verify',None)
    pwd = request.POST.get('pwd',None)
    pwd1 = request.POST.get('pwd1',None)

    data = models.msg_veri.objects.filter(Tel=str(phone), ver=str(veri))

    if not phone:
        return render(request, 'register.html',{"verif":'', "repwd": pwd, "repwd1": pwd1,"able1":'true'})
    else:
        if not data or not pwd or not pwd1 or pwd != pwd1 or len(pwd)<6 or len(pwd1)<6:
            return render(request, 'register.html',{"phone_num": phone, "rephone": phone, "verif":'', "repwd": pwd, "repwd1": pwd1,"able1":'true'})

        else:
            sql.add_reginfo(phone,pwd)
            request.session['username'] = phone
            request.session['is_login'] = True
            return redirect('/index')

