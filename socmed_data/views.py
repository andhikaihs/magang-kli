import datetime
from django.shortcuts import get_object_or_404, render
import requests
from input_agenda_setting.models import InputAgendaSetting
from socmed_data.models import SocialMediaData
from socmed_data.utils import scrape_instagram_data_webscrap, scrape_instagram_data_api
from requests_oauthlib import OAuth2Session
from requests_oauthlib.compliance_fixes import linkedin_compliance_fix
from input_agenda_setting.models import InputAgendaSetting
from socmed_data.models import LinkedInPost

"""
INSTAGRAM with Web Scrapping
"""
def instagram_detail_webscrap(request, ue1):
    agenda_setting = get_object_or_404(InputAgendaSetting)
    agenda_start = agenda_setting.agenda_date_time_start
    agenda_end = agenda_setting.agenda_date_time_end

    socmed_data = SocialMediaData.objects.filter(ue1=ue1, created_at__range=(agenda_start, agenda_end))

    for data in socmed_data:
        if data.social_media == 'Instagram':
            scraped_data = scrape_instagram_data_webscrap(data.account_url, agenda_start, agenda_end)
            data.captions = "\n".join(scraped_data['captions'])
            data.likes = scraped_data['likes']
            data.comments = scraped_data['comments']
            data.viewers = scraped_data['viewers']
            data.posts = scraped_data['posts']
            data.followers = scraped_data['followers']
            data.post_urls = scraped_data['post_urls']

    context = {
        'ue1': ue1,
        'agenda_start': agenda_start,
        'agenda_end': agenda_end,
        'socmed_data': socmed_data,
    }

    return render(request, 'instagram/instagram_detail_webscrap.html', context)

"""
INSTAGRAM with API Library
"""
def instagram_detail_api(request, ue1):
    agenda_setting = get_object_or_404(InputAgendaSetting)
    agenda_start = agenda_setting.agenda_date_time_start
    agenda_end = agenda_setting.agenda_date_time_end

    socmed_data = SocialMediaData.objects.filter(ue1=ue1, created_at__range=(agenda_start, agenda_end))

    for data in socmed_data:
        if data.social_media == 'Instagram':
            scraped_data = scrape_instagram_data_api(data.account_url, agenda_start, agenda_end)
            data.captions = "\n".join(scraped_data['captions'])
            data.likes = scraped_data['likes']
            data.comments = scraped_data['comments']
            data.viewers = scraped_data['viewers']
            data.posts = scraped_data['posts']
            data.followers = scraped_data['followers']
            data.post_urls = scraped_data['post_urls']

    context = {
        'ue1': ue1,
        'agenda_start': agenda_start,
        'agenda_end': agenda_end,
        'socmed_data': socmed_data,
    }

    return render(request, 'instagram/instagram_detail_api.html', context)


