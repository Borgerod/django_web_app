from django.db import models

# Create your models here.
class Location(models.Model):
    '''
    This is the location of the Items
    '''
    locationName = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.locationName

class Item(models.Model):
    '''
    This is the Item in a Location
    '''
    itemName = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)
    itemLocation = models.ForeignKey(Location, on_delete=models.CASCADE) # TODO [ ] learn what a ForeinKey is
    
    def __str__(self) -> str:
        return self.itemName

