from django.db import models

# Create your models here.

class Brand(models.Model):
    brand_name = models.CharField(max_length=30)

class Feature(models.Model):
    feature = models.CharField(max_length=100)

class Product(models.Model):
    model = models.CharField(max_length=50)
    model_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model_features = models.ManyToManyField(Feature)

