"""mid_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include


from login import views as t1
from index import views as t2
from cart import views as t3

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^register$', t1.register_get_veri),
    url(r'^hand_regst_msg$', t1.hand_regst_msg),
    url(r'^login$', t1.login),

    url(r'^index$',t2.index),
    url(r'^logout$',t2.logout),
    url(r'^member_index$',t2.member_index),
    url(r'^shop_detail$',t2.shop_index),
    url(r'^member_addr$',t2.member_addr),
    url(r'^add_addr$',t2.add_addr),
    url(r'^del_addr$',t2.del_addr),
    url(r'^member_order$',t2.member_order),
    url(r'^del_order$',t2.del_order),
    url(r'^confirm_receipt$',t2.confirm_receipt),
    url(r'^shop_intro$',t2.shop_intro),
    url(r'^shop_collect$',t2.shop_collect),
    url(r'^member_collect$',t2.member_collect),
    url(r'^shop_collect_detail$',t2.shop_collect_detail),

    url(r'^cartCountPar1$',t3.cartCountPar1),
    url(r'^clearCart$',t3.clearCart),
    url(r'^cartBuy$',t3.cartBuy),
    url(r'^addOrmul$',t3.addOrmul),
]
