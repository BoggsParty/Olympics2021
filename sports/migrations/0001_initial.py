# Generated by Django 2.2.24 on 2021-07-11 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(default='', help_text='Full name', max_length=200)),
                ('abbreviation', models.CharField(default='', help_text='3 letter abbreviation', max_length=3)),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('sport_name', models.CharField(default='', max_length=200)),
                ('slug', models.SlugField(default='')),
                ('lock_date', models.DateField()),
                ('award_date', models.DateField()),
                ('locked', models.BooleanField(default=False)),
                ('sport_description', models.TextField(default='Sport Description')),
                ('scoring', models.TextField(default='score')),
                ('favorite', models.TextField(default='favorites')),
                ('competition_dates', models.TextField(default='dates')),
                ('rankings_url', models.URLField(blank=True, help_text='The official website rankings list.')),
                ('menu_image', models.ImageField(blank=True, upload_to='')),
                ('winner_type', models.CharField(choices=[('IN', 'Individual'), ('TM', 'Team')], default='TM', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Sport_Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('alt', models.CharField(default='', max_length=100)),
                ('active', models.BooleanField(default=False, help_text='All active will display.')),
                ('image_attribute', models.CharField(blank=True, default='', max_length=200)),
                ('image_source', models.URLField(blank=True, default='')),
                ('sport', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='sport+', to='sports.Sport')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('athlete_name', models.CharField(default='', help_text='Full Name', max_length=200)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='country+', to='sports.Country')),
                ('sports', models.ManyToManyField(blank=True, related_name='_athlete_sports_+', to='sports.Sport')),
            ],
        ),
    ]
