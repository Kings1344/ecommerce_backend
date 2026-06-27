from django.db import transaction

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

from carts.models import Cart

from .models import Order, OrderItem

from .serializers import OrderSerializer
from products.permissions import IsAdminUserRole
class CheckoutView(APIView):

    permission_classes = [

        IsAuthenticated

    ]

    @transaction.atomic

    def post(self, request):

        cart = request.user.cart

        items = cart.items.all()

        if not items.exists():

            return Response({

                "success": False,

                "message": "Cart is empty"

            }, status=400)

        total = 0

        for item in items:

            if item.quantity > item.product.stock_quantity:

                return Response({

                    "success": False,

                    "message":

                    f"Not enough stock for {item.product.name}"

                }, status=400)

            total += (

                item.product.price

                * item.quantity

            )

        order = Order.objects.create(

            user=request.user,

            total_price=total

        )

        for item in items:

            OrderItem.objects.create(

                order=order,

                product=item.product,

                quantity=item.quantity,

                price=item.product.price

            )

            item.product.stock_quantity -= item.quantity

            item.product.save()

        items.delete()

        serializer = OrderSerializer(

            order

        )

        return Response({

            "success": True,

            "message":

            "Order created successfully",

            "data":

            serializer.data

        }, status=201)
from rest_framework import generics
class OrderListView(

    generics.ListAPIView

):

    serializer_class = OrderSerializer

    permission_classes = [

        IsAuthenticated

    ]

    def get_queryset(self):

        return Order.objects.filter(

            user=self.request.user

        )
class OrderDetailView(

    generics.RetrieveAPIView

):

    serializer_class = OrderSerializer

    permission_classes = [

        IsAuthenticated

    ]

    def get_queryset(self):

        return Order.objects.filter(

            user=self.request.user

        )
class UpdateOrderStatusView(

    APIView

):

    permission_classes = [

        IsAdminUserRole

    ]

    def put(

        self,

        request,

        pk

    ):

        serializer = StatusSerializer(

            data=request.data

        )

        serializer.is_valid(

            raise_exception=True

        )

        order = Order.objects.get(

            pk=pk

        )

        order.status = serializer.validated_data[

            'status'

        ]

        order.save()

        return Response({

            "success":True,

            "message":

            "Status updated",

            "data":{

                "status":

                order.status

            }

        })