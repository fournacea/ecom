from .cart import Cart


# Create context processor for Cart to work on all pages
def cart(request):
    # Return default data from Cart
    return {'cart': Cart(request)}