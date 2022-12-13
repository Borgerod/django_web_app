SETUP TUTORIAL
==============

step 1: Virtual Env 
--------------
    - create env

        pip install virtualenv
        virtualenv NAME_OF_ENV
    
    - activate env

        source NAME_OF_ENV/bin/activate (MAC)

        NAME_OF_ENV/Scripts/activate (WINDOWS)


step 2: Make project 
--------------
    - make app root
    django-admin startproject NAME_OF_PROJECT_ROOT

    - make core 
    python NAME_OF_PROJECT_ROOT/manage.py startapp core
    Remember that core should be inside NAME_OF_PROJECT_ROOT


step 3: Edit settings
--------------

- installed apps:
    in INSTALLED_APPS, add; 'core', 'channels', #'NAME_OF_PROJECT_ROOT',

- add ASGI_APPLICATION.
    under WSGI_APPLICATION, add; ASGI_APPLICATION = 'djangochat.asgi.application'

step 4: Start Building
--------------
Front end pages will/should be located in the core folder. 
 - Create templates folder in core. 
  
### Base page:
  - Create another core folder in templates.
  - create base.html in templates/core
    - write whatever but remember to include: 
      - < script src="https://cdn.tailwindcss.com">  < /script>
  
  - create views.py in core:

        from django.shortcuts import render

        # Create your views here.
        def fronpage(request):
            return render(request, 'core/base.html')

  - create urls.py in core:



        from django.urls import path
        from . import views

        urlpatterns =[ 
            path('', views.fronpage, name='frontpage'),
        ]

  - edit original urls.py in NAME_OF_PROJECT_ROOT:
    
          from django.contrib import admin
          from django.urls import path, include

          urlpatterns = [
              path('admin/', admin.site.urls),
              path('', include('core.urls')),
          ]

### Front Page
Extend Base Page with Front Page
    - create frontpage.html and add to the top:

        {% extends 'core/base.html' %}

    - in views.py: change render request to render frontpage.html 
        
        def fronpage(request):
            return render(request, 'core/frontpage.html')


step 5: Run server 
-----------------
(in cmd)

- migrate

    python manage.py migrate
  
- run server

    python manage.py runserver



