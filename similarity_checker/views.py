import json
from django.shortcuts import get_object_or_404, render, redirect
from input_agenda_setting.models import InputAgendaSetting
from similarity_checker.models import SimilarityChecker
from django.contrib import messages
import pandas as pd
from django.http import HttpResponse, JsonResponse
from socmed_data.models import SocialMediaData
from socmed_data.utils import scrape_instagram_data_api
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.metrics import jaccard_distance

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


"""
SIMILARITY ACCURACY
"""
def calculate_similarity(text1, text2):
    # Tokenize the texts
    tokens1 = set(word_tokenize(text1.lower()))
    tokens2 = set(word_tokenize(text2.lower()))

    # Remove stop words
    stop_words = set(stopwords.words("indonesian"))
    tokens1 = tokens1 - stop_words
    tokens2 = tokens2 - stop_words

    # Calculate Jaccard similarity
    intersection = len(tokens1.intersection(tokens2))
    union = len(tokens1) + len(tokens2) - intersection
    jaccard_similarity = intersection / union

    # Convert similarity to percentage
    similarity_percentage = jaccard_similarity * 100

    return similarity_percentage

def agenda_accuracy(request, ue1):
    agenda_setting = get_object_or_404(InputAgendaSetting)
    agenda_start = agenda_setting.agenda_date_time_start
    agenda_end = agenda_setting.agenda_date_time_end

    stop_words = set(stopwords.words("indonesian"))

    socmed_data = SocialMediaData.objects.filter(ue1=ue1, created_at__range=(agenda_start, agenda_end))

    labels_graph = []
    data_graph = []

    for socmed_item in socmed_data:
        scraped_data = scrape_instagram_data_api(socmed_item.account_url, agenda_start, agenda_end)
        socmed_item.captions = "\n".join(scraped_data.get('captions', []))
        socmed_item.post_urls = scraped_data.get('post_urls', [])
        captions = socmed_item.captions.split('\n')  # Split captions into a list
        post_urls = socmed_item.post_urls

        print("list captions: ", captions)
        print("list posts: ", post_urls)

        for post_url, caption in zip(post_urls, captions):
            caption_tokens = set(word_tokenize(caption.lower())) - stop_words
            pesan_kunci_tokens = set(word_tokenize(agenda_setting.pesan_kunci.lower())) - stop_words
            similarity = 1 - jaccard_distance(caption_tokens, pesan_kunci_tokens)
            
            labels_graph.append(post_url)
            data_graph.append(similarity) 

    # Calculate average similarity after the loop
    if len(data_graph) > 0:
        average_similarity_graph = sum(data_graph) / len(data_graph)
        print("avg sim graph: ", average_similarity_graph)
    else:
        average_similarity_graph = 0.0
        print("avg is 0.0")

    context = {
        'agenda_setting': agenda_setting,
        'ue1': ue1,
        'average_similarity': average_similarity_graph,
        'labels_json': json.dumps(labels_graph),
        'data_json': json.dumps(data_graph),
    }

    return render(request, 'text_similarity_ue1.html', context)

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
