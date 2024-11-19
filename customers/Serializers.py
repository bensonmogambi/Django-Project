from rest_framework import serializers
from customers.models import Customer, Order


class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'gender', 'age']


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['name', 'price', 'quantity']
