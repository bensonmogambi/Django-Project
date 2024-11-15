from gc import get_objects

from django.shortcuts import render, redirect
from pyexpat.errors import messages

from customers.forms import CustomerForm
from customers.models import Customer

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
















