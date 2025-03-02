from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def product_list(request):
    products = Product.objects.all()  # Fetch products from DB
    # Get cart count for the navbar
    cart = request.session.get('cart', {})
    cart_count = sum(item['quantity'] for item in cart.values())
    return render(request, 'store/product_list.html', {
        "products": products,
        "cart_count": cart_count
    })

def cart(request):
    cart = request.session.get('cart', {})  # Ensure cart exists in session
    cart_items = []
    total = 0

    for product_id, item in cart.items():
        item_total = item["price"] * item["quantity"]
        total += item_total
        cart_items.append({
            "id": product_id,
            "name": item["name"],
            "price": item["price"],
            "quantity": item["quantity"],
            "image_url": item.get("image_url", ""),
            "total": item_total
        })

    return render(request, "store/cart.html", {
        "cart_items": cart_items,
        "total": total,
        "cart_count": sum(item['quantity'] for item in cart.values())
    })

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        cart[str(product_id)] = {
            'name': product.name,
            'price': float(product.price),
            'quantity': 1,
            'image_url': product.image.url if product.image else ""
        }

    request.session['cart'] = cart
    request.session.modified = True
    messages.success(request, f"{product.name} added to your cart!")
    return redirect('cart')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
        request.session.modified = True
        messages.success(request, "Item removed from cart!")
    
    return redirect('cart')

def decrease_quantity(request, product_id):
    cart = request.session.get('cart', {})
    
    if str(product_id) in cart:
        if cart[str(product_id)]['quantity'] > 1:
            cart[str(product_id)]['quantity'] -= 1
        else:
            del cart[str(product_id)]
        
        request.session['cart'] = cart
        request.session.modified = True
    
    return redirect('cart')

def checkout(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for product_id, item in cart.items():
        item_total = item["price"] * item["quantity"]
        total += item_total
        cart_items.append({
            "id": product_id,
            "name": item["name"],
            "price": item["price"],
            "quantity": item["quantity"],
            "total": item_total
        })

    return render(request, 'store/checkout.html', {
        "cart_items": cart_items,
        "total": total,
        "cart_count": sum(item['quantity'] for item in cart.values())
    })