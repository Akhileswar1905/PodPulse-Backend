"""
URL configuration for PodPulse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from  PodPulseApp import views
from django.conf import settings
from django.conf.urls.static import static
from knox import views as knox_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', views.RegisterAPI.as_view(), name='register'),
    path('api/login/', views.LoginAPI.as_view(), name='login'),#normal login
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    re_path(r'^auth/', include('drf_social_oauth2.urls', namespace='drf')),
    path('api/addAudio/',views.AddAudioFiles.as_view()),#to add audio podcasts
    path('api/addVideo/',views.AddVideoFiles.as_view()),#to add vedio podcasts
    path('api/audiopodcasts/',views.GetAudioFiles.as_view()),#to retrive audio podcasts based on rating sorted already so,no need to sort again
    path('api/videopodcasts/',views.GetVideoFiles.as_view()),# same as above but for video podcasts
    path('api/addaudiofavourates/',views.AddUserFavouratesAudios.as_view()),#add a audio podcast into favourate
    path('api/addvideofavourates/',views.AddUserFavouratesAudios.as_view()),#add a video podcast into favourate
    path('api/favourateaudios/',views.GetFavourateAudios.as_view()),#to retrive favourate audio podcasts
    path('api/favouratevideos/',views.GetFavourateVideos.as_view()),#to retrive favourate vedio podcasts
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

#Note to access the audio and video file after making the api request
#you basically get the path of the file 
#so you need to make another 'GET' request as shown below
#http://127.0.0.1:8000/media/<the path of the file that you received in the request>
#also note that every time you make a request you need to send  access token
#which you get as response when you login 
#in headers you need to send it as shown below
# Authorization : Token <token>