# Generated by Django 4.0.6 on 2022-07-20 10:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0005_video_info_delete_video'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('watch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dislikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='channel.video_info')),
            ],
        ),
    ]
