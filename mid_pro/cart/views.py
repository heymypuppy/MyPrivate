from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
import datetime
import random
from pymongo import MongoClient

from index import sql as index
from cart import sql as cart
from cart import models
from index import models as t1

# Create your views here.
#添加购物车
def cartCountPar1(request):

    dishName = request.POST.get('dishName',None)
    dishValue = request.POST.get('dishValue',None)[1:]
    dishValue = round(float(dishValue))
    cartInfo = cart.check_whe_commodity(dishName,request.session['username'])
    commdtInfo = index.shop_commodity()
    addrModels = cart.checkAddr(request.session['username'])

    #购物车清单
    if cartInfo:
        Num = cartInfo[0][3]+1
        cart.updateCommodityNum(request.session['username'],dishName,Num,dishValue)
    else:
        cart.add_commodityCart(request.session['username'],dishName,dishValue)

    collect_status = index.collect_status(request.session['username'])
    cartModels = cart.cartModels(request.session['username'])

    totalMoney = 0
    for i in cartModels:
        totalMoney = totalMoney + i[5]

    if collect_status :
        return render(request, 'shop_detail.html',{'username': request.session['username'], 'able1': 'true', 'commodtInfo': commdtInfo,'cartModels':cartModels,'totalMoney':totalMoney,'addrModels':addrModels})
    else:
        return render(request, 'shop_detail.html',{'username': request.session['username'], 'able1': 'false', 'commodtInfo': commdtInfo,'cartModels':cartModels,'totalMoney':totalMoney,'addrModels':addrModels})
#清空购物车
def clearCart(request):
    cart.cleaCart(request.session['username'])
    collect_status = index.collect_status(request.session['username'])
    addrModels = cart.checkAddr(request.session['username'])

    if collect_status :
        commdtInfo = index.shop_commodity()
        return render(request, 'shop_detail.html',{'username': request.session['username'], 'able1': 'true', 'commodtInfo': commdtInfo,'totalMoney':0,'addrModels':addrModels})
    else:
        commdtInfo = index.shop_commodity()
        return render(request, 'shop_detail.html',{'username': request.session['username'], 'able1': 'false', 'commodtInfo': commdtInfo,'totalMoney':0,'addrModels':addrModels})

#处理加减
def addOrmul(request):
    dishName = request.POST.get('dishName',None)
    button = request.POST.get('submit',None)
    commdtInfo = index.shop_commodity()
    collect_status = index.collect_status(request.session['username'])
    num = (models.TemCountValue.objects.filter(dishName=dishName, basicTel=request.session['username']))[0].dishNum
    value = (models.TemCountValue.objects.filter(dishName=dishName, basicTel=request.session['username']))[0].dishValue
    addrModels = cart.checkAddr(request.session['username'])


    if collect_status:
        if button == '-':#根据按钮判断操作
            num -= 1
            if num == 0:#修改
                models.TemCountValue.objects.filter(dishName=dishName, basicTel=request.session['username']).delete()
            else:
                models.TemCountValue.objects.filter(dishName=dishName, basicTel=request.session['username']).update(dishNum=num,dishTotal=num*value)

            cartModels = cart.cartModels(request.session['username'])
            totalMoney = 0
            for i in cartModels:
                totalMoney = totalMoney + i[5]
            return render(request, 'shop_detail.html',{'username': request.session['username'], 'able1': 'true', 'commodtInfo': commdtInfo,'cartModels': cartModels, 'totalMoney': totalMoney,'addrModels':addrModels})

        else:
            num +=1
            models.TemCountValue.objects.filter(dishName=dishName, basicTel=request.session['username']).update(dishNum=num,dishTotal=num*value)

            cartModels = cart.cartModels(request.session['username'])
            totalMoney = 0
            for i in cartModels:
                totalMoney = totalMoney + i[5]
            return render(request, 'shop_detail.html',{'username': request.session['username'], 'able1': 'true', 'commodtInfo': commdtInfo,'cartModels': cartModels, 'totalMoney': totalMoney,'addrModels':addrModels})

    else:
        if button == '-':#根据按钮判断操作
            num -= 1
            if num == 0:#修改
                models.TemCountValue.objects.filter(dishName=dishName, basicTel=request.session['username']).delete()
            else:
                models.TemCountValue.objects.filter(dishName=dishName, basicTel=request.session['username']).update(dishNum=num,dishTotal=num*value)

            cartModels = cart.cartModels(request.session['username'])
            totalMoney = 0
            for i in cartModels:
                totalMoney = totalMoney + i[5]
            return render(request, 'shop_detail.html',{'username': request.session['username'], 'able1': 'false', 'commodtInfo': commdtInfo,'cartModels': cartModels, 'totalMoney': totalMoney,'addrModels':addrModels})

        else:
            num +=1
            models.TemCountValue.objects.filter(dishName=dishName, basicTel=request.session['username']).update(dishNum=num,dishTotal=num*value)

            cartModels = cart.cartModels(request.session['username'])
            totalMoney = 0
            for i in cartModels:
                totalMoney = totalMoney + i[5]
            return render(request, 'shop_detail.html',{'username': request.session['username'], 'able1': 'false', 'commodtInfo': commdtInfo,'cartModels': cartModels, 'totalMoney': totalMoney,'addrModels':addrModels})


#购买按钮处理
def cartBuy(request):
    totalMoney = request.POST.get('totalMoney',None)
    addrid = request.POST.get('addr',None)
    if addrid == None:
        return HttpResponse('购买失败')
    else:
    #订单部分(用户信息)
        addrInfo = t1.addr_handler.objects.filter(id=addrid)
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
        orderInfo = {'basicTel':request.session['username'],'recvName':addrInfo[0].recv_name,'recvTel':addrInfo[0].recv_tel,'recvAddr':addrInfo[0].recv_addr,'buyTime':nowTime}
    #订单部分(店信息)
        orderNum = str(chr(random.randint(65,90)))+'-'+str(random.randint(10000,99999))
        commodityInfo = t1.shop_brand.objects.filter(id=1)
        orderInfo1 = {'orderNum':orderNum,'shopImage':commodityInfo[0].image_addr,'shopName':commodityInfo[0].shop_name,'shopTel':'13768203864','orderType':'货到付款','orderStatus':'未送达','orderTotalMoney':totalMoney}
    #订单部分(购买信息)
        dishInfo = models.TemCountValue.objects.filter(basicTel=request.session['username'])
        temDishContent = []
        dishContent = {}
        for i in dishInfo:
            dishContentPart = {}
            dishContentPart['dishName'] = i.dishName
            dishContentPart['dishNum'] = i.dishNum
            dishContentPart['dishValue'] = i.dishValue
            dishContentPart['dishTotal'] = i.dishTotal
            temDishContent.append(dishContentPart)
        dishContent['content'] = temDishContent
    orderInfo = dict(orderInfo)
    orderInfo.update(orderInfo1)
    orderInfo.update(dishContent)

    clinent = MongoClient()
    db = clinent.orderContent
    order = db.orderInfo
    order.insert(orderInfo)
    models.TemCountValue.objects.filter(basicTel=request.session['username']).delete()
    return HttpResponse("购买成功")


#需求：商品数量限制
