# Generated by Django 4.1 on 2022-08-24 11:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tutorial",
            name="tutorial_published",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 24, 13, 27, 35, 240248),
                verbose_name="date published",
            ),
        ),
    ]