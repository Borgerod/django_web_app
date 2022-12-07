# from django.shortcuts import render

# # Create your views here.

from rest_framework import generics
from .models import Item, Location
from .serializers import ItemSerializer, LocationSerializer



class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        return super().get_queryset()

class ItemDetail(generics.ListCreateAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        return super().get_queryset()

class LocationList(generics.ListCreateAPIView):
    serializer_class = LocationSerializer

    def get_queryset(self):
        return super().get_queryset()

class LocationDetail(generics.ListCreateAPIView):
    serializer_class = LocationSerializer

    def get_queryset(self):
        return super().get_queryset()
