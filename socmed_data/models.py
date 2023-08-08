from django.db import models
from django.utils import timezone

class SocialMediaData(models.Model):
    SOCIAL_MEDIA_CHOICES = (
        ('Instagram', 'Instagram'),
        ('Facebook', 'Facebook'),
        ('Linkedin', 'Linkedin'),
        ('Tiktok', 'Tiktok'),
        ('Twitter', 'Twitter'),
        ('YouTube', 'YouTube'),
    )
    
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
    account_url = models.URLField()
    social_media = models.CharField(max_length=20, choices=SOCIAL_MEDIA_CHOICES)
    ue1 = models.CharField(max_length=50, choices=UE1_CHOICES)
    captions = models.TextField(null=True, blank=True)
    likes = models.IntegerField(null=True, blank=True)
    comments = models.IntegerField(null=True, blank=True)
    viewers = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.social_media} - {self.ue1}"
    
class LinkedInPost(models.Model):
    post_id = models.CharField(max_length=200, unique=True)
    captions = models.TextField(null=True, blank=True)
    reactions = models.IntegerField(default=0, null=True, blank=True)
    post_date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"LinkedIn Post {self.post_id}"