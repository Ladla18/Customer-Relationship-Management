from django.urls import path
from . import views

urlpatterns=[
    path('customerhome/',views.customerhome,name='customerhome'),
    path('logout/',views.logout,name='logout'),
    path('response/', views.response, name='response'),
    path('changepassword',views.changepassword,name="changepassword"),
    path('viewprofile/',views.viewprofile,name="viewprofile"),
    path('products',views.products,name='products'),
    path('buy/<id>',views.buy,name='buy'),
    path('vieworders',views.vieworders,name='vieworders'),
]