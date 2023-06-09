from django.urls import path
from cartapp import views
app_name='cartapp'

urlpatterns=[
    path('add/<int:product_id>', views.add_cart, name="add_cart"),
    path('',views.cart_detail,name="cart_detail"),
    path('remove/<int:product_id>', views.remove_item, name="remove_item"),
    path('delete/<int:product_id>', views.delete_item, name="delete_item"),

]