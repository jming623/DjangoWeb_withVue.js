from django.db import models
from django.forms import CharField

class Category(models.Model):
    title = models.CharField(max_length=255) #CharField는 고정길이 문자열 max_length를 지정해야한다.
    slug = models.SlugField(max_length=255) #SlugField는 일반적으로 URL에 사용된다.
    ordering = models.IntegerField(default=0) 

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('ordering',)

    def __str__(self):
        return self.title

class Product(models.Model):
    
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)#related_name은 Category를 통해 Product를 불러올떄 사용할 이름
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    is_featured = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.title