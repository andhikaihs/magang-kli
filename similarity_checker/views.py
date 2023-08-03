from django.shortcuts import render, redirect
from similarity_checker.models import SimilarityChecker
from django.contrib import messages

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

        # messages.success(request, 'Similarity checked!')
        # return redirect('similarity_checker')

    # ue1_choices = SimilarityChecker.UE1_CHOICES
    # social_media_choices = SimilarityChecker.SOCIAL_MEDIA_CHOICES
    # kesesuaian_choices = SimilarityChecker.SIMILARITY_CHOICES
    # context = {
    #     'ue1_choices': ue1_choices,
    #     'social_media_choices': social_media_choices,
    #     'kesesuaian_choices': kesesuaian_choices,
    # }

    return render(request, 'similarity-checker.html')