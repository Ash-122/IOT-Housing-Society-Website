# Generated by Django 2.0.2 on 2018-02-28 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20180228_1648'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Complaints',
            new_name='Complaint',
        ),
    ]
