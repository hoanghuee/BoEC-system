from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, CASCADE

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=800)
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)

    description = models.TextField()
    imglink = models.CharField(max_length=800)
    def __str__(self) -> str:
        return self.name



class Address(models.Model):
    homeNumber = models.IntegerField()
    street = models.CharField(max_length=400)
    district = models.CharField(max_length=400)
    city = models.CharField(max_length=400)
    def __str__(self) -> str:
        return self.name


class Fullname(models.Model):
    first_name = models.CharField(max_length=400)
    middleName = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    def __str__(self) -> str:
        return self.name

class User(models.Model):
    id = models.AutoField(primary_key=True)
    age = models.IntegerField()
    contactInfo = models.CharField(max_length=400)
    address = models.OneToOneField(Address,on_delete=models.CASCADE)
    fullname = models.OneToOneField(Fullname,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name


class MemberShip(models.Model):
    name = models.CharField(max_length=400)
    description = models.CharField(max_length=400)
    def __str__(self) -> str:
        return self.name


class Customer(User):
    typeOfMemberShip =  models.OneToOneField(MemberShip,on_delete=CASCADE)
    def __str__(self) -> str:
        return self.name
    
class Promotion(models.Model):
    percent = models.FloatField()
    expireDate = models.DateField()
    def __str__(self) -> str:
        return self.name

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.OneToOneField(Product,on_delete= models.CASCADE)
    promotion = models.ForeignKey(Promotion,on_delete=CASCADE)
    cart = models.ForeignKey(Cart,on_delete=CASCADE)
    def __str__(self) -> str:
        return self.name

class Comment(models.Model):
    content= models.CharField(max_length=400)
    dateTimePost = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer,on_delete=CASCADE)
    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    customerInfo = models.ForeignKey(Customer, on_delete=CASCADE)
    payment_method = models.CharField(max_length=400)
    payment_data = models.CharField(max_length=400)
    items = models.TextField()
    fulfilled = models.BooleanField()
    def __str__(self) -> str:
        return self.name

class bussinessEmpl(User):

    def __str__(self) -> str:
        return self.name

