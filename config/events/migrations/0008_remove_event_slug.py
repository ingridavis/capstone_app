# Generated by Django 3.1.4 on 2021-02-06 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20210202_0151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='slug',
        ),
    ]
