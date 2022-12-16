from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the src index.")

def frontpage(request):
    return render(request, 'frontpage.html')
    # return render(request, 'templates/frontpage.html')
    # C:/Users/Big Daddy B/GitHub/django_web_app/Setting_up_tailwind_with_django/demo_app/src/core/frontpage.html
    # demo_app/src/core/frontpage.html