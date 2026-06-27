from django.urls import path

from .views import (

    AddToCartView,

    CartView, UpdateCartView, RemoveCartItemView

)

urlpatterns = [

    path(

        'cart/add/',

        AddToCartView.as_view()

    ),

    path(

        'cart/',

        CartView.as_view()

    ),
    path(
        "cart/update",
        UpdateCartView.as_view()
    ),
    path(
        "cart/remove/<int:product_id>/",
        RemoveCartItemView.as_view()
    ),
]