from rest_framework import serializers
from .models import CoinCJ, BuyConCJ


class CoinCJSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CoinCJ
        fields = ['id', 'product', 'qnt', 'valor']


class BuyCoinCJSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BuyConCJ
        fields = ['id', 'product', 'qnt', 'valor']