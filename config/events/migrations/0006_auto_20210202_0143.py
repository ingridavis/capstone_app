# Generated by Django 3.1.4 on 2021-02-02 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_event_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('food', 'FOOD'), ('jewelry', 'JEWELRY'), ('produce', 'PRODUCE'), ('clothing', 'CLOTHING'), ('yardsale', 'YARDSALE'), ('other', 'OTHER')], default='other', max_length=10),
        ),
    ]
