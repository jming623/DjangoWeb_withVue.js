from django.conf import settings

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.SESSION_COOKIE_AGE)

        print("cart.py에서 실행됨=====")
        print("request로부터 넘어온 세션에 .get(settings.SESSION_COOKIE_AGE)값: "+cart)
        print("not cart: "+(not cart))
        print("self.session[settings.CART_SESSION_ID]: "+self.session[settings.CART_SESSION_ID])

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        
        print("self.session[settings.CART_SESSION_ID] = \{\}한 이후에 cart로 저장된 값: " + cart)
        print("cart.py에서 실행됨=====")
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        price = product.price

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0, 'price': price, 'id':product_id}

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] = self.cart[product_id]['quantity'] + 1
        
        self.save()
    
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True