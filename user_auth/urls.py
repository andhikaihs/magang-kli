from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('forget_password/', views.forget_password, name='forget_password'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('reset_password/<uidb64>/<token>/', views.reset_password_confirm, name='reset_password_confirm'),
]
