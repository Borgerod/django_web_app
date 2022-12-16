from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='base'),
    # path('', views.index, name='index'),
    # path('', views.index, name='src'),
    path('', views.frontpage, name='frontpage'),
]
