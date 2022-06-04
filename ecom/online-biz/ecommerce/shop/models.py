from django.db import models
from django.db.models.fields import CharField, URLField

# Create your models here.


class Product(models.Model):
	title = models.CharField(max_length=250)
	price = models.FloatField()
	discounted_price = models.FloatField()
	category = models.CharField(max_length=200)
	description = models.TextField()
	image = models.CharField(max_length=300)


class Order(models.Model):
	items = models.CharField(max_length=1000, default=None)
	name = models.CharField(max_length=200,default=None)
	email = models.CharField(max_length=200, default=None)
	address = models.CharField(max_length=1000, default=None)
	city = models.CharField(max_length=200, default=None)
	state = models.CharField(max_length=200, default=None)
	zipcode = models.CharField(max_length=200, default=None)