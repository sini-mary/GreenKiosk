from django.urls import path
from .views import payment_list

urlpatterns = [
    path("payment/list",payment_list,name= "payment_view"),
]


