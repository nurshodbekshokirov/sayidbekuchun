from rest_framework import serializers
from .models import *

class ProfilSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = "__all__"