from django.contrib import admin

from .models import Brand, Feature, Product
# Register your models here.
admin.site.register(Product)
admin.site.register(Feature)
admin.site.register(Brand)