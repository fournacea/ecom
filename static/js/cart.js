
console.log("TEST!!!")

console.log("FROM cart.js!!! Static tags are working! Feel the powa!")


document.addEventListener('click', function(event) {
    if (event.target.id === 'add-cart') {
        event.preventDefault();
        var xhr = new XMLHttpRequest();
        // Get URL from HTML template
        var cartAddUrl = document.getElementById('dynamic-data').getAttribute('data-cart-add-url');

        var url = cartAddUrl;
        var formData = new FormData();
        formData.append('product_id', document.getElementById('add-cart').value);
        // formData.append('product_qty', document.getElementById('qty-cart').options[document.getElementById('qty-cart').selectedIndex].text);
        formData.append('csrfmiddlewaretoken', '{{ csrf_token }}');
        formData.append('action', 'post');

        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    var response = JSON.parse(xhr.responseText);
                    document.getElementById('cart_quantity').textContent = response.qty;
                    location.reload();
                } else {
                    // Handle error
                }
            }
        };

        xhr.open('POST', url, true);
        xhr.send(formData);
    }
});
