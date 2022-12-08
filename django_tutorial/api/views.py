# from django.shortcuts import render

# # Create your views here.

from rest_framework import generics
from .models import Item, Location
from .serializers import ItemSerializer, LocationSerializer


''' Descr. of "get_queryset()":


"location" in "queryset = queryset.filter(itemLocation=location)";
    => "location" is the information that is going to get passed 
        via the query parameter in the url.  

    we're going to filter the itemLocation field from api.models.Item
'''


# TODO [ ] make choice (Original, Test)

#* Original; ItemList 
class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(itemLocation=location)
        return queryset

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

class LocationList(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    
class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    