from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('similarity-checker/', views.similarity_checker, name='similarity-checker'),
    path('roles/', views.roles, name='roles'),
    path('statistic/', views.statistic, name='statistic'),
]
