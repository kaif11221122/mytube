# Generated by Django 4.0.6 on 2022-07-17 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0003_remove_video_channel_video_channel_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='channel_id',
            field=models.CharField(max_length=40),
        ),
    ]
