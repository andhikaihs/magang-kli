from django.db import models

class SimilarityChecker(models.Model):
    SIMILARITY_CHOICES = [
        ('Sesuai', 'Sesuai'), 
        ('Tidak Sesuai', 'Tidak Sesuai'),
    ]

    UE1_CHOICES = (
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

    SOCIAL_MEDIA_CHOICES = [
        ('Facebook', 'Facebook'),
        ('Instagram', 'Instagram'),
        ('Linkedin', 'Linkedin'),
        ('Tiktok', 'Tiktok'),
        ('Twitter', 'Twitter'),
        ('YouTube', 'YouTube'),
    ]

    ue1 = models.CharField(max_length=255, choices=UE1_CHOICES)
    social_media = models.CharField(max_length=20, choices=SOCIAL_MEDIA_CHOICES)
    account_url = models.URLField(max_length=200)
    post_url = models.URLField(max_length=200)
    captions = models.TextField()
    topik = models.CharField(max_length=255)
    pesan_kunci = models.CharField(max_length=255)
    sub_pesan_kunci = models.CharField(max_length=255)
    kesesuaian = models.CharField(max_length=50, choices=SIMILARITY_CHOICES)
    catatan = models.TextField(blank=True)
    checked_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.ue1} - {self.topik} - {self.account_url}"
