from django.shortcuts import render

# Create your views here.

def productslist(request):
    return render(request, 'productslist.html')

