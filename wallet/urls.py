from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('load/', views.load_money, name='load_money'),
    path('transfer/', views.transfer_money, name='transfer_money'),
    path('logout/', LogoutView.as_view(), name='logout'),
  
    
]
