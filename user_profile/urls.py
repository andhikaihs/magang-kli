from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    #path('profile/update/', views.update_profile, name='update_profile'),
    path('similarity-checker/', views.similarity_checker, name='similarity-checker'),
    path('roles/', views.roles, name='roles'),
    path('input-as/', views.input_as, name='input-as'),
    path('statistic/', views.statistic, name='statistic'),
]
