# Generated by Django 2.0.2 on 2018-03-28 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_auto_20180327_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='member_registration',
            name='Main_amount',
            field=models.IntegerField(default='3000', editable=False),
        ),
        migrations.AddField(
            model_name='member_registration',
            name='No_of_rooms',
            field=models.IntegerField(default='2', help_text='Enter the number of rooms you have'),
        ),
    ]