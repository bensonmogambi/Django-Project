from gc import get_objects

from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import render, redirect
from pyexpat.errors import messages
from rest_framework import status
from rest_framework.decorators import api_view

from customers.Serializers import CustomerSerializers, OrderSerializers
from customers.forms import CustomerForm
from customers.models import Customer, Order

import os
from django.contrib import messages
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    return render(request, 'index.html')

#fetching data from the db
def about(request):
    data = Customer.objects.all()
    context = {'data': data}
    return render(request, 'about.html', context)





def contact(request):
    #connecting the form here and also connecting it to the db
    #we can also capture image by adding request.files
    if request.method == 'POST':
        form =CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(contact)
    else:
        form=CustomerForm()

    return render(request, 'contact.html', {"form":form})


#Updating and deleting a record from the db

def update(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

            if 'image' in request.FILES:
                file_name = os.path.basename(request.FILES['image'].name)
                messages.success(request, f'Customer updated successfully! {file_name} Uploaded')

            else:
                messages.error(request , 'Customer details updated successfully!')

            return redirect('about')

        else:
            messages.error(request , 'Please confirm your Changes!')

    else:
        form = CustomerForm(instance=customer)

    return render(request, 'update.html', {"form":form, "customer":customer})


def delete(request, id):
    customer = get_object_or_404(Customer, id=id)

    try:
        customer.delete()
        messages.success(request, f'Customer deleted successfully!')

    except Exception as e:
        messages.error(request, 'Customer not Deleted!')

    return redirect('about')



#API NOV 19

@api_view(['GET', 'POST'])

def customersapi(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer= CustomerSerializers(customers, many=True)
        return JsonResponse(serializer.data, safe= False)

    elif request.method == 'POST':
        serializer = CustomerSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe= False,status=status.HTTP_201_CREATED) #new record created
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def orderapi(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializers(orders, many=True)
        return JsonResponse(serializer.data, safe= False)

    elif request.method == 'POST':
        serializer = OrderSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)















