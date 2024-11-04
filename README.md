#1 - pip install django
#2 - django-admin startproject 'OnlineShop' .    # - Creats the main project, 'Project' this should be the project name
# and the full stop should be there then a space
#3 - python manage.py startapp 'signUp'    # - creats a part of the app eg users, accounts login etc
#4 - python manage.py runserver

- register the products and signup apps under the settings in the main project which is the onlineshop
- then go under installed apps list and add the names
- go to the urls file and update the apps ....
- something like path('signUp/', include('signUp.urls')) and also do the include import










