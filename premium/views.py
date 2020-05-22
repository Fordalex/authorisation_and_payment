from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET

@login_required()
def premium(request):

    if True:
        return render(request, 'register.html')

    return render(request, 'premium.html', {"publishable": settings.STRIPE_PUBLISHABLE})
