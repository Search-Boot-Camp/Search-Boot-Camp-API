from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import BootCamp
from .serializers import BootCampSerializer

class BootCampListAPI(APIView):
    def get(self, request):
        queryset = BootCamp.objects.all()
        serializer = BootCampSerializer(queryset, many=True)
        return Response(serializer.data)