"""
LINKEDIN with OAuth2
"""
def fetch_linkedin_data_oauth2(request):
    agenda_setting = InputAgendaSetting.objects.get(id=2)

    agenda_start = agenda_setting.agenda_date_time_start
    agenda_end = agenda_setting.agenda_date_time_end

    # Informasi otentikasi
    client_id = "86gtvok96q2ah1"  # Ganti dengan Client ID dari LinkedIn Developer Network
    client_secret = "GXs7kpDvE8wjtfvt"  # Ganti dengan Client Secret dari LinkedIn Developer Network
    redirect_uri = "http://localhost:8000/linkedin-data/"  # URL callback sesuai dengan konfigurasi di Developer Network
    scope = ["r_organization_social"]

    # Session OAuth2
    linkedin = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)
    linkedin = linkedin_compliance_fix(linkedin)

    # URL untuk otentikasi
    authorization_url, state = linkedin.authorization_url("https://www.linkedin.com/oauth/v2/authorization")

    # Tampilkan URL otentikasi -> kirimkan pengguna ke URL tersebut
    print("Silakan kunjungi URL berikut untuk melakukan otentikasi:")
    print(authorization_url)

    # Jika pengguna sudah melakukan otentikasi dan mendapatkan kode otorisasi, lanjutkan proses pengambilan data
    if 'code' in request.GET:
        code = request.GET.get('code')

        # Menukar kode otorisasi dengan token akses
        token_url = "https://www.linkedin.com/oauth/v2/accessToken"
        token_data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': redirect_uri,
            'client_id': client_id,
            'client_secret': client_secret
        }

        # Kirim permintaan POST untuk menukar kode otorisasi dengan token akses
        response = linkedin.fetch_token(token_url, code=code, include_client_id=True, **token_data)

        # Dapatkan token akses dari respons
        access_token = response.get('access_token')

        # Gunakan token akses untuk mengakses endpoint API LinkedIn yang sesuai
        if access_token:
            # Ambil data jumlah followers dari halaman profil perusahaan menggunakan API LinkedIn
            followers_url = "https://api.linkedin.com/v2/organizationalEntityFollowerStatistics?q=organizationalEntity&organizationalEntity=urn:li:organization:kementerian-keuangan-republik-indonesia"
            headers = {
                'Authorization': f'Bearer {access_token}'
            }
            followers_response = requests.get(followers_url, headers=headers)
            if followers_response.status_code == 200:
                followers_data = followers_response.json()
                jumlah_followers = followers_data['elements'][0]['totalFollowers']
                agenda_setting.jumlah_followers = jumlah_followers

            context = {}

            # Ambil data total postingan dari halaman profil perusahaan menggunakan API LinkedIn
            total_posts_url = "https://api.linkedin.com/v2/organizationalEntityShareStatistics?q=organizationalEntity&organizationalEntity=urn:li:organization:kementerian-keuangan-republik-indonesia"
            total_posts_response = requests.get(total_posts_url, headers=headers)
            if total_posts_response.status_code == 200:
                total_posts_data = total_posts_response.json()
                total_postingan = total_posts_data['elements'][0]['totalShareStatistics']['shareCount']
                agenda_setting.total_postingan = total_postingan

            # Simpan data jumlah followers dan total postingan ke model InputAgendaSetting
            agenda_setting.save()

            # Add the total_postingan to the context dictionary
            context['total_postingan'] = total_postingan

            # Ambil data postingan dari kurun waktu agenda setting
            posts_url = "https://api.linkedin.com/v2/ugcPosts?q=authors&authors=urn:li:organization:kementerian-keuangan-republik-indonesia"
            headers = {
                'Authorization': f'Bearer {access_token}'
            }

            posts_response = requests.get(posts_url, headers=headers)
            if posts_response.status_code == 200:
                posts_data = posts_response.json()
                for post in posts_data['elements']:
                    post_id = post['id']
                    caption = post['specificContent']['com.linkedin.ugc.ShareContent']['shareCommentary']['text']
                    reactions = post['totalSocialActivity']['likes'] + post['totalSocialActivity']['comments']
                    post_date_time = datetime.datetime.fromtimestamp(post['created']).astimezone()
                    LinkedInPost.objects.create(post_id=post_id, caption=caption, reactions=reactions, post_date_time=post_date_time)
            
            return render(request, "linkedin/data_linkedin.html", context)
        else:
            return render(request, "linkedin/error_linkedin.html")

    return render(request, "linkedin/authorization_linkedin.html", {'authorization_url': authorization_url})

"""
LINKEDIN without OAuth2
"""
def fetch_linkedin_data(request):
    agenda_setting = InputAgendaSetting.objects.get(id=2)

    # Get the agenda start and end date
    agenda_start = agenda_setting.agenda_date_time_start
    agenda_end = agenda_setting.agenda_date_time_end

    # Fetch LinkedIn data without authorization (replace kementerian-keuangan-republik-indonesia with your actual LinkedIn organization ID)
    followers_url = f"https://www.linkedin.com/company/86gtvok96q2ah1?viewAsMember=true"
    followers_response = requests.get(followers_url)
    if followers_response.status_code == 200:
        followers_data = followers_response.json()
        jumlah_followers = followers_data['elements'][0]['totalFollowers']
        agenda_setting.jumlah_followers = jumlah_followers

    total_posts_url = f"https://www.linkedin.com/company/86gtvok96q2ah1?viewAsMember=true"
    total_posts_response = requests.get(total_posts_url)
    if total_posts_response.status_code == 200:
        total_posts_data = total_posts_response.json()
        total_postingan = total_posts_data['elements'][0]['totalShareStatistics']['shareCount']
        agenda_setting.total_postingan = total_postingan
    else:
        print("Error fetching total posting count:")
        print(f"Status Code: {total_posts_response.status_code}")
        print(f"Response Content: {total_posts_response.content}")
        total_postingan = None

    agenda_setting.save()

    # Fetch posts within the specified time range
    posts_url = f"https://www.linkedin.com/company/kementerian-keuangan-republik-indonesia?viewAsMember=true"
    posts_response = requests.get(posts_url)
    if posts_response.status_code == 200:
        posts_data = posts_response.json()
        for post in posts_data['elements']:
            post_id = post['id']
            caption = post['specificContent']['com.linkedin.ugc.ShareContent']['shareCommentary']['text']
            reactions = post['totalSocialActivity']['likes'] + post['totalSocialActivity']['comments']
            post_date_time = datetime.datetime.fromtimestamp(post['created']).astimezone()
            # Save post data to LinkedInPost model (you may adjust this based on your app logic)
            LinkedInPost.objects.create(post_id=post_id, caption=caption, reactions=reactions, post_date_time=post_date_time)

    context = {
        'agenda_setting': agenda_setting,
        'total_postingan': total_postingan,
    }
    return render(request, "linkedin/data_linkedin.html", context)