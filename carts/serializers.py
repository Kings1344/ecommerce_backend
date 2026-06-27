from rest_framework import serializers


class AddToCartSerializer(serializers.Serializer):

    product_id = serializers.IntegerField()

    quantity = serializers.IntegerField(min_value=1)
from .models import CartItem
class CartItemSerializer(serializers.ModelSerializer):

    name = serializers.CharField(
        source='product.name',
        read_only=True
    )

    price = serializers.DecimalField(
        source='product.price',
        max_digits=10,
        decimal_places=2,
        read_only=True
    )

    image_url = serializers.CharField(
        source='product.image_url',
        read_only=True
    )

    subtotal = serializers.SerializerMethodField()

    class Meta:

        model = CartItem

        fields = [

            'product',

            'name',

            'price',

            'image_url',

            'quantity',

            'subtotal'

        ]

    def get_subtotal(self, obj):

        return obj.product.price * obj.quantity
class UpdateCartSerializer(serializers.Serializer):

    product_id = serializers.IntegerField()

    quantity = serializers.IntegerField(
        min_value=1
    )