# Generated by Django 2.0.2 on 2018-03-05 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20180305_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='Complaint_No',
            field=models.CharField(help_text='Enter a Society ID', max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='member_registration',
            name='Member_ID',
            field=models.CharField(help_text='Enter a Society ID', max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='notice',
            name='Notice_No',
            field=models.CharField(help_text='Enter a Society ID', max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rent_registration',
            name='Rent_ID',
            field=models.CharField(help_text='Enter a Society ID', max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='society_registration',
            name='Society_ID',
            field=models.CharField(help_text='Enter a Society ID', max_length=10, primary_key=True, serialize=False),
        ),
    ]
