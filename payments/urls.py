from django.urls import path

from .views import (

InitiatePaymentView,

VerifyPaymentView

)

urlpatterns = [

path(

'payments/initiate/',

InitiatePaymentView.as_view()

),

path(

'payments/verify/',

VerifyPaymentView.as_view()

),

]