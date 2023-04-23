from django.db import models

# Create your models here.
class UploadAudio(models.Model):
    PodcastName=models.CharField(max_length=200)
    SpeakerName=models.CharField(max_length=200)
    PodcastDescription=models.TextField(max_length=500)
    PodcastFile=models.FileField(upload_to='Aduio/')
class UploadVideo(models.Model):
    PodcastName=models.CharField(max_length=200)
    SpeakerName=models.CharField(max_length=200)
    PodcastDescription=models.TextField(max_length=500)
    PodcastFile=models.FileField(upload_to='Vedios/')
