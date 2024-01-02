# Generated by Django 4.2.7 on 2023-12-30 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tugoingewa', '0013_initiative'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('initiative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='tugoingewa.initiative')),
            ],
        ),
    ]