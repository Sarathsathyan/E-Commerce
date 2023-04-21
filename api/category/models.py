from django.db import models

# Create your models here.

class Category(models.Model):
    # Model to store all categories
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    # Model to store all subcategories
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    description = models.TextField()

    def __str__(self):
        return self.name
    