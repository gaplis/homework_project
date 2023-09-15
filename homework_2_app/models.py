from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    date_registration = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Имя: {self.name}, E-mail: {self.email}, телефон: {self.phone}, адрес: {self.address}, ' \
               f'дата регистрации: {self.date_registration}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    count = models.IntegerField(default=0)
    date_added = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='products/', null=True)


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(default=0, max_digits=20, decimal_places=2)
    date_ordered = models.DateField(auto_now_add=True)
