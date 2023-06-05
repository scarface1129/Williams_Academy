from courses.models import *
from cart.models import *

def categories_processor(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.get(user_id = user.id)
        Orders = Order.objects.filter(cart_id = cart.id)     
        orders = len(Orders)     
        return {'items_in_cart': orders}
    return {'items_in_cart':'0'}