# Generated by Django 2.2.24 on 2021-07-12 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0002_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='sport',
            name='awarded',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sport',
            name='bronze',
            field=models.ManyToManyField(blank=True, related_name='_sport_bronze_+', to='sports.Athlete'),
        ),
        migrations.AddField(
            model_name='sport',
            name='gold',
            field=models.ManyToManyField(blank=True, related_name='_sport_gold_+', to='sports.Athlete'),
        ),
        migrations.AddField(
            model_name='sport',
            name='silver',
            field=models.ManyToManyField(blank=True, related_name='_sport_silver_+', to='sports.Athlete'),
        ),
        migrations.DeleteModel(
            name='Winner',
        ),
    ]
