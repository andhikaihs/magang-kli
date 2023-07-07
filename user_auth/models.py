from django.db import models

class User(models.Model):
    ROLE_CHOICES = [
        ('petugas_monitor', 'Petugas Monitor'),
        ('petugas_input_agenda_setting', 'Petugas Input Agenda Setting'),
    ]
        
    full_name = models.CharField(max_length=255)
    nip = models.CharField(max_length=30)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    
    def __str__(self):
        return self.full_name
