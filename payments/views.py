import uuid

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

from orders.models import Order

from .models import Payment

from .serializers import (

InitiatePaymentSerializer

)
class InitiatePaymentView(

    APIView

):

    permission_classes = [

        IsAuthenticated

    ]

    def post(

        self,

        request

    ):

        serializer = InitiatePaymentSerializer(

            data=request.data

        )

        serializer.is_valid(

            raise_exception=True

        )

        order = Order.objects.get(

            id=serializer.validated_data[

                'order_id'

            ],

            user=request.user

        )

        payment, created = Payment.objects.get_or_create(

            order=order,

            defaults={

                'reference':

                f"PAY-{uuid.uuid4()}"

            }

        )

        return Response({

            "success":True,

            "message":

            "Payment initiated",

            "data":{

                "reference":

                payment.reference,

                "status":

                payment.status

            }

        })
class VerifyPaymentView(

    APIView

):

    permission_classes = [

        IsAuthenticated

    ]

    def post(

        self,

        request

    ):

        reference = request.data.get(

            'reference'

        )

        payment = Payment.objects.get(

            reference=reference

        )

        payment.status = 'successful'

        payment.save()

        payment.order.status = 'paid'

        payment.order.save()

        return Response({

            "success":True,

            "message":

            "Payment successful"

        })