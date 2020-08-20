# Generated by Django 3.0.9 on 2020-08-05 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0004_auto_20200804_0538'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='start_url',
            field=models.URLField(blank=True, null=True, verbose_name='link for the Host to start the Meeting'),
        ),
    ]