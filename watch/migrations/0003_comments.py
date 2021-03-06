# Generated by Django 4.0.6 on 2022-07-20 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0005_video_info_delete_video'),
        ('watch', '0002_dislikes'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(max_length=500)),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch.comments')),
                ('video_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='channel.video_info')),
            ],
        ),
    ]
