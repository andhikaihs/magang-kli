from django.urls import path
from . import views

urlpatterns = [
    path('similarity-checker/', views.similarity_checker, name='similarity-checker'),
]
