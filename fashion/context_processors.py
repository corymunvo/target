from .models import Cart

def cart_total(request):
   cart_total = 0
   if request.user.is_authenticated:
      cart_total = Cart.objects.filter(user=request.user).count()

   return {'cart_total': cart_total}

    