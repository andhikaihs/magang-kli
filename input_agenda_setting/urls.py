from django.urls import path
from . import views

urlpatterns = [
    path('input-agenda-setting/', views.input_as, name='input-as'),
]
