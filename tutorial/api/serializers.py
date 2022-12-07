from rest_framework import serializers
from models import Item, Location

'''
will turn the db models into json that we can work with
'''

class ItemSerializer(serializers.ModelSerializer):
    class Meta: #TODO [ ] what out what this i for
        model = Item
        fields = ('__all__')

class LocationSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Location
        fields = ('__all__')