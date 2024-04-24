from django.urls import path
from store import views
urlpatterns = [
    path('home/', views.home.as_view(),name="home"),
    path('prod/<int:pk>', views.Productview.as_view(),name="prod"),
    path('proddetail/<int:pk>', views.proddetailview.as_view(),name="proddetail"),
    path('reg/', views.Registerview.as_view(),name="reg"),
    path('', views.Loginview.as_view(),name="login"),
    path('logout/', views.signout.as_view(),name="logout"),
    path('cart/<int:pk>', views.addtocartview.as_view(),name="cart"),
    path('cartview1/', views.cartview.as_view(),name="cartview1"),
    path('cartdel/<int:pk>', views.cartdelview.as_view(),name="cartdel"),
    path('order/<int:pk>', views.orderview.as_view(),name="order"),
    path('orderlist/', views.orderlist.as_view(),name="orderlist"),
    path('orderdel/', views.removeorder.as_view(),name="orderdel"),
    
]
