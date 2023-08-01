from django.db import models
from input_agenda_setting.models import InputAgendaSetting
from instaloader import Instaloader, Profile

class InstagramAccount(models.Model):
    account_url = models.URLField()

    def __str__(self):
        return self.account_url

class InstagramCaption(models.Model):
    account = models.ForeignKey(InstagramAccount, on_delete=models.CASCADE)
    caption = models.TextField(blank=True)  # Allow empty caption
    posted_date_time = models.DateTimeField(blank=True, null=True)  # Allow empty posted_date_time
    agenda = models.ForeignKey(InputAgendaSetting, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.account} - {self.agenda.topik_agenda}"

    def fetch_and_save_captions(self):
        loader = Instaloader()
        profile = Profile.from_username(loader.context, self.account.account_url)

        for post in profile.get_posts():
            if post.date_local <= self.agenda.agenda_date_time:
                caption_text = post.caption
                if caption_text:
                    self.caption = caption_text
                    self.posted_date_time = post.date_local
                    self.save()
                    break
