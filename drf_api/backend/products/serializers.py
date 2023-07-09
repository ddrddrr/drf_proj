from rest_framework import serializers
from .models import Product


class FullProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'short_title',
            'discount'
        ]

    def get_discount(self, obj):
        if not isinstance(obj, Product):
            return None
        return obj.discount_price()


class PartialProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['price', 'short_title']
