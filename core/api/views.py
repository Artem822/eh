from django.shortcuts import render
from rest_framework import generics
from .serializers import *

class EmployeeView(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class EventView(generics.ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class NewsView(generics.ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()

