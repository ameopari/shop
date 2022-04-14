"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from .views import *
from Home import views
from Home.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
# from .forms import LoginForm


urlpatterns = [
    path('home/',views.home,name='home'),
    path('register',Register.as_view(),name='register'),
    path('login',views.Login.as_view(),name='login'),
    path('logout',views.LogoutView.as_view(),name='logout'),
    path('index',views.index,name='index'),
    path('add',views.Addproduct.as_view(),name='add'),
    path('show',views.Show,name='show'),
    path('cat',views.Cate,name='cat'),
    path('update/<int:id>',views.upd,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('addtocart/',addtocart.as_view(),name='addtocart'),
    path('showproduct',views.ShowProduct.as_view(),name='showproduct'),
    path('payment',views.Payment.as_view(),name='payment')
]



