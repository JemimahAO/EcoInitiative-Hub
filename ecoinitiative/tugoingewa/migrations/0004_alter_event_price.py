# Generated by Django 4.2.7 on 2023-11-20 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tugoingewa', '0003_remove_event_pice_event_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
