from django.shortcuts import render, get_object_or_404
from .models import SocmedData, Instagram
from input_agenda_setting.models import InputAgendaSetting
from .utils import *

def socmed_data(request):
    socmed_data_list = SocmedData.objects.all()
    context = {'socmed_data_list': socmed_data_list}
    return render(request, 'socmed_data.html', context)

def instagram_posts_by_ue1(request):
    ue1 = request.GET.get('ue1', 'All')
    if ue1 == 'All':
        posts = get_instagram_posts_all()
    else:
        posts = get_instagram_posts_by_ue1(ue1)

    context = {
        'posts': posts,
    }
    return render(request, 'instagram_posts.html', context)
