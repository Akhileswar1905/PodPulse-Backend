# Generated by Django 4.2 on 2023-04-24 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PodPulseApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavourateAudios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('audioid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FavourateVideos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('videoid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RatingVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('video', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='PodPulseApp.uploadvideo')),
            ],
        ),
        migrations.CreateModel(
            name='RatingAudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('audio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='PodPulseApp.uploadaudio')),
            ],
        ),
    ]