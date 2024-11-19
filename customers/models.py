from django.db import models

from django.core.validators import RegexValidator


# Create your models here.

class Customer(models.Model):
    image= models.ImageField(upload_to='customers_images/', blank=True)
    name = models.CharField(max_length=22)
    admissions = models.CharField(max_length=22, validators=[
            RegexValidator(
                regex=r'^DIP/PL/\d{7}$',
                message='Admission must be in the format DIP/PL/XXXXXXX (7 digits).',
                code='invalid_admission'),],)

    email = models.CharField(max_length=25)
    gender = models.CharField(max_length=22)
    age = models.IntegerField()

    def __str__(self):
        return self.name


#CREATE AN API THAT CAN GET ORDERS
class Order(models.Model):
    name = models.CharField(max_length=22)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Order: {self.name} | Quantity: {self.quantity} | Price: {self.price}"



