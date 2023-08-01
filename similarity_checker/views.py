import datetime
from django.shortcuts import render
from .models import InstagramCaption, InstagramAccount
from input_agenda_setting.models import InputAgendaSetting

def similarity_checker(request):
    if request.method == 'POST':
        agenda_date_time = request.POST.get('agenda_date_time')
        agenda_date_time = datetime.datetime.strptime(agenda_date_time, '%Y-%m-%d %H:%M:%S')

        account_urls = [
            'https://www.instagram.com/smindrawati/',
            'https://www.instagram.com/suahasil/',
            'https://www.instagram.com/frans1108/',
            'https://www.instagram.com/yonarsal/',
            'https://www.instagram.com/andinhadiyanto/',
            -----------
            'https://www.instagram.com/setjenkemenkeu/',
            'https://www.instagram.com/rocankeu.kemenkeu/',
            'https://www.instagram.com//organta_setjen/',
            'https://www.instagram.com/rokum.kemenkeu//',
            'https://www.instagram.com/biroadvokasi/',
            'https://www.instagram.com/birosdmkemenkeu/',
            'https://www.instagram.com/pastikanasetkita/',
            'https://www.instagram.com//ppk_kemenkeu/',
            'https://www.instagram.com/pusintek.kemenkeu/',
            'https://www.instagram.com/set.pp_kemenkeuri/',
            'https://www.instagram.com/kneks.id/',
            'https://www.instagram.com/gkn.bandaaceh/',
            'https://www.instagram.com/gknjayapura/',
            'https://www.instagram.com/gknkupang/',
            'https://www.instagram.com/gkn_palembang/',
            'https://www.instagram.com/gknsingaraja/',
        ]

        for account_url in account_urls:
            account, created = InstagramAccount.objects.get_or_create(account_url=account_url)

            instagram_caption = InstagramCaption(
                account=account,
                agenda_date_time=agenda_date_time,
                agenda=InputAgendaSetting.objects.filter(agenda_date_time=agenda_date_time).first(),
            )
            instagram_caption.fetch_and_save_captions()

    captions = InstagramCaption.objects.all()
    context = {
        'captions': captions
    }

    return render(request, 'similarity-checker.html', context)
