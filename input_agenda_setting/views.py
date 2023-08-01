from django.shortcuts import render
from .models import InputAgendaSetting

def input_as(request):
    if request.method == 'POST':
        nomor_agenda = request.POST.get('nomor_agenda')
        topik_agenda = request.POST.get('topik_agenda')
        pesan_kunci = request.POST.get('pesan_kunci')
        sub_pesan_kunci = request.POST.get('sub_pesan_kunci')
        
        # Ambil rentang tanggal dan waktu dari form
        rentang_tanggal_waktu = request.POST.get('agenda_date_time')
        tanggal_awal, tanggal_akhir = rentang_tanggal_waktu.split(' to ')

        InputAgendaSetting.objects.create(
            nomor_agenda=nomor_agenda,
            topik_agenda=topik_agenda,
            pesan_kunci=pesan_kunci,
            sub_pesan_kunci=sub_pesan_kunci,
            agenda_date_time_start=tanggal_awal,
            agenda_date_time_end=tanggal_akhir, 
        )

    return render(request, 'input-as.html')
