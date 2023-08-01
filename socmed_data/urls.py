from django.urls import path
from . import views

urlpatterns = [
    path('socmed-data/', views.socmed_data, name='socmed_data'),
    path('instagram-posts/ue1/<str:ue1>/', views.instagram_posts_by_ue1, name='instagram_posts_by_ue1'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('socmed-data/', views.socmed_data, name='socmed_data'),
    path('instagram-posts/', views.instagram_posts_by_ue1, name='instagram_posts_by_ue1'),
]
