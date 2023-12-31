# Generated by Django 4.2.7 on 2023-12-30 15:50

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tugoingewa', '0012_delete_initiative'),
    ]

    operations = [
        migrations.CreateModel(
            name='Initiative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('initiative_image', sorl.thumbnail.fields.ImageField(upload_to='')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('goals', ckeditor.fields.RichTextField()),
                ('organiser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='initiative_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
