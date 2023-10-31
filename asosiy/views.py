from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import ProfilSerializers




class ProfilViewset(ModelViewSet):
    queryset = Profil.objects.all()
    serializer_class = ProfilSerializers

# Create your views here.
