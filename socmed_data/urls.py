from django.urls import path
from . import views

urlpatterns = [
    # PATH IG API LIBRARY (jangan dihapus)
    path('social-media/instagram/<str:ue1>/', views.instagram_detail_api, name='instagram_detail_api'),
    # PATH IG WEB SCRAP (jangan dihapus)
    # path('social-media/instagram/<str:ue1>/', views.instagram_detail_webscrap, name='instagram_detail_webscrap'),

    path('social-medial/linkedin/', views.fetch_linkedin_data, name='linkedin_data_detail'),

    # PATH TWITTER, TIKTOK, FACEBOOK (jangan dihapus)
#     path('social-medial/twitter/<str:ue1>/', name='twitter_data_detail'),
#     path('social-medial/tiktok/<str:ue1>', name='tiktok_data_detail'),
#     path('social-medial/facebook/<str:ue1>/', name='facebook_data_detail'),
]