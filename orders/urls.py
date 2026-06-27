from django.urls import path

from .views import (

CheckoutView,

OrderListView,

OrderDetailView,

UpdateOrderStatusView

)

urlpatterns = [

path(

'orders/checkout/',

CheckoutView.as_view()

),

path(

'orders/',

OrderListView.as_view()

),

path(

'orders/<int:pk>/',

OrderDetailView.as_view()

),

path(

'orders/<int:pk>/status/',

UpdateOrderStatusView.as_view()

),

]