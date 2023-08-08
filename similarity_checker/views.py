from django.shortcuts import render, redirect
from input_agenda_setting.models import InputAgendaSetting
from similarity_checker.models import SimilarityChecker
from django.contrib import messages
import pandas as pd
from django.http import HttpResponse
from socmed_data.models import SocialMediaData

def similarity_checker(request):
    if request.method == 'POST':
        print(request.POST)
        ue1 = request.POST.get('ue1')
        social_media = request.POST.get('social_media')
        account_url = request.POST.get('account_url')
        post_url = request.POST.get('post_url')
        captions = request.POST.get('captions')
        topik = request.POST.get('topik')
        pesan_kunci = request.POST.get('pesan_kunci')
        sub_pesan_kunci = request.POST.get('sub_pesan_kunci')
        kesesuaian = request.POST.get('kesesuaian')
        catatan = request.POST.get('catatan')

        # Save data to the database
        SimilarityChecker.objects.create(
            ue1=ue1,
            social_media=social_media,
            account_url=account_url,
            post_url=post_url,
            captions=captions,
            topik=topik,
            pesan_kunci=pesan_kunci,
            sub_pesan_kunci=sub_pesan_kunci,
            kesesuaian=kesesuaian,
            catatan=catatan,
        ) 
    return render(request, 'similarity-checker.html')

def accuracy_agenda(request):
    # Ambil data dari database berdasarkan range tanggal dari InputAgendaSetting
    agenda_setting = InputAgendaSetting.objects.first()  # Ganti dengan metode pemilihan agenda_setting yang sesuai
    start_date = agenda_setting.agenda_date_time_start
    end_date = agenda_setting.agenda_date_time_end
    posts = SocialMediaData.objects.filter(post_date_time__range=(start_date, end_date))

    # Proses data untuk mendapatkan jumlah kata-kata pesan_kunci dan sub_pesan_kunci dalam caption
    pesan_kunci = agenda_setting.pesan_kunci.split()
    sub_pesan_kunci = agenda_setting.sub_pesan_kunci.split()

    # Hitung seberapa banyak kata-kata tersebut muncul dalam setiap caption
    pesan_kunci_count = {word: 0 for word in pesan_kunci}
    sub_pesan_kunci_count = {word: 0 for word in sub_pesan_kunci}

    for post in posts:
        caption_words = post.caption.split()
        for word in pesan_kunci:
            pesan_kunci_count[word] += caption_words.count(word)
        for word in sub_pesan_kunci:
            sub_pesan_kunci_count[word] += caption_words.count(word)

    total_caption_count = len(posts)
    pesan_kunci_percentage = {word: count / total_caption_count * 100 for word, count in pesan_kunci_count.items()}
    sub_pesan_kunci_percentage = {word: count / total_caption_count * 100 for word, count in sub_pesan_kunci_count.items()}

    context = {
        'posts': posts,
        'pesan_kunci_count': pesan_kunci_count,
        'sub_pesan_kunci_count': sub_pesan_kunci_count,
        'pesan_kunci_percentage': pesan_kunci_percentage,
        'sub_pesan_kunci_percentage': sub_pesan_kunci_percentage,
    }
    return render(request, 'accuracy_agenda.html', context)

def download_excel(request):
    agenda_setting = InputAgendaSetting.objects.first()  # Ganti dengan metode pemilihan agenda_setting yang sesuai
    start_date = agenda_setting.agenda_date_time_start
    end_date = agenda_setting.agenda_date_time_end
    posts = SocialMediaData.objects.filter(post_date_time__range=(start_date, end_date))

    # Buat dataframe untuk data caption, likes, comments, dan viewers
    data = {
        'Caption': [post.caption for post in posts],
        'Likes': [post.likes for post in posts],
        'Comments': [post.comments for post in posts],
        'Viewers': [post.viewers for post in posts],
    }
    df = pd.DataFrame(data)

    # Simpan dataframe ke file Excel
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="social_media_posts.xlsx"'
    df.to_excel(response, index=False)

    return response
