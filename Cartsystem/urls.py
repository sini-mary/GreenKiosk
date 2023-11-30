from django.urls import path
from .views import upload_cart,cart_list,cart_detail
urlpatterns = [
    path("cart/upload",upload_cart,name="cart_upload_view"),
    path("cart/list",cart_list,name="cart_list_view"),
    path("cart/detail",cart_detail,name="cart_detail_view")

]