from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from category.models import Category


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='image', upload_to='product')
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = 'Products'
        verbose_name = 'Product'
