from django.urls import path
from .views import ItemList, ItemDetail, LocationList, LocationDetail
'''
Create url structures.

    We will need, 4 endpoints:
        - view all of the items
        - view all of the locations 
        - view individual item
        - view individual location

    Will also include a query parameter in the views 
'''

'''
    "<int:pk>/" ==> stands for primary key 
'''

urlpatterns = [
    path('item/', ItemList.as_view()),
    path('item/<int:pk>/', ItemDetail.as_view()),
    path('location/', LocationList.as_view()),
    path('location/<int:pk>/', LocationDetail.as_view()),
]
