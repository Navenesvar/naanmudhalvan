# Generated by Django 5.0.4 on 2024-04-06 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0003_song_credit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('channel_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000)),
                ('music', models.CharField(max_length=100000000)),
            ],
        ),
    ]