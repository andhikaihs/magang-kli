from django.shortcuts import render
from input_agenda_setting.models import InputAgendaSetting

def statistic_agenda(request):
    jumlah_agenda_setting = InputAgendaSetting.objects.count()
    jumlah_postingan = InputAgendaSetting.objects.count()
    jumlah_postingan_sesuai_agenda = InputAgendaSetting.objects.filter(sesuai_agenda=True).count()

    context = {
        'jumlah_agenda_setting': jumlah_agenda_setting,
        'jumlah_postingan': jumlah_postingan,
        'jumlah_postingan_sesuai_agenda': jumlah_postingan_sesuai_agenda,
    }
    return render(request, 'statistic.html', context)
