from django.db import models
from django.contrib.auth.models import User

class Müşteri(models.Model):
    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=100)
    phone_number = models.PhoneNumberField(_(max_length=10))
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Yemek(models.Model):
    name = models.CharField(max_length=100)
    image=models.ImageField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=50)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Müşteri, on_delete=models.CASCADE)
    items = models.ManyToManyField(Yemek, through='OrderItem')
    delivery_address = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)
    is_delivered = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.meal.name} - {self.quantity}"