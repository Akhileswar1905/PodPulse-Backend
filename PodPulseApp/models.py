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
class FavourateAudios(models.Model):
    userid=models.IntegerField()
    audioid=models.IntegerField()
class FavourateVideos(models.Model):
    userid=models.IntegerField()
    videoid=models.IntegerField()
class RatingAudio(models.Model):
    rating=models.IntegerField()
    audio=models.OneToOneField(to=UploadAudio,on_delete=models.CASCADE)
class RatingVideo(models.Model):
    rating=models.IntegerField()
    video=models.OneToOneField(to=UploadVideo,on_delete=models.CASCADE)
