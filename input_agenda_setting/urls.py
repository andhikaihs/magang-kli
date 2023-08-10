from django.urls import path
from . import views

urlpatterns = [
    path('input-agenda-setting/', views.input_as, name='input-as'),
    path('data-input-agenda-setting/', views.table_input_as, name='table_input_as'),
    path('edit-agenda-setting/<int:id>', views.edit_agenda_setting, name='edit_agenda_setting')
]
