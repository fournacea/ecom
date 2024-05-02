from django.shortcuts import render

def cart_summary(request):
    """Render cart summary."""
    return render(request, 'cart_summary.html', {})


def cart_add(request):
    """Add items to cart."""
    pass


def cart_delete(request):
    """Delete items from cart."""
    pass


def cart_update(request):
    """Update items in cart."""
    pass
