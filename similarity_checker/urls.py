from django.urls import path
from . import views

urlpatterns = [
    path('similarity-checker/', views.similarity_checker, name='similarity-checker'),
    path('agenda-accuracy/<str:ue1>/', views.agenda_accuracy, name='agenda_accuracy'),
    path('download-excel/', views.download_excel, name='download-excel'),
]