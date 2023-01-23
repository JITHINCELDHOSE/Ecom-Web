from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


# Create your models here.
class categ(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    img = models.ImageField(upload_to='product_images')

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('prodcat', args=[self.slug])


class products(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    img = models.ImageField(upload_to='product_images')
    desc = models.TextField()
    available = models.BooleanField()
    price = models.PositiveIntegerField()
    mrp = models.PositiveIntegerField()
    offer = models.PositiveIntegerField(null=True, blank=True)
    category = models.ForeignKey(categ, on_delete=models.CASCADE)
    stock = models.IntegerField()

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('details', args=[self.category.slug, self.slug])


class favourite(models.Model):
    fpro = models.ForeignKey(products, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.fpro)