from django.shortcuts import render
# For Multilanguage
from django.utils import translation
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from rest_framework.viewsets import ModelViewSet
from .serializer import *
from .models import *



class DirectorViewset(ModelViewSet):
    queryset =  Director.objects.all()
    serializer_class = DirectorSerializer
    
class ManagerViewset(ModelViewSet):
    queryset =  Manager.objects.all()
    serializer_class = ManagerSerializer
