# Generated by Django 3.2.25 on 2025-02-13 23:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accommodation', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='accommodationreview',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='favorite_reviews', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='accommodationreview',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_reviews', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='accommodationreview',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accommodation_reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]
