# Generated by Django 2.0.2 on 2018-02-28 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_name', models.CharField(help_text='Enter a author name', max_length=20)),
                ('author_gender', models.CharField(help_text='Enter author gender', max_length=2)),
                ('author_id', models.IntegerField(max_length=20, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['author_name'],
            },
        ),
    ]