from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=50 , unique=True)
    slug = models.SlugField(max_length=100 , unique=True)
    description = models.TextField(max_length=255)
    cart_image = models.ImageField(upload_to='photos/categories/', blank=True)

    # print("Model Printing" , models.Model)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name