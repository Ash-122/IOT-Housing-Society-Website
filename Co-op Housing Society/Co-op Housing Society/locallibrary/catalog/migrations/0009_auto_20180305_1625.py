# Generated by Django 2.0.2 on 2018-03-05 10:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20180305_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member_registration',
            name='Member_ID',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for the Member', primary_key=True, serialize=False),
        ),
    ]
