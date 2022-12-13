from django.shortcuts import render

# Create your views here.
# def fronpage(request):
def frontpage(request):
    return render(request, 'core/frontpage.html')