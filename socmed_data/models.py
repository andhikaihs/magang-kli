from django.db import models
from input_agenda_setting.models import InputAgendaSetting

UE1_CHOICES = (
    ('All', 'All'),
    ('Kemenkeu', 'Kemenkeu'),
    ('Setjen', 'Setjen'),
    ('DJA', 'DJA'),
    ('DJP', 'DJP'),
    ('DJPPR', 'DJPPR'),
    ('DJPB', 'DJPB'),
    ('DJKN', 'DJKN'),
    ('DJBK', 'DJBK'),
    ('Itjen', 'Itjen'),
    ('DJBC', 'DJBC'),
    ('BKF', 'BKF'),
    ('BPPK', 'BPPK'),
    ('SMV', 'SMV'),
)

class SocmedData(models.Model):
    ue1 = models.CharField(max_length=255, choices=UE1_CHOICES)
    account_url = models.URLField()
    input_agenda_setting = models.ForeignKey(InputAgendaSetting, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ue1} - {self.account_url}"

class Instagram(SocmedData):
    pass

class Linkedin(SocmedData):
    pass

class Youtube(SocmedData):
    pass

class Tiktok(SocmedData):
    pass

class Facebook(SocmedData):
    pass

class Twitter(SocmedData):
    pass