from django.urls import path

#import the views from views.py
from .views import upload_product,product_detail,products_list,edit_product
from .import views

urlpatterns = [
    path("products/upload", upload_product, name="product_upload_view"),
    path("products/list/", products_list, name = "products_list_view"),
    path("products/<int:id>/",product_detail, name="product_detail_view"),
    path("",views.index, name='indexx'),
    path("products/edit/<int:id>/", edit_product, name="product_edit_view"),
    ]
