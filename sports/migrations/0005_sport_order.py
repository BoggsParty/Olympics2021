# Generated by Django 2.2.24 on 2021-07-14 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0004_auto_20210712_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='sport',
            name='order',
            field=models.IntegerField(default=100),
        ),
    ]
