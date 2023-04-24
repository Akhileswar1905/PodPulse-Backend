from django.shortcuts import render
import json
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework import generics, permissions
from knox.auth import TokenAuthentication
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer,UploadAudioSerializer,UploadVideoSerializer,FavourateAudiosSerializer,FavourateVideosSerializer
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from .models import UploadAudio,UploadVideo,RatingAudio,FavourateAudios,FavourateVideos,RatingVideo
# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
class AddAudioFiles(generics.GenericAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes=(permissions.IsAuthenticated,)
    def post(self,request,format=None):
        serializer=UploadAudioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message':'save the audio file successfully'
            })
        else:
            return Response({
                'message':'error is saving the file'
            })
class AddVideoFiles(generics.GenericAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes=(permissions.IsAuthenticated,)
    def post(self,request,format=None):
        serializer=UploadVideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message':'saved the vedio file successfully'
            })
        else:
            return Response({
                'message':'error is saving the file'
            })
class GetAudioFiles(generics.GenericAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes=(permissions.IsAuthenticated,)
    def get(self,request,format=None):
        ids=RatingAudio.objects.all().order_by('-rating').values()
        ids=[[i['audio_id'],i['rating']] for i in ids]
        querySet=[]
        for i in ids:
            query=UploadAudio.objects.get(id=i[0])
            audio =query.PodcastFile
            audio=str(audio)
            obj={
                'PodcastName':query.PodcastName,
                'SpeakerName':query.SpeakerName,
                'PodcastDescription':query.PodcastDescription,
                'PodcastFile':audio,
                'rating':i[1]
            }
            querySet.append(obj)
        jsonData=json.dumps(querySet)
        return  Response(jsonData)
class GetVideoFiles(generics.GenericAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes=(permissions.IsAuthenticated,)
    def get(self,request,format=None):
        ids=RatingVideo.objects.all().order_by('-rating').values()
        ids=[[i['video_id'],i['rating']] for i in ids]
        querySet=[]
        for i in ids:
            query=UploadVideo.objects.get(id=i[0])
            video =query.PodcastFile
            video=str(video)
            obj={
                'PodcastName':query.PodcastName,
                'SpeakerName':query.SpeakerName,
                'PodcastDescription':query.PodcastDescription,
                'PodcastFile':video,
                'rating':i[1]
            }
            querySet.append(obj)
        jsonData=json.dumps(querySet)
        return  Response(jsonData)
class AddUserFavouratesAudios(generics.GenericAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes=(permissions.IsAuthenticated,)
    def post(self,request,format=None):
        serializer=FavourateAudiosSerializer(data={'userid':request.user.id,'audioid':request.data['audioid'][0]})
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message':'saved the audio favourates successfully'
            })
        else:
            return Response({
                'message':'error is saving the file'
            })
class AddUserFavouratesVideos(generics.GenericAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes=(permissions.IsAuthenticated,)
    def post(self,request,format=None):
        serializer=FavourateVideosSerializer(data={'userid':request.user.id,'videoid':request.data['videoid'][0]})
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message':'saved the audio favourates successfully'
            })
        else:
            return Response({
                'message':'error is saving the file'
            })
class GetFavourateAudios(generics.GenericAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes=(permissions.IsAuthenticated,)
    def get(self,request,format=None):
        ids=FavourateAudios.objects.filter(userid=request.user.id).values()
        querySet=[]
        for i in ids:
            id=i['audioid']
            query=UploadAudio.objects.get(id=id)
            audio =query.PodcastFile
            audio=str(audio)
            obj={
                'PodcastName':query.PodcastName,
                'SpeakerName':query.SpeakerName,
                'PodcastDescription':query.PodcastDescription,
                'PodcastFile':audio,
                'rating':RatingAudio.objects.get(audio=id).rating
            }
            querySet.append(obj)
        jsonData=json.dumps(querySet)
        return  Response(jsonData)
class GetFavourateVideos(generics.GenericAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes=(permissions.IsAuthenticated,)
    def get(self,request,format=None):
        ids=FavourateVideos.objects.filter(userid=request.user.id).values()
        querySet=[]
        for i in ids:
            id=i['audioid']
            query=UploadVideo.objects.get(id=id)
            audio =query.PodcastFile
            audio=str(audio)
            obj={
                'PodcastName':query.PodcastName,
                'SpeakerName':query.SpeakerName,
                'PodcastDescription':query.PodcastDescription,
                'PodcastFile':audio,
                'rating':RatingVideo.objects.get(audio=id).rating
            }
            querySet.append(obj)
        jsonData=json.dumps(querySet)
        return  Response(jsonData)
class Search(generics.GenericAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes=(permissions.IsAuthenticated,)
    def post(self,request,format=None):
        obj=request.data
        if obj['type']=='audio':
            query=UploadAudio.objects.filter(PodcastName__icontains=obj['searchString']).values()
            querySet=[]
            for i in query:
                obj={
                    'PodcastName':i['PodcastName'],
                    'PodcastFile':i['PodcastFile']
                }
                querySet.append(obj)
            return Response(json.dumps(querySet))
        if obj['type']=='video':
            query=UploadVideo.objects.filter(PodcastName__icontains=obj['searchString']).values()
            querySet=[]
            for i in query:
                obj={
                    'PodcastName':i['PodcastName'],
                    'PodcastFile':i['PodcastFile']
                }
                querySet.append(obj)
            return Response(json.dumps(querySet))
        
