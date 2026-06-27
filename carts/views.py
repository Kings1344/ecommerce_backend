from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from products.models import Product

from .models import Cart, CartItem
from .serializers import AddToCartSerializer
class AddToCartView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = AddToCartSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        product = Product.objects.get(
            id=serializer.validated_data["product_id"]
        )

        quantity = serializer.validated_data["quantity"]

        cart, created = Cart.objects.get_or_create(
            user=request.user
        )

        cart_item, item_created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={"quantity": quantity}
        )

        if not item_created:
            cart_item.quantity += quantity
            cart_item.save()

        return Response({
            "success": True,
            "message": "Product added to cart successfully."
        }, status=201)
from .serializers import CartItemSerializer
class CartView(APIView):

    permission_classes = [

        IsAuthenticated

    ]

    def get(self, request):

        cart, created = Cart.objects.get_or_create(

            user=request.user

        )

        items = cart.items.all()

        serializer = CartItemSerializer(

            items,

            many=True

        )

        total = sum(

            item.product.price * item.quantity

            for item in items

        )

        return Response({

            "success": True,

            "data": {

                "items": serializer.data,

                "total_price": total

            }

        })
from .serializers import (
    AddToCartSerializer,
    CartItemSerializer,
    UpdateCartSerializer
)
class UpdateCartView(APIView):

    permission_classes = [

        IsAuthenticated

    ]

    def put(self, request):

        serializer = UpdateCartSerializer(

            data=request.data

        )

        if not serializer.is_valid():

            return Response(

                serializer.errors,

                status=400

            )

        product_id = serializer.validated_data[

            'product_id'

        ]

        quantity = serializer.validated_data[

            'quantity'

        ]

        cart = request.user.cart

        try:

            cart_item = CartItem.objects.get(

                cart=cart,

                product_id=product_id

            )

        except CartItem.DoesNotExist:

            return Response({

                "success": False,

                "message": "Item not found in cart"

            }, status=404)

        if quantity > cart_item.product.stock_quantity:

            return Response({

                "success": False,

                "message": "Quantity exceeds stock"

            }, status=400)

        cart_item.quantity = quantity

        cart_item.save()

        return Response({

            "success": True,

            "message": "Cart updated successfully"

        })
class RemoveCartItemView(APIView):

    permission_classes = [

        IsAuthenticated

    ]

    def delete(

        self,

        request,

        product_id

    ):

        cart = request.user.cart

        try:

            item = CartItem.objects.get(

                cart=cart,

                product_id=product_id

            )

        except CartItem.DoesNotExist:

            return Response({

                "success": False,

                "message": "Item not found"

            }, status=404)

        item.delete()

        return Response({

            "success": True,

            "message": "Item removed successfully"

        })