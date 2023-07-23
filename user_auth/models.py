from django.db import models
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