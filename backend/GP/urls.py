from django.urls import path
from .views import showhome  ,showabout , showauthentification , showcreate , shows , showpay ,detail ,order

urlpatterns = [
  path('aa/' , showhome.as_view() , name='home') ,
  path('about/' ,showabout.as_view(),name='about' ) ,
  path('authentification/' ,showauthentification.as_view(),name='au' ) ,
  path('' ,showcreate.as_view(),name='ss' ) ,
   path('s/' ,shows.as_view(),name='sr' ) ,
  path('pay/' ,showpay.as_view(),name='mouad' ) ,
  path('details/<str:name>' ,detail.as_view(),name='detail' ) ,
  path('ordernow/<int:name>' ,order.as_view() ,name='order' ) ,

    
]