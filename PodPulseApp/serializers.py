from rest_framework import serializers
from django.contrib.auth.models import User
from .models import  UploadAudio,UploadVideo,RatingAudio,RatingVideo,FavourateAudios,FavourateVideos
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user
class UploadAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model=UploadAudio
        fields=('PodcastName','SpeakerName','PodcastDescription','PodcastFile')
class UploadVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=UploadVideo
        fields=('PodcastName','SpeakerName','PodcastDescription','PodcastFile')
class RatingAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model=RatingAudio
        fields=('rating','audio')
class RatingVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=RatingVideo
        fields=('rating','video')
class FavourateAudiosSerializer(serializers.ModelSerializer):
    class Meta:
        model=FavourateAudios
        fields=('userid','audioid')
class FavourateVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model=FavourateVideos
        fields=('userid','videoid')

