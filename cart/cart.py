from store.models import Product


class Cart:
    # def __init__(self, request):
        # self.session = request.session

        # # Get current cart from session or create a new one if not exists
        # self.cart = self.session.get('cart', {})

    def __init__(self, request):
        self.session = request.session
        # Get request
        self.request = request
        # Get the current session key if it exists
        cart = self.session.get('session_key')

        # If the user is new, no session key!  Create one!
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}


	    # Make sure cart is available on all pages of site
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        if product_id in self.cart:
            print("Product already in cart")
        else:
            self.cart[product_id] = int(product_qty)
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
        print(f"Product IDs: {product_ids}, {self.cart.items()}")
        # Use ids to lookup products in database model, store in list
        products = Product.objects.filter(id__in=product_ids)
        print(f"Products: {products}", "FROM get_products cart.py")
        return products
    

    def get_quantities(self):
        # Get quantities from cart
        quantities = self.cart
        print(f"From get_quantities: {quantities}")
        return quantities
        
        

    def __len__(self):
        return len(self.cart)
    

    def __iter__(self):
        # Iterate over items in the cart and yield product instances
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            yield product
            
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)
        
        # Get cart
        current_cart = self.cart
        
        # Update cart
        current_cart[product_id] = product_qty
        
        # Set session modified to True
        self.session.modified = True
        
        return self.cart
        
        
        
    

    
    
    


