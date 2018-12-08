import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mid_pro.settings")# project_name 项目名称
django.setup()
import pymysql

from index import models

def shop_brand_is_woring():
    basic_info_connect = pymysql.connect(host='localhost', user='root', password='suqi95716aa', database='mid_pro')
    cur = basic_info_connect.cursor()
    cur.execute("SELECT * FROM index_shop_brand WHERE is_working=1")
    data = cur.fetchall()
    return data

def shop_brand_is_not_working():
    basic_info_connect = pymysql.connect(host='localhost', user='root', password='suqi95716aa', database='mid_pro')
    cur = basic_info_connect.cursor()
    cur.execute("SELECT * FROM index_shop_brand WHERE is_working=0")
    data1 = cur.fetchall()
    return data1

def addr_cir(basic_tel):
    basic_info_connect = pymysql.connect(host='localhost', user='root', password='suqi95716aa', database='mid_pro')
    cur = basic_info_connect.cursor()
    cur.execute("SELECT * FROM index_addr_handler WHERE basic_tel='%s';"%(basic_tel))
    data2 = cur.fetchall()
    return data2

def add_addr(name,tel,addr,basic_tel):
    basic_info_connect = pymysql.connect(host='localhost', user='root', password='suqi95716aa', database='mid_pro')
    cur = basic_info_connect.cursor()
    cur.execute("insert into index_addr_handler (recv_name,recv_tel,recv_addr,basic_tel)values('%s','%s','%s','%s');"%(name,tel,addr,basic_tel))
    basic_info_connect.commit()

def del_addr(id):
    basic_info_connect = pymysql.connect(host='localhost', user='root', password='suqi95716aa', database='mid_pro')
    cur = basic_info_connect.cursor()
    cur.execute("DELETE FROM index_addr_handler WHERE id=%d;"%(id))
    basic_info_connect.commit()

def orderHandler(basic_tel):
    basic_info_connect = pymysql.connect(host='localhost', user='root', password='suqi95716aa', database='mid_pro')
    cur = basic_info_connect.cursor()
    cur.execute("SELECT * FROM index_orderinfo WHERE basicTel='%s';" % (basic_tel))
    data3 = cur.fetchall()
    return data3

def resCollect_add(basic_tel):
    basic_info_connect = pymysql.connect(host='localhost', user='root', password='suqi95716aa', database='mid_pro')
    cur = basic_info_connect.cursor()
    cur.execute("INSERT INTO index_collect (basicTel,resName,resType,resLevel,resImg,collect_status)VALUES('%s','肯德基(西大店)','饮料小吃','52.00','/static/images/shop_brand/kfc.jpg','已收藏');" % (basic_tel))
    basic_info_connect.commit()

def resCollect_del(basic_tel):
    basic_info_connect = pymysql.connect(host='localhost', user='root', password='suqi95716aa', database='mid_pro')
    cur = basic_info_connect.cursor()
    cur.execute("DELETE FROM index_collect WHERE resName='肯德基(西大店)' AND basicTel='%s';"%(basic_tel))
    basic_info_connect.commit()

def collect_status(basic_tel):
    basic_info_connect = pymysql.connect(host='localhost', user='root', password='suqi95716aa', database='mid_pro')
    cur = basic_info_connect.cursor()
    cur.execute("SELECT collect_status FROM index_collect WHERE resName='肯德基(西大店)' AND basicTel='%s';"%(basic_tel))
    data2 = cur.fetchall()
    return data2

def member_collect(basic_tel):
    basic_info_connect = pymysql.connect(host='localhost', user='root', password='suqi95716aa', database='mid_pro')
    cur = basic_info_connect.cursor()
    cur.execute("SELECT * FROM index_collect WHERE basicTel='%s' AND resName='肯德基(西大店)';" % (basic_tel))
    data5 = cur.fetchall()
    return data5

def shop_commodity():
    basic_info_connect = pymysql.connect(host='localhost', user='root', password='suqi95716aa', database='mid_pro')
    cur = basic_info_connect.cursor()
    cur.execute("SELECT * FROM cart_commodity;")
    data6 = cur.fetchall()
    return data6