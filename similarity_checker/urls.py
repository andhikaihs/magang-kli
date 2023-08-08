from django.urls import path
from . import views

urlpatterns = [
    path('similarity-checker/', views.similarity_checker, name='similarity-checker'),
    path('accuracy-agenda/', views.accuracy_agenda, name='accuracy-agenda'),
    path('download-excel/', views.download_excel, name='download-excel'),
]