from django.db import models
from django.utils import timezone
import uuid

class CustomUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('petugas_monitor', 'Petugas Monitor'),
        ('petugas_agenda', 'Petugas Agenda'),
    )

    full_name = models.CharField(max_length=100)
    nip = models.CharField(max_length=20)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.email
    
    """
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(User, self).save(*args, **kwargs)
    
    
    INSERT INTO `user_auth_user` (`id`, `full_name`, `nip`, `role`, `email`, `password`, `created`, `modified`, `verification`) VALUES
    (9, 'input', '1', 'Petugas Input Agenda Setting', 'input@admin.com', 'pbkdf2_sha256$600000$XeXpL5T0H09SyTvtGrlBuR$cPb1vBAHf3ps336fhtHMjZziUtL9hPrdi1jNp2dK51s=', '2023-07-17 16:04:58.945096', '2023-07-17 16:04:58.945096', 'false'),
    (10, 'monitor', '2', 'Petugas Monitor', 'monitor@admin.com', 'pbkdf2_sha256$600000$LgO7iFYnXniopY9IDNKBUg$am1xBFae3W9sfBxLvIMVjsv4jk2431+DMyMMa88SL98=', '2023-07-17 16:05:11.910046', '2023-07-17 16:05:11.910046', 'false'),
    (11, 'input2', '3', 'Petugas Input Agenda Setting', 'input2@admin.com', 'pbkdf2_sha256$600000$opbJ8A3pxQnsGFndVqT4aC$Perhk4YSMjrdqeZ3jIOEIoFCttIYW8KOPYWFx3qBPS8=', '2023-07-17 16:05:34.188313', '2023-07-17 16:05:34.188313', 'false'),
    (12, 'monitor2', '4', 'Petugas Monitor', 'monitor2@admin.com', 'pbkdf2_sha256$600000$QkmVXtZGvt6RwOiN76Xz3l$KM9xm3+z5SgINbLgA9vMcgZ+Mh6TZRk7c8sLTx+v63U=', '2023-07-17 16:05:50.950572', '2023-07-17 16:05:50.950572', 'false');
    (1, 'admin', '1', 'admin', 'admin@kemenkeu.com', 'pbkdf2_sha256$600000$RR7yVJRt5qBPJ41tb1Y9vG$h3DFlw/N7oSpNI5sQaAmuxoDpwEf5ixoM/TzESrI/Kc=', '2023-07-17 13:56:08.453226', '2023-07-17 13:56:08.453226', 'true'),
    """