from django.db import models
from django.contrib.auth import get_user_model
import random

# Create your models here.

def get_upload_path(instance, filename):
    return f'images/avatars/{filename}'


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=50)
    # price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.CharField(max_length=1000)
    image_url = models.CharField(max_length=200)
    # rating = models.FloatField(default=0.0)
    stock = models.PositiveIntegerField(default=random.randint(1,5))
    likes = models.ManyToManyField(get_user_model(), related_name='users', blank=True)

    categories = models.ManyToManyField(Category, related_name='books')

    def __str__(self):
        return f"{self.title}"

class Author(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='authors')



class CheckoutItem(models.Model):
    checkout = models.ForeignKey('Checkout', on_delete=models.CASCADE, related_name='checkout_items')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='checkout_items')
    quantity = models.PositiveIntegerField(default=0)



class Checkout(models.Model):
    owner = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='checkout')
    books = models.ManyToManyField(Book, through=CheckoutItem, related_name='user_checkout', blank=True)

    def __str__(self):
        return f"{self.owner}"
