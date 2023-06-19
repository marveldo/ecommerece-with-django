from base import views
from django.urls import path


urlpatterns = [
    path('',views.home, name= 'home'),
    path('reviews/', views.reviews, name = 'reviews'),
    path('theteam/', views.Theteam , name = 'Theteam'),
    path('shop/' , views.shop , name = 'shop'),
    path('buyproduct/<str:pk>', views.bookonline, name= 'bookonline'),
    path('shoppingbag/', views.shoppingbag, name= 'shoppingbag'),
    path('login/', views.customerlogin, name = 'login'),
    path('logout/', views.logoutcustomer, name = 'logout'),
    path('registeruser/', views.registerCustomer, name= 'register'),
    path('changeproduct/',views.changeproduct, name = 'changeproduct'),
    path('checkout/', views.checkout, name = 'checkout' ),
    path('orders/', views.Pendingorders, name = 'orders'),
    path('Completeorder/', views.Completeorders),
    path('Create/', views.Createitems, name = 'createitems'),
    path('Update/<str:pk>/', views.Updateitems, name= 'update'),
    path('delete/', views.deleteitems)

    
]