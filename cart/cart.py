from store.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session

        # Get current cart from session or create a new one if not exists
        self.cart = self.session.get('cart', {})

    def add(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            print("Product already in cart")
        else:
            self.cart[product_id] = {'price': str(product.price)}
            print("Product added to cart")

        self.session['cart'] = self.cart
        self.session.modified = True
        # print(self.cart.keys())
        # print(self.cart.values())
        # print(self.cart.items())
        # print(self.cart)

    
    def get_products(self):
        # Get keys from cart
        product_ids = self.cart.keys()
        # Use ids to lookup products in database model, store in list
        products = Product.objects.filter(id__in=product_ids)
        return products
        
        

    def __len__(self):
        return len(self.cart)
    

    def __iter__(self):
        # Iterate over items in the cart and yield product instances
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            yield product
    

    
    
    


