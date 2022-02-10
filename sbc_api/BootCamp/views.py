from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BootCamp
from .pagination import BootCampPagination
from .serializers import BootCampSerializer
from django.db.models import Q


class BootCampListAPI(ListAPIView):
    queryset = BootCamp.objects.all()
    serializer_class = BootCampSerializer
    pagination_class = BootCampPagination

class BootCampDetailAPI(APIView):
    def get_object(self, pk):
        return get_object_or_404(BootCamp, pk=pk)

    def get(self, request, pk):
        bootcamp = self.get_object(pk)
        serializer = BootCampSerializer(bootcamp)
        bootcamp.count += 1
        bootcamp.save()

        return Response(serializer.data)

class SearchBootCampAPI(APIView):
    def get(self, request):
        bootcamps = BootCamp.objects.all()
        search = request.GET.get('search')
        if search:
            queryset = bootcamps.filter(
                Q(brand_name__icontains=search) |
                Q(bootcamp_name__icontains=search) |
                Q(program__icontains=search) |
                Q(tech_stack__icontains=search)
            )
        serializer = BootCampSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class OptionBootCampAPI(APIView):
    def get(self, request):
        bootcamps = BootCamp.objects.all()
        program = request.GET.get('program')
        tech_stack = request.GET.get('tech_stack')
        accept = request.GET.get('accept')
        on_offline = request.GET.get('on_offline')
        k_digital = request.GET.get('k_digital')

        search_list = {"program":program, "tech_stack":tech_stack, "accept":accept, "on_offline":on_offline, "k_digital":k_digital}

        q = Q()

        for key in search_list:
            if search_list[key]:
                if key == "program":
                    q.add(Q(program__icontains=program), q.AND)
                elif key == "tech_stack":
                    q.add(Q(tech_stack__icontains=tech_stack), q.AND)
                elif key == "accept":
                    q.add(Q(accept__icontains=accept), q.AND)
                elif key == "on_offline":
                    q.add(Q(on_offline__icontains=on_offline), q.AND)
                else:
                    q.add(Q(k_digital__icontains=k_digital), q.AND)

        queryset = bootcamps.filter(q)
        serializer = BootCampSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

def BootCampUpdate(request):
    exec(open('BootCamp/BootCampUpdate.py').read())
    data = {'result': "DB update success"}
    return JsonResponse(data, status=status.HTTP_200_OK)

