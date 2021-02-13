"""faceRecog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.urls import  path
from django.contrib import admin
from attendence import views as app_views
from .views import All_sample
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'All_sample',All_sample)

urlpatterns = [
    path('', include(router.urls)),
    url(r'^$', app_views.index),
    url(r'^create_dataset$', app_views.create_dataset),
    url(r'^trainer$', app_views.trainer),
    url(r'^detect$', app_views.detect),
    url(r'^video_feed$', app_views.video_feed),
    url(r'employee-attendence-summery', app_views.employee_attendence_summery),
    url(r'^create_dataset_new$', app_views.create_dataset_new),
    url(r'upload_face_video/', app_views.upload_face_video),
]
