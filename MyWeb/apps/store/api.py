import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from apps.cart.cart import Cart

from .models import Product

def api_add_to_cart(request):
    data = json.load(request.body)
    
    print("api.py에서 실행됨=====")
    print("json데이터로 넘어온 data객체: "+data)
    
    jsonresponse = {'seccess':True}
    product_id = data['product_id']
    update = data['update']
    quantity = data['quantity']
 
    cart = Cart(request)

    product = get_object_or_404(Product, pk=product_id)

    if not update:
        cart.add(product=product, quantity=1, update_quantity=False)
    else:
        cart.add(product=product, quantity=quantity, update_quantity=True)

    print("api.py에서 실행됨=====")
    return JsonResponse(jsonresponse)