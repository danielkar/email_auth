# Generated by Django 3.1.2 on 2020-10-08 20:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailkey',
            name='expiry_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 8, 20, 7, 48, 920320, tzinfo=utc)),
        ),
    ]