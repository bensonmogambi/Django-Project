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















