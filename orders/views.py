from django.shortcuts import render,redirect
from .models import Order,OrderedItem
from products.models import Product



# Create your views here.
def show_cart(request):
    user=request.user
    customer=user.customer_profile
    cart_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
    context={'cart':cart_obj}

    return render(request,'cart.html',context)

def add_to_cart(request):
    if request.POST:
        user=request.user
        customer=user.customer_profile
        quantity=int(request.POST.get('quantity'))
        product_id=request.POST.get('product_id')
        cart_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE

        )
        product=Product.objects.get(pk=product_id)
        ordered_Item,created=OrderedItem.objects.get_or_create(
            product=product,
            owner=cart_obj,
            

        )
        if created:
            ordered_Item.quantity=quantity
            ordered_Item.save()
        else:
            ordered_Item.quantity=ordered_Item.quantity+quantity
            ordered_Item.save()  
    return redirect('cart')




