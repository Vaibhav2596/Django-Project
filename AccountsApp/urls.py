from django.contrib import admin
from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.home,name="home"),
    path('products/', v.products,name="products"),
    path('customer/<str:pk>', v.customer,name="customer"),

    path('create_order/<str:pk>',v.createOrder,name="create_order"),
    path('update_order/<int:pk>/',v.updateOrder,name="update_order"),
    path('delete_order/<str:pk>/',v.deleteOrder,name="delete_order"),

    path('register/', v.registerPage,name="register"),
    path('login/', v.loginPage,name="login"),
    path('logout/', v.logoutUser,name="logout"),

    path('user/', v.userPage,name="user-page"),
    path('account/',v.accountSettings,name='account'),


]
