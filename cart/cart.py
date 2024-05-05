class Cart():
    def __init__(self, request):
        self.session = request.session

        # Get current session key if exists
        cart = self.session.get('session_key')

        # If user is new, no session key. Create one!
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}


        # Make cart available on all pages of site
        self.cart = cart


    def add(self, product):
        product_id = str(product)

        if product_id in self.cart:
            pass
        else:
            self.cart = {'price': str(product.price)}

        self.session.modified = True