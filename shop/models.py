from django.db import models
from django.urls import reverse
class Category(models.Model):
    name = models.CharField(max_length=150,unique=True)
    slug = models.SlugField(max_length=150,unique=True)
    decription = models.TextField(blank=True)
    Image = models.ImageField(upload_to='Category', blank=True)
# for we need  to add them in the class in order to pass three option to their model
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('shop:Product_by_category',args=[self.slug])


    def __str__(self):
        return '{}'.format(self.name)
class Product(models.Model):
    name =       models.CharField(max_length=150,unique=True)
    slug =       models.SlugField(max_length=150,unique=True)
    decription = models.TextField(blank=True)
    category =   models.ForeignKey(Category,on_delete= models.CASCADE)
    price =      models.DecimalField(max_digits=10 ,decimal_places= 2)
    image =      models.ImageField(upload_to='product',blank=True)
    stock =      models.IntegerField()
    available =  models.BooleanField(default=True)
    created =    models.DateTimeField(auto_now_add=True)
    updated =    models.DateTimeField(auto_now=True)
# for we need  to add them in the class in order to pass three option to their model
    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_url(self):
        return reverse('shop:ProductCatDetail',args=[self.category.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)