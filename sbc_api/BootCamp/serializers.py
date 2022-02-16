from rest_framework import serializers
from .models import BootCamp, SearchBootCampDTO

class BootCampSerializer(serializers.ModelSerializer):
    class Meta:
        model = BootCamp
        fields = '__all__'

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchBootCampDTO
        fields = 'search',

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BootCamp
        fields = 'program', 'tech_stack', 'accept', 'on_offline', 'k_digital'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BootCamp
        fields = 'image_id',
