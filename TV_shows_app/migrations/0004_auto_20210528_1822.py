# Generated by Django 2.2 on 2021-05-29 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TV_shows_app', '0003_auto_20210528_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.DateField(null=True),
        ),
    ]
