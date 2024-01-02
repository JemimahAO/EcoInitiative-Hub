# Generated by Django 4.2.7 on 2023-11-19 13:01

import ckeditor.fields
from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('event_image', sorl.thumbnail.fields.ImageField(upload_to='images/events')),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('event_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('pice', models.IntegerField()),
                ('description', ckeditor.fields.RichTextField()),
                ('location', models.CharField(max_length=255)),
            ],
        ),
    ]