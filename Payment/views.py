from django.shortcuts import render
# from .forms import PaymentForm
from Payment.models import Payment

# Create your views here.
def payment_list(request):
    payment=Payment.objects.all()
    
    return render (request, "payment/payment_form.html",{"payment":payment})