from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.contrib import messages

def cart_summary(request):
    """Render cart summary."""
    cart = Cart(request)
    cart_products = cart.get_products
    return render(request, 'cart_summary.html', {"cart_products":cart_products})


# def cart_add(request):
#     # Get the cart
#     cart = Cart(request)
    
#     # Initialize flag for product already added
#     product_already_added = False
    
#     # Test for POST
#     if request.POST.get('action') == 'post':
#         # Get product ID from POST data
#         product_id = int(request.POST.get('product_id'))
        
#         # Lookup product in DB
#         product = get_object_or_404(Product, id=product_id)
        
#         # Check if product is already in cart
#         if product in cart:
#             product_already_added = True
#             # Store the message in the session
#             request.session['product_already_added'] = True
#         else:
#             # Save product to session
#             cart.add(product=product)
#             # Store the success message in the session
#             request.session['product_added'] = True
    
#     # Get cart quantity
#     cart_quantity = len(cart)
    
#     # Prepare response data
#     response_data = {'qty': cart_quantity}
    
#     # If product was already added, include the message
#     if product_already_added:
#         response_data['message'] = 'Product already added'
    
#     # Return response
#     return JsonResponse(response_data)
    

def cart_add(request):
    # Get the cart
    cart = Cart(request)
    # test for POST
    if request.POST.get('action') == 'post':
        print(f"request.POST.get: {request.POST.get}")
        # Get stuff
        product_id = int(request.POST.get('product_id'))
        

        # lookup product in DB
        product = get_object_or_404(Product, id=product_id)
        print(f"product:{product}")

        # Check if product is already in cart
        if product in cart:
            # Add a message
            messages.warning(request, 'Product already added')
        else:
            # Save product to session
            cart.add(product=product)
            # Add a success message
            messages.success(request, 'Product added to cart successfully!')
        

        # Get Cart Quantity
        cart_quantity = cart.__len__()
        print(cart_quantity)


        # Return resonse
        # response = JsonResponse({'Product Name: ': product.name})
    response = JsonResponse({'qty': cart_quantity})
    
    return response




def cart_delete(request):
    """Delete items from cart."""
    pass


def cart_update(request):
    """Update items in cart."""
    pass

