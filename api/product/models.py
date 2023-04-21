from django.db import models

from api.category.models import SubCategory
# Create your models here.

class Product(models.Model):
    # Model to store all products
    name = models.CharField(max_length=100)
    sub_category = models.ForeignKey(SubCategory, related_name='products',
                                     on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name