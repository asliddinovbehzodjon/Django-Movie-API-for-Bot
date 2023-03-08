from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from .serializer import *
from .models import *
from rest_framework.viewsets import ModelViewSet
class MovieViewset(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    def create(self, request, *args, **kwargs):
        data = request.data
        movie  = Movie.objects.create(name=data['name'],file_id=data['file_id'])
        return Response({'status':movie.id},status=status.HTTP_201_CREATED)
