
from django.contrib import admin
from django.urls import path
from django.urls import include
#import View 
from .views import *

#this imports need for shows static files
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", Home.as_view(), name='home_url' ),
]

