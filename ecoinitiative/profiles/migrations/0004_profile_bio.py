# Generated by Django 4.2.7 on 2023-11-23 06:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]
