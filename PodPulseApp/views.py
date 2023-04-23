from django.shortcuts import render
from rest_framework import generics, permissions
from knox.auth import TokenAuthentication
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer,UploadAudioSerializer,UploadVideoSerializer
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
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
    def get(self,request):
        
        pass
class AddVedioFiles(generics.GenericAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes=(permissions.IsAuthenticated,)
    def post(self,request,format=None):
        serializer=UploadVideoSerializer(data=request.DATA,files=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message':'saved the vedio file successfully'
            })
        else:
            return Response({
                'message':'error is saving the file'
            })
