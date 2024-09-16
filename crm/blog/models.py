# crm/blog/models.py
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

class Category(models.Model):
    customer_country_catalog = models.CharField(max_length=100)

    def __str__(self):
        return self.customer_country_catalog

    def get_absolute_url(self):
        return reverse("home")

class Customer(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    situation = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.name} | by author {self.author}'

    def get_absolute_url(self):
        return reverse("home")
