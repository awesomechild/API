# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .models import Names
from .serializers import NameSerializer

# class NameList(APIView):
#     def get(self, request):
#         names=Names.objects.all()
#         serializer = NameSerializer(names, many=True)
#         return Response(serializer.data)
#     def __pos__(self):
#         pass
#



class NameList(generics.ListCreateAPIView):
    queryset = Names.objects.all()
    serializer_class = NameSerializer

class NameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Names.objects.all()
    serializer_class = NameSerializer
