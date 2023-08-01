import instaloader
from django.db.models import Q
from input_agenda_setting.models import InputAgendaSetting
from socmed_data.models import Instagram

def fetch_instagram_posts(account_url, start_date, end_date):
    loader = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(loader.context, account_url)

    posts = []
    for post in profile.get_posts():
        if start_date <= post.date <= end_date:
            post_info = {
                'caption': post.caption,
                'likes': post.likes,
                'comments': post.comments,
                'start_date': start_date,
                'end_date': end_date,
            }
            if post.is_video:
                post_info['viewers'] = post.video_view_count
            posts.append(post_info)

    return posts

def get_instagram_posts_by_agenda(nomor_agenda):
    try:
        agenda = InputAgendaSetting.objects.get(nomor_agenda=nomor_agenda)
        start_date = agenda.agenda_date_time_start
        end_date = agenda.agenda_date_time_end
        account_url = agenda.account_url

        posts = fetch_instagram_posts(account_url, start_date, end_date)
        return posts
    except InputAgendaSetting.DoesNotExist:
        return []

def get_instagram_posts_all():
    all_posts = []
    socmed_data_with_account_url = Instagram.objects.filter(Q(account_url__isnull=False) & ~Q(account_url=''), input_agenda_setting__isnull=False)
    for socmed_data in socmed_data_with_account_url:
        if socmed_data.input_agenda_setting:
            start_date = socmed_data.input_agenda_setting.agenda_date_time_start
            end_date = socmed_data.input_agenda_setting.agenda_date_time_end
            account_url = socmed_data.account_url

            posts = fetch_instagram_posts(account_url, start_date, end_date)
            all_posts.extend(posts)

    return all_posts

def get_instagram_posts_by_ue1(ue1):
    posts_by_ue1 = []
    socmed_data_with_account_url = Instagram.objects.filter(Q(account_url__isnull=False) & ~Q(account_url=''), input_agenda_setting__isnull=False, ue1=ue1)
    for socmed_data in socmed_data_with_account_url:
        if socmed_data.input_agenda_setting:
            start_date = socmed_data.input_agenda_setting.agenda_date_time_start
            end_date = socmed_data.input_agenda_setting.agenda_date_time_end
            account_url = socmed_data.account_url

            posts = fetch_instagram_posts(account_url, start_date, end_date)
            posts_by_ue1.extend(posts)

    return posts_by_ue1
