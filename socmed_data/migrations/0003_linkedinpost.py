# Generated by Django 4.1.7 on 2023-08-06 18:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('socmed_data', '0002_socialmediadata_captions_socialmediadata_comments_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkedInPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=200, unique=True)),
                ('captions', models.TextField(blank=True, null=True)),
                ('reactions', models.IntegerField(blank=True, default=0, null=True)),
                ('post_date_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]