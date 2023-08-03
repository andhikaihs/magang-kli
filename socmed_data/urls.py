from django.urls import path
from . import views

urlpatterns = [
    path('instagram-posts/', views.instagram_posts_all, name='instagram_posts_all'),
    path('instagram-posts/<str:ue1>/', views.instagram_posts_by_ue1, name='instagram_posts_by_ue1'),
    path('instagram-posts/agenda/<int:nomor_agenda>/', views.instagram_posts_by_agenda, name='instagram_posts_by_agenda'),
]