import pymysql

from login import models

def add_veri(phone,veri):
    models.msg_veri.objects.create(Tel=str(phone), ver=str(veri))

def del_veri(veri):
    basic_info_connect = pymysql.connect(host='localhost', user='root', password='suqi95716aa', database='mid_pro')
    cur = basic_info_connect.cursor()
    cur.execute("DELETE FROM login_msg_veri WHERE ver='%s';" % (veri))
    basic_info_connect.commit()

def add_reginfo(phone,pwd):
    basic_info_connect = pymysql.connect(host='localhost', user='root', password='suqi95716aa', database='mid_pro')
    cur = basic_info_connect.cursor()
    cur.execute("INSERT INTO login_userinfo (tel,pwd) value('%s','%s');"%(phone,pwd))
    basic_info_connect.commit()

def veri_logininfo(phone,pwd):
    data = models.UserInfo.objects.filter(tel=str(phone),pwd=str(pwd))
    return data