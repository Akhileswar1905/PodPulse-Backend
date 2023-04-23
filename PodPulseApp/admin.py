from django.contrib import admin
from .models import UploadAudio,UploadVideo
# Register your models here.
@admin.register(UploadVideo)
class AdminUploadVideo(admin.ModelAdmin):
    list_display=('PodcastName','SpeakerName','PodcastDescription','PodcastFile')
@admin.register(UploadAudio)
class AdminUploadAudio(admin.ModelAdmin):
    list_display=('PodcastName','SpeakerName','PodcastDescription','PodcastFile')