from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('role/', views.role, name='role'),
    path('role/delete/', views.delete, name='delete'),
    path('role/verification/', views.verification, name='verification'),
]
