
from django import forms

from customers.models import Customer

#here is where we style the form
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        #we will use the contact page to display this form....ere is where we style the form
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Enter Your Name'}),
            'admissions':  forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'DIP/PL/2019033'}),
            'email': forms.EmailInput(attrs={'class': 'form-control' , 'placeholder': 'Enter Your Email'}),
            'gender': forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Enter Your Gender'}),
            'age': forms.NumberInput(attrs={'class': 'form-control' , 'placeholder': 'Enter Your Age'}),

        }




















