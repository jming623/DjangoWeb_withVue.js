from django.contrib import admin

from .models import Category, Product

#이곳에 등록을 하면 admin페이지에 store카테고리 하위 카테고리로 등록 됨.
admin.site.register(Category);
admin.site.register(Product);