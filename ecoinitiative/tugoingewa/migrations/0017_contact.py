# Generated by Django 4.2.7 on 2023-12-31 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tugoingewa', '0016_alter_initiative_organiser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
    ]
