from django.shortcuts import render

from customers.forms import CustomerForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    #connecting the form here
    form =CustomerForm()
    return render(request, 'contact.html', {"form":form})








