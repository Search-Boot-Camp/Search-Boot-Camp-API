from rest_framework import serializers
from .models import BootCamp

class BootCampSerializer(serializers.ModelSerializer):
    class Meta:
        model = BootCamp
        fields = '__all__'
