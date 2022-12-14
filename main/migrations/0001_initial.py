# Generated by Django 4.1 on 2022-09-02 17:08

import datetime
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TutorialCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial_category', models.CharField(max_length=200)),
                ('category_summary', models.CharField(max_length=200)),
                ('category_slug', models.CharField(default=1, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='TutorialSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial_series', models.CharField(max_length=200)),
                ('series_summary', models.CharField(max_length=200)),
                ('tutorial_category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.tutorialcategory', verbose_name='Category')),
            ],
            options={
                'verbose_name_plural': 'Series',
            },
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial_title', models.CharField(max_length=200)),
                ('tutorial_content', tinymce.models.HTMLField()),
                ('tutorial_published', models.DateTimeField(default=datetime.datetime(2022, 9, 2, 19, 8, 44, 787568), verbose_name='date published')),
                ('tutorial_slug', models.CharField(default=1, max_length=200)),
                ('tutorial_series', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.tutorialseries', verbose_name='Series')),
            ],
        ),
    ]
