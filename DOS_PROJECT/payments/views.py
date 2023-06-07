from django.shortcuts import render, redirect
from .models import *
from django.conf import settings
from courses.models import *
from cart.models import *
from django.contrib.auth.decorators import login_required


@login_required(login_url='/user/login/')
def initiate_payment(request):
    if request.method == "POST":
        amount = request.POST['amount']
        email = request.POST['email']
        if email == '':
            print(email)
            print('#################')
            email = 'agboemmanuel002@gmail.com'

        pk = settings.PAYSTACK_PUBLIC_KEY

        payment = Payment.objects.create(amount=amount, email=email, user=request.user)
        payment.save()

        context = {
            'payment': payment,
            'field_values': request.POST,
            'paystack_pub_key': pk,
            'amount_value': payment.amount_value(),
        }
        return render(request, 'payments/make_payment.html', context)

    return render(request, 'payments/payment.html')

@login_required(login_url='/user/login/')
def verify_payment(request, ref):
    payment = Payment.objects.get(ref=ref)
    verified = payment.verify_payment()

    if verified:
        # user_wallet = UserWallet.objects.get(user=request.user)
        # user_wallet.balance += payment.amount
        # user_wallet.save()
        user = request.user
        cart = Cart.objects.get(user_id = user.id)
        Orders = Order.objects.filter(cart_id = cart.id)     
        Orders.delete()     
        print(request.user.username, " funded wallet successfully")
        return render(request, "payments/success.html")
    return render(request, "payments/success.html")