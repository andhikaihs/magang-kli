from django.shortcuts import render, get_object_or_404
from .models import SocmedData, Instagram
from input_agenda_setting.models import InputAgendaSetting
from .utils import get_instagram_posts_by_agenda, get_instagram_posts_all, get_instagram_posts_by_ue1

def socmed_data(request):
    socmed_data_list = SocmedData.objects.all()
    context = {'socmed_data_list': socmed_data_list}
    return render(request, 'socmed_data.html', context)

def instagram_posts_by_agenda(request, nomor_agenda):
    posts = get_instagram_posts_by_agenda(nomor_agenda)
    context = {
        'posts': posts,
    }
    return render(request, 'instagram_posts.html', context)

def instagram_posts_all(request):
    posts = get_instagram_posts_all()
    context = {
        'posts': posts,
    }
    return render(request, 'instagram_posts.html', context)

def instagram_posts_by_ue1(request, ue1):
    # Get the start_date and end_date from the request query parameters (URL parameters)
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # Get the Instagram posts based on 'ue1', 'start_date', and 'end_date'
    posts = get_instagram_posts_by_ue1(ue1, start_date=start_date, end_date=end_date)

    context = {
        'ue1': ue1,
        'start_date': start_date,
        'end_date': end_date,
        'posts': posts,
    }
    return render(request, 'instagram_posts.html', context)
