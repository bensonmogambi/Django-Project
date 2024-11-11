#1 - pip install django
#2 - django-admin startproject 'OnlineShop' .    - Creats the main project, 'Project' this should be the project name and the full stop should be there then a space
#3 - python manage.py startapp 'signUp'     - creats a part of the app eg users, accounts login etc
#4 - python manage.py runserver

- register the products and signup apps under the settings in the main project which is the onlineshop
- then go under installed apps list and add the names
- go to the urls file and update the apps ....
- something like path('signUp/', include('signUp.urls')) and also do the include import

#NOVEMBER 5
#BRINGING FRONTEND OR HTML TEMPLATES INTO THE PROJECT
Creat a templates directory in the app you want eg here we have done under customers and call it templates .
Creat an index file inside the templates dir
If you want dammy words use lorem number of words then tab, eg lorem69 then tab
Next creat a url, by making a view, then create a urls.py file under the app .....you should have urls file in the main project and the apps level

#Adding Stylesheets
create a static directory under the name of the project - do not forget to register it in the settings file here STATIC_URL = '/static/'
It will host all stylings
add a style sheet under style 
now when connecting the html files to the style, creat link tags in the html files  <link rel="stylesheet" href="../../static/style/style.css">

the dots help us move out of the directory then go to the static directory and locate the style.css


nov 06
adding bootstrap
by pasting it to the style file then add the following links to the index file to check for css and js
<link rel="stylesheet" href="../../static/style/bootstrap/css/bootstrap.min.css">
<link rel="stylesheet" href="../../static/style/bootstrap/js/bootstrap.min.js">

add a navbar in the index, by going to boostrap and selecting code for any nav bar


ginger templating
helps not repeat eg doing a navbar in each page eg home etc, we can reuse it repeatatively 
using {% load static %}
if you do this to one file then delete all content in the other pages so we have one html file and then do all other thing there
now lets creat a html base file 
now we will have content only in the base file all the other files/pages should be empty

in the base fle we will put all things that are repeated each time and do not change from page to page .
the unique content of each file are kept here 
{% block content %}

all the unique things should be implemented here

{% endblock %}




#nov 07
making our nav bar links work
use {% url 'home' %} under the href




NOVEMBER 08
#MODELS-       done under the models.py file
Allows us to creat forms for the templates 
HELPS CaPTURE DATA AND STORE IT IN THE DB
eg name,gender , email, phone number etc

now create a file forms after doing the class function in the models.py
then cretae a button that collect all the data 

NOVEMBER 11
Converting models into database tables and connecting backend to frontend
we register the models in the admin.py file

# Register your models here.

admin.site.register(Customer)

after this, create a credential to access the db in the terminal 
python manage.py createsuperuser
then do the migrations 
python manage.py makemigrations
python manage.py migrate
then create the credentials using - python manage.py createsuperuser
p is 9330

to create a logic that collects data from the frontend and storing the data in the db, create it in the views file







