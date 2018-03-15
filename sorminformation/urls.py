"""sorm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib import admin
from . import views


urlpatterns = [
#    url(r'^create_type_information',views.sormcreatetypeinformation, name='sormcreatetypeinformation'),
    url(r'^type_information', views.sormtypeinformation, name='sormtypeinformation'),
    url(r'^create_type_information', views.sormcreatetypeinformation, name='sormcreatetypeinformation'),
    url(r'^delete_type_information/(?P<typeinformation_id>[0-9]+)$',views.sormdeletetypeinformation, name='sormdeletetypeinformation'),


    url(r'^information', views.sorminformation, name='sorminformation'),
    url(r'^create_information', views.sormcreateinformation, name='sormcreateinformation'),
    url(r'^delete_information/(?P<information_id>[0-9]+)$',views.sormdeleteinformation, name='sormdeleteinformation'),
    url(r'^edit_information/(?P<information_id>[0-9]+)$',views.sormeditinformation, name='sormeditinformation'),

    url(r'^category_information', views.sormcategoryinformation, name='sormcategoryinformation'),
    url(r'^create_category_information', views.sormcreatecategoryinformation, name='sormcreatecategoryinformation'),
    url(r'^delete_category_information/(?P<category_information_id>[0-9]+)$',views.sormdeletecategoryinformation, name='sormdeletecategoryinformation'),

    url(r'^envobject', views.sormenvobject, name='sormenvobject'),
    url(r'^create_envobject', views.sormcreateenvobject, name='sormcreateenvobject'),
    url(r'^delete_envobject/(?P<envobject_id>[0-9]+)$', views.sormdeleteenvobject, name='sormdeleteenvobject'),


]
