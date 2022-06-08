"""MyWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from apps.core.views import frontpage, contactpage, aboutpage
from apps.store.views import product_detail, category_detail
from apps.cart.views import cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', cart, name="cart")
    path('', frontpage , name='frontpage'),
    path('contact/', contactpage , name='contactpage'), #name값은 장고 템플릿 url태그에서 사용하는 값
    path('about/', aboutpage , name='aboutpage'),
    path('<slug:category_slug>/<slug:slug>/', product_detail, name='product_detail'),
    path('<slug:slug>/', category_detail, name='category_detail'),   
]

