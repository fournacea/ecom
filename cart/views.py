from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

def cart_summary(request):
    """Render cart summary."""
    return render(request, 'cart_summary.html', {})


def cart_add(request):
    """Add items to cart."""
    print(request)
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Retrieve the product_id from the URI(Request made by AJAX) 
        product_id = int(request.POST.get('product_id'))

        # Get the product from the database using the product ID #
        product = get_object_or_404(Product, id=product_id)

        # Save to session
        cart.add(product=product)

        # Return response
        response = JsonResponse({"Product Name: ":product.name})
        return response


def cart_delete(request):
    """Delete items from cart."""
    pass


def cart_update(request):
    """Update items in cart."""
    pass
