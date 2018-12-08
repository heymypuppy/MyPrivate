from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from pymongo import MongoClient
from bson import ObjectId

from index import sql
from cart import sql as cart
from index import models
# Create your views here.


def index(request):
    if request.method == 'GET':
        data = request.session.get('is_login',None)
        if data:
            data_is_working = sql.shop_brand_is_woring()
            data_is_not_working = sql.shop_brand_is_not_working()

            return render(request, 'shop_brand.html', {'username': request.session['username'],'data_is_working':data_is_working,'data_is_not_working':data_is_not_working})
        else:
            return render(request,'login.html')

def logout(request):
    request.session.clear()
    return redirect('/login')

def member_index(request):
    return render(request,'member_index.html',{'username':request.session['username']})



# -------------------------------------------
# add address
def member_addr(request):
    basic_tel = request.session['username']
    data = sql.addr_cir(basic_tel)
    return render(request,'member_addr.html',{'username':request.session['username'],"addr_contr":data})

def add_addr(request):
    name = request.POST.get('recv_name',None)
    tel = request.POST.get('recv_tel',None)
    addr = request.POST.get('recv_addr',None)
    basic_tel = request.session['username']
    sql.add_addr(name,tel,addr,basic_tel)
    return redirect('/member_addr')

def del_addr(request):
    id = request.POST.get('id',None)
    if id:
        sql.del_addr(int(id))
        return redirect('/member_addr')
    else:
        return redirect('/member_addr')


# ---------------------------------------------
# orderHandler
def member_order(request):
    clinent = MongoClient()
    db = clinent.orderContent
    order = db.orderInfo
    orderInfo = []
    for i in order.find({'basicTel':request.session['username']}):
        i = list(i.values())
        lastElem = i[13]
        i.pop()
        tempDish = []
        for j in lastElem:
            temp = list(j.values())
            tempDish.append(temp)
        i.append(tempDish)
        orderInfo.append(i)
    return render(request,'member_order.html',{'username':request.session['username'],'orderinfo':orderInfo})

def del_order(request):
    clinent = MongoClient()
    db = clinent.orderContent
    order = db.orderInfo

    id = request.POST.get('orderID',None)
    print(id)
    order.delete_one({'_id':ObjectId(id)})
    return redirect('/member_order')

def confirm_receipt(request):
    clinent = MongoClient()
    db = clinent.orderContent
    order = db.orderInfo

    id = request.POST.get('orderID',None)
    oldQuery = {'orderStatus':'未送达','_id':ObjectId(id)}
    newQuery = {"$set":{'orderStatus':'已送达'}}
    print(request.POST.get('orderID',None))

    order.update_one(oldQuery,newQuery)
    return redirect('/member_order')

# ------------------------------------------------


def shop_index(request):
    if request.method == 'GET':
        collect_status = sql.collect_status(request.session['username'])
        cartModels = cart.cartModels(request.session['username'])
        addrModels = cart.checkAddr(request.session['username'])

        totalMoney = 0
        for i in cartModels:
            totalMoney = totalMoney + i[5]


        if collect_status:
            commdtInfo = sql.shop_commodity()
            return render(request,'shop_detail.html',{'username': request.session['username'],'collect_status':collect_status[0][0],'commodtInfo':commdtInfo,'cartModels':cartModels,'totalMoney':totalMoney,'addrModels':addrModels})
        else:
            commdtInfo = sql.shop_commodity()
            return render(request,'shop_detail.html',{'username': request.session['username'],'collect_status':'未收藏','commodtInfo':commdtInfo,'cartModels':cartModels,'totalMoney':totalMoney,'addrModels':addrModels})
# -------------------------------------------------
def shop_intro(request):
    if request.method == 'GET':
        collect_status = sql.collect_status(request.session['username'])
        if collect_status:
            return render(request,'shop_intro.html',{'username': request.session['username'],'collect_status':collect_status[0][0]})
        else:
            return render(request,'shop_intro.html',{'username': request.session['username'],'collect_status':'未收藏'})


def shop_collect(request):
    collect = request.POST.get('collect',None)
    if collect == '未收藏':
        sql.resCollect_add(request.session['username'])
        return render(request, 'shop_intro.html', {'username': request.session['username'], 'able1': 'true'})
    else:
        sql.resCollect_del(request.session['username'])
        return render(request, 'shop_intro.html', {'username': request.session['username'], 'able1': 'false'})

def member_collect(request):
    data = sql.member_collect(request.session['username'])
    return render(request,'member_collect.html',{'username':request.session['username'],'member_collect':data})


def shop_collect_detail(request):
    collect = request.POST.get('collect1', None)
    cartModels = cart.cartModels(request.session['username'])
    addrModels = cart.checkAddr(request.session['username'])
    print(addrModels)
    totalMoney = 0
    for i in cartModels:
        totalMoney = totalMoney + i[5]

    if collect == '未收藏':
        commdtInfo = sql.shop_commodity()
        sql.resCollect_add(request.session['username'])
        return render(request, 'shop_detail.html', {'username': request.session['username'], 'able1': 'true','commodtInfo':commdtInfo,'cartModels':cartModels,'totalMoney':totalMoney,'addrModels':addrModels})
    else:
        commdtInfo = sql.shop_commodity()
        sql.resCollect_del(request.session['username'])
        return render(request, 'shop_detail.html', {'username': request.session['username'], 'able1': 'false','commodtInfo':commdtInfo,'cartModels':cartModels,'totalMoney':totalMoney,'addrModels':addrModels})



