from django.contrib import admin
from .models import UploadAudio,UploadVideo,RatingAudio,RatingVideo,FavourateVideos,FavourateAudios
# Register your models here.
@admin.register(UploadVideo)
class AdminUploadVideo(admin.ModelAdmin):
    list_display=('id','PodcastName','SpeakerName','PodcastDescription','PodcastFile')
@admin.register(UploadAudio)
class AdminUploadAudio(admin.ModelAdmin):
    list_display=('id','PodcastName','SpeakerName','PodcastDescription','PodcastFile')

@admin.register(RatingAudio)
class AdminRatingAudio(admin.ModelAdmin):
    list_display=('rating','audio')
@admin.register(RatingVideo)
class AdminRatingVideo(admin.ModelAdmin):
    list_display=('rating','video')
@admin.register(FavourateAudios)
class AdminFavourateAudios(admin.ModelAdmin):
    list_display=('userid','audioid')
@admin.register(FavourateVideos)
class AdminFavourateVideos(admin.ModelAdmin):
    list_display=('userid','videoid')