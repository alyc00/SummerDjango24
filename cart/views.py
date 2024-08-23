from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from store.models import Studio, Show
from cart.models import Order, OrderItem


# Create your views here.

def cart_page(request):
    return render(request, 'cart/cart_detail.html', {})


@login_required
def order_detail(request):
    order, created = Order.objects.get_or_create(user=request.user)
    return render(request, 'order/order_detail.html', {'order': order})


@login_required
def add_to_order(request, show_id):
    product = get_object_or_404(Show, id=show_id)
    order, created = Order.objects.get_or_create(user=request.user)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

    return redirect('order:cart_detail')


@login_required
def remove_from_order(request, product_id):
    order = order.objects.get(user=request.user)
    order_item = get_object_or_404(OrderItem, order=order, product_id=product_id)
    order_item.delete()

    return redirect('order:cart_detail')
