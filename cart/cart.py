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

    def __len__(self):
        return len(self.cart)
