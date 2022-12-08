## What are the tools? 
- Django 	:	Framework
- Wagtail	:	CMS, Control who can do what. Control how content is organised and displayed. 
- Tailwind	:	Huge collection of cs utility classes
- https://play.tailwindcss.com/ 	: 	


## Getting Started

### Step 0
Create framework
In project folder;  
	
	# Create venv
	python -m venv ./venv  		# with regular python
	python3 -m venv ./venv 		# or with python3

	# install django, django-tailwind, wagtail
	pip install -r requirements.txt

	# Generate (main) web_framework 
	django-admin startproject NAME_OF_APP . 	#make in current folder
	django-admin startproject NAME_OF_APP	 	#make new folder

	# Generate API framework 
	django-admin startapp api

#### Step 0.1Alt
(1) Create pipenv: 

	pip install pipenv

	pipenv install -r requirements.txt

(2) run venv:

	cd venv

	<!-- run venv shell  -->
	run pipenv shell


#### Step 0.2
Integrate api/ with tutorial/ [web_framework/]  
In "INSTALLED_APPS" from tutorial/settings.py, ADD:

	'api.apps.ApiConfig',
	'rest_framework',

	# "api.apps.ApiConfig" => ApiConfig from api/apps.py 
	# "rest_framework" => ??






### Step 1
Create models, will make two models; Location and Item:
Location:   

	# This is the location for the Item
	class Location(models.Model): #will inherit django's premade base model

	# Will display the actual name in the admin panel, rather then the ID 
	def __str__(self) -> str:
		return self.locationName
	
Item:

	itemLocation = models.ForeignKey(Location, on_delete=models.CASCADE)
	'''
		- link/send back to the first model (Location),   "..gnKey(Location, .."  
		- "on_delete=models.CASCADE" will make sure that when location is deleted,   
		   all the items in the location will be deleted aswell.
	'''  
- itemName: Name of the item
- date_added: when the item was added, with automatic now 
- itemLocation: is a link betweeen Item and Location  

	
### Step 2 - Admin 

(1) Import your models to api/admin.py
	
	from .models import Item, Location 
	
(2) Register models to admin 
	
	# Now, when you open up admin you will actually see the models there.
	admin.site.register(Item)
	 ...


### Step 3 - Migrations  
(1) Make the database migrations:

	python3 manage.py makemigrations
	#or
	python manage.py makemigrations

OUTPUT:

	Migrations for 'api':
	api\migrations\0001_initial.py
		- Create model Location
		- Create model Item

(2) Migrate over to actually create them in the db:

	python manage.py migrate
	
OUTPUT:

	Running migrations:
		Applying contenttypes.0001_initial... OK
		Applying auth.0001_initial... OK
		Applying admin.0001_initial... OK
		Applying admin.0002_logentry_remove_auto_add... OK
		Applying admin.0003_logentry_add_action_flag_choices... OK
		Applying api.0001_initial... OK
		Applying contenttypes.0002_remove_content_type_name... OK
		Applying auth.0002_alter_permission_name_max_length... OK
		Applying auth.0003_alter_user_email_max_length... OK
		Applying auth.0004_alter_user_username_opts... OK
		Applying auth.0005_alter_user_last_login_null... OK
		Applying auth.0006_require_contenttypes_0002... OK
		Applying auth.0007_alter_validators_add_error_messages... OK
		Applying auth.0008_alter_user_username_max_length... OK
		Applying auth.0009_alter_user_last_name_max_length... OK
		Applying auth.0010_alter_group_name_max_length... OK
		Applying auth.0011_update_proxy_permissions... OK
		Applying auth.0012_alter_user_first_name_max_length... OK
		Applying sessions.0001_initial... OK

(3) Create super-user

	python manage.py createsuperuser

OUTPUT:

	Username (leave blank to use 'big_daddy_b'): admin
	Email address: borgerod@hotmail.com
	Password:
	Password (again):
	Superuser created successfully.

(5) Run server to check if everything works

	python manage.py runserver

OUTPUT:

	System check identified no issues (0 silenced).
	December 07, 2022 - 13:45:12
	Django version 4.1, using settings 'demo_app.settings'
	Starting development server at http://127.0.0.1:8000/
	Quit the server with CTRL-BREAK.

Create Venv;

	# locate pip3
	where pip

	#[optional] create new project folder
	mkdir NAME_OF_PYTHON_PROJECT

	#[optional] go into folder
	cd NAME_OF_PYTHON_PROJECT

	#create venv
	python3 -m venv ./venv 		# "./venv" to create a new folder called venv


### step 4 -  Project URLs

(1) create urls 

	touch api/urls.py 
	
(2) create serializers 	

	''' 
	used by rest_framework to 
	convert the data from django db models 
	into somehing we can turn into Json
	'''
	touch api/serializers.py













### 







## smal notes:
pip loc:
- C:\Users\Big Daddy B\AppData\Local\Programs\Python\Python310\Scripts\pip.exe
pip3 loc:
C:\Users\Big Daddy B\AppData\Local\Programs\Python\Python310\Scripts\pip3.exe

commands to make tutorial app:
	mkdir tutorial
	cd tutorial
	django-admin startproject demo_app .
	django-admin startapp api