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
    path('api/login/', views.LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    re_path(r'^auth/', include('drf_social_oauth2.urls', namespace='drf')),
    path('api/addAudio/',views.AddAudioFiles.as_view()),
    path('api/addVideo/',views.AddVedioFiles.as_view())
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)