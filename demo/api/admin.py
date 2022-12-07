from django.contrib import admin

# Import your models.
from .models import Location, Item


# Register your models to admin here.
admin.site.register(Item)
admin.site.register(Location)
