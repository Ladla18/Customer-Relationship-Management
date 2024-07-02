from django.urls import path
from . import views

urlpatterns = [
    path('adminhome/',views.adminhome,name='adminhome'),
    path('logout/',views.logout,name='logout'),
    path('viewcustomers/',views.viewcustomers,name='viewcustomers'),
    path('viewenquiries/',views.viewenquiries,name='viewenquiries'),
    path('delenq/<id>',views.delenq,name='delenq'),
    path('viewfeedbacks',views.viewfeedbacks,name='viewfeedbacks'),
    path('delfeed/<id>',views.delfeed,name='delfeed'),
    path('viewcomplaints',views.viewcomplaints,name='viewcomplaints'),
    path('delcomp/<id>',views.delcomp,name='delcomp'),
    path('changeadminpassword/',views.changeadminpassword,name='changeadminpassword'),
    path('product/',views.product,name='product'),
    path('viewproducts',views.viewproducts,name='viewproducts'),
    path('delp/<id>',views.delp,name='delp'),
    path('viewcustorders/',views.viewcustorders,name='viewcustorders'),
]