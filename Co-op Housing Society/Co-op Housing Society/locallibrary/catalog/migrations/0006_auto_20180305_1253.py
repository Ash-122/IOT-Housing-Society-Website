# Generated by Django 2.0.2 on 2018-03-05 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20180228_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='society_registration',
            name='Society_name',
            field=models.CharField(help_text='Enter a Society name', max_length=100),
        ),
    ]
