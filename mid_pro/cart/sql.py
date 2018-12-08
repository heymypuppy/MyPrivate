import pymysql
from pymongo import MongoClient

# def get_collect_status(basic_tel):
#     basic_info_connect = pymysql.connect(host='localhost', user='root', password='suqi95716aa', database='mid_pro')
#     cur = basic_info_connect.cursor()
#     cur.execute("SELECT collect_status FROM index_collect WHERE resName='肯德基(西大店)' AND basicTel='%s';"%(basic_tel))
#     data = cur.fetchall()
#     return data

def check_whe_commodity(dishName,basic_tel):
    basic_info_connect = pymysql.connect(host='localhost', user='root', password='suqi95716aa', database='mid_pro')
    cur = basic_info_connect.cursor()
    cur.execute("SELECT * FROM cart_temcountvalue WHERE dishName='%s' AND basicTel='%s';" % (dishName,basic_tel))
    data = cur.fetchall()
    return data

def add_commodityCart(basicTel,dishName,dishValue):
    basic_info_connect = pymysql.connect(host='localhost', user='root', password='suqi95716aa', database='mid_pro')
    cur = basic_info_connect.cursor()
    cur.execute("INSERT INTO cart_temcountvalue (basicTel,dishName,dishNum,dishValue,dishTotal)VALUES('%s','%s',1,%d,%d);" % (basicTel,dishName,dishValue,dishValue))
    basic_info_connect.commit()

def updateCommodityNum(basicTel,dishName,dishNum,dishValue):
    basic_info_connect = pymysql.connect(host='localhost', user='root', password='suqi95716aa', database='mid_pro')
    cur = basic_info_connect.cursor()
    cur.execute("UPDATE cart_temcountvalue SET dishNum=%d,dishtotal=%d WHERE basicTel='%s' AND dishName='%s';"%(dishNum,dishValue*dishNum,basicTel,dishName))
    basic_info_connect.commit()

def cartModels(basic_tel):
    basic_info_connect = pymysql.connect(host='localhost', user='root', password='suqi95716aa', database='mid_pro')
    cur = basic_info_connect.cursor()
    cur.execute("SELECT * FROM cart_temcountvalue WHERE basicTel='%s';"%(basic_tel))
    data = cur.fetchall()
    return data

def cleaCart(basic_tel):
    basic_info_connect = pymysql.connect(host='localhost', user='root', password='suqi95716aa', database='mid_pro')
    cur = basic_info_connect.cursor()
    cur.execute("DELETE FROM cart_temcountvalue WHERE basicTel='%s';"%(basic_tel))
    basic_info_connect.commit()

def checkAddr(basic_tel):
    basic_info_connect = pymysql.connect(host='localhost', user='root', password='suqi95716aa', database='mid_pro')
    cur = basic_info_connect.cursor()
    cur.execute("SELECT * FROM index_addr_handler WHERE basic_tel='%s';" % (basic_tel))
    data = cur.fetchall()
    return data

