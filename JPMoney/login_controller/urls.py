from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  
from django.conf.urls import url 

urlpatterns = [
    path('login/', views.login),
    path('auth/', views.auth_view),       
    path('logout/', views.logout),       
    path('loggedin/', views.loggedin),       
    path('invalidlogin/', views.invalidlogin),  
] 
 
 